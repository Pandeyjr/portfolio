from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Post
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    posts = Post.objects.all().order_by('-date')
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
                subject=f"New Contact Message from {name}",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,  # <-- Fixed here
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Message sent successfully!")
            return redirect('home')

    return render(request, 'index.html', {
        'posts': posts,
        'form': form
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

# Optional: Remove this view if not needed
# def contact(request):
#     return render(request, 'index.html')
