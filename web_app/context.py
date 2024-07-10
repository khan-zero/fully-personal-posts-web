from .models import *
from django.contrib.auth.models import User

def get_context():
    everything_p = Post.objects.all()
    category = Category.objects.all()
    single_post = Blog_area_single_post.objects.all()
    list_post = Blog_area_list_post.objects.all()
    single_widget = Single_widget_area.objects.all()
    instagram_item = Instagram_item.objects.all()
    user_info = User.objects.all()
    user_adress = Adress.objects.all()
    
    context = {
        'posts': everything_p,
        'categories': category,
        'single_post': single_post,
        'list_post': list_post,
        'single_widget': single_widget,
        'insta_item': instagram_item,
        'user_info': user_info,
        'user_adress': user_adress
    }
    return context
