from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from .models import Message


# Cache the inbox view for 60 seconds
@login_required
@cache_page(60)  # 60 seconds cache timeout
def inbox(request):
    messages = (
        Message.objects.filter(receiver=request.user)
        .select_related("sender", "receiver", "parent_message")
        .prefetch_related("replies")
        .order_by("-timestamp")
    )
    return render(request, "messaging/inbox.html", {"messages": messages})

