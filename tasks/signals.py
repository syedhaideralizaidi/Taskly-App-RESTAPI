from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from tasks.models import Task, TASK_STATUS_CHOICES
@receiver(post_save, sender = Task)
def update_house_points(sender, instance, created, **kwargs):
    house = instance.task_list.house
    if instance.status == TASK_STATUS_CHOICES[1]["COMPLETE"]:
        house.points += 10
    elif instance.status == TASK_STATUS_CHOICES[0]["NOT_COMPLETE"]:
        if house.points > 10:
            house.points -= 10
    house.save()
@receiver(post_save, sender = Task)
def update_tasklist_status(sender, instance, created, **kwargs):
    task_list = instance.task_list
    is_complete = True
    for task in task_list.tasks.all():
        if task.status != TASK_STATUS_CHOICES[1]["COMPLETE"]:
            is_complete = False
    task_list.status = TASK_STATUS_CHOICES[1]["COMPLETE"] if is_complete else TASK_STATUS_CHOICES[1]["NOT_COMPLETE"]
    task_list.save()