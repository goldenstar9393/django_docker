from marshmallow import validate
from marshmallow import fields
from marshmallow import Schema
from marshmallow.decorators import post_load

from rest_framework import serializers
from techtest.articles.models import Article
from techtest.regions.models import Region
from techtest.regions.schemas import RegionSchema


class ArticleSchema(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields= ['id', 'title', 'content', 'regions', 'authors']
    id = fields.Integer()
    title = fields.String(validate=validate.Length(max=255))
    content = fields.String()
    regions = fields.Method(
        required=False, serialize="get_regions", deserialize="load_regions"
    )
    regions = fields.Method(
        required=False, serialize="get_authors", deserialize="load_authors"
    )

    def get_regions(self, article):
        return RegionSchema().dump(article.regions.all(), many=True)

    def load_regions(self, regions):
        return [
            Region.objects.get_or_create(id=region.pop("id", None), defaults=region)[0]
            for region in regions
        ]
    def get_authors(self, article):
        return RegionSchema().dump(article.authors.all(), many=True)

    def load_regions(self, authors):
        return [
            Region.objects.get_or_create(id=author.pop("id", None), defaults=author)[0]
            for author in authors
        ]
