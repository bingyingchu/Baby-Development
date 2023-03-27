import pickle
import zmq
from django.core.mail import EmailMessage
from django.shortcuts import render
from .forms import ApplicationForm
from .models import Users
from django.contrib import messages

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            week = form.cleaned_data["week"]
            choice = form.cleaned_data["choice"]

            Users.objects.create(first_name=first_name, last_name=last_name,
                                 email=email, week=week, choice=choice)

            message_body = " ".join(process_data([week, choice]))
            send_email(first_name, email, message_body)

            messages.success(request, f"Thanks for your submission, {first_name}."
                                      f"\nYour baby development info has been sent to your email at {email}")
    return render(request, "index.html")


def process_data(info):
    info = pickle.dumps(info)
    socket.send(info)
    return pickle.loads(socket.recv())


def send_email(first_name, email, message_body):
    email_message = EmailMessage(f"Hello {first_name}", message_body, to=[email])
    email_message.send()
