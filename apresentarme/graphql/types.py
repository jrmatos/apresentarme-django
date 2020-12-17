import graphene
from apresentarme.main.models import Card
from graphene_django import DjangoObjectType


class CardType(DjangoObjectType):
    class Meta:
        model = Card
        fields = "__all__"

class CreateCardInput(graphene.InputObjectType):
    url = graphene.String(required=True)
    name = graphene.String(required=True)
    bio = graphene.String(required=True)
    facebook_url = graphene.String(required=True)
