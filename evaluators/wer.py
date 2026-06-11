import difflib

def calculate_wer(reference: str, hypothesis: str) -> float:
    if not reference:
        raise ValueError("Reference cannot be empty")
    if not hypothesis:
        raise ValueError("Hypothesis cannot be empty")
    
    ref_words = reference.lower().split()
    hyp_words = hypothesis.lower().split()
    
    # use difflib to find differences
    matcher = difflib.SequenceMatcher(None, ref_words, hyp_words)
    
    substitutions = 0
    deletions = 0
    insertions = 0
    
    for opcode, r1, r2, h1, h2 in matcher.get_opcodes():
        if opcode == 'replace':
            substitutions += max(r2 - r1, h2 - h1)
        elif opcode == 'delete':
            deletions += r2 - r1
        elif opcode == 'insert':
            insertions += h2 - h1
    
    wer = (substitutions + deletions + insertions) / len(ref_words)
    return round(wer, 4)
    

# Should give WER = 0.5 (2 errors / 4 words)
print(calculate_wer("I live in Chicago", "I love Chicago"))   

"""
There are 5 opcodes: I love Chicago vs I live in Chicago
OpcodeMeaningExampleequalwords are the same"I" == "I"replaceword was substituted"live" → "love" deleteword was removed"in" → nothinginsertword was addednothing → "extra"movenot used in SequenceMatcher—
So get_opcodes() returns a list of tuples like:
python[
    ('equal', 0, 1, 0, 1),    # "I" matches "I"
    ('replace', 1, 2, 1, 2),  # "live" replaced with "love"  
    ('delete', 2, 3, 2, 2),   # "in" deleted
    ('equal', 3, 4, 2, 3),    # "Chicago" matches "Chicago"
]
Each tuple is:
(opcode, ref_start, ref_end, hyp_start, hyp_end)
So our code loops through each operation and counts how many substitutions, deletions, and insertions happened.
It's the same logic as WER — just difflib doing the heavy lifting of finding the differences.
Now run the test — what does calculate_wer("I live in Chicago", "I love Chicago") return? 

"""