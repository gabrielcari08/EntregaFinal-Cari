from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    sent_messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {
        "received_messages": messages,
        "sent_messages": sent_messages
    })

@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST, sender=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm(sender=request.user)

    return render(request, 'messaging/send_message.html', {"form": form})

@login_required
def edit_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, sender=request.user)
    
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message, sender=request.user)
        if form.is_valid():
            form.save()
            return redirect('inbox')
    else:
        form = MessageForm(instance=message, sender=request.user)
    
    return render(request, 'messaging/edit_message.html', {
        'form': form,
        'message': message
    })

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, sender=request.user)
    if request.method == "POST":
        message.delete()
        return redirect('inbox')
    return render(request, 'messaging/confirm_delete.html', {'message': message})