from django import forms

qnty=[(i,str(i)) for i in range(1,21)]

class addcartForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=qnty,coerce=int)
    override=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)