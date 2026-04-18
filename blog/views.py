import uuid

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def _ensure_owner_id(request):
    owner_id = request.session.get('blog_owner_id')
    if not owner_id:
        owner_id = str(uuid.uuid4())
        request.session['blog_owner_id'] = owner_id
    return owner_id


def index(request):
    owner_id = _ensure_owner_id(request)
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner_id = owner_id
            post.save()
            messages.success(request, 'Your thought was posted successfully.')
            return redirect('index')
    else:
        form = PostForm()

    return render(
        request,
        'blog/index.html',
        {
            'form': form,
            'posts': posts,
            'owner_id': owner_id,
        },
    )


def edit_post(request, post_id):
    owner_id = _ensure_owner_id(request)
    post = get_object_or_404(Post, id=post_id, owner_id=owner_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post was updated successfully.')
            return redirect('index')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    owner_id = _ensure_owner_id(request)
    post = get_object_or_404(Post, id=post_id, owner_id=owner_id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('index')

    return render(request, 'blog/confirm_delete.html', {'post': post})
