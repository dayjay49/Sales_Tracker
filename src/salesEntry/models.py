from django.db import models

# Create your models here.
class SalesEntry(models.Model):

    # JEFFTERRY = 'JT'
    # THOMASBLACK = 'TB'
    # JOHNRICE = 'JR'
    # LARRYLONG = 'LL'
    # STAFF_CHOICES = [
    #     (JEFFTERRY, 'Jeff Terry'),
    #     (THOMASBLACK, 'Thomas Black'),
    #     (JOHNRICE, 'John Rice'),
    #     (LARRYLONG, 'Larry Long'),
    # ]
    # FRESHLEMON = 'FLL'
    # ORANGELEMON = 'OLS'
    # SUGARSHOCKER = 'SS'
    # WILDWHISKEY = 'WWW'
    # DRINK_CHOICES = [
    #     (FRESHLEMON, 'Fresh Lemon Lemonade'),
    #     (ORANGELEMON, 'Orange & Lemon Splash'),
    #     (SUGARSHOCKER, 'Sugary Shocker'),
    #     (WILDWHISKEY, 'Wild Whiskey Whack')
    # ]

    # drink = models.CharField(
    #     max_length=50,
    #     choices=DRINK_CHOICES,
    #     default=FRESHLEMON
    # )
    # staffName = models.CharField(
    #     max_length=40,
    #     choices=STAFF_CHOICES,
    #     default=THOMASBLACK
    # )
    staffName = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    # quantity = models.PositiveSmallIntegerField()
