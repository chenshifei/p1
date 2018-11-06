from locale import strxfrm

fromdict = {}
todict = {}
result = {}

def build_dict(fromlang, tolang):
    with open('inducks_charactername.isv') as f:
        for line in f:
            entry = line.strip().split('^')
            preferred = entry[3].upper() == 'Y'
            if preferred:
                lang = entry[1]
                key = entry[0]
                title = entry[2]
                if lang == fromlang:
                    fromdict[key] = title
                elif lang == tolang:
                    todict[key] = title

def find_same_title():
    for k, v in fromdict.items():
        if k in todict and v != todict[k]:
            new_key = v
            new_value = todict[k]
            result[new_key] = new_value

def print_result():
    max_length = 0
    for key in result.keys():
        if len(key) > max_length:
            max_length = len(key)
    
    for key in sorted(result, key=strxfrm):
        print(key.ljust(max_length + 1), result[key])

def translate(fromlang, tolang):
    build_dict(fromlang, tolang)
    find_same_title()
    print_result()
