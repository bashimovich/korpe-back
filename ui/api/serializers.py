from rest_framework import serializers
from ui.models import HomeDailyBlog

class HomeDailyBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeDailyBlog
        fields = '__all__' 