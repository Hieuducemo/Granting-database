# from flask import Flask
# from flask_graphql import GraphQLView
# import graphene

# class AcProgram(graphene.ObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     name_en = graphene.String()
#     type_id = graphene.String()
#     lastchange = graphene.String()

# class AcSubject(graphene.ObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     name_en = graphene.String()
#     program_id = graphene.String()
#     lastchange = graphene.String()

# class CreateAcProgram(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)
#         name = graphene.String(required=True)
#         nameEn = graphene.String(required=True)  # camelCase
#         typeId = graphene.String(required=True)  # camelCase
#         lastchange = graphene.String()

#     acprogram = graphene.Field(lambda: AcProgram)

#     def mutate(self, info, id, name, nameEn, typeId, lastchange):
#         acprogram = AcProgram(id=id, name=name, name_en=nameEn, type_id=typeId, lastchange=lastchange)
#         return CreateAcProgram(acprogram=acprogram)

# class CreateAcSubject(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)
#         name = graphene.String(required=True)
#         nameEn = graphene.String(required=True)  # camelCase
#         programId = graphene.String(required=True)  # camelCase
#         lastchange = graphene.String()

#     acsubject = graphene.Field(lambda: AcSubject)

#     def mutate(self, info, id, name, nameEn, programId, lastchange):
#         acsubject = AcSubject(id=id, name=name, name_en=nameEn, program_id=programId, lastchange=lastchange)
#         return CreateAcSubject(acsubject=acsubject)

# class Mutation(graphene.ObjectType):
#     createAcProgram = CreateAcProgram.Field()
#     createAcSubject = CreateAcSubject.Field()


# class Query(graphene.ObjectType):
#     hello = graphene.String()

#     def resolve_hello(self, info):
#         return "Hello world!"

# schema = graphene.Schema(query=Query, mutation=Mutation)

# app = Flask(__name__)
# app.add_url_rule(
#     '/graphql',
#     view_func=GraphQLView.as_view(
#         'graphql',
#         schema=schema,
#         graphiql=True,  # for having the GraphiQL interface
#     )
# )

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
# app.py
from flask import Flask
import graphene
from flask_graphql import GraphQLView

# Mock data lists
acprograms_data = []
acsubjects_data = []

class AcProgram(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    nameEn = graphene.String()
    typeId = graphene.String()
    lastchange = graphene.String()

class AcSubject(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    nameEn = graphene.String()
    programId = graphene.String()
    lastchange = graphene.String()

class Query(graphene.ObjectType):
    acprograms = graphene.List(AcProgram)
    acsubjects = graphene.List(AcSubject)

    def resolve_acprograms(self, info):
        return acprograms_data

    def resolve_acsubjects(self, info):
        return acsubjects_data

class CreateAcProgram(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        nameEn = graphene.String()
        typeId = graphene.String()
        lastchange = graphene.String()

    acprogram = graphene.Field(lambda: AcProgram)

    def mutate(self, info, id, name, nameEn, typeId, lastchange):
        acprogram = AcProgram(id=id, name=name, nameEn=nameEn, typeId=typeId, lastchange=lastchange)
        acprograms_data.append(acprogram)
        return CreateAcProgram(acprogram=acprogram)

class CreateAcSubject(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        nameEn = graphene.String()
        programId = graphene.String()
        lastchange = graphene.String()

    acsubject = graphene.Field(lambda: AcSubject)

    def mutate(self, info, id, name, nameEn, programId, lastchange):
        acsubject = AcSubject(id=id, name=name, nameEn=nameEn, programId=programId, lastchange=lastchange)
        acsubjects_data.append(acsubject)
        return CreateAcSubject(acsubject=acsubject)

class Mutation(graphene.ObjectType):
    create_acprogram = CreateAcProgram.Field()
    create_acsubject = CreateAcSubject.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
