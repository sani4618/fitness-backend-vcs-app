from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fitness.serializers import FitnessSerializers
from fitness.models import Fitnessapp 
import json


@csrf_exempt
def newregister(request):
    if request.method=="POST":
        received_json_data=json.loads(request.body)
        getFirstName=received_json_data["firstName"]
        getMiddleName=received_json_data["middleName"]
        getLastName=received_json_data["lastName"]
        getGender=received_json_data["gender"]
        getDateOfBirth=received_json_data["dateOfBirth"]
        getDepartment=received_json_data["department"]
        getUserName=received_json_data["userName"]
        getEmail=received_json_data["email"]
        getPassword=received_json_data["confirmPassword"]
        getConfirmPassword=received_json_data["password"]
        data={"firstName":getFirstName,"middleName":getMiddleName,"lastName":getLastName,"gender":getGender,"dateOfBirth":getDateOfBirth,"department":getDepartment,"userName":getUserName,"email":getEmail,"password":getPassword,"confirmPassword":getConfirmPassword}
        print(data)

        fitness_Serialize=FitnessSerializers(data=data)
        if fitness_Serialize.is_valid():
            fitness_Serialize.save()
            return HttpResponse(json.dumps({"status":"added success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
    else:
        
        return HttpResponse("Invalid Register form")

