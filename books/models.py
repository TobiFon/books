from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
class Book(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  
  def __str__(self):
      return self.title
  def get_absolute_url(self):
      return reverse("book_detail", kwargs={"pk": self.pk})
    
class Review(models.Model):
  
  book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
  review = models.CharField(max_length=200)
  arthur = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  
  def __str__(self):
      return self.review
  
  
  
