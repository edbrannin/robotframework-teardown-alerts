import os

def resolve_filename(filename, suffix=".wav"):
    if os.path.exists(filename):
        return filename
    elif os.path.exists(filename + suffix):
        return filename + suffix
    else:
        raise Exception("File not found: {0} ({1})".format(filename, os.path.abspath(filename)))


def play_sound(sound):
    filename = resolve_filename(sound)
    try:
        import winsound
    except:
        print("Unable to load winsound.  Please pretend you just heard {0}".format(filename))
        # TODO: support Linux?
        # https://wiki.python.org/moin/Audio/
        # TODO: Make this a RIDE plugin?
        # http://www.wxpython.org/docs/api/wx.media.MediaCtrl-class.html
        return
    # http://stackoverflow.com/a/311634
    winsound.PlaySound(filename, winsound.SND_FILENAME)

def play_success():
    play_sound("253887__themusicalnomad__positive-beeps.wav")

def play_failure_alert():
    play_sound("124996__phmiller42__aww.wav")

