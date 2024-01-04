from . import models, forms
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin


class StreamVideo(FormMixin, DetailView):
    model = models.Video
    form_class = forms.CommentForm
    template_name = 'stream.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = models.Comment.objects.filter(video=self.object).order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        self.object = self.get_object() 
        form = self.get_form()
        return self.form_valid(form) if form.is_valid() else self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.video = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('video_streaming:stream', kwargs={'slug': self.object.slug})