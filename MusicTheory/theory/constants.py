SCALE_FORUMULAS = {
    'Ionian': 'W,W,H,W,W,W,H',
    'Dorian': 'W,H,W,W,W,H,W',
    'Phrygian': 'H,W,W,W,H,W,W',
    'Lydian': 'W,W,W,H,W,W,H',
    'Mixolydian': 'W,W,H,W,W,H,W',
    'Aeolian': 'W,H,W,W,H,W,W',
    'Locrian': 'H,W,W,H,W,W,W'
}

RANGE = [0,1,2,3,4,5,6,7,8]

ORDER = [0,1,1,2,3,3,4,5,6,6,7,8,8,9,10,10,11]

NOTES = [
    'C', 'C sharp', 'D flat', 'D',
    'D sharp', 'E flat', 'E', 'F', 
    'F sharp', 'G flat', 'G', 'G sharp'
    'A flat', 'A', 'A sharp'
    'B flat', 'B' 
]

NOTE_LETTER_DISTANCE = {
    '0': ['C', 'C sharp'],
    '1': ['D flat', 'D', 'D sharp'],
    '2': ['E flat', 'E', 'E sharp'],
    '3': ['F flat', 'F', 'F sharp'],
    '4': ['G flat', 'G', 'G sharp'],
    '5': ['A flat', 'A', 'A sharp'],
    '6': ['B flat', 'B'],
}

NOTE_LETTER = {
    '0': ['C'],
    '1': ['C sharp', 'D flat'],
    '2': ['D'],
    '3': ['D sharp', 'E flat'],
    '4': ['E'],
    '5': ['F'],
    '6': ['F sharp', 'G flat'],
    '7': ['G'],
    '8': ['G sharp', 'A flat'],
    '9': ['A'],
    '10': ['A sharp', 'B flat'],
    '11': ['B'],
}
