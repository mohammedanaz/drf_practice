from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

class Author(models.Model):
    '''
    To store datas of Authors.
    '''
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    '''
    To store datas of books. it has FK relation to Author model.
    '''
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


class Store(models.Model):
    '''
    To store datas of shops. it has M2M relation to Book model.
    '''
    name = models.CharField(max_length=100, null=False, blank=False)
    book = models.ManyToManyField(Book, related_name='stores')

    def __str__(self):
        return self.name


@receiver(post_save, sender=Book)
@receiver(post_delete, sender=Book)
def delete_cache_books(sender, **kwargs):
    '''
    This signal receiver function deletes books cache upon adding, updating 
    or deleting book instances.
    '''
    cache.delete('books')
    print('books cache deleted.')