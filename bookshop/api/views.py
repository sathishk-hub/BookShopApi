from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Bookserializers, Userserializers, Transactionserializers
from .models import Book, User, Transaction

# Create your views here.
class BookView(APIView):

    def get(self, request, *args, **kwargs):
        book_serializer = Bookserializers(Book.objects.all(), many=True)
        return  Response(book_serializer.data)

    def post(self, request, *args, **kwargs):
        book_serializer = Bookserializers(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')

        else:
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs): 
        update_content = Transaction.objects.filter(book_name=request.data.get('book_name'),author_name=request.data.get('author_name'))
        update_content.update(book_name=request.data.get('up_book_name'),author_name=request.data.get('up_author_name'))
        return Response(status=status.HTTP_200_OK)    

    def delete(self, request, *args, **kwargs):
        del_content = Transaction.objects.filter(book_name=request.data.get('book_name'),author_name=request.data.get('author_name'))
        del_content .delete()
        return Response(status=status.HTTP_200_OK)    
      

class UserView(APIView):

    def get(self, request, *args, **kwargs):
        user_serializer = Userserializers(User.objects.all(), many=True)
        return  Response(user_serializer.data)

    def post(self, request, *args, **kwargs):
       user_serializer = Userserializers(data=request.data)
       if user_serializer.is_valid():
           user_serializer.save()
           return Response(user_serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
       else:
           return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionView(APIView):

    def get(self, request, *args, **kwargs):
        transaction = Transaction.objects.all()
        transaction_serializer = Transactionserializers(transaction, many=True)
        return  Response(transaction_serializer.data)

    def post(self, request, *args, **kwargs):
       book_serializer = Transactionserializers(data=request.data)
       if book_serializer.is_valid():
          book_serializer.save()
          return Response(book_serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
       else:
          return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, *args, **kwargs):           
       del_content = Transaction.objects.filter(number=request.data.get('number'))
       del_content .delete()
       return Response(status=status.HTTP_200_OK)    
      
       