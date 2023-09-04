from rest_framework import serializers
from fitness.models import Fitnessapp


class FitnessSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fitnessapp
        fields =(
            'firstName',
            'middleName',
            'lastName',
            'gender',
            'dateOfBirth',
            'department',
            'userName',
            'email',
            'password',
            'confirmPassword'
        )