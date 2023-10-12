from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.urls import reverse


class person:
   

    def __init__(self,usname,pasw):
        self.username=usname
        self.password=pasw




        





class NewTaskForm(forms.Form):
    taskU=forms.CharField(label='username')
    taskP=forms.CharField(label='password')
    



#rfrs
#https://www.geeksforgeeks.org/python-get-first-element-of-each-sublist/
def Extract(lst):
    return [item[0] for item in lst]
    


  

# Create your views here.


def index(request):
#as we discussed , you told me to put note over here.    

# and here we will remove the request.session because we cannot add obj with it .
    if "people" not in request.session:
        request.session['people'] = []

    return render (request,"sign_in/index.html", {
        'people':Extract(request.session['people'])
    }) 




def add(request):

    if request.method=="POST":


        form = NewTaskForm(request.POST)
        

        if form.is_valid():

            username = form.cleaned_data['taskU']
            password = form.cleaned_data['taskP']
            
            p=person(username,password)

#as we discussed , you told me to put note over here.          
# request.session[people].append(p)
            request.session['people']+=[[p.username,p.password]]



            


            return HttpResponseRedirect(reverse("sign_in:index"))

        else:

            return render (request,"sign_in/spage.html",{
        "form": form })


    return  render (request,"sign_in/spage.html",{
        "form":NewTaskForm()})

