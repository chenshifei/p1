def build_dict(target_lang):
    result = {}
    with open('inducks_charactername.isv') as f:
        for line in f:
            character, lang, name, preferred, dummy_comment, _ = line.strip().split('^')
            if preferred and target_lang == lang:
                result[character] = name
    return result

def find_same_name(from_dict, to_dict):
    result = {}
    for character, name in from_dict.items():
        if character in to_dict and name != to_dict[character]:
            key = name
            value = to_dict[character]
            result[key] = value
    return result

def print_results(results, lang='en'):
    max_length = 0
    for key in results.keys():
        if len(key) > max_length:
            max_length = len(key)
    '''
    I found PyICU could be a possible solution to sorting these strings by their language code.
    Something like this

    collator = icu.Collator.createInstance(icu.Locale(lang))

    But I can never get PyICU built properly on my macOS. So I couldn't verify this :(
    '''
    for key in sorted(results):
        print(key.ljust(max_length + 1), results[key])

def translate(fromlang, tolang):
    from_dict = build_dict(fromlang)
    to_dict = build_dict(tolang)
    results = find_same_name(from_dict, to_dict)
    print_results(results)
