from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, user, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not user:
            raise ValueError('Error: The User you want to create must have an username, try again')

        my_user = self.model(
            user=self.model.normalize_username(user),
        )

        my_user.set_password(password)
        my_user.save(using=self._db)
        return my_user

    def create_superuser(self, user, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        my_user = self.create_user(
            user,
            password=password,
        )
        my_user.staff = True
        my_user.admin = True
        my_user.save(using=self._db)
        return my_user
