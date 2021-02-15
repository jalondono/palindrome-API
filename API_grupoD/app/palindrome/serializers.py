from rest_framework import serializers
from rest_framework import exceptions


class PalindromeSerializer(serializers.Serializer):
    text = serializers.CharField(allow_blank=False, allow_null=False)

    def validate(self, data):
        text = data.get("text", "")

        if text:
            if isinstance(text, str):
                data["text"] = text
            else:
                msg = "The input should be a valid string"
                raise exceptions.ValidationError(msg)
        else:
            msg = "The string mustn't be empty"
            raise exceptions.ValidationError(msg)
        return data
