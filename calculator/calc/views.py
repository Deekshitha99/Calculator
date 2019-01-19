from django.shortcuts import render

# Create your views here.
def calc(requests):
    field1=requests.GET['field1']
    field2=requests.GET['field2']
    operation=requests.GET['optradio']
    result=0
    if operation=='+':
        result=field1+field2
    elif operation=='-':
        result=field1-field2
    elif operation=='*':
        result=field1*field2
    else:
        result=field1/field2   
    return render(requests,'calc/calcy.html')
def home(requests):
	return render(requests,'calc/home.html')