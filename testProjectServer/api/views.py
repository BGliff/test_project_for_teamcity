from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Client, ClientProfile
from api.serializers import ClientSerializer, ClientProfileSerializer, ClientItem, ClientItemSerializer


@permission_classes((IsAuthenticated,))
class ClientView(APIView):
    def post(self, request):
        data = request.data

        profile_serializer = ClientProfileSerializer(data=data)
        profile_serializer.is_valid(raise_exception=True)
        profile = profile_serializer.save()

        client_serializer = ClientSerializer(data=data)
        client_serializer.is_valid(raise_exception=True)
        client = client_serializer.save()

        client.profile = profile
        client.save()

        serializer = ClientItemSerializer(prepare_clients([client])[0])

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        data = request.data

        client = get_object_or_404(Client, id=id)

        client_serializer = ClientSerializer(data=data, instance=client)
        client_serializer.is_valid(raise_exception=True)
        client_serializer.save()

        profile_serializer = ClientProfileSerializer(data=data, instance=client.profile)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        serializer = ClientItemSerializer(prepare_clients([client])[0])

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        client = get_object_or_404(Client, id=id)
        client.profile.delete()
        client.delete()

        return Response({'message': 'deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_all_clients(request):
    clients = Client.objects.all()
    serializer = ClientItemSerializer(prepare_clients(clients), many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


def prepare_clients(clients):
    items = []

    for client in clients:
        client_item = ClientItem(
            id=client.id,
            first_name=client.first_name,
            last_name=client.last_name,
            date_of_birth=client.date_of_birth,
            gender=client.gender,
            photo_url=client.profile.photo_url
        )
        items.append(client_item)

    return items



