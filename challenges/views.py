from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuestionForm, ChallengeCreationForm, ReviewForm
from .models import Submission, Challenges
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


# Create your views here.


def index(request):
    context = {
    }
    return render(request, template_name='challenges/Home.html', context=context)


def challengeList(request):
    queryset = Challenges.objects.all()
    context = {
        'challenges': queryset,
    }
    return render(request, template_name='challenges/challengeList.html', context=context)


@login_required(login_url='user-login')
def challengeSubmission(request, id):
    form = QuestionForm()
    instance = get_object_or_404(Challenges, id=id)
    print(instance)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            challenge_form = form.save(commit=False)
            challenge_form.challenge = instance
            challenge_form.applyer = request.user
            print(challenge_form.applyer)
            challenge_form.save()
            return redirect('challenge-list')

        else:
            print(form.errors)
    context = {
        'form': form,
        'challenge': instance
    }
    return render(request, template_name='challenges/createSubmission.html', context=context)


def challengeDetail(request, id):
    queryset = Challenges.objects.get(id=id)
    submissions = Submission.objects.filter(challenge=queryset)
    submission_count = submissions.count()
    context = {
        'challenges': queryset,
        'submission_count': submission_count,
    }
    return render(request, template_name='challenges/challengeDetail.html', context=context)


@login_required(login_url='user-login')
def CreateChallenge(request):
    form = ChallengeCreationForm()
    if request.method == 'POST':
        form = ChallengeCreationForm(request.POST, request.FILES)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.instance.created_by = request.user
            challenge.save()
            return redirect('challenge-list')
        else:
            print(form.errors)

    context = {
        'form': form,
    }
    return render(request, template_name='challenges/challengecreation.html', context=context)


def hosterMyChallenges(request):
    mychallenges = Challenges.objects.filter(created_by=request.user)
    context = {
        'mychallenges': mychallenges
    }
    return render(request, template_name='challenges/myChallenges.html', context=context)


@login_required(login_url='user-login')
def challengeUpdate(request, id):
    instance = get_object_or_404(Challenges, id=id)
    form = ChallengeCreationForm(instance=instance)
    if request.method == 'POST':
        form = ChallengeCreationForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            print('post validated....')
            form.save()
            print('updated...')
            return redirect('challenge-list')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, template_name='challenges/challengeUpdation.html', context=context)


@login_required(login_url='user-login')
def viewChallengeSubmission(request, id):
    current_challenge = Challenges.objects.get(id=id)
    submissions_query_set = Submission.objects.filter(challenge=current_challenge, review_status=False).order_by(
        '-submitted_at')
    # review_score = submissions_query_set[1].
    # print(review_score)
    context = {
        'submissions': submissions_query_set,
    }

    return render(request, template_name='challenges/viewSubmissions.html', context=context)


@login_required(login_url='user-login')
def reviewSubmission(request, id):
    current_submission = Submission.objects.get(id=id)
    print(current_submission)
    form = ReviewForm()
    context = {
        'submission': current_submission,
        'form': form,
    }
    if request.method == 'POST':
        try:
            form = ReviewForm(request.POST)
            t_score = int(request.POST.get('criteria1')) + int(request.POST.get('criteria2')) + int(
                request.POST.get('criteria3')) + int(request.POST.get('criteria4')) + int(request.POST.get('criteria5'))
            if form.is_valid():
                review_score = form.save(commit=False)
                review_score.TotalScore = t_score
                review_score.submission = current_submission
                review_score.reviewed_by = request.user
                review_score.submission.review_status = True
                review_score.save()
                return redirect('challenge-list')
            else:
                print(form.errors)

        except IntegrityError:
            messages.error(request, 'Already Reviewed...')

    return render(request, template_name='challenges/challenge_submission_review.html', context=context)


def innovatorMyProposals(request):
    queryset = Submission.objects.filter(applyer=request.user)
    print(queryset)
    context = {
        'submissions': queryset,
    }
    return render(request, template_name='challenges/myProposals.html', context=context)
