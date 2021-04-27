from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .apps import PredictorConfig
from .forms import DocumentForm
from .models import Document
from .Metadata import getmetadata
import warnings
from .predict import predict_gen
from django.contrib import messages
warnings.simplefilter('ignore')
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
class IndexView(ListView):
    template_name= 'music/index.html'
    def get_queryset(self):
        return True

def model_form_upload(request):

    documents = Document.objects.all()
    if request.method == 'POST':
        if len(request.FILES) == 0:
            messages.error(request,'Upload a file')
            return redirect("predictor:index")

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploadfile = request.FILES['document']
            print(uploadfile.name)
            print(uploadfile.size)
            if not uploadfile.name.endswith('.wav'):
                messages.error(request,'Only .wav file type is allowed')
                return redirect("predictor:index")
            meta = getmetadata(uploadfile)
            
            genre = predict_gen(meta)
            print(genre)

            context = {'genre':genre}
            return render(request,'music/result.html',context)

    else:
        form = DocumentForm()

    return render(request,'music/result.html',{'documents':documents,'form':form})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("predictor:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="music/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("predictor:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="music/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("predictor:login")