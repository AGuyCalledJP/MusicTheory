from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=255, default='')
    order = models.IntegerField(default=0)
    range = models.IntegerField(default=0)
    intervals = models.ManyToManyField('Interval', related_name='notes_in_interval')
    keys = models.ManyToManyField('Key', related_name='notes_in_key')
    scales = models.ManyToManyField('Scales', related_name='notes_in_scale')

    @property
    def distance_to_note(self, note):
        low = min(self.order, note.order)
        high = max(self.order, note.order)
        return high - low

    @property
    def note_by_step(self, step):
        order = self.order
        if step == 'W':
            order = (self.order + 2) % 12
        elif step == 'H':
            order = (self.order + 1) % 12
        if order < self.order and self.range == 8:
            return None
        if order < self.order:
            return Note.objects.filter(
                range=self.range + 1, order=order)
        else:
            return Note.objects.filter(
                range=self.range, order=order)


    def __str__(self):
        return str(self.name)


class Key(models.Model):
    name = models.CharField(max_length=255, default='')
    root = models.ForeignKey('Note', on_delete=models.CASCADE, related_name='key_roots')
    intervals = models.ManyToManyField('Interval', related_name='intervals_in_key')
    chords = models.ManyToManyField('Chord', related_name='chords_in_key')

    def __str__(self):
        return str(self.name)


class Scale(models.Model):
    name = models.CharField(max_length=255, default='')
    key = models.ForeignKey('Key', on_delete=models.DO_NOTHING, related_name='scales_in_key')
    notes = models.ManyToManyField('Note', related_name='notes_in_scale')
    pattern = models.CharField(max_length=255, default='')
    intervals = models.ManyToManyField('Interval', related_name='intervals_in_scale')
    chords = models.ManyToManyField('Chord', related_name='chords_in_scale')

    def __str__(self):
        return str(self.name)


class Interval(models.Model):
    name = models.CharField(max_length=255, 
        choices=[
            ('semitone', 'Semitone'),
            ('tone', 'Tone'),
            ('unison', 'Unison'),
            ('2nd', '2nd'),
            ('3rd', '3rd'),
            ('4th', '4th'),
            ('5th', '5th'),
            ('6th', '6th'),
            ('7th', '7th'),
            ('octave', 'Octave'),
        ]
    )
    quality = models.CharField(max_length=255, 
        choices=[
            ('major', 'Major'),
            ('minor', 'Minor'), 
            ('perfect', 'Perfect'),
            ('augmented', 'Augemented'),
            ('diminished', 'Diminished')
        ]
    )
    chords = models.ManyToManyField('Chord', related_name='chord_in_interval')

    def __str__(self):
        return str(self.name)


class Chord(models.Model):
    name = models.CharField(max_length=255, default='')
    root_note = models.CharField(max_length=255, default='')
    intervals = models.ManyToManyField('Interval', related_name='intervals_in_chord')

    def __str__(self):
        return str(self.name)
