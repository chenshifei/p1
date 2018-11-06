def frame_str(text):
    text_len = len(text)
    padding = 2
    width = text_len + 2 * padding
    print( width * '*' )
    print('* ' + text + ' *')
    print( width * '*' )

