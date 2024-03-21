# import
from .models import Blog
from .serializers import BlogSerializer

# Http
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from rest_framework.permissions import AllowAny

class test_index(APIView):
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Blog.objects.all()
    
    def get(self, request):
        print(request.data)

        blogs = self.get_queryset()
        data = {'data': BlogSerializer(blogs, many=True).data}
        if request.GET.get('json', False):
            return JsonResponse()
        else:
            return Response(data)

    def post(self, request):
        print(request.data)

        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
