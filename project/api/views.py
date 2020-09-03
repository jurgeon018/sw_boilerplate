from .serializers import * 
from rest_framework import generics

class ProjectUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer


class ProjectUserDetailView(generics.ListCreateAPIView):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request 
        query_params = request.query_params
        username = query_params.get('username')
        if username:
            queryset = queryset.filter(username=username)
        return queryset 

