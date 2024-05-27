from .forms import UserCreationFormsWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.
class SingUpView(CreateView):
  form_class = UserCreationFormsWithEmail
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
  
  def get_success_url(self) -> str:
    return reverse_lazy('login') + '?register'
  
  def get_form(self, form_class=None):
    form = super(SingUpView, self).get_form()
    form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
    form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Correo Electronico'})
    form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
    form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Repite tu Contraseña'})
    return form
  
