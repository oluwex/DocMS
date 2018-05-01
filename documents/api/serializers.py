from rest_framework.serializers import (
    ModelSerializer
)

from documents.models import Document


class DocumentUploadSerializer(ModelSerializer):

    class Meta:
        model = Document
        fields = [
            'doc',
        ]

    def validate(self, data):
        document_file = data.get('doc', None)
        # print(document_file)
        print(document_file.content_type)
        return data
