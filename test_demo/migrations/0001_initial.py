# Generated by Django 4.2.9 on 2024-01-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoalListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('goal_name', models.CharField(max_length=100)),
                ('goal_description', models.CharField(max_length=100)),
                ('goal_status', models.CharField(max_length=100)),
                ('goal_start_date', models.CharField(max_length=100)),
                ('goal_end_date', models.CharField(max_length=100)),
                ('goal_tag', models.CharField(choices=[('personal', 'Personal'), ('professional', 'Professional'), ('other', 'Other')], default='personal', max_length=100)),
                ('goal_priority_tag', models.CharField(choices=[('short-term', 'Short-term'), ('medium-term', 'Medium-term'), ('long-term', 'Long-term')], default='short-term', max_length=100)),
            ],
            options={
                'db_table': 'goal_list_collection',
            },
        ),
    ]
