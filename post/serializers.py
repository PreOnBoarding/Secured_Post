import re
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Post as PostModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['password', 'title', 'content', 'created_at', 'updated_at']
     
    def validate(self, data):
        correct_password = re.compile('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$')
                                        
        if data.get('password'):
            password_input = correct_password.match(data.get('password'))
            if password_input == None:
                raise serializers.ValidationError(
                detail={'password': '비밀번호는 6자리 이상이며 최소 하나 이상의 영문자와 숫자로 작성해주세요.'})
        
        
        return data
    

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        post = PostModel(**validated_data)
        post.save()
        return post