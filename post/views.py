from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from post.services.post_service import (
    create_post,
)

class PostView(APIView):
    """
    게시글의 CRUD를 담당하는 View
    """
    def post(self, request):
        try:
            if request.data:
                create_post(request.data)
                return Response({'detail': '게시물을 작성했습니다.'}, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError as e:
            name = list(e.detail.keys())[0]
            error = ''.join([str(value) for values in e.detail.values() for value in values])
            return Response({name: error}, status=status.HTTP_400_BAD_REQUEST)