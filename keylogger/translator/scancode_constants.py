UNPRESS_INTERVAL = 128  # Unpress scancode will be +128 the press scancode

SPACE = '57'
ENTER = '28'

CAPS_LOCK = '58'
CAPS_LOCK_UNPRESS = '186'
CAPS_LOCK_EXTRA_CODE = '250'

SPECIAL_KEY = '224' # Don't for sure but this code appears when press some keys

BACK = '158'
HELP = '138'
CALC = '140'
SETUP = '141'
SLEEP = '142'
WAKEUP = '143'
PROG1 = '148'
PROG2 = '149'
WWW = '150'
MAIL = '155'
BOOKMARKS = '156'
COMPUTER = '157'
BACK = '158'
FORWARD = '159'
NEXTSONG = '163'
PLAYPAUSE = '164'
PREVIOUSSONG = '165'
STOPCD = '166'
REFRESH = '173'
F13 = '183'
F14 = '184'
F15 = '185'
F22 = '192'
F23 = '193'
SEARCH = '217'
BRIGHTNESSUP = '225'
MEDIA = '226'
SWITCHVIDEOMODE = '227'
BATTERY = '236'
BLUETOOTH = '237'

IGNORED_KEYS = [CAPS_LOCK_UNPRESS, CAPS_LOCK_EXTRA_CODE, BACK, HELP, CALC,
                SETUP, SLEEP, WAKEUP, PROG1, PROG2, WWW, MAIL, BOOKMARKS,
                COMPUTER, BACK, FORWARD, NEXTSONG, PLAYPAUSE, PREVIOUSSONG,
                STOPCD, REFRESH, F13, F14, F15, F22, F23, SEARCH,
                SPECIAL_KEY, BRIGHTNESSUP, MEDIA, SWITCHVIDEOMODE,
                BATTERY, BLUETOOTH] # Collisions with unpress scancodes
