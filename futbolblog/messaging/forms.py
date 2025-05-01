from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
        
    def __init__(self, *args, **kwargs):
        self.sender = kwargs.pop('sender', None)
        super(MessageForm, self).__init__(*args, **kwargs)
        if self.sender:
            # Excluir al usuario actual de la lista de receptores
            self.fields['receiver'].queryset = User.objects.exclude(id=self.sender.id)

    def clean(self):
        cleaned_data = super().clean()
        receiver = cleaned_data.get('receiver')
        if receiver and self.sender and receiver == self.sender:
            raise forms.ValidationError("No puedes enviarte mensajes a ti mismo.")
        return cleaned_data