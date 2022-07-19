from django import forms
# TODO: from .widgets import CustomClearableFileInput
from .models import BodyPart, Equipment, Target, Workout


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = '__all__'

    # TODO:
    # image = forms.ImageField(
    #     label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        body_parts = BodyPart.objects.all()
        equipment = Equipment.objects.all()
        targets = Target.objects.all()
        friendly_names = [(b.id, b.friendly_name2) for b in body_parts]
        equipment_friendly_names = [(e.id, e.friendly_name2) for e in equipment]
        target_friendly_names = [(t.id, t.friendly_name2) for t in targets]

        self.fields['body_part'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['equipment'].choices = equipment_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['target'].choices = target_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
