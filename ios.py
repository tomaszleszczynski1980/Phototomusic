"""
This is an implementation of picture to wave to be run in Pythonista IDE for iOS
Try to built real iOS app with XCode and some tricks
"""

import appex, sound     # special Pythonista for iOS modules (run only in Pythonista IDE on iOS)
from PIL import Image   # not standart but very popular library for image processing, you can get them from PyPI
import numpy as np      # the same as above, but for scientific computing
import picture_to_wave  # my own module that converts picture to wave, should be in same folder as this file


def main(wav_file):
    # checking if this script is run properly (as an iOS extension)
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return None

    # gets selected picture
    picture = appex.get_image(image_type='pil')
    if not picture:
        print('No input image')
        return None

    # main operation of conversion and creating wav file
    pixels = np.array(Image.open(picture))
    audio = picture_to_wave.image_to_sound(pixels)
    picture_to_wave.save_wav(wav_file, audio)

    # playing just created wav file
    sound.set_volume(1)
    player = sound.Player(wav_file)
    player.play()


if __name__ == '__main__':
    main(wav_file = 'temp.wav')
