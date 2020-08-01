from django import forms


class GuestBookForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Автор', initial='Unknown')
    email = forms.EmailField(max_length=50, required=True, label='Email автора')
    text = forms.CharField(max_length=3000, required=True, label="Текст", widget=forms.Textarea)



