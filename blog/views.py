from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views import View
from .forms import PostForm
from .models import Post


# Create your views here.
class BlogCreateView(View):

    def get(self, request):
        # Renderizar el formulario para crear un nuevo post
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog_create.html', context)

    def post(self, request):

        if request.method == 'POST':
    
            form = PostForm(request.POST)

            if form.is_valid():
                # Extraer los datos del formulario
                # y crear el objeto Post
                titulo = form.cleaned_data['title']
                contenido = form.cleaned_data['content']

                p, created = Post.objects.get_or_create(
                    title=titulo,
                    content=contenido
                )
                messages.success(request, 'El post se envió correctamente.')
                return redirect('blog:blog_list')

        # Si el formulario no es válido, se vuelve a mostrar el formulario con los errores
        context = {
            'form': form
        }

        return render(request, 'blog_create.html', context)


class BlogListView(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        context = {
            'posts': posts
        }
        return render(request, 'blog_list.html', context)
    
class BlogUpdateView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(instance=post)
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            messages.info(request, 'El post se actualizó correctamente.')
            return redirect('blog:blog_list')

        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog_create.html', context)

class BlogDeleteView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.status = False
        post.save()
        messages.warning(request, 'El post se eliminó correctamente.')
        return redirect('blog:blog_list')