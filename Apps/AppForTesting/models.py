from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Cat(models.Model):
    name = models.CharField(max_length = 150)
    breed = models.CharField(max_length = 150)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    class Meta:
        verbose_name = ("Cat")
        verbose_name_plural = ("Cats")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Cat_detail", kwargs={"pk": self.pk})


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1, 
        choices=MEALS, 
        default=MEALS[0][0]
        )
    cat = models.ForeignKey("Cat", on_delete=models.CASCADE) 

    class Meta:
        verbose_name = ("Feeding")
        verbose_name_plural = ("Feedings")

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    def get_absolute_url(self):
        return reverse("Feeding_detail", kwargs={"pk": self.pk})
