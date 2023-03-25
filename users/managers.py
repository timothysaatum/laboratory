from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


#class CustomManager(BaseUserManager):
#
#	def create(self, email, password, **extra_fields):
#		if not email:
#			raise ValueError('Official email name must be set')
#		email = self.normalize_email(email)
#		user = self.model(email=email, **extra_fields)
#		user.set_password(password)
#		user.save()
#
#		return user
#
#
#	def create_superuser(self, email, password, **extra_fields):
#		extra_fields.setdefault('is_staff', True)
#		extra_fields.setdefault('is_superuser', True)
#		extra_fields.setdefault('is_active', True)
#
#		if extra_fields.get('is_staff') is not True:
#			raise ValueError('Superuser must have is_staff=True')
#		if extra_fields.get('is_superuser') is not True:
#			raise ValueError('Superuser must have is_superuser=True')
#		return self.create_user(email, password, **extra_fields)





class CustomManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, telephone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            telephone=telephone,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user