from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Введите имя',
            }
        )
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Введите телефон',
            }
        )
    )
    email = forms.EmailField(
        label='Почта',
        max_length=200,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Введите почту',
            }
        )
    )