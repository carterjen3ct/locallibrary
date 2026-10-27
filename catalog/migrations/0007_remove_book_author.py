from django.db import migrations


def authorize_books(apps, schema_editor):
    Book = apps.get_model("catalog", "Book")
    BookAuthor = apps.get_model("catalog", "BookAuthor")

    for book in Book.objects.exclude(author_id=None):
        if not BookAuthor.objects.filter(book=book, author_id=book.author_id).exists():
            next_order = BookAuthor.objects.filter(book=book).count() + 1
            BookAuthor.objects.create(book=book, author_id=book.author_id, author_order=next_order)


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_book_author'),
    ]

    operations = [
        migrations.RunPython(authorize_books),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]
