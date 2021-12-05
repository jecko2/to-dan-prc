from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    subject = models.ManyToManyField('Task')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Task(models.Model):
    SUBJECT_CHOICE = (
        ('MR', 'Movie Review'),
        ('EW', 'Essay Writing'),
        ('TW', 'Thesis Writing'),
        ('DW', 'Dissertation Writing'),
        ('AW', 'Assignment Writing'),
        ('PS', 'Personal Statement'),
        ('CSW', 'Case Study Writing'),
        ('CPW', 'Capstone Project Writing'),
        ('SW', 'Speech Writing'),
        ('LRW', 'Lab Report Writing'),
    )
    ACADEMIC_LEVEL = (
        ('HS', 'High School'),
        ("CL", 'College'),
        ("UG", 'Undergraduate'),
        ('PM', 'PostGraduate-Masters'),
        ('PPH', 'PostGraduate-Phd'),
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICE)
    academic_level = models.CharField(max_length=300, choices=ACADEMIC_LEVEL)
    pages = models.PositiveIntegerField()
    word_count = models.PositiveIntegerField()
    additional_files = models.FileField(upload_to='media', blank=True, null=True,)
    images = models.FileField(upload_to='media', blank=True, null=True)
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    
    def __str__(self):
        return str(self.client)



