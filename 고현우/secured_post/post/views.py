from rest_framework.views import APIView
from rest_framework import status, exceptions
from rest_framework.response import Response

from post.Services.post_service import (
    get_post,
    create_post,
    update_post,
    delete_post,
    check_is_password,
    )
from post.models import Post as PostModel

# Create your views here.

class PostView(APIView):
    """
    post의 CRUD를 담당하는 View
    """
    def get(self, request):
        try :
            page = int(self.request.query_params.get("page"))
        except TypeError:
            page == 1
        
        if get_post(page) == {}:
            return Response({"detail" : "아직 게시글이 존재하지 않습니다. 제일 먼저 만들어보세요!!"}, status=status.HTTP_200_OK)
        page_post_serializer = get_post(page)
        return Response(page_post_serializer, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            create_post(request.data)
            return Response({"detail" : "게시글을 작성하였습니다."}, status=status.HTTP_200_OK)
        except exceptions.ValidationError:
            return Response({"detail" : "형식을 벗어난 입력값이 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, post_id):
        if check_is_password(request.data, post_id):
            try:
                update_post(request.data, post_id)
                return Response({"detail" : "게시글을 수정하였습니다."}, status=status.HTTP_200_OK)
            except exceptions.ValidationError:
                return Response({"detail" : "형식을 벗어난 입력값이 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)
            except PostModel.DoesNotExist:
                return Response({"detail" : "게시물이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail" : "비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        if check_is_password(request.data, post_id):
            try:
                delete_post(post_id)
                return Response({ "detail" : "게시글이 삭제 되었습니다."}, status=status.HTTP_200_OK)
            except PostModel.DoesNotExist:
                return Response({"detail" : "게시물이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail" : "비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
        