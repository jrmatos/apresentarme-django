import graphene
from apresentarme.graphql.types import CardType, CreateCardInput
from apresentarme.main.models import Card


class CreateCard(graphene.Mutation):
    class Arguments:
        card_data = CreateCardInput(required=True)

    card = graphene.Field(CardType)

    def mutate(self, root, card_data=None):
        card = Card(
            url=card_data.url,
            name=card_data.name,
            bio=card_data.bio,
            facebook_url=card_data.facebook_url
        )
    
        card.save()

        return CreateCard(card=card)


class Mutation(graphene.ObjectType):
    create_card = CreateCard.Field()
