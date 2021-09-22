from django.forms import *
from django.core.exceptions import ValidationError
from .models import Thread, Reply
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Submit
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField



class BootstrapModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({
                'placeholder': field.label,
                'class': 'form-control',       
            })
            field.label = ''


class PlaceholderModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.label = ''


class ThreadForm(BootstrapModelForm):
    #nickname = CharField(required=True, label='별명')
    tags = CharField(
        required=True, label='태그를 입력하세요.', 
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': '태그'})
    )
    #password = CharField(widget=PasswordInput(render_value=True))
    contents = SummernoteTextField()
    class Meta:
        model = Thread
        fields = ('title', 'nickname', 'password', 'tags', 'contents')
        widgets = {
            'contents': SummernoteWidget(),
        }
        # widgets = {
        #     'contents': forms.TextArea(attrs={'cols': 80, 'rows': 20})
        # }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'form'
    #     self.helper.form_class = 'forms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'list'

    #     self.helper.add_input(Submit('submit', 'Submit'))



class ReplyForm(BootstrapModelForm):
    class Meta:
        model = Reply
        fields = ('author', 'message')


