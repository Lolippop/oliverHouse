__author__ = 'oliver'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','oliverHouse.settings')

import django
django.setup()

from bgapplication.models import Category,Page
def populate():
    python_cat = add_cat('Python')
    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/")
    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")
    django_cat = add_cat("Django")
    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")
    frame_cat = add_cat("Other Frameworks")

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c),str(p))

def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)
    return p
def add_cat(name):
    c = Category.objects.get_or_create(name=name)
    return c

if __name__ == '__main__':
    print "Starting"
    populate()