from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from post.models import Post as PostModel


class CreatePostSerializer(serializers.ModelSerializer):

    def validate(self, data):
        condition = all(x not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] for x in data["password"])
        if len(data["password"]) < 6 or condition:
            raise serializers.ValidationError("비밀번호는 6자 이상, 숫자를 꼭 포함해주세요!")
        return data
    
    def create(self,validated_data):
        validated_data["password"] = make_password(str(validated_data["password"]))
        post = self.Meta.model(**validated_data)
        post.save()
        return post

    class Meta:
        model = PostModel
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostModel
        fields = "__all__"

        extra_kwargs = {"password": {"write_only": True}}

