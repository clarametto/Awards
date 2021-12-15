from django.contrib.auth.models import User
from django.test import TestCase
from .models import  Profile, Project, Rating
class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="test_user"
        )
        self.profile = Profile(
            bio="Test profile_photo",
            user=user,
            contact="Test Contact",
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
    def test_update_method(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    def test_create_method(self):
        self.profile.create_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

class ProjectTestClass(TestCase):
    def setUp(self):

        user = User.objects.create(
            username="test_user", first_name="clara", last_name="metto"
        )
        self.project = Project(
            title="Test Photos",
            description="Test Category",
            photo="image.png",
            user=user,
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))
    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
    def test_update_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
    def test_delete_method(self):
        self.project.save_project()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)
    
class RatingTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="test_user", first_name="clara", last_name="metto"
        )
        self.rating = Rating(
            user=user,
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))
