from django.views.generic import View
from django.shortcuts import render

class homeView(View):
    """
    Home view for the application.
    """
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to the home page.
        """
        context = {
            'title': 'Home',
            'description': 'Welcome to the home page of our application.',
        }
        return render(request, self.template_name, context)