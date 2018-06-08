from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.

#list of posts
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')      #filter all posts where published date is earlier or equal to current date, order by published date
    return render(request, 'blog/post_list.html', {'posts':posts})                                  #render post_list.html template with parameter 'posts'

#post details page with parameter pk (primary key)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)                               #get either object with existing ID or 404 page
    return render(request, 'blog/post_detail.html', {'post':post})      #render post_detail.html template with parameter 'post'

#add post form
def post_new(request):
    if request.method == 'POST':                            #if data was sent to POST (form was saved)
        form = PostForm(request.POST)                       #create model PostForm with POST request parameters
        if form.is_valid():                                 #if form is valid
            post = form.save(commit=False)                  #don't save form yet
            post.author = request.user                      #add author to form
            #post.published_date = timezone.now()            #add published_date to form
            post.save()                                     #save form
            return redirect('post_detail', pk=post.pk)      #redirect to post_detail page with parameter pk = post primary key
    else:                                                                   #if no data was sent to POST
        form = PostForm()                                                   #create empty model PostForm

    return render(request, 'blog/post_edit.html', {'form':form})        #display new post form template post_edit.html with parameter 'form'

#edit post form. Send parameter pk (primary key)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)                   #get either object with existing ID or 404 page
    if request.method == 'POST':                            #if data was sent to POST (form was saved)
        form = PostForm(request.POST, instance=post)        #create PostForm model with all request parameters and existing instance 'post'
        if form.is_valid():                                 #if form is valid
            post = form.save(commit=False)                  #don't save form yet
            post.author = request.user                      #add author to form
            #post.published_date = timezone.now()            #add published_date to form
            post.save()                                     #save form
            return redirect('post_detail', pk=post.pk)      #redirect to post_detail view method with parameter pk = post primary key
    else:                                                               #if no data was sent to POST
        form = PostForm(instance=post)                                  #create PostForm model with existing instance 'post'

    # display post_edit.html template with parameter 'form'. Since form object was created using instance of existing instance 'post', fields will be filled with data
    return render(request, 'blog/post_edit.html', {'form':form})

#list of unpublished posts - drafts
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull = True).order_by('created_date')   #filter all posts where published_date is null, order by created_date
    return render(request, 'blog/post_draft_list.html', {'posts':posts})                   #render post_draft_list.html template with parameter 'posts'

#publish post, take parameter pk (primary key)
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)           #get either object with existing ID or 404 page
    post.publish()                                  #publish post
    return redirect('post_detail', pk=post.pk)      #redirect to post_detail view method with parameter pk = post primary key

#delete post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()                                   #django model method delete() that deletes the record from db
    return redirect('post_list')