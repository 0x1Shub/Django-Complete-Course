from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models

# Create your views here.
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = models.Students.objects.all()
        data = [{"id": s.id, "name":s.name, "grade": s.grade} for s in students]
        return Response(data)

    elif request.method == 'POST':
        name = request.data.get('name')
        age = request.data.get('age')
        grade = request.data.get('grade')

        if name and age and grade:
            student = models.Students.objects.create(name=name, age=age, grade=grade)
            return Response({
                "id": student.id,
                "name": student.name,
                "age": student.age
            }, status = status.HTTP_201_CREATED)
        
        else: 
            return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = models.Students.objects.get(pk = pk)
    except models.Students.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        return Response({"id": student.id, "name": student.name, "grade": student.grade})
    
    elif request.method == "PUT":
        student.name = request.data.get("name", student.name)
        student.age = request.data.get("age", student.age)
        student.grade = request.data.get("grade", student.grade)
        student.save()
        return Response({"id": student.id, "name": student.name, "age": student.age, "grade": student.grade})
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
