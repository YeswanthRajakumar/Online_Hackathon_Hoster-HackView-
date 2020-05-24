from django.db.models.signals import post_save
from .models import ReviewSubmissionScore


# def setReviewStatus(sender, instance, created, **kwargs):
#     print(instance.submission.review_status)
#     instance.submission.review_status = True
#
#
# post_save.connect(setReviewStatus, sender=ReviewSubmissionScore)
