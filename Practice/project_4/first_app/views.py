from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    
    d = {'lst' : ['Python','is','best'],'date' : datetime.datetime.now(),'val' : 20, 'cap' : 'shihab','str':'Python is fun',
         'lst1' : [
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
         ],
         'lst2' : ['Apple', 'Mango', 'Orange'],'name' : 'Shihab Shahriar', 'sent' : 'Django is best','str1' : 'Happy coding, Python is fun.'
         }
    
    return render(request,'home.html',d)