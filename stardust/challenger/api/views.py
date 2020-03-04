from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class IndexView(APIView):
    def get(self, request):
        print(request)
        data = request
        return Response(data, status=status.HTTP_200_OK)