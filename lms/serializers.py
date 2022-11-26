from rest_framework import views, serializers

from lms.models import Curator


class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        fields = '__all__'