from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    text = request.GET.get('fulltext')
    words = text.split()
    word_count = len(words)
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    context = {
                'full': text, 
                'word_count': word_count,
                'dictionary': word_dictionary.items()
               }
    return render(request, 'result.html', context)