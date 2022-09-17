from django.contrib.auth.hashers import check_password
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from post.services.post_service import (
    get_post,
    create_post,
    update_post,
    delete_post
)
from post.models import Post as PostModel


class PostView(APIView):
    """
    게시글의 CRUD를 담당하는 View
    """
    def get(self, request):
        params = request.GET.get('page', '1')
        page = int(params) - 1
        posts_serializer = get_post(page)
        return Response(posts_serializer, status=status.HTTP_200_OK)


    def post(self, request):
        try:
            if request.data:
                create_post(request.data)
                return Response({'detail': '게시물을 작성했습니다.'}, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError as e:
            name = list(e.detail.keys())[0]
            error = ''.join([str(value) for values in e.detail.values() for value in values])
            return Response({name: error}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, post_id):
        try:
            post = PostModel.objects.get(id=post_id)
        except PostModel.DoesNotExist:
            return Response({'detail': '수정할 게시글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        if check_password(request.data.pop('password'), post.password):
            if request.data['content'] == {}:
                return Response({'detail': '수정할 내용이 비어있습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            if post.content == request.data['content']: 
                return Response({'detail': '수정할 내용을 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST) 
            updated_log = update_post(post_id, request.data)
            return Response(updated_log, status=status.HTTP_201_CREATED)
        return Response({'detail': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
    def delete(self, request, post_id):
        try:
            post = PostModel.objects.get(id=post_id)    
        except PostModel.DoesNotExist:
            return Response({'detail': '삭제할 게시글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        if check_password(request.data.pop('password'), post.password):
            delete_post(post_id)
            return Response({'detail': '게시글이 삭제되었습니다.'}, status=status.HTTP_200_OK)
        return Response({'detail': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)