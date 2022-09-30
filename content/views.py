from django.forms import model_to_dict
from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import Content


class ContentView(APIView):
    def get(self, request):
        contents = Content.objects.all()

        contents_dict = [model_to_dict(content) for content in contents]

        return Response(contents_dict, status.HTTP_200_OK)

    def post(self, request):
        content = request.data

        keys = [
            ("title", str),
            ("module", str),
            ("students", int),
            ("description", str),
            ("is_active", bool),
        ]

        # Validação se todas as chaves existem e tem a tipagem certa
        for key in keys:
            if key[0] not in content.keys():
                return Response(
                    f"missing key: {key[0]}",
                    status.HTTP_400_BAD_REQUEST,
                )
            elif type(content[key[0]]) != key[1]:
                return Response(
                    f"{key[0]}: must be a {key[1].__name__}",
                    status.HTTP_400_BAD_REQUEST,
                )

        # Criando objeto apenas com os atributos necessarios
        content = Content.objects.create(
            title=content["title"],
            module=content["module"],
            students=content["students"],
            description=content["description"],
            is_active=content["is_active"],
        )

        content_dict = model_to_dict(content)

        return Response(content_dict, status.HTTP_201_CREATED)


class ContentDetailView(APIView):
    def get(self, request, content_id):
        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response(
                {"message": "Content not found."},
                status.HTTP_404_NOT_FOUND,
            )

        content_dict = model_to_dict(content)

        return Response(content_dict, status.HTTP_200_OK)

    def patch(self, request, content_id):

        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response(
                {"message": "Content not found."},
                status.HTTP_404_NOT_FOUND,
            )

        for key, value in request.data.items():
            setattr(content, key, value)

        content.save()
        content_dict = model_to_dict(content)

        return Response(content_dict)

    def delete(self, request, content_id):

        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response(
                {"message": "Content not found."},
                status.HTTP_404_NOT_FOUND,
            )

        content.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ContentParamView(APIView):
    def get(self, request):
        title = request.query_params.get("title", None)

        contents = Content.objects.filter(title__icontains=title)
        content_dict = [model_to_dict(content) for content in contents]

        return Response(content_dict, status.HTTP_200_OK)
