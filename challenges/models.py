from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Challenges(models.Model):
    challenge_title = models.CharField(max_length=100)
    challenge_image = models.ImageField(null=True, upload_to='challenge-images')
    challenge_description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.challenge_title


class Submission(models.Model):

    challenge = models.ForeignKey(Challenges, on_delete=models.SET_NULL, null=True)
    applyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    qa1 = models.TextField()
    qa2 = models.TextField()
    qa3 = models.TextField()
    qa4 = models.TextField()
    qa5 = models.TextField()
    qa6 = models.TextField()
    review_status = models.BooleanField(default=False)

    def __str__(self):
        return self.challenge.challenge_title


class ReviewSubmissionScore(models.Model):
    MARK_CHOICES = (
        ('0', '0'), ('2', '2'), ('4', '4'),
        ('6', '6'), ('10', '10'), ('20', '20')
    )
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
    criteria1 = models.CharField(max_length=10, choices=MARK_CHOICES, default=0)
    criteria2 = models.CharField(max_length=10, choices=MARK_CHOICES, default=0)
    criteria3 = models.CharField(max_length=10, choices=MARK_CHOICES, default=0)
    criteria4 = models.CharField(max_length=10, choices=MARK_CHOICES, default=0)
    criteria5 = models.CharField(max_length=10, choices=MARK_CHOICES, default=0)
    TotalScore = models.CharField(max_length=10, null=False)
    reviewed_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f' Submission for {self.submission.challenge}'
