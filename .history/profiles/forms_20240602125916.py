from django import forms
from .models import Profile, ProfileImage


class ProfileForm(forms.ModelForm):
    avatar = forms.ModelChoiceField(queryset=ProfileImage.objects.all(), widget=forms.Select(attrs={
        'class': 'mt-2 bg-[#9CA3AF] w-[220px]'
    }), required=False)

    class Meta:
        model = Profile
        fields = ['name', 'is_kid', 'pin',
                  'enter_pin', 'confirm_pin', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'w-full h-fit px-3 py-3 bg-[#666666] placeholder-white text-white text-xl'
            }),
            'is_kid': forms.CheckboxInput(attrs={
                'class': 'border-[#818081] py-4 px-4 bg-transparent'
            }),
            'pin': forms.PasswordInput(attrs={
                'placeholder': 'Enter Pin',
                'class': 'w-fit h-fit px-3 py-3 bg-[#666666] placeholder-white text-center text-white text-xl'
            }),
            'enter_pin': forms.PasswordInput(attrs={
                'placeholder': 'Enter Pin',
                'class': 'w-fit h-fit px-3 py-3 bg-[#9CA3AF] placeholder-white text-center text-black text-xl placeholder-black'
            }),
            'confirm_pin': forms.PasswordInput(attrs={
                'placeholder': 'Confirm Pin',
                'class': 'w-fit h-fit px-3 py-3 bg-[#9CA3AF] placeholder-white text-center text-black text-xl placeholder-black'
            })
        }
