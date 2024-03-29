# import
from .models import Blog
from .serializers import BlogSerializer

# Http
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render

# autentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class test_index(APIView):
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Blog.objects.all()

    def get(self, request):
        print(request.COOKIES)

        blogs = self.get_queryset()
        data = {'data': BlogSerializer(blogs, many=True).data}
        if request.GET.get('json', False):
            return JsonResponse(data)
        else:
            return Response(data)

    def post(self, request):
        print(request.data)

        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class test_detail(APIView):
    permission_classes = [AllowAny]

    def get_queryset(self, pk):
        return Blog.objects.get(id=pk)

    def get(self, request, pk):
        blog = self.get_queryset(pk)
        serializer = BlogSerializer(blog)
        if request.GET.get('json', False):
            return JsonResponse(serializer.data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        blog = self.get_queryset(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog = self.get_queryset(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class test_JWT_authentication(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        print(f"유저 : {user}")

        if not user:
            return Response({"error": "접근 권한이 없습니다."})

        return Response({"message": "Accepted"})


class test_open_view(APIView):
    def get(self, request):
        destination = request.GET.get("dest", 'test')
        return render(request, f'{destination}.html')
