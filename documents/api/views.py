from rest_framework.views import (
    APIView,
)

from rest_framework.response import Response

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.permissions import (
    AllowAny,
)

from .serializers import DocumentUploadSerializer


class DocumentUploadView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = DocumentUploadSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = DocumentUploadSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response({'message': 'Document uploaded successfully'},
                            status=HTTP_200_OK)
        # return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)