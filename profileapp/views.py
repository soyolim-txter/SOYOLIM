from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorator import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:home')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        # 임시 대기중 데이터라 생각하라(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()

        print(self)
        print(form)
        return super().form_valid(form)

@method_decorator(profile_ownership_required,'post')
@method_decorator(profile_ownership_required,'get')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = 'profileapp/update.html'