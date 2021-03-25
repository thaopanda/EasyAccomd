from Post.models import Post
from Account.models import Renter, MyUser
from Notification.models import Notification
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


class NotificationList(APIView):
    permission_classes = (AllowAny,)
    class NotificationListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Notification
            fields = ['message', 'time']

    def get(self, request, format=None):
        notificationList = Notification.objects.filter(user=request.user, read=False)
        for i in notificationList:
            i.read = True
            i.save()
        serializer = self.NotificationListSerializer(notificationList, many=True)
        return Response(serializer.data)

class ReadNotificationView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, pk, format=None):
        notification = Notification.objects.get(pk=pk)
        notification.read = True
        notification.save()
        return(Response(f'ok'))

class CreateNotification(APIView):
    permission_classes = (IsAuthenticated,)
    class CreateNotification(serializers.ModelSerializer):
        class Meta:
            model = Notification
            fields = ['message']
    
    def post(self, request, pk, format=None):
        user = MyUser.objects.get(pk=pk)
        serializer = self.CreateNotification(data=request.data)
        if(serializer.is_valid()):
            Notification.objects.CreateNotification(user, serializer.validated_data['message'])
            return Response(f'ok')
        return Response(f'not ok')