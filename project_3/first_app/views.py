from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age' : 5,'lst': ['Python','is','best'],'birthday': datetime.datetime.now(),'val': '','courses' : [
        
        {
            'id': 1,
            'course': 'Python',
            'fee': 5000  
        },
        {
            'id': 2,
            'course': 'Django',
            'fee': 10000
        },
        {
            'id': 3,
            'course': 'C',
            'fee': 1000
        }
    ]}
    return render(request,'home.html',d)