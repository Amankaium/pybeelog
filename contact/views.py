from django.views.generic import ListView
from django.shortcuts import redirect

from django.views.generic import FormView


from .models import Subscribe, Feedback
from .forms import FeedbackForm



class FeedbackView(FormView, ListView):
    template_name = 'contact/contact.html'
    form_class = FeedbackForm
    success_url = '/contact/'
    model = Feedback
    context_object_name = 'contact'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def subscribe(request):
    if request.method == 'POST':
        sub = Subscribe()
        sub.email = request.POST.get('email')
        sub.save()
    return redirect('contact/contact.html')





