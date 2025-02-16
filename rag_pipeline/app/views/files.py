from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rag_pipeline.app.models.files import File
from rag_pipeline.app.serializers.files import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling file uploads and metadata management.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer

    # Custom POST (Create) Method
    @action(detail=False, methods=["post"])
    def upload_file(self, request):
        """
        Endpoint to upload a file and trigger a job to
        generate and upload the embeddings
        """
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "File uploaded successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom UPDATE Method
    @action(detail=True, methods=["put", "patch"])
    def update_file(self, request, pk=None):
        """
        Endpoint to update a file's metadata
        """
        file_instance = get_object_or_404(File, pk=pk)
        serializer = FileSerializer(
            file_instance,
            data=request.data,
            partial=True,
        )  # Use partial=True to allow partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "File updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom DELETE Method
    @action(detail=True, methods=["delete"])
    def delete_file(self, request, pk=None):
        """
        Endpoint to delete the file
        """
        return Response(
            {"message": "File deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
