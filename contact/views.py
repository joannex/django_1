from django.shortcuts import render
from contact.forms import ContactForm

def contact(request):
	if request.method == 'POST':
		# request.POST is a dict 
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'], 
				cd['message'],
				cd.get('email', 'noreply@example.com'), ['siteowner@example.com'], 
			)
			return HttpResponseRedirect('/contact/thanks/')
	else: 
		form = ContactForm()
	return render(request, 'contact_form.html', {'form': form}) 
