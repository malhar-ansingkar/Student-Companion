from rest_framework import serializers
from .models import shop


class ShopSerializer(serializers.ModelSerializer):

    ShopName = serializers.CharField()
    image = serializers.ImageField()
    college = serializers.CharField()
    Type = serializers.CharField()
    description = serializers.CharField()
    distance = serializers.FloatField()
    phoneNumber = serializers.IntegerField()

    rating = serializers.FloatField()
    AveragePrice = serializers.IntegerField()
    Direction = serializers.CharField()
    Amenities = serializers.CharField()
    address = serializers.CharField()

    time = serializers.CharField(max_length=100)

    class Meta:
        model = shop
        fields = ('ShopName', 'image', 'college', 'Type', 'description', 'distance', 'phoneNumber',
                  'rating', 'AveragePrice', 'Direction', 'Amenities', 'address', 'time')
