from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        activity = Activity.objects.create(user=user, type='Running', duration=30)
        self.assertEqual(str(activity), 'testuser - Running')

    def test_leaderboard_creation(self):
        user = User.objects.create_user(username='testuser2', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, score=50)
        self.assertEqual(str(leaderboard), 'testuser2: 50')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(str(workout), 'Test Workout')
