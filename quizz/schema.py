import graphene

from graphene_django import DjangoObjectType

from .models import Question


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class QuestionQuery(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)

    def resolve_all_questions(root, info):
        # We can easily optimize query count in the resolve method
        return Question.objects.all()


class QuestionMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        text = graphene.String(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    question = graphene.Field(QuestionType)
	
    @classmethod
    def mutate(cls, root, info, text, id):
        question = Question.objects.get(pk=id)
        question.text = text
        question.save()
        # Notice we return an instance of this mutation
        return QuestionMutation(question=question)

class Mutation(graphene.ObjectType):
    update_question = QuestionMutation.Field()

schema = graphene.Schema(query=QuestionQuery,mutation=Mutation)