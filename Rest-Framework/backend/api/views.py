from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer

 
# Create your views here.
@api_view(['GET', 'POST'])
def welcome(request):
    data = request.data
    print(data)
    return Response('welcome to Django rest framework' )

@api_view(['GET'])
def getEmployee(request):
    employee=Employee.objects.all()
    print(Employee)
    serializer=EmployeeSerializer(employee, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
def addEmployee(request):
    newEmployee= request.data

    serializer=EmployeeSerializer(data=newEmployee,many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(f"Employee Successfully Added {serializer.data}")
    return Response(serializer.errors)


@api_view(['PUT'])
def putEmployee(request):
    employeedata=request.data
    try:
        oldemployeedata=Employee.objects.get(id=employeedata['id'])
    except Employee.DoesNotExist:
        return Response("Please Provide a Valid Employee ID")
    serializer=EmployeeSerializer(oldemployeedata, data=employeedata)
    if serializer.is_valid():
        serializer.save()
        return Response(f"Employee Successfully Updated {serializer.data}")
    return Response(serializer.errors)


@api_view(['PATCH'])
def patchEmployee(request):
    employeedata=request.data
    try:
        oldemployeedata=Employee.objects.get(id=employeedata['id'])
    except Employee.DoesNotExist:
        return Response("Please Provide a Valid Employee ID")
    # except/turn request("Employee Did not Found")
    serializer=EmployeeSerializer(oldemployeedata, data=employeedata)
    if serializer.is_valid():
        serializer.save()
        return Response(f"Employee Successfully Modified {serializer.data}")
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteEmployee(request):
    delEmployee = request.data
    try:
        Employee.objects.get(id=delEmployee['id']).delete()
    except Employee.DoesNotExist:
        return Response("Please Provide a Valid Employee ID")
    return Response("Employee successfully deleted")