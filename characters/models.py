from django.db import models


class Character(models.Model):

    # GENDERS Keys
    MALE = "M"
    FEMALE = "F"
    NON_SPECIFIED = ""

    # GENDER Choices
    GENDER_CHOICES = [
        (NON_SPECIFIED, "Not specified"),
        (MALE,"Male"),
        (FEMALE,"Female"),
    ]

    # NATIONALITY Keys

    JAPAN = "JP"
    MEXICO = "MX"
    CARIBBEAN = "BQ"
    FRANCE = "FR"
    SWEDEN = "SE"
    EGYPT = "EG"
    CZECHIA = "CZ"
    USA = "US"
    ICELAND = "IS"
    KENYA = "KE"

    # NATIONALITY Choices

    NATIONALITY_CHOICES = [
        (MEXICO, "Mexico"),
        (JAPAN, "Japan"),
        (CARIBBEAN, "Caribbean"),
        (FRANCE, "France"),
        (SWEDEN, "Sweden"),
        (EGYPT, "Egypt"),
        (CZECHIA, "Czechia"),
        (USA, "United States of America"),
        (ICELAND, "Iceland"),
        (KENYA, "Kenya"),
    ]

    # Attributes
    name = models.CharField(max_length=255)
    japanese_name = models.CharField(max_length=255, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, default=NON_SPECIFIED)
    age = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="character_image", blank=True, null=True )

    def __str__(self) -> str:
        return self.name


class Body(models.Model):

    # Attributes
    type = models.CharField(max_length=255)
    motif = models.CharField(max_length=255)

    class Meta:
        ordering = ('type',)
        verbose_name = 'Body Type'
        verbose_name_plural = 'Body Types'
    
    def __str__(self) -> str:
        return f"{self.type} - {self.motif}"


class Medal(models.Model):

    # Attributes
    name = models.CharField(max_length=255)
    japanese_name = models.CharField(max_length=255, default="")
    letter = models.CharField(max_length=1)
    attribute = models.CharField(max_length=255)
    nature = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="medal_image", blank=True, null=True )

    class Meta:
        ordering = ('letter',)
        verbose_name = 'Medal'
        verbose_name_plural = 'Medals'

    def __str__(self) -> str:
        return self.name


class Medarot(models.Model):

    # GENDERS Keys
    MALE = "M"
    FEMALE = "F"
    NON_SPECIFIED = ""

    # GENDER Choices
    TINPET_CHOICES = [
        (NON_SPECIFIED, "Not specified"),
        (MALE,"Male"),
        (FEMALE,"Female"),
    ]
    
    # Attributes
    name = models.CharField(max_length=255)
    japanese_name = models.CharField(max_length=255, default="")
    tinpet = models.CharField(max_length=1, choices=TINPET_CHOICES, default=NON_SPECIFIED, blank=False)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="medarot_image", blank=True, null=True)
    serial_no = models.CharField(max_length=255)
    head = models.CharField(max_length=255)
    r_arm = models.CharField(max_length=255)
    l_arm = models.CharField(max_length=255)
    legs  = models.CharField(max_length=255)

    # RELATIONS
    body = models.ForeignKey(Body, related_name="medarots", null=True, on_delete=models.SET_NULL)
    medal = models.ForeignKey(Medal, related_name="medarots", blank=True, null=True, on_delete=models.SET_NULL)
    medarotter = models.ForeignKey(Character, related_name="medarots",blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:

        ordering = ['body__type',]
        verbose_name_plural = 'Medarots'

    def __str__(self) -> str:
        return self.name