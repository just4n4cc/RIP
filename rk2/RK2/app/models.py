from django.db import models


class BookManager(models.Manager):
    def ordered(self):
        return self.all().order_by('title')

    def report(self):
        books = self.all().order_by('lib_id')
        return books


class LibManager(models.Manager):
    def ordered(self):
        return self.all().order_by('name')


class Book(models.Model):
    book_id = models.AutoField('book_id', primary_key=True)
    author = models.CharField('Author', max_length=50)
    title = models.CharField('Title', max_length=50)
    pub_year = models.IntegerField('Publish year')
    lib_id = models.ForeignKey('Library', models.DO_NOTHING, db_column='lib_id')

    objects = BookManager()


class Library(models.Model):
    lib_id = models.AutoField('lib_id', primary_key=True)
    name = models.CharField('Name', max_length=50)
    phone = models.CharField('Phone', max_length=30)
    email = models.CharField('Email', max_length=50)

    objects = LibManager()

    def __str__(self):
        return str(self.name)

