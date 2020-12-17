import graphene
from graphene_django import DjangoObjectType

from apresentarme.main.models import Category, Ingredient, Card

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class CardType(DjangoObjectType):
    class Meta:
        model = Card
        fields = "__all__"

class CreateCardInput(graphene.InputObjectType):
    url = graphene.String(required=True)
    name = graphene.String(required=True)
    bio = graphene.String(required=True)
    facebook_url = graphene.String(required=True)

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

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    all_cards = graphene.List(CardType)

    def resolve_all_ingredients(self, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(self, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    def resolve_all_cards(self, info):
        return Card.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
