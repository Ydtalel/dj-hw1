from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from .filters import AdvertisementFilter
from .models import Advertisement
from .permissions import IsOwnerOrAdminOrReadOnly
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        pass

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrAdminOrReadOnly()]
        return []

    # @action(detail=True, methods=['post'])
    # def add_fav(self, request, pk=None):
    #     user = self.get_object()
    #     adv = Advertisement.objects.filter(id=pk)
    #     serializer = AdvertisementSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.validated_data['password'])

    @action(detail=False, methods=['get'])
    def closed_ads(self, request):
        closed = Advertisement.objects.filter(status="CLOSED")
        serializer = AdvertisementSerializer(closed, many=True)

        return Response(serializer.data)

    # @action(detail=True, methods=['get'])
    # def add_favorite(self, request, pk=None):
    #     adv = self.get_object()
    #     adv.favorites =
    #
    #     serializer = AdvertisementSerializer(adv)
    #     if serializer.is_valid():
    #         self.get_object().favorites.add_favorite(serializer.validated_data)
    #     print(serializer)
    #
    #     return Response(serializer.data)

    # @action(detail=True, methods=['post'])
    # def custom_action(self, request, pk=None):
    #     instance = self.get_object()
    #     # Do something with the object
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # @action(detail=True, methods=['post'])
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.validated_data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})

# @action(methods=['post'], detail=True)
#     def follow(self, request, *args, **kwargs):
#         user = self.get_object()
#         target_user = int(kwargs['target_id'])
#         Follow.objects.create(user=user, target=target_user)
#         return Response(status=status.HTTP_204_NO_CONTENT)

# urlpatterns = [
#                   path('users/<int:pk>/follow/<int:target_id>/', UserViewSet.as_view({"post": "follow"}))

              # ]