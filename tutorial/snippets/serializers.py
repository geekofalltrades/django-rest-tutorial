from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
