from typing import Dict
from post.serializers import PostSerializer


def create_post(create_post_data: Dict[str, str]) -> None:
    """
    Post의 Create를 담당하는 Service
    Args :
        create_post_data (dict) : {
            'title' (str): 게시글의 제목,
            'content' (str) : 게시글의 내용
        }
    Return :
        None
    """
    post_serializer = PostSerializer(data=create_post_data)
    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()