from django.forms import ValidationError
from django.db import IntegrityError
from .models import BodyPart, Equipment, Target, Workout
from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):

    def test_get_workouts(self):
        """ Test that when browsing to /workouts/ we get a 302 code,
        because we need to be logged in """
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 302)


class TestModels(TestCase): 

    # Create some test objects
    def setUp(self):
        self.test_bodypart = BodyPart.objects.create(
            name="test_bodypart")

        self.test_equipment = Equipment.objects.create(
            name="test_equipment")

        self.test_target = Target.objects.create(
            name="test_target")    
            

        self.test_workout = Workout.objects.create(
            name="Test Workout",
            description="Test",
            image="test.jpg",
            bodypart=self.test_bodypart,
            equipment=self.test_equipment,
            target=self.test_target            
            )
    
    def test_delete_fields_of_workout(self):
        """Test that when the bodypart, equipment and target objects are deleted for a workout,
        those fields on the workout are set to null"""
        self.test_bodypart.delete()
        self.test_equipment.delete()
        self.test_target.delete()
        with self.assertRaises(BodyPart.DoesNotExist):
            BodyPart.objects.get(name="test_bodypart")
        with self.assertRaises(Equipment.DoesNotExist):
            Equipment.objects.get(name="test_equipment")
        with self.assertRaises(Target.DoesNotExist):
            Target.objects.get(name="test_target")
        workout = Workout.objects.get(name="Test Workout")
        self.assertIsNone(workout.bodypart)
        self.assertIsNone(workout.equipment)
        self.assertIsNone(workout.target)

    # Tests for BodyPart model
    def test_all_blank_bodypart(self):
        """Test that when a bodypart is created with no
        info, we get a ValidationError"""
        bodypart = BodyPart.objects.create()
        with self.assertRaises(ValidationError):
            bodypart.full_clean()

    def test_friendly_name_blank_bodypart(self):
        """Test that when a bodypart is created, friendly name is blank"""
        bodypart = BodyPart.objects.create(
            name='test_part')
        self.assertFalse(bodypart.friendly_name)

    def test_max_length_name_bodypart(self):
        """Test that when a bodypart is created with a name longer than
        254 characters, we get a ValidationError"""
        long_name = "x" * 255
        bodypart = BodyPart.objects.create(name=long_name)
        with self.assertRaises(ValidationError):
            bodypart.full_clean()
    
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
        """Test that when a workout is created, bodypart, equipment,
        rating and target are blank"""
        workout = Workout.objects.create(
            name='test_workout', description='test description', image='test.gif')
        self.assertFalse(workout.bodypart)
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

