from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required


app_name = "main"

urlpatterns = [
	
	#Se hacen los enlaces a los templates de HTML.
	
	path('', views.IndexView.as_view(), name="home"),
	
	path('registrar/', views.registerPage, name="register"),
	path('accounts/login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	path('blog-upload/', login_required(views.BlogUploadView.as_view()), name="blogs-upload"),

	path('review/', views.ReviewView.as_view(), name="reviews"),
	path('review/<slug:slug>', views.ReviewDetailView.as_view(), name="review"),
	path('review-upload/', login_required(views.ReviewUploadView.as_view()), name="reviews-upload"),
	]

    