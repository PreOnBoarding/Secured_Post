from django.contrib.auth.hashers import check_password

from post.models import Post as PostModel
from post.serializers import CreatePostSerializer, PostSerializer

def get_post(page:int) -> PostSerializer:
    """
    Args:
        page (int): Get을 할 때 해당 페이지
    Returns:
        PostSerializer: 해당 페이지에서 필요한 post 데이터
    """
    page_post = PostModel.objects.all()[:page*20]
    page_post_serializer = PostSerializer(page_post, many=True).data
    return page_post_serializer

def create_post(create_data: dict[str, str]) -> None:
    """
    Args:
        create_data (dict[str, str]): {
            "title" (str) : 20자 이하의 제목,
            "content" (str) : 200자 이하의 내용,
            "password" (str) : 숫자를 포함한 6글자 이상의 비밀번호
        }
    """
    post_serializer = CreatePostSerializer(data = create_data)
    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()

def update_post(update_data : dict[str, str], post_id : int) -> None:
    """
    Args:
        update_data (dict[str, str]): {
            "title" (str) : 20자 이하의 제목 or
            "content" (str) : 200자 이하의 내용
        }
        post_id (int): 수정할 post_id
    """
    update_post_obj = PostModel.objects.get(id=post_id)
    post_serializer = PostSerializer(update_post_obj, update_data, partial= True)
    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()

def check_is_password(check_data : dict[str, str], post_id : int) -> bool:
    """
    Args:
        check_data (dict[str, str]): {
            "password" (str) : 일치하는지 확인을 할 비밀번호, + a
        }
        post_id (int): 비밀번호를 대조할 게시글의 post_id

    Returns:
        bool: 일치하면 True, 불일치하면 False
    """
    check_post = PostModel.objects.get(id=post_id)
    if check_password(check_data["password"], check_post.password):
        return True
    return False

def delete_post(post_id : int) -> None:
    """
    Args:
        post_id (int): 삭제할 게시글의 post_id
    """
    delete_post_obj = PostModel.objects.get(id=post_id)
    delete_post_obj.delete()