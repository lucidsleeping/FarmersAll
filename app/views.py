from django import forms
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from . import pred_models

def selector_view(request) : 
    
    return render(request,"index.html") 

def cultivated_or_not(request): 
    
    class FileForm(forms.Form): 
        file = forms.FileField()

    title = "Cultivated or not"
     
    message_tag = 'alert-info'

    if request.method == "POST" : 

        form = FileForm(request.POST,request.FILES) 

        uploaded_image = request.FILES.get('file')

        test = pred_models.cultivated_or_not() 
        
        result,class_names,prediction = test.predict(uploaded_image)
       
        result_str = f"Result is {result}"

        if result == "good" : 
            messages.success(request,result_str)
        else : 
            messages.error(request,result_str)


        return redirect('index')

    else : 
        form = FileForm()

    return render(request,'form.html',locals()) 


def rice_classification(request): 
    
    class FileForm(forms.Form): 
        file = forms.FileField()

    title = "Rice classification"

    if request.method == "POST" : 

        form = FileForm(request.POST,request.FILES) 

        uploaded_image = request.FILES.get('file')

        test = pred_models.rice_classification() 
        
        result,class_names,prediction = test.predict(uploaded_image)
        result_str = f"Result is {result}"
        
        if result == "substandard" : 
            messages.error(request,result_str)
        else: 
            messages.success(request,result_str)
        return redirect('index')

    else : 
        form = FileForm()

    return render(request,'form.html',locals()) 

def Substandard_or_not(request): 
    
    class FileForm(forms.Form): 
        file = forms.FileField()

    title = "Substandard or not"

    if request.method == "POST" : 

        form = FileForm(request.POST,request.FILES) 

        uploaded_image = request.FILES.get('file')

        test = pred_models.Substandard_or_not() 

        result,class_names,prediction = test.predict(uploaded_image)
        result_str = f"Result is {result}"
        if result == "good" : 
            messages.success(request,result_str)
        else : 
            messages.error(request,result_str)

        return redirect('index')
        

    else : 
        form = FileForm()

    return render(request,'form.html',locals())  


def stages_of_paddy(request): 
    
    class FileForm(forms.Form): 
        file = forms.FileField()
    
    title = "Stages of paddy"

    if request.method == "POST" : 

        form = FileForm(request.POST,request.FILES) 

        uploaded_image = request.FILES.get('file')

        test = pred_models.stages_of_paddy() 
        
        result,class_names,prediction = test.predict(uploaded_image)
        result_str = f"Result is {result}"

        messages.info(request,result_str)
        
        return redirect('index')
    else : 
        form = FileForm()

    return render(request,'form.html',locals()) 