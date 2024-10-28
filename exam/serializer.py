from rest_framework import serializers
from .models import Registeration, Register
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class ResgisterationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Registeration
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'DOB']
    
    # def validate(self, data):

    #     if not Registeration.objects.filter(first_name=data['first_name']).capitalize():
    #         raise serializers.ValidationError("First name must be capital")
        
    #     if not Registeration.objects.filter(last_name=data['last_name']).capitalize():
    #         raise serializers.ValidationError("Last name must be capital")
        
    #     if Registeration.objects.len(phone_number=data['phone_number']) < 11:
    #         raise serializers.ValidationError("Phone number must be 11 digits")
        
    #     if Registeration.objects.len(phone_number=data['phone_number']) > 11:
    #         raise serializers.ValidationError("Phone number must not exceed 11 digits") 
        
    #     if Registeration.objects.filter(DOB=data['DOB'])  :
            
        
    #     return data      

    
    def create(self, data):
        
        register = Registeration.objects.create_user(
            first_name = data.get['first_name'],
            last_name = data.get['last_name'],
            phone_number = data.get['phone_number'],
            email = data.get['email'],
            password = data.get['password'],
            DOB = data.get['DOB']
            )
        
        register.save()

        stringrep = render_to_string("Verification.html", {
        "name": data['email'],
        "verification_link": f"http://localhost:3000/verify/{user.id}"
        

        })
    
        striphtml = strip_tags(stringrep)

        theemail = EmailMultiAlternatives(
        subject= "verification",
        body= striphtml,
        from_email= "netodboss@gmail.com",
        to= [data['email']]
        )

        theemail.attach_alternative(stringrep, "text/html")

        theemail.send()
   
        return register
    

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
    
    def create(self, data):

        Register.objects.create(
            phone_number=data['phone_number'],
            mobile_network=data['mobile_network']
        )

        return data



    


        
        

