from django.db.models import Avg

from store.models import UserBookRelation


def set_rating(book):
    raiting =  UserBookRelation.objects.filter(book = book).aggregate(raiting = Avg('rate')).get('raiting')
    book.raiting = raiting
    book.save()
