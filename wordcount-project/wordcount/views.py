from django.shortcuts import render
from operator import itemgetter

def home(request):
    return render(request,'home.html', {'key':56})

def count(request):
    if request.method == 'GET':
        data = request.GET['fulltext']
        words_list = data.split()
        word_dict = {}
        for word in words_list:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        sortedlist = sorted(word_dict.items(), key=itemgetter(1), reverse=True)
    return render(request,'count.html', {'data':data, 'total':len(words_list), 'sortedlist':sortedlist})
