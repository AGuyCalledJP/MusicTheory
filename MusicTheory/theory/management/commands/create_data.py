from django.core.management.base import BaseCommand, CommandError
from theory.models import Note, Interval, Scale, Key, Chord
from theory.constants import RANGE, NOTES, ORDER, SCALE_FORUMULAS

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass

    def create_notes(self):
        for i in RANGE:
            for j, note in enumerate(NOTES):
                Note.objects.create(name=note, range=i, order=ORDER[j])

    def create_keys(self):
        notes = Note.objects.filter(range=0)
        for note in notes:
            Key.objects.create(
                name=note.name,
                root=note)

    def create_scales(self):
        keys = Key.objects.all()
        for key in keys:
            for scale_name in SCALE_FORUMULAS.keys():
                scale = Scale.objects.create(
                    name=scale_name,
                    key=key,
                    pattern=SCALE_FORUMULAS.get(scale_name))
                notes = []
                curr_note = scale.key.root
                while curr_note:
                    for step in scale.pattern.split(','):
                        notes.append(curr_note)
                        curr_note = curr_note.note_by_step(step)
                scale.notes.set(notes)
    
    def set_scale_intervals(self):
        pass

    def set_scale_chords(self):
        pass

    def create_intervals(self):
        pass

    def create_chords(self):
        pass