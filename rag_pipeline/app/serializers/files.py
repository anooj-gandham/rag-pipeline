from rest_framework import serializers

from rag_pipeline.app.models.files import File


class FileSerializer(serializers.ModelSerializer):
    """
    Serializer for the File model.
    """

    class Meta:
        model = File
        fields = "__all__"
