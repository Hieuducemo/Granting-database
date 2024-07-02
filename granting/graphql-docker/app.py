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
aclessontypes_data = []
aclessons_data = []
actopics_data = []
acclassifications_data = []
acprogramtypes_data = []
acsemesters_data = []
acclassificationtypes_data = []
acclassificationlevels_data = []

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

class AcLessonType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    nameEn = graphene.String()
    
    
class AcLesson(graphene.ObjectType):
    id = graphene.ID()
    topicId = graphene.ID()
    typeId = graphene.ID()
    lastchange = graphene.String()
    count = graphene.Int()

class AcTopic(graphene.ObjectType):
    id = graphene.ID()
    semesterId = graphene.ID()
    lastchange = graphene.String()
    name = graphene.String()
    nameEn = graphene.String()
    
class AcClassification(graphene.ObjectType):
    id = graphene.ID()
    userId = graphene.ID()
    semesterId = graphene.ID()
    classificationLevelId = graphene.ID()
    lastchange = graphene.String()
    order = graphene.Int()

class AcProgramType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    nameEn = graphene.String()
    titleId = graphene.ID()
    formId = graphene.ID()
    languageId = graphene.ID()
    levelId = graphene.ID()
    
class AcSemester(graphene.ObjectType):
    id = graphene.ID()
    subjectId = graphene.ID()
    classificationtypeId = graphene.ID()
    lastchange = graphene.String()
    order = graphene.Int()
    credits = graphene.Int()
    
class AcClassificationType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    nameEn = graphene.String()

class AcClassificationLevel(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    nameEn = graphene.String()

class Query(graphene.ObjectType):
    acprograms = graphene.List(AcProgram)
    acsubjects = graphene.List(AcSubject)
    aclessontypes = graphene.List(AcLessonType)
    aclessons = graphene.List(AcLesson)
    actopics = graphene.List(AcTopic)
    acclassifications = graphene.List(AcClassification)
    acprogramtypes = graphene.List(AcProgramType)
    acsemesters = graphene.List(AcSemester)
    acclassificationtypes = graphene.List(AcClassificationType)
    acclassificationlevels = graphene.List(AcClassificationLevel)

    def resolve_acprograms(self, info):
        return acprograms_data

    def resolve_acsubjects(self, info):
        return acsubjects_data
    
    def resolve_aclessontypes(self, info):
        return aclessontypes_data
    
    def resolve_aclessons(self, info):
        return aclessons_data
    
    def resolve_actopics(self, info):
        return actopics_data
    
    def resolve_acclassifications(self, info):
        return acclassifications_data
    
    def resolve_acprogramtypes(self, info):
        return acprogramtypes_data
    
    def resolve_acsemesters(self, info):
        return acsemesters_data
    
    def resolve_acclassificationtypes(self, info):
        return acclassificationtypes_data
    
    def resolve_acclassificationlevels(self, info):
        return acclassificationlevels_data

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
    
class CreateAcLessonType(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        nameEn = graphene.String()

    aclessontype = graphene.Field(lambda: AcLessonType)
    
    def mutate(self, info, id, name, nameEn):
        aclessontype = AcLessonType(id=id, name=name, nameEn=nameEn)
        aclessontypes_data.append(aclessontype)
        return CreateAcLessonType(aclessontype=aclessontype)
    
class CreateAcLesson(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        topicId = graphene.ID()
        typeId = graphene.ID()
        lastchange = graphene.String()
        count = graphene.Int()

    aclesson = graphene.Field(lambda: AcLesson)

    def mutate(self, info, id, topicId, typeId, lastchange, count):
        aclesson = AcLesson(id=id, topicId=topicId, typeId=typeId, lastchange=lastchange, count=count)
        aclessons_data.append(aclesson)
        return CreateAcLesson(aclesson=aclesson)
    
class CreateAcTopic(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        semesterId = graphene.ID()
        lastchange = graphene.String()
        name = graphene.String()
        nameEn = graphene.String()

    actopic = graphene.Field(lambda: AcTopic)

    def mutate(self, info, id, semesterId, lastchange, name, nameEn):
        actopic = AcTopic(id=id, semesterId=semesterId, lastchange=lastchange, name=name, nameEn=nameEn)
        actopics_data.append(actopic)
        return CreateAcTopic(actopic=actopic)
    
class CreateAcClassification(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        userId = graphene.ID()
        semesterId = graphene.ID()
        classificationLevelId = graphene.ID()
        lastchange = graphene.String()
        order = graphene.Int()

    acclassification = graphene.Field(lambda: AcClassification)

    def mutate(self, info, id, userId, semesterId, classificationLevelId, lastchange, order):
        acclassification = AcClassification(id=id, userId=userId, semesterId=semesterId, classificationLevelId=classificationLevelId, lastchange=lastchange, order=order)
        acclassifications_data.append(acclassification)
        return CreateAcClassification(acclassification=acclassification)
    
class CreateAcProgramType(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        nameEn = graphene.String()
        titleId = graphene.ID()
        formId = graphene.ID()
        languageId = graphene.ID()
        levelId = graphene.ID()

    acprogramtype = graphene.Field(lambda: AcProgramType)

    def mutate(self, info, id, name, nameEn, titleId, formId, languageId, levelId):
        acprogramtype = AcProgramType(id=id, name=name, nameEn=nameEn, titleId=titleId, formId=formId, languageId=languageId, levelId=levelId)
        acprogramtypes_data.append(acprogramtype)
        return CreateAcProgramType(acprogramtype=acprogramtype)
    
class CreateAcSemester(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        subjectId = graphene.ID()
        classificationtypeId = graphene.ID()
        lastchange = graphene.String()
        order = graphene.Int()
        credits = graphene.Int()

    acsemester = graphene.Field(lambda: AcSemester)

    def mutate(self, info, id, subjectId, classificationtypeId, lastchange, order, credits):
        acsemester = AcSemester(id=id, subjectId=subjectId, classificationtypeId=classificationtypeId, lastchange=lastchange, order=order, credits=credits)
        acsemesters_data.append(acsemester)
        return CreateAcSemester(acsemester=acsemester)
    
class CreateAcClassificationType(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        nameEn = graphene.String()

    acclassificationtype = graphene.Field(lambda: AcClassificationType)

    def mutate(self, info, id, name, nameEn):
        acclassificationtype = AcClassificationType(id=id, name=name, nameEn=nameEn)
        acclassificationtypes_data.append(acclassificationtype)
        return CreateAcClassificationType(acclassificationtype=acclassificationtype)

class CreateAcClassificationLevel(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        nameEn = graphene.String()

    acclassificationlevel = graphene.Field(lambda: AcClassificationLevel)

    def mutate(self, info, id, name, nameEn):
        acclassificationlevel = AcClassificationLevel(id=id, name=name, nameEn=nameEn)
        acclassificationlevels_data.append(acclassificationlevel)
        return CreateAcClassificationLevel(acclassificationlevel=acclassificationlevel)
    
class Mutation(graphene.ObjectType):
    create_acprogram = CreateAcProgram.Field()
    create_acsubject = CreateAcSubject.Field()
    create_aclessontype = CreateAcLessonType.Field()
    create_aclesson = CreateAcLesson.Field()
    create_actopic = CreateAcTopic.Field()
    create_acclassification = CreateAcClassification.Field()
    create_acprogramtype = CreateAcProgramType.Field()
    create_acsemester = CreateAcSemester.Field()
    create_acclassificationtype = CreateAcClassificationType.Field()
    create_acclassificationlevel = CreateAcClassificationLevel.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
