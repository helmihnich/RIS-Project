from rest_framework import serializers
from .models import (
    Doctors,
    Patient,
    Equipement,
    ExamenRadiologique,
    Worklist,
    RendezVous,
    ImageRadiologique,
)


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ["id", "username", "speciality", "first_name", "last_name", "email"]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "last_name",
            "birthday",
            "address",
            "mobile_number",
            "insurance_name",
            "CIN",
            "social_security_number",
            "situation",
            "doctor",
        ]


class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = ["nom_equipement", "fabricant", "modele", "annee_achat"]


class ExamenRadiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenRadiologique
        fields = [
            "id",
            "date_heure_examen",
            "patient",
            "Doctor",
            "equipement",
            "resultats",
        ]


class WorklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worklist
        fields = ["id", "id_examen", "date_creation", "statut", "priorite", "notes"]


class RendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = RendezVous
        fields = ["id", "date_heure_rendez_vous", "patient", "Doctor", "type_examen"]


class ImageRadiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRadiologique
        fields = [
            "id",
            "examen_radiologique",
            "chemin_acces_image",
            "date_heure_creation",
        ]