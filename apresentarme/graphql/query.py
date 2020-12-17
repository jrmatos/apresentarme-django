import graphene
from apresentarme.graphql.types import CardType
from apresentarme.main.models import Card


class Query(graphene.ObjectType):
    all_cards = graphene.List(CardType)

    def resolve_all_cards(self, info):
        return Card.objects.all()
