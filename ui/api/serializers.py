from rest_framework import serializers
from ui.models import HomeDailyBlog, HomeAudioImages

class HomeDailyBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeDailyBlog
        fields = '__all__' 

class HomeAudioImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAudioImages
        fields = '__all__' 