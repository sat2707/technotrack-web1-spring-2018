from django.db import models
from users.models import User
# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Label(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return str(self.label)


class Report (models.Model):
    NEW = 1
    PROCESSED = 2
    CLOSED = 3
    REOPEN = 4
    NOT_A_BUG = 5
    STATUS = (
        (NEW, 'NEW'),
        (PROCESSED, 'PROCESSED'),
        (CLOSED, 'CLOSED'),
        (REOPEN, 'REOPEN'),
        (NOT_A_BUG, 'NOT A BUG')
    )
    LEVEL = (
        (NEW, 1),
        (PROCESSED, 2),
        (CLOSED, 3),
        (REOPEN, 4)
    )
    TYPE = (
        (NEW, 'ISSUE'),
        (PROCESSED, 'FUTURE REQUEST')
    )
    status = models.IntegerField(choices=STATUS)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_created_by')  #
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    level = models.IntegerField(choices=LEVEL)
    priority = models.IntegerField(choices=LEVEL)
    type = models.IntegerField(choices=TYPE)
    updated_at = models.DateTimeField(auto_now=True)  # updated_at
    labels = models.ManyToManyField(Label)
    assigned_to = models.ManyToManyField(User, related_name='report_assigned_to')

    def __str__(self):
        return str(self.name)


class Answer(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    prev_ans = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_created_by')
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) #uptated_at
    created_at = models.DateTimeField(auto_now=True) #created_at

    def __str__(self):
        return str(self.id)


