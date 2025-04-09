from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm , UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponse
from .prompts import random_prompt
from django.shortcuts import render
from .models import Tweet

def create_tweet(request):
    prompt = random_prompt()
    print("DEBUG PROMPT:", prompt)  # <- check your terminal for this
    return render(request, "tweet/create_tweet.html", {"prompt": prompt})
    

def tweet_list(request):
    prompt = random_prompt()
    print("DEBUG PROMPT:", prompt)  # <- check your terminal for this
    return render(request, "tweet/tweet_list.html", {"prompt": prompt})

def tweet_list(request):
    prompt = request.GET.get('prompt')  # ✅ Get from URL
    tweets = Tweet.objects.all().order_by('-created_at')

    return render(request, 'tweet_list.html', {
        'tweets': tweets,
        'prompt': prompt
    })






# from django.http import HttpResponse
def home(request):
    return render(request, 'index.html')
# Create your views here.

def index(request):
    return render(request, 'index.html')

# def index(request):
#     return HttpResponse("Hello from the Tweet app!")

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html',{'tweets':tweets})


@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
     
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form':form})
    
@login_required
def tweet_edit(request ,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_form.html', {'form':form})

@login_required
def tweet_delete(request ,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User =form.save(commit=False)
            User.set_password(form.cleaned_data['password1'])
            User.save()
            login(request,User)
            return redirect('tweet_list')
        
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html',
    {'form':form})