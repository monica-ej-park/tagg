from django.http import request
from django.shortcuts import render, redirect
from .forms import ThreadForm, ReplyForm
from .models import LikeMap, Thread, Reply, TagDictionary, TagThreadMap
from account.models import User
from django.db.models import F, Count


# Create your views here.
def get_list(request):
    thread_list = Thread.objects.all().order_by('-created_time')
                 
    return render(
        request, 
        'forum/list.html', 
        {
            #'field_names': ['title', 'nickname'],
            'data_list': thread_list
        }
    )


def get_most_view_list(request):
    thread_list = Thread.objects.all().order_by('-view_count')
             
    return render(
        request, 
        'forum/list.html', 
        {
            #'field_names': ['title', 'nickname'],
            'data_list': thread_list
        }
    )


def get_most_like_list(request):  
    thread_list = LikeMap.objects.values('thread').annotate(
        like_count=Count('thread')
    ).order_by('-like_count').annotate(
        id=F('thread__id'), author=F('thread__author'),
        nickname=F('thread__nickname'), password=F('thread__password'),
        title=F('thread__title'), contents=F('thread__contents'),
        tags=F('thread__tags'), is_sticky_thread=F('thread__is_sticky_thread'),
        view_count=F('thread__view_count'), created_time=F('thread__created_time'),
        updated_time=F('thread__updated_time')
    )


    return render(
        request, 
        'forum/list.html', 
        {
            'data_list': thread_list
        }
    )


def get_list_by_me(request):
    t = Thread.objects.all().last()
    thread_list = Thread.objects.filter(author_id=request.user.id).order_by('-created_time')

    print(thread_list)
    return render(
        request,
        'forum/list.html', 
        {
            'data_list': thread_list
        }
    )


def get_list_by_tag(request, tag):
    tag_dic = TagDictionary.objects.get(tag=tag.strip())
    if tag_dic:
        tag_dic.hit_count += 1
        tag_dic.save()

    thread_list = TagThreadMap.objects.filter(tag=tag_dic).annotate(
        author=F('thread__author'), nickname=F('thread__nickname'), password=F('thread__password'), 
        title=F('thread__title'), contents=F('thread__contents'), 
        tags=F('thread__tags'), is_sticky_thread=F('thread__is_sticky_thread'), 
        view_count=F('thread__view_count'), #like_count=F('thread__like_count'), 
        created_time=F('thread__created_time'), updated_time=F('thread__updated_time')
    )

    return render(
        request,
        'forum/list.html',
        {
            'data_list': thread_list
        }
    )


def view_detail(request, data_id):
    thread = Thread.objects.get(id=data_id)
    thread.view_count += 1
    thread.save()
    like_count = LikeMap.objects.filter(thread=data_id).count()
    like = False
    if request.user.is_authenticated: #request.user.is_anonymous():
        if LikeMap.objects.filter(user=request.user, thread=data_id).count() > 0:
            like = True

    return render(
        request, 
        'forum/thread.html', 
        {
            'data': thread,
            'like_count': like_count,
            'like': like
        }
    )


def write(request):
    if request.method == 'POST':
        
        form = ThreadForm(request.POST)
        if form.is_valid():      
            thread = form.save(commit=False)
            
            try:
                thread.author = request.user
            except:
                thread.author = None
                
            thread.save()
            tags = [tag.strip() for tag in form.cleaned_data.get('tags').split(',')]
            for tag in tags:
                tag_dic = (TagDictionary.objects.filter(tag=tag) | TagDictionary.objects.filter(synonyms=tag)).last()
                if tag_dic == None: # 등록되지 않은 태그    
                    tag_dic = TagDictionary.objects.create(tag=tag)
                else:
                    tag_dic.register_count += 1
                    tag_dic.save()
                TagThreadMap.objects.create(tag=tag_dic, thread=thread)
            
            return redirect("list")
        else:
            print(form.errors)

    # get
    form = ThreadForm()
    if request.user.is_authenticated:
        print(request.user.password)
        user = User.objects.filter(id=request.user.id).last()
        lastThread = Thread.objects.filter(author=user).last()
        
        if lastThread:
            form.initial['nickname'] = lastThread.nickname
            form.initial['password'] = lastThread.password
        else:
            form.initial['nickname'] = user.name
            #form.initial['password'] = ""
        #form.initial['password'] = user.password
        #form.fields['password'].widget.attrs.update({
            #'disabled': True,
            #'hidden': True
        #})
    #form.initial['password'] = ''

    return render(
        request, 
        'forum/thread_form.html', 
        {
            'form': form,
            'mode': 'write',
            'is_authenticated': request.user.is_authenticated
        }
    )


def modify(request, data_id):
    thread = Thread.objects.get(id=data_id)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():  
            thread.title = form.cleaned_data['title']
            thread.nickname = form.cleaned_data['nickname']
            thread.contents = form.cleaned_data['contents']
            thread.password = form.cleaned_data['password']
            thread.tags = form.cleaned_data['tags']
            thread.save()
            return redirect("list")
        else:
            print(form.errors)
    
    thread = Thread.objects.get(id=data_id)
    form = ThreadForm(instance=thread)
    return render(
        request, 
        'forum/thread_form.html', 
        {
            'form': form,
            'mode': 'modify',
            'data_id': data_id
        }
    )
            
def search(request):
    keyword = request.GET.get('search_box', '').strip()
    
    tag_dic = TagDictionary.objects.get(tag=keyword)
    if tag_dic:
        tag_dic.search_count += 1
        tag_dic.save()

    thread_list = (
        Thread.objects.filter(
            title__contains=keyword
        ) | Thread.objects.filter(
            contents__contains=keyword
        ) | Thread.objects.filter(
            tags__contains=keyword
        )
    )

    return render(
        request,
        'forum/list.html',
        {
            'data_list': thread_list
        }
    )


def get_tag_rank(request):
    best_hit_tags = TagDictionary.objects.all().order_by('-hit_count')[:10]
    best_search_tags = TagDictionary.objects.all().order_by('-search_count')[:10]
    frequently_registered_tags = TagDictionary.objects.all().order_by('-register_count')[:10]
    # frequently_registered_tags = TagThreadMap.objects.values('thread__tags').annotate(
    #     #tag=F('thread__tag'),
    #     tag_count=Count('thread__tags')
    # ).filter(tag_count__gt=1)

    return render(
        request,
        'forum/tag_rank.html',
        {
            'best_hit_tags': best_hit_tags,
            'best_search_tags': best_search_tags,
            'frequently_registered_tags': frequently_registered_tags
        }
    )



def like(request, data_id, value):
    thread = Thread.objects.get(id=data_id)
    try:
        like_map = LikeMap.objects.get(user=request.user, thread=thread)
        if like_map:
            like_map.delete()
    except:
        LikeMap.objects.create(user=request.user, thread=thread)

    like_count = LikeMap.objects.filter(thread=data_id).count()
    like = False
    if LikeMap.objects.filter(user=request.user, thread=data_id).count() > 0:
        like = True

    return render(
        request, 
        'forum/thread.html', 
        {
            'data': thread,
            'like_count': like_count,
            'like': like
        }
    )


