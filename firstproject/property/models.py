from django.conf import settings
from django.db import models

REGION = (
    ('Italy', 'Italy'),
    ('Spain', 'Spain'),
    ('Croatia', 'Croatia'),
    ('Montenegro', 'Montenegro'),
    ('Albania', 'Albania'),
)

YESNO = (
    ('Yes', 'Yes'),
    ('No', 'No'),

)


# Create your models here.
class Property(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=40)
    region = models.CharField(max_length=30, choices=REGION)  # регіон
    description = models.TextField()  # опис
    image = models.ImageField(upload_to='static/images', default='image_8.jpg')
    lot_area = models.DecimalField(max_digits=9, decimal_places=2)
    floor_area = models.DecimalField(max_digits=9, decimal_places=2)
    bed_room = models.IntegerField()
    bath_room = models.IntegerField()

    year_build = models.IntegerField(default=2019)
    floors = models.IntegerField(default=2)
    garage = models.CharField(max_length=3, choices=YESNO, default='Yes')
    luggage = models.CharField(max_length=3, choices=YESNO, default='Yes')

    price = models.DecimalField(max_digits=9, decimal_places=2)

    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # get url page, single property
    def get_url_property(self):
        return f'/property/property_detail/{self.id}'

    # get url page for editing single property
    def get_url_property_edit(self):
        return f'/property/property_edit/{self.id}'

    # get url page for delete single property
    def get_url_property_delete(self):
        return f'/property/property_delete/{self.id}'
