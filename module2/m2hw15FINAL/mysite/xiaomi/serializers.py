from rest_framework_json_api import serializers
from xiaomi.models import Phone


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ('title', 'price', 'link')