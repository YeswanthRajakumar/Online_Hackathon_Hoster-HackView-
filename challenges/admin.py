from django.contrib import admin
from .models import Challenges,Submission,ReviewSubmissionScore
# Register your models here.
admin.site.register(Challenges)
admin.site.register(Submission)
admin.site.register(ReviewSubmissionScore)
