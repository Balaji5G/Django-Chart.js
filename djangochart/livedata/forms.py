from django import forms

class userinput(forms.Form):
    entervalue=forms.IntegerField(max_value=12,required=False,label= False,widget=forms.NumberInput(attrs={'placeholder': 'Enter value for last n hour '}))