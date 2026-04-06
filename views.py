from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Assignment


@login_required
def assignment_list(request):
    assignments = Assignment.objects.filter(assigned_to=request.user).order_by('due_date')
    return render(request, 'assignments/list.html', {"assignments": assignments})


@login_required
def assignment_detail(request, pk: int):
    assignment = get_object_or_404(Assignment, pk=pk, assigned_to=request.user)
    return render(request, 'assignments/detail.html', {"assignment": assignment})


@login_required
def calendar_view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        events = [
            {
                "title": a.title,
                "date": a.due_date.isoformat(),
                "url": request.build_absolute_uri(a.get_absolute_url()) if hasattr(a, 'get_absolute_url') else '',
            }
            for a in Assignment.objects.filter(assigned_to=request.user)
        ]
        return JsonResponse({"events": events})
    return render(request, 'assignments/calendar.html')

# Create your views here.
