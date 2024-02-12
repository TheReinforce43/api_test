from rest_framework import serializers
from . models import TeacherModel


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model=TeacherModel
        fields=['Name','CourseName','Duration','Seat']


# class TeacherSerializer(serializers.Serializer):
#     Name=serializers.CharField(max_length=250)
#     CourseName=serializers.CharField(max_length=250)
#     Duration=serializers.IntegerField(default=0)
#     Seat=serializers.IntegerField(default=0)
        
#     def create(self,validated_data):
#         return TeacherModel.objects.create(**validated_data)
          
#     def update(self,instance,validated_data):
#         instance.Name=validated_data.get('Name',instance.Name)
#         instance.CourseName=validated_data.get('CourseName',instance.CourseName)
#         instance.Duration=validated_data.get('Duration',instance.Duration)
#         instance.Seat=validated_data.get('Seat',instance.Seat)
#         instance.save()
#         return instance


