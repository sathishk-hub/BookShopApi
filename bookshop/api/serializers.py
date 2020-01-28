from rest_framework import serializers
from .models import User, Book, Transaction

class Userserializers(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = '__all__'

class Bookserializers(serializers.ModelSerializer):
   class Meta:
      model = Book
      fields = '__all__'

class Transactionserializers(serializers.ModelSerializer):
   class Meta:
      model = Transaction
      fields = '__all__'

