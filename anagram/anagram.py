def find_anagrams(word, candidates):
    result = []
    for cand in candidates:
        if word.lower() != cand.lower() and sorted(word.lower()) == sorted(cand.lower()):
            result.append(cand)
    return result
