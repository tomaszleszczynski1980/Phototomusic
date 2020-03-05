from math import sin, pi
from PIL import Image
import numpy
# import imageio
import wave
import struct


def read_image(image_file_path: str):
    """
    Opens image file, writes its pixels as numpy array
    :param image_file_path: str
    :return numpy array:
    """

    pixels = numpy.array(Image.open(image_file_path))

    return pixels


def write_wav_file(wavefilename: str, picture, sample_rate=44100):

    with wave.open(wavefilename, 'w') as output:
        output.setparams((1, 2, sample_rate, 0, 'NONE', 'not compressed'))

        for sub_array in picture:
            for item in sub_array:
                amplitude = item[0]
                frequency = item[1]
                time = item[2]
                sound = amplitude * sin(2 * pi * frequency * (time / sample_rate))
                packed_sound = struct.pack('h', int(sound))
                output.writeframes(packed_sound)


def main(image_file, wav_file):
    picture = read_image(image_file)
    write_wav_file(wav_file, picture)


if __name__ == '__main__':
    from sys import argv

    try:
        if len(argv) >= 3:
            print('Processing...')
            main(argv[1], argv[2])
        elif len(argv) == 2:
            print('Processing...')
            main(argv[1], (argv[1].split('.')[0]) + '.wav')
        else:
            filename = input('Image file path> ')
            print('Processing...')
            main(filename, (filename.rsplit('.')[0]) + '.wav')

    except FileNotFoundError:
        print('File not found')
    except Image.UnidentifiedImageError:
        print('Invalid image format')
