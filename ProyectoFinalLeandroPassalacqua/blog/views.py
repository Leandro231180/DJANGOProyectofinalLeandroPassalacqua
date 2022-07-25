# from email import message
# from pyexpat.errors import messages
from email import message
from re import template
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from matplotlib.pyplot import title
from matplotlib.style import context
from blog.models import Post, Avatar
from .forms import Project_Form, UserRegisterForm, UserEditForm
from blog.forms import Project_Form
#from PIL import Image
# from blog.forms import Project_Form

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import is_valid_path, reverse_lazy
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#LISTADO DE POST

def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render(request, "blog.html", {"posts": posts, "total_posts": total_posts})

# DETALLE DE LOS POST
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})

#FORMULARIO DE CARGA DE POSTEOS NUEVOS

def carga_blog(request):
    mi_formulario=Project_Form()
    if request.method=='POST':
        mi_formulario=Project_Form(request.POST, request.FILES)
        if mi_formulario.is_valid():
            
            mi_formulario.save()
            #return render(request, 'cargablog.html',{'mi_formulario': mi_formulario})
            return redirect('/blog/')
    else:
        print('invalido')
    
    return render(request,"cargablog.html", {'mi_formulario': mi_formulario})
    
    
#Clases Basadas en vistas
class Postlista(ListView):
    model=Post
    template_name='editar.html'


class Postview(DetailView):
    model= Post
    template_name='detalle.html'



# class Postupdate(UpdateView):
#     model= Post
#     success_url: 'editar.html'

class Postdelete(DeleteView):
    model= Post
    success_url=  'blog/borrarProd'



#ELIMINAR POST
@login_required
def eliminar_post(request,post_id):
    variable_pos=Post.objects.get(id=post_id)
    variable_pos.delete()    
    return redirect('/blog/')

#EDITAR POST
@login_required
def editar_blog(request, post_id):
    post=Post.objects.get(id=post_id)
    if request.method=='POST':
        mi_formulario=Project_Form(request.POST, request.FILES, instance=post)
        mi_formulario.save()
        return redirect('/blog/')
    else:
        
        mi_formulario=Project_Form(instance=post)
    context={'mi_formulario':mi_formulario}
    return render(request, 'editarpost.html', context)    



#LOGUiN




def register(request):
    if request.method =='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/')
    else:
        form=UserRegisterForm()

    context={'form': form}
    return render(request, 'registro.html', context)

    
def login_request(request):      
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
            
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
               
            user = authenticate(username = usuario , password = contra)
                 
            if user is not None:
                login(request, user)

                #return render (request, "/blog/")#, {"mensaje": f"Bienvenido/a {usuario}"})
                messages.success(request, f'Usuario {usuario} login')
                return redirect('/',)
            else:
                       
                return render (request, "login.html", {"mensaje":"Error en los datos"})
        else:
            #return render(request, "login.html", {"mensaje":"Formulario erroneo"})
            messages.success(request, 'Los datos son invalidos')
            return redirect('/')
      
    form = AuthenticationForm()
    
    return render(request, "login.html", {'form': form})

#EDITAR PERFIL

@login_required
def editarPerfil(request):
      
    usuario = request.user
      
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data
                  
                  
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            #return render(request, "perfiledit.html")
            return redirect('/') 

    else:
            #creo el formulario con los datos que voy a modificar
        miFormulario = UserEditForm(initial={'email':usuario.email,'password': usuario.password})
      
      #voy al HTML que me permite editar
    return render(request, "perfiledit.html", {"miFormulario": miFormulario, "usuario": usuario})


def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "navbar.html" ,{"url": avatares[0].imagen.url})
      #return render(request,"AppCoder/inicio.html")
