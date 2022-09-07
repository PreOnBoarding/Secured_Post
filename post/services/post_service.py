from typing import Dict
from post.serializers import CreatePostSerializer, PostSerializer
from post.models import Post as PostModel


def get_post(page: int) -> PostSerializer:
    """
    모든 게시글의 조회를 담당하는 Service
    Args :
        page (int): 20개씩 게시글 표시, url에 담아서 보내줌
    Return :
        get_posts_serializer
    """
    get_posts = PostModel.objects.all().order_by('-created_at')
    first_index = page * 20
    end_index = first_index + 20
    
    if len(get_posts) < first_index or page < 0:
        return []
    get_posts_serializer = PostSerializer(get_posts[first_index:end_index], many=True)
    return get_posts_serializer.data


def create_post(create_post_data: Dict[str, str]) -> None:
    """
    게시글 생성을 담당하는 Service
    Args :
        create_post_data (dict) : {
            title (str): 게시글의 제목,
            content (str) : 게시글의 내용
        }
    Return :
        None
    """
    post_serializer = CreatePostSerializer(data=create_post_data)
    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()
    
    
def update_post(post_id: int, update_post_data: Dict[str, str]) -> Dict[str, str]:
    """
    게시글 수정을 담당하는 Service
    Args :
        post_id (int): posts.Post 외래키, url에 담아서 보내줌,
        update_post_data (dict): {
            title (str): 게시글의 제목 or
            content (str): 게시글의 내용
        }
    Return :
        dict[str, str]
    """
    update_post = PostModel.objects.get(id=post_id)
    update_post_serializer = PostSerializer(update_post, update_post_data, partial=True)
    update_post_serializer.is_valid(raise_exception=True)
    update_post_serializer.save()
    return ({'update_post': update_post_serializer.data})


def delete_post(post_id: int) -> None:
    """
    게시글 삭제를 담당하는 Service
    Args :
        post_id (int): posts.Post 외래키, url에 담아서 보내줌
    Return :
        None
    """
    delete_post = PostModel.objects.get(id=post_id)
    delete_post.delete()
