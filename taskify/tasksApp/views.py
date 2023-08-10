from datetime import datetime, timedelta
from urllib.parse import urlparse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from taskify.tasksApp.forms import TaskAddForm, TaskEditForm
from taskify.tasksApp.models import Task, Category, TaskStatus


class Dashboard(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/dashboard.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['categories'] = Category.objects.all()
        context['statuses'] = TaskStatus.objects.all()
        context['today'] = datetime.today().date()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input
            )
        context['search_input'] = search_input

        category_input = self.request.GET.get('category') or ''
        if category_input:
            context['tasks'] = context['tasks'].filter(
                category__name__iexact=category_input
            )
        context['category_input'] = category_input

        status_input = self.request.GET.get('status') or ''
        if status_input:
            context['tasks'] = context['tasks'].filter(
                status__status__iexact=status_input
            )
        context['status_input'] = status_input

        origin_url = self.request.path
        for task in context['tasks']:
            task.origin_url = origin_url
            task.save()

        return context


class TaskAdd(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskAddForm
    template_name = 'tasks/add_task_dashboard.html'
    success_url = reverse_lazy('dashboard')

    def get_template_names(self):
        if 'calendar' in self.request.path:
            return ['task-calendar.html']
        return super().get_template_names()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskAdd, self).form_valid(form)

    def get_success_url(self):
        origin_url = self.request.GET.get('origin_url') or self.request.POST.get('origin_url')
        if origin_url and 'calendar' in urlparse(origin_url).path:
            return reverse_lazy('task_calendar')
        return reverse_lazy('dashboard')


class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/details_task.html'
    context_object_name = 'task'

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise Http404
        return task


class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskEditForm
    template_name = 'tasks/edit_task.html'

    def get_success_url(self):
        return reverse_lazy('details_task', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise Http404
        return task


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'task'

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise Http404
        return task


@login_required
def task_calendar(request):
    categories = Category.objects.all()
    form = TaskAddForm(initial={'origin_url': request.path})
    context = {
        'categories': categories,
        'form': form
    }
    return render(request, 'tasks/task-calendar.html', context)


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    tasks_list = []

    for task in tasks:
        color = task.category.color
        origin_url = request.path
        task.origin_url = origin_url
        if task.status.status == 'Completed':
            color = 'green'
        task.save()

        due_date = task.due_date + timedelta(days=1)

        start_date_iso = task.start_date.isoformat() if task.start_date else None
        due_date_iso = due_date.isoformat() if task.due_date else None
        tasks_list.append({
            'id': task.pk,
            'title': task.title,
            'start': start_date_iso,
            'end': due_date_iso,
            'category': task.category.name,
            'category_color': color,
        })
    return JsonResponse(tasks_list, safe=False)


def mark_task_as_completed(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.status = TaskStatus.objects.get(status='Completed')
        task.save()
        return JsonResponse({'success': True})
    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Task not found'})
