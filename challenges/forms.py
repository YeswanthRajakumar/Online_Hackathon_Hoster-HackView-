from django import forms
from .models import Submission, Challenges, ReviewSubmissionScore
from django.utils.translation import ugettext_lazy as _


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = ('challenge', 'applyer', 'review_status', 'submitted_at')

        labels = {
            'qa1': _('1.Can you describe the problem in your own words exactly how you experience it ?'),
            'qa2': _('2.How have you tried to solve this problem before? Can you explain the solution?'),
            'qa3': _('3.Why did you not make tht solution permanent?What were the gaps in the solution?'),
            'qa4': _('4.What are the other constraints?challenges that have to be overcome or accommodated while '
                     'solving the problem?'),
            'qa5': _('5.How will you benefit from solving the problem?How much is solving this problem worth to you ?'),
            'qa6': _('6.How important to you is solving this problem among other priorities?'),
        }


class ChallengeCreationForm(forms.ModelForm):
    class Meta:
        model = Challenges
        exclude = ('created_by',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewSubmissionScore
        fields = ['criteria1', 'criteria2', 'criteria3', 'criteria4', 'criteria5', 'tip']
        labels = {
            'criteria1': _('Is the Problem Statement Defined Clearly ?'),
            'criteria2': _('Is the Problem Worth Solving ?'),
            'criteria3': _('Is the Chosen Target Customer(Type/Profile) Strongly Motivated to solve the Problem ?'),
            'criteria4': _('Is the Core Value Proportion Defined,Quantified And Validated ?'),
            'criteria5': _('Is the Problem Statement Defined Clearly ?'),
            'tip': _('Any tip for submitters ? (Optional)'),
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget = forms.RadioSelect()
