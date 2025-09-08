import ahocorasick
from chord_extractor import extract_progression

patterns = [("P1", ['#ivø4b3', '#ivø4b3']), ("P2", ['IV', 'IV'])]

def build_automaton(patterns):
    A = ahocorasick.Automaton()
    for name, prog in patterns:
        A.add_word("|".join(prog), (name, prog))
    A.make_automaton()
    return A

def detect_patterns(A, sequence):
    seq_str = "|".join(sequence)
    results = []
    for end_char_index, (name, prog) in A.iter(seq_str):
        tokens_up_to_end = seq_str[:end_char_index+1].split("|")
        token_end_index = len(tokens_up_to_end) - 1
        token_start = token_end_index - len(prog) + 1
        matched = sequence[token_start:token_end_index+1]
        results.append((name, prog, token_start, token_end_index, matched))
    return results

if __name__ == "__main__":
    input_track = input("Enter the track path : ")
    sequence, detected_key = extract_progression(input_track) # extracting chord progression sequence and key
    print("Detected Key:", detected_key)
    print("Roman numeral progression:", sequence)
    A = build_automaton(patterns) # building automaton
    matches = detect_patterns(A, sequence) # detecting known patterns
    if matches:
        for name, prog, start, end, matched in matches:
            print(f"Found {name}: {prog} at {start}..{end} ------> {' '.join(matched)}")
    else:
        print("No match found")