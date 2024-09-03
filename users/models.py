from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Manajemen User
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email harus diisi")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# Model User
class User(AbstractBaseUser):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    objects = UserManager()

    def __str__(self):
        return self.email

# Model Kategori Pelatihan
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Model Pelatihan
class Training(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='trainings', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - {self.instructor}"

# Model Pelatihan yang Diikuti User
class UserTraining(models.Model):
    user = models.ForeignKey(User, related_name='trainings', on_delete=models.CASCADE)
    training = models.ForeignKey(Training, related_name='users', on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.fullname} - {self.training.title}"
