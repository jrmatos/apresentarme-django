import graphene
from apresentarme.graphql.mutation import Mutation
from apresentarme.graphql.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
