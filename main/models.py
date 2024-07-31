from django.db import models

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
