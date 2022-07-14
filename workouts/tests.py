from django.forms import ValidationError
from django.db import IntegrityError
from .models import BodyPart, Equipment, Target, Workout
from django.test import TestCase

# Create your tests here.
# TODO: use tests in products as basis

class TestViews(TestCase):

    def test_get_workouts(self):
        """ Test that when browsing to /workouts/ we get a 302 code,
        because we need to be logged in """
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 302)


class TestModels(TestCase):

    # Tests for BodyPart model
    def test_all_blank_body_part(self):
        """Test that when a body_part is created with no
        info, we get a ValidationError"""
        body_part = BodyPart.objects.create()
        with self.assertRaises(ValidationError):
            body_part.full_clean()

    def test_friendly_name_blank_body_part(self):
        """Test that when a body_part is created, friendly name is blank"""
        body_part = BodyPart.objects.create(
            name='test_part')
        self.assertFalse(body_part.friendly_name)

    def test_max_length_name_body_part(self):
        """Test that when a body_part is created with a name longer than
        254 characters, we get a ValidationError"""
        long_name = "x" * 255
        body_part = BodyPart.objects.create(name=long_name)
        with self.assertRaises(ValidationError):
            body_part.full_clean()
    
    # Tests for Equipment model
    def test_all_blank_equipment(self):
        """Test that when a equipment is created with no
        info, we get a ValidationError"""
        equipment = Equipment.objects.create()
        with self.assertRaises(ValidationError):
            equipment.full_clean()

    def test_friendly_name_blank_equipment(self):
        """Test that when a equipment is created, friendly name is blank"""
        equipment = Equipment.objects.create(
            name='test_equipment')
        self.assertFalse(equipment.friendly_name)

    def test_max_length_name_equipment(self):
        """Test that when a equipment is created with a name longer than
        254 characters, we get a ValidationError"""
        long_name = "x" * 255
        equipment = Equipment.objects.create(name=long_name)
        with self.assertRaises(ValidationError):
            equipment.full_clean()

    # Tests for Target model
    def test_all_blank_target(self):
        """Test that when a target is created with no
        info, we get a ValidationError"""
        target = Target.objects.create()
        with self.assertRaises(ValidationError):
            target.full_clean()

    def test_friendly_name_blank_target(self):
        """Test that when a target is created, friendly name is blank"""
        target = Target.objects.create(
            name='test_target')
        self.assertFalse(target.friendly_name)

    def test_max_length_name_target(self):
        """Test that when a target is created with a name longer than
        254 characters, we get a ValidationError"""
        long_name = "x" * 255
        target = Target.objects.create(name=long_name)
        with self.assertRaises(ValidationError):
            target.full_clean()

    # Tests for Workout model
    def test_blank_name_workout(self):
        """Test that when a workout is created with no name,
        we get a ValidationError"""
        workout = Workout.objects.create(
            description='test description', image='test.gif')
        with self.assertRaises(ValidationError):
            workout.full_clean()
    
    def test_blank_description_workout(self):
        """Test that when a workout is created with no description,
        we get a ValidationError"""
        workout = Workout.objects.create(name='test_workout', image='test.gif')
        with self.assertRaises(ValidationError):
            workout.full_clean()
    
    def test_blank_image_workout(self):
        """Test that when a workout is created with no image,
        we get a ValidationError"""
        with self.assertRaises(ValidationError):
            workout = Workout.objects.create(
                name='test_workout', description='test description')
            workout.full_clean()
    
    def test_blank_fields_workout(self):
        """Test that when a workout is created, body_part, equipment,
        rating and target are blank"""
        workout = Workout.objects.create(
            name='test_workout', description='test description', image='test.gif')
        self.assertFalse(workout.body_part)
        self.assertFalse(workout.equipment)
        self.assertFalse(workout.rating)
        self.assertFalse(workout.target)

    def test_max_length_name_workout(self):
        """Test that when a workout is created with a name
        longer than 254 characters, we get a ValidationError"""
        long_name = "x" * 255
        workout = Workout.objects.create(
            name=long_name, description='test description', image='test.gif')
        with self.assertRaises(ValidationError):
            workout.full_clean()
