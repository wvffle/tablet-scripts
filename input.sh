import os, curses
s = curses.initscr()
curses.cbreak()
curses.noecho()
s.keypad(1)

s.addstr(0, 0, '~~:q to quit')
s.refresh()

# FIX: Add End, Home recognized as ~
map = {
    339: 'Prior',
    338: 'Next',
    331: 'Insert',
    330: 'Delete',
    276: 'F12',
    275: 'F11',
    274: 'F10',
    273: 'F9',
    272: 'F8',
    271: 'F7',
    270: 'F6',
    269: 'F5',
    268: 'F4',
    267: 'F3',
    266: 'F2',
    265: 'F1',
    261: 'Right',
    260: 'Left',
    259: 'Up',
    258: 'Down',
    127: 'BackSpace',
    126: 'asciitilde',
    125: 'braceright',
    124: 'bar',
    123: 'braceleft',
    96: 'grave',
    95: 'underscore',
    94: 'asciicircum',
    93: 'bracketright',
    92: 'backslash',
    91: 'bracketleft',
    64: 'at',
    63: 'question',
    62: 'greater',
    63: 'equal',
    60: 'less',
    58: 'colon',
    59: 'semicolon',
    47: 'slash',
    46: 'period',
    45: 'minus',
    44: 'comma',
    43: 'plus',
    42: 'asterisk',
    41: 'parenright',
    40: 'parenleft',
    39: 'apostrophe',
    38: 'ampersand',
    37: 'percent',
    36: 'dollar',
    34: 'quotedbl',
    33: 'exclam',
    32: 'space',
    27: 'Escape',
    10: 'Return',
    9: 'Tab'
}

combo = ''
while 1:
    key = s.getch()
    # TODO: support ctrl
    # TODO: support shift+ctrl
    s.addstr(1, 0, ' ' * 16)
    if key in map:
        ch = map[key]
        combo += chr(key)
    else:
        ch = chr(key)
        combo += ch
    combo = combo[-4:]
    if combo == '~~:q':
        break
    s.addstr(1, 0, '{} {}'.format(combo, ch))
    s.refresh()
    os.system('xdotool key --clearmodifiers {}'.format(ch))
