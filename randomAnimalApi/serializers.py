import rest_framework.serializers as serializers

from randomAnimalApi.models import AnimalMeme, MemeTag


class MemeTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemeTag
        fields = ('id', 'tag')


class AnimalMemeSerializer(serializers.ModelSerializer):
    tags = MemeTagSerializer(many=True, read_only=True)

    class Meta:
        model = AnimalMeme
        fields = ('id', 'name', 'image_url', 'tags', 'description')
