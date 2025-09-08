from music21 import converter, roman

def extract_progression(midi_file):
    score = converter.parse(midi_file) # loading the MIDI file
    k = score.analyze('key') # analyzing the key
    # extracting chord progression
    progression = []
    for c in score.chordify().recurse().getElementsByClass('Chord'):
        rn = roman.romanNumeralFromChord(c, k)
        progression.append(rn.figure)
    return (progression, k) # return the progression and key