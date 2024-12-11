from django.shortcuts import render, get_object_or_404, redirect
from .models import PostsModel
from django.http import HttpResponse

# Create Post View
def create_post_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        content_type = request.POST.get("type")
        image = request.FILES.get("image")

        if title and content and content_type:
            PostsModel.objects.create(
                title=title,
                content=content,
                content_type=content_type,
                image=image
            )
            return redirect('posts_list')  # Redirect to the posts list view after creating a post
    return render(request, "posts/create_post.html")

# Update Post View
def update_post_view(request, post_id):
    post = get_object_or_404(PostsModel, id=post_id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.content_type = request.POST.get("type")
        post.image = request.FILES.get("image") if request.FILES.get("image") else post.image
        post.save()

        return redirect('posts_list')  # Redirect to the posts list view after updating

    return render(request, "posts/update_post.html", {'post': post})

# Delete Post View
def delete_post_view(request, post_id):
    post = get_object_or_404(PostsModel, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect('posts_list')  # Redirect to the posts list view after deleting

    return render(request, "posts/delete_post.html", {'post': post})

# Search Post View
def search_post_view(request):
    query = request.GET.get('q')
    posts = PostsModel.objects.all()

    if query:
        posts = posts.filter(title__icontains=query)

    return render(request, "posts/search_post.html", {'posts': posts})

# List Posts View (Optional: for the posts listing page)
def posts_list_view(request):
    posts = PostsModel.objects.all()
    return render(request, "posts/posts_list.html", {'posts': posts})
