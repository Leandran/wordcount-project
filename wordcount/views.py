from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render (request,'home.html',)


def about(request):
    return render (request,'about.html',)

def count(request):
	fulltext = request.GET["fulltext"]
	#print(fulltext)
	wordlist = fulltext.split()

	worddictionary = dict()

	for word in wordlist:
		if word in worddictionary:
		#increase
		    worddictionary[word] += 1
		else:
			#add to dictionary
			worddictionary[word] = 1

	sorted_words = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=False)#chose to sort words in ascending  

	return render(request,'count.html',{"fulltext":fulltext,"count":len(wordlist),"sorted_words":sorted_words})