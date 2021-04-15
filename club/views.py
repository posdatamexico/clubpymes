from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Publicacion, Seccion
from .forms import PublicacionForm, EditForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# Create your views here.
def LikeView(request, pk):
	publicacion = get_object_or_404(Publicacion, id=request.POST.get('publicacion_id'))
	liked = False
	if publicacion.likes.filter(id=request.user.id).exists():
		publicacion.likes.remove(request.user)
		liked = False
	else:
		publicacion.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class HomeView(ListView):
	model = Publicacion
	template_name = 'home.html'
	secs = Seccion.objects.all()
	ordering = ['fecha']

	def get_context_data(self, *args, **kwargs):
		seccion_menu = Seccion.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["seccion_menu"] = seccion_menu
		return context

def SeccionList(request):
	seccion_menu_list = Seccion.objects.all()
	return render(request, 'secciones_list.html', {'seccion_menu_list': seccion_menu_list})

def SeccionView(request, secs):
	seccion_publicacion = Publicacion.objects.filter(seccion=secs)
	return render(request, 'secciones.html', {'secs': secs, 'seccion_publicacion': seccion_publicacion})

class Detail(DetailView):
	model = Publicacion
	template_name = 'detail.html'

	def get_context_data(self, *args, **kwargs):
		seccion_menu = Seccion.objects.all()
		context = super(Detail, self).get_context_data(*args, **kwargs)

		stuff = get_object_or_404(Publicacion, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["seccion_menu"] = seccion_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class Publicar(CreateView):
	model = Publicacion
	template_name = 'publicacion_form.html'
	form_class = PublicacionForm

class UpdatePublicacion(UpdateView):
	model = Publicacion
	template_name = 'editar_publicacion.html'
	fields = ['titulo', 'descripcion', 'contenido']

class Delete(DeleteView):
	model = Publicacion
	template_name = 'delete_publicacion.html'
	success_url = reverse_lazy('home')

	