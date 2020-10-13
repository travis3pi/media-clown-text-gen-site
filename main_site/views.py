from django.contrib import messages
from django.shortcuts import render
from textgenrnn import textgenrnn

from .forms import TextGenForm

textgen = textgenrnn(weights_path='./des-train_weights.hdf5', vocab_path='./des-train_vocab.json',
                     config_path='./des-train_config.json')


# Create your views here.

def index_view(request):
    form = TextGenForm()
    form['temp'].help_text = 'Value between 0 and 1'
    form['max_gen_length'].help_text = 'The maximum number of words for each generation. Between 1 and 200'
    form['number_of_texts'].help_text = 'The number of text segments to be generated. Between 1 and 5'
    text = None
    if request.method == 'POST':
        form = TextGenForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                temp = float(form.cleaned_data['temp'])
                max_length = int(form.cleaned_data['max_gen_length'])
                number_of_texts = int(form.cleaned_data['number_of_texts'])
                text = textgen.generate(temperature=temp, return_as_list=True, max_gen_length=max_length,
                                        n=number_of_texts)
                messages.success(request, 'Text has been generated successfully.')
            except Exception as e:
                print(e)
                messages.error(request, 'Could not generate text.')
    return render(request, 'index.html', {'form': form, 'text': text})
