from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('home')

def inbox(request):
    messages = (
        Message.objects.filter(receiver=request.user)   # REQUIRED ✔
        .select_related("sender", "receiver", "parent_message")  # REQUIRED ✔
        .prefetch_related("replies")  # REQUIRED ✔
        .order_by("-timestamp")
    )

    return render(request, "messaging/inbox.html", {"messages": messages})


def get_thread(message):
    thread = [message]
    for reply in message.replies.all().select_related("sender", "receiver"):
        thread.extend(get_thread(reply))
    return thread



@login_required
def view_thread(request, message_id):
    message = (
        Message.objects
        .select_related("sender", "receiver")
        .get(id=message_id)
    )

    replies = get_thread(message)   # REQUIRED recursive behavior ✔

    return render(request, "messaging/thread.html", {
        "root_message": message,
        "thread": replies
    })
