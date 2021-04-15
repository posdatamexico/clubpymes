from django.urls import path
from .views import HomeView, SeccionView, SeccionList, Detail, Publicar, UpdatePublicacion, Delete, LikeView


urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('publicacion/<int:pk>', Detail.as_view(), name='detail'),
	path('publicar/', Publicar.as_view(), name='publicar'),
	path('publicacion/edit/<int:pk>', UpdatePublicacion.as_view(), name='edit'),
	path('publicacion/delete/<int:pk>', Delete.as_view(), name='delete'),
	path('seccion/<str:secs>/', SeccionView, name='seccion'),
	path('seccion-list/', SeccionList, name='seccion-list'),
	path('like/<int:pk>', LikeView, name="like"),
]