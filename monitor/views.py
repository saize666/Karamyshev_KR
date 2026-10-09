from django.db.models import Count
from django.shortcuts import render
from .models import AccessEvent


def _counts():
    all_events = AccessEvent.objects.all()
    return {
        'total': all_events.count(),
        'allowed': all_events.filter(decision='ALLOW').count(),
        'denied': all_events.filter(decision='DENY').count(),
        'closed': all_events.filter(decision='CLOSE').count(),
    }


def dashboard(request):
    selected = request.GET.get('decision', 'ALL').upper()
    if selected not in ('ALL', 'ALLOW', 'DENY', 'CLOSE'):
        selected = 'ALL'
    selected_vm = request.GET.get('vm', 'ALL')
    if selected_vm not in ('ALL', 'pay-01', 'test-01'):
        selected_vm = 'ALL'
    events = AccessEvent.objects.all()
    if selected != 'ALL':
        events = events.filter(decision=selected)
    if selected_vm != 'ALL':
        events = events.filter(vm_name=selected_vm)
    return render(request, 'monitor/index.html', {
        'counts': _counts(), 'events': events[:25], 'selection': selected,
        'vm_selection': selected_vm,
    })


def statistics(request):
    counts = _counts()
    total = counts['total'] or 1
    for key in ('allowed', 'denied', 'closed'):
        counts[key + '_pct'] = round(100 * counts[key] / total, 1)
        counts[key + '_pct_css'] = round(100 * counts[key] / total)
    vm_stats = AccessEvent.objects.values('vm_name').annotate(total=Count('id')).order_by('-total')
    device_stats = AccessEvent.objects.values('device').annotate(total=Count('id')).order_by('-total')
    denial_reasons = (AccessEvent.objects.filter(decision='DENY')
                      .values('reason').annotate(total=Count('id')).order_by('-total')[:5])
    return render(request, 'monitor/stats.html', {
        'counts': counts, 'vm_stats': vm_stats, 'device_stats': device_stats,
        'denial_reasons': denial_reasons,
    })


def requirements(request):
    return render(request, 'monitor/requirements.html')
