from rest_framework import serializers

from apps.blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

    def create(self, validated_data):
        print("*** Custom Create Method ***")
        return super(BlogSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        print("*** Custom Update Method ***")
        return super(BlogSerializer, self).update(instance, validated_data)
