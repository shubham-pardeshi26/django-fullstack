from rest_framework import serializers
from .models import GoalListModel


class AllGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalListModel
        fields = "__all__"

    def validate_user_id(self, value):
        # Check if any existing record has the same user_id
        if GoalListModel.objects.filter(user_id=value).exists():
            raise serializers.ValidationError(
                "A goal with this user_id already exists."
            )
        return value


class SomeGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalListModel
        fields = ("goal_name", "goal_description", "goal_status", "goal_priority_tag")
