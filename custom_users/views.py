import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from rest_framework import views, response, status

from custom_users.models import CustomUser
from custom_users.serializers import CustomUserSerializer
from custom_users.tasks import send_welcome_email
from services.sqs import SQSService


class ListCreateCustomUser(views.APIView):
    def get(self, request):
        queryset = CustomUser.objects.all()
        logging.info("Middle log")
        serializer = CustomUserSerializer(queryset, many=True)
        return response.Response({"users": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        user = CustomUser(**request.data)
        try:
            user.save()
            # SQSService().send_message(
            #     "Sending email to new user",
            #     {
            #         "title": {"DataType": "String", "StringValue": "Mail sending"},
            #         "body": {"DataType": "String", "StringValue": "Congrats new user"},
            #         "email": {
            #             "DataType": "String",
            #             "StringValue": user.email,
            #         },
            #         "name": {
            #             "DataType": "String",
            #             "StringValue": user.name,
            #         },
            #     }
            # )
            # send_welcome_email.delay(user.name, user.email)
            # SESService().send_email(f"Welcome, {user.name}!", "Welcome to our website, and thanks for your registration.", user.email)
        except IntegrityError as ex:
            pass
        # serializer = CustomUserInSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response({"message": "ok"})


class CustomUserDetails(views.APIView):
    def get(self, request, pk):
        user = CustomUser.objects.get(id=pk)

        try:
            user = CustomUser.objects.get(id=pk)
        except ObjectDoesNotExist:
            return response.Response(
                {"message": "Catched"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CustomUserSerializer(user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
