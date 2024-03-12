from django.db import models


class MemeTag(models.Model):
    """
    This class represents a tag for an animal meme.
    """
    tag = models.CharField(max_length=50)

    def __str__(self) -> str:

        """
        This function returns the tag.
        :return: tag
        """
        return self.tag


class AnimalMeme(models.Model):
    """
    This class represents an animal meme.
    """
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    tags = models.ManyToManyField(MemeTag)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        This function returns the name of the animal meme.
        :return: name of the animal meme
        """
        return self.name
