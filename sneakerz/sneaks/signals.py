'''from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from .models import customer



 def create_customer(sender, instance, created, **kwargs):
        #check if instance is created
        if created:
            Customer.objects.create(user=instance)
            print('Customer created')

    post_save.connect(create_customer, sender=User) #create_customer is the reciever

    def update_customer(sender, instance, created, **kwargs):
        if created == False:
            instance.customer.save()
            print('Customer updated')

    post_save.connect(update_customer, sender=User) #update_customer is the reciever'''