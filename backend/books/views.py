from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class CreateBook(APIView):
    def post(self, request):
        title = request.data['title']
        existingbook = Book.objects.filter(title=title)
        if existingbook:
            return Response({'message': 'Book with this title already exists'}, status=304)
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response({'message': 'Book Created', 'book': book.data})
        else:
            return Response({'message': 'Book cant be Created... Try Again'}, status=304)

class GetBook(APIView):
    def get(self, request):
        books = Book.objects.all()
        if not books:
            return Response({'message': 'No Book Found'}, status=404)
        serialized = BookSerializer(books, many=True)
        return Response({'message': 'Books Found', 'data': serialized.data})

class UpdateBook(APIView):
    def post(self, request):
        id = request.data['id']
        newgenre = request.data['newgenre']
        newauth = request.data['newauthor']
        book = Book.objects.get(pk=id)
        if not book:
            return Response({'message': 'Not Found'}, status=404)
        book.genre = newgenre
        book.author = newauth
        return Response({"message": 'Updated'})

class DeleteBook(APIView):
    def post(self, request):
        id = request.data['id']
        book = Book.objects.get(pk=id)
        if not book:
            return Response({"message": "Book Not Found"}, status=404)
        book.delete()
        return Response({'message': 'Deleted Successfully'})