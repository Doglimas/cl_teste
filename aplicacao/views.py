from rest_framework import viewsets
from aplicacao.models import Postagem
from aplicacao.serializer import PostagemSerializer
from rest_framework.response import Response


class PostagensViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
   
    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.GET.get('username', None)
        id = self.request.GET.get('id', None)
        
        if username is not None:
            queryset = queryset.filter(username=username)
        if id is not None:
            queryset = queryset.filter(id=id)
            
        return queryset
    
