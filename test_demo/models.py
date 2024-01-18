from django.db import models


class GoalListModel(models.Model):
    class Meta:
        db_table = "goal_list_collection"

    TAG_CHOICES = [
        ("personal", "Personal"),
        ("professional", "Professional"),
        ("other", "Other"),
    ]
    PRIORITY_CHOICES = [
        ("short-term", "Short-term"),
        ("medium-term", "Medium-term"),
        ("long-term", "Long-term"),
    ]
    user_id = models.IntegerField()
    goal_name = models.CharField(max_length=100)
    goal_description = models.CharField(max_length=100)
    goal_status = models.CharField(max_length=100)
    goal_start_date = models.CharField(max_length=100)
    goal_end_date = models.CharField(max_length=100)
    goal_tag = models.CharField(
        max_length=100,
        choices=TAG_CHOICES,
        default="personal",  # Set your default value here
    )
    goal_priority_tag = models.CharField(
        max_length=100,
        choices=PRIORITY_CHOICES,
        default="short-term",  # Set your default value here
    )
