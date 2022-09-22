"""
    Importacion de librerias necesarias.
	Importaciones de las tablas creadas en models.py.
"""
from django.shortcuts import render
from django.contrib import messages
from .models import (
		Blog,
		Review,
		Portada,
	)

from django.views import generic


from . forms import ReviewForm, CreateUserForm
from . forms import BlogForm


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


"""
	Vista de registrar usuarios.

	valida si el usuario está logueado o no, en el caso de que no lo esté, le permite
	crearlo y lo redirecciona a la vista de inicio de sesión.
"""
def registerPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Se creó la cuenta para  ' + user)

				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'main/registrar.html', context)


"""
	Vista de inicio de sesión.

	Evalua si el usuario introducido está autenticado o no, en el caso de no
	estarlo, mostrará un mensaje de error y volverá a cargar la página de inicio de sesión.
"""
def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:home")
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)

"""
	Vista de cierre de sesión.

	Se encarga de cerrar la sesión actual y mandar al index.
"""
def logoutUser(request):
	logout(request)
	return redirect('main:home')

"""
	Vista del index.

	Se encarga de mostrar la página principal, toma los datos de portadas, blogs
	y reviews para utilizarlos en ella.
"""
class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		portadas = Portada.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		reviews = Review.objects.filter(is_active=True)
		
		context["portadas"] = portadas
		context["blogs"] = blogs
		context["reviews"] = reviews
		return context

"""
	Vista de blog.

	Muestra la ventana de los blogs en general
"""
class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 25
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

"""
	Vista de detalles de blog.

	Muestra los blogs en especifico mediante el slug.
"""
class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-details.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		blogs = Blog.objects.filter(is_active=True)
		
		context["blogs"] = blogs

		return context


"""
	Vista de crear blogs.

	Permite subir los datos del blog a la tabla mediante una ventana para el usuario.
"""
class BlogUploadView(generic.FormView):
	template_name = "main/crear-blog.html"
	form_class = BlogForm


	success_url = "../blog-upload/"
	
	def form_valid(self, form):
		
		form.save()
		messages.success(self.request, 'Su blog se creó de forma exitosa.')
		return super().form_valid(form)

"""
	Vista de review.

	Muestra la ventana de las reviews en general
"""
class ReviewView(generic.ListView):
	model = Review
	template_name = "main/review.html"
	paginate_by = 25
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


"""
	Vista de detalles de review.

	Muestra los blogs en especifico mediante el slug.
"""
class ReviewDetailView(generic.DetailView):
	model = Review
	template_name = "main/review-details.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		reviews = Review.objects.filter(is_active=True)
		
		context["reviews"] = reviews
		
		return context

"""
	Vista de crear reviews.

	Permite subir los datos del la review a la tabla mediante una ventana para el usuario.
"""
class ReviewUploadView(generic.FormView):
	template_name = "main/crear-review.html"
	form_class = ReviewForm
	success_url = "../review-upload/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Su review se creó de forma exitosa.')
		return super().form_valid(form)
