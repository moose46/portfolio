from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Post, Comment

# Create your views here.
"""
Note: The life cycle of submitting a form can be a little complicated, so here’s an outline of how it works:

When a user visits a page containing a form, they send a GET request to the server.
In this case, there’s no data entered in the form, so we just want to render the form and display it.
When a user enters information and clicks the Submit button, a POST request,
containing the data submitted with the form, is sent to the server.
At this point, the data must be processed, and two things can happen:
 The form is valid, and the user is redirected to the next page.
 The form is invalid, and empty form is once again displayed.
 The user is back at step 1, and the process repeats.
"""


def blog_index(request):
    """ return a list of blogs """
    posts = Post.objects.all().order_by('-created_on')

    context = {
        'posts': posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    """ Return a list of categories """
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog_category.html", context=context)


# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     comments = Comment.objects.filter(post=post)
#     context = {
#         "post": post,
#         "comments": comments,
#     }

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)
