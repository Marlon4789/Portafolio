from django.shortcuts import render, redirect, get_object_or_404

from .models import QuillPost
from .forms import QuillPostForm


def layout_base(request):
    return render(request, 'layouts/base_blog.html')

def model_form_view(request):
    if request.method == 'POST':
        form = QuillPostForm(request.POST)
        if form.is_valid():
            quillpost = form.save()
            return redirect('show_all_posts')

    else:
        form = QuillPostForm()
    return render(request, 'content/create_post.html', {'form': form})


def quillpost_detail(request, quillpost_id):
    quillpost = get_object_or_404(QuillPost, pk=quillpost_id)
    quill_content_html = quillpost.content.html
    return render(request, 'content/detail.html', {'quill_content_html': quill_content_html, 'quillpost': quillpost})


def show_all_post(request):
    quill_posts = QuillPost.objects.all().order_by('-id')
    return render(request, 'content/show_all_posts.html', {'quill_posts': quill_posts})

