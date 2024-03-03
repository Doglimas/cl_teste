from rest_framework import serializers
from aplicacao.models import Postagem

class PostagemSerializer(serializers.ModelSerializer):
    read_only_fields = ('created_datetime',) 
    
    def validate(self, attrs):
        if self.instance:
            if 'created_datetime' in attrs and self.instance.created_datetime != attrs['created_datetime']:
                raise serializers.ValidationError("O campo created_datetime não pode ser alterado.")
            if 'username' in attrs and self.instance.username != attrs['username']:
                raise serializers.ValidationError("O campo username não pode ser alterado.")
            if 'id' in attrs and self.instance.id != attrs['id']:
                raise serializers.ValidationError("O campo id não pode ser alterado.")
        return attrs

    class Meta:
        model = Postagem
        fields = ['id', 'username', 'title', 'content', 'created_datetime']

