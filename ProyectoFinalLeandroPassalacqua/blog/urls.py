from unicodedata import name
from django.urls import path
from blog import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'blog'

urlpatterns = [
    path("", views.renderPosts, name="posts"),
    path("<int:post_id>", views.post_detail, name="post_detail"),
    path('cargablog/', views.carga_blog, name="carga_blog"),

    path('editar/',views.Postlista.as_view(), name='editar'),
      
    path('eliminar/<int:post_id>', views.eliminar_post, name='eliminar_post'),
    path('editarpost/<int:post_id>', views.editar_blog , name='editarpost'),
    
    path('registro/', views.register, name='registro'), 
    
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', views.login_request, name='login'),
    path('perfiledit/', views.editarPerfil, name='perfiledit'),
    
]



