def recite(start_verse, end_verse):
    verse = {
        1: "Jack built.",
        2: "lay in the house",
        3: "ate the malt",
        4: "killed the rat",
        5: "worried the cat",
        6: "tossed the dog",
        7: "milked the cow with the crumpled horn",
        8: "kissed the maiden all forlorn",
        9: "married the man all tattered and torn",
        10: "woke the priest all shaven and shorn",
        11: "kept the rooster that crowed in the morn",
        12: "belonged to the farmer sowing his corn"
    }
    header = {
        1: "house",
        2: "malt",
        3: "rat",
        4: "cat",
        5: "dog",
        6: "cow with the crumpled horn",
        7: "maiden all forlorn",
        8: "man all tattered and torn",
        9: "priest all shaven and shorn",
        10: "rooster that crowed in the morn",
        11: "farmer sowing his corn",
        12: "horse and the hound and the horn"
    }
    poem = []
    for num in range(start_verse, end_verse + 1):
        line = f'This is the {header[num]}'
        for i in range(num, 0, -1):
            line += f' that {verse[i]}'
        poem.append(line)
    return poem
