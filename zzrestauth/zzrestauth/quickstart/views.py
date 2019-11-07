from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from zzrestauth.quickstart.serializers import UserSerializer, GroupSerializer


# This mixin force everything ReadOnly at View layer.
# It seems to be precedence all permissions set at upper layers i.e. urls route and settings
# Experiment with ModelViewSet vs ReadOnlyListViewset
class ReadOnlyListViewset(
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass


# class UserViewSet(ReadOnlyListViewset):
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.IsAuthenticated,)

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
class GroupViewSet(ReadOnlyListViewset):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
