from django import forms


class TextGenForm(forms.Form):
    temp = forms.DecimalField(decimal_places=2, min_value=0, max_value=1)
    max_gen_length = forms.IntegerField(min_value=1, max_value=200)
    number_of_texts = forms.IntegerField(min_value=1, max_value=5)
