from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from django.forms import ModelForm


class college(models.Model):

    # ...
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default="", blank=False)

    def __str__(self):
        return self.name


SEMESTER_CHOICES = (
    ("gym", "gym"),
    ("bookStore", "bookStore"),
    ("medicalFacility", "medicalFacility"),
    ("hostel", "hostel"),
    ("Restaurant", "Restaurant"),
    ("Event", "Event"),

)


class shop(models.Model):

    # ...
    ShopName = models.CharField(max_length=55,)
    image = models.ImageField(upload_to='uploads/', default="demo.jpg")
    college = models.ForeignKey(college, on_delete=models.CASCADE, related_name='college'
                                )
    Type = models.CharField(max_length=255, choices=SEMESTER_CHOICES)
    description = models.CharField(max_length=300)
    distance = models.FloatField()
    phoneNumber = models.IntegerField()

    rating = models.FloatField()
    AveragePrice = models.IntegerField()
    Direction = models.CharField(max_length=300)
    Amenities = models.CharField(max_length=100)
    address = models.CharField(max_length=300)

    time = models.CharField(max_length=100)

    def __str__(self):
        return self.ShopName


class PostImage(models.Model):
    post = models.ForeignKey(shop, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.ShopName


class suggestions(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class suggestionsForm(ModelForm):
    class Meta:
        model = suggestions
        fields = ['name', 'email', 'message']


class faqs(models.Model):
    question = models.CharField(primary_key=True, max_length=200)
    answer = models.CharField(max_length=600)

    def __str__(self):
        return self.question
