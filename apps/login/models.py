from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters!"
        if len(postData['reg_email']) < 2:
            errors['reg_email'] = "Email should be at least 2 characters!"
        if len(postData['reg_password']) < 8:
            errors['reg_password'] = "Password should be at least 8 characters!"
        if postData['reg_password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords must match!"

        return errors
    
    def login_validator(self, postData):
        errors = {}

        if len(postData['log_email']) < 2:
            errors['log_email'] = "Email should be at least 2 characters!"
        if len(postData['log_password']) < 8:
            errors['log_password'] = "Password should be at least 8 characters!"

        # if 'email' in Info:
        #     errors['email'] = "The User already exists, please login"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = (models.CharField(max_length=255))
    objects = UserManager()

    def __repr__(self):
        return f"<User object: {self.first_name} {self.last_name} {self.email} {self.password}>"

