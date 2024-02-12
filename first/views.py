from django.shortcuts import render
from . models import TeacherModel
from .serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

def teacher_info(request):
    teacher_data=TeacherModel.objects.all()
    serializer=TeacherSerializer(teacher_data,many=True)
    json_data = JSONRenderer().render(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,'application/json')

def teacher_instance(request,pk):
    teacher_data=TeacherModel.objects.get(id=pk)
    serializer=TeacherSerializer(teacher_data)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,'application/json')



@csrf_exempt
def teacher_create(request):

    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        # phthon to stream
        python_data=JSONParser().parse(stream)
        # python to complex dafa
        serializers=TeacherSerializer(data=python_data)

        if serializers.is_valid():
            serializers.save()
            res={
                'msg':'Successfully data inserted'
            }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, 'application/json')
        else:
            json_data=JSONRenderer().render(serializers.errors())
        return HttpResponse(json_data,'application/json')
    
    if request.method=='PUT':

        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        teacher_instance=TeacherModel.objects.get(id=id)
        serializer=TeacherSerializer(teacher_instance,data=python_data,partial=True)

        if serializer.is_valid():
            serializer.save()
            res={
                'msg':'Successfully Data Updated'
            }
            json_data = JSONRenderer().render(res)
            
        else:
            json_data=JSONRenderer().render(serializer.errors())
            
        return HttpResponse(json_data,'application/json')
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        teacher_ins=TeacherModel.objects.get(id=id)
        teacher_ins.delete()
        res={
            'msg':'Data Deleted Succesfully'
        }
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,'application/json')


@api_view(['GET','POST','PUT','PATCH','DELETE'])

def teacher_apiView(request,pk=None):

    if request.method=='GET':
        id=pk
        if id:
            teacher_ins=TeacherModel.objects.get(id=id)
            serializer=TeacherSerializer(teacher_ins)
            return Response(serializer.data)
        else:
            teacher=TeacherModel.objects.all()
            serializer=TeacherSerializer(teacher,many=True)
            return Response(serializer.data)
        
    if request.method=='POST':
        serializer=TeacherSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response({'message':'Data Inserted Successfully'})
        else:
            return Response(serializer.errors)

    if request.method=='PUT':
        id=pk
        teacher_ins=TeacherModel.objects.get(id=id)
        serializer=TeacherSerializer(teacher_ins,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Successfully Updated'})
        else:
            return Response(serializer.errors)

    if request.method=='PATCH':
        id=pk
        teacher_ins=TeacherModel.objects.get(id=id)
        serializer=TeacherSerializer(teacher_ins,data=request.data,partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Partially Updated'})
        else:
            return Response(serializer.errors())

    if request.method=='DELETE':
        id=pk
        teacher_ins=TeacherModel.objects.get(id=id)
        teacher_ins.delete()
        return Response({'msg':'Data Deleted Successfully'})       

        
    

