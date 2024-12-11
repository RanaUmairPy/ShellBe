from django.shortcuts import render
from post.models import PostsModel


def createposts_view(request):
    if request.method=="POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        content_type = request.POST.get("type")
        image = request.FILES.get("image")
        
        if title and content and content_type:
            post = PostsModel.objects.create(
                              title=title,
                              content=content,
                              content_type=content_type,
                              image=image
                                   )
            
            #post.save() or objects.create()
            
    return render(request,"createposts.html")
        
        
        
def post_display_view(request):
    posts = PostsModel.objects.all()
    return render(request,'postdisplay.html',{"posts":posts})