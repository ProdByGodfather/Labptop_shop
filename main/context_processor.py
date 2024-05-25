from main.models import Category


def cate_show(request):
    cate = Category.objects.all()
    return {'category': cate}