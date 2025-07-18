from rest_framework import serializers
from .models import Users


class UserSerializers(serializers.ModelSerializer):
    full_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def get_full_info(self, obj):
        return f"{obj.full_name} - {obj.email}"

    def validate(self, data):
        # Ensure full_name is not the same as email's prefix
        if data.get('full_name') and data.get('email'):
            if data['full_name'].lower() == data['email'].split('@')[0].lower():
                raise serializers.ValidationError(
                    "Full name and email username should not be the same.")
        return data

    def validate_age(self, value):
        if value < 10:
            raise serializers.ValidationError("Age must be greater than 10.")
        return value

    def create(self, validated_data):
        # Fixed typo: changed `validate_data` to `validated_data`
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
