"""
This module implements functions that changes picture file to wave file
"""

from PIL import Image
from math import sin, pi
import numpy as np
import wave
import struct


def read_image(image_file_path: str):
    """
    Opens image file, writes its pixels as numpy array
    :param image_file_path: str
    :return numpy array:
    """

    pixels = np.array(Image.open(image_file_path))

    return pixels


def image_to_sound(pixels, sample_rate=44100.0):
    """
    Converts numpy array to wave file basing on conversion pattern
    :param pixels: numpy array
    :param sample_rate: float: value in Hz
    :return audio: list
    """

    # musical scale frequency includes in range from about 20Hz to 8000Hz
    # color values are represented by 3-byte value (red, green, blue)
    # let's take first byte (red) for frequency (in range 20 Hz to 5120 Hz)
    # second byte (green) for duration in milliseconds (from 1 do 256)
    # and third (blue) for volume in range (0, 1)

    audio = []
    for item in pixels:
        for item2 in item:
            frequency = (item2[0] + 1) * 20
            duration = item2[1] + 1
            volume = item2[2] / 255
            samples_number = int(duration * (sample_rate / 1000.0))

        for sample in range(1, samples_number + 1):
            audio.append(volume * sin(2 * pi * frequency * (sample / sample_rate)))

    return audio


def image_to_sound_2(pixels, sample_rate=44100.0):
    """
    Converts numpy array to wave file basing on conversion pattern
    :param pixels: numpy array
    :param sample_rate: float: value in Hz
    :return audio: list
    """

    # musical scale frequency includes in range from about 20Hz to 8000Hz
    # color values are represented by 3-byte value (red, green, blue)
    # let's take first byte (red) for frequency (in range 20 Hz to 5120 Hz)
    # second byte (green) for duration in milliseconds (from 1 do 256)
    # and third (blue) for volume in range (0, 1)

    audio = []
    for item in pixels:
        for item2 in item:
            frequency = (item2[0] + 1) * 20
            duration = item2[1] + 1
            volume = item2[2] / 255
            audio.append(volume * sin(2 * pi * frequency * (sample_rate / duration)))

    return audio


def save_wav(wav_file_path: str, audio: list, overwrite=False,
             num_channels=1, sample_width=2, sample_rate=44100.0):
    """
    Writes wave file
    :param wav_file_path: str
    :param audio: list
    :param overwrite: bool (default False): if True overwrites existing file
    :param sample_width: int: wave param
    :param num_channels:  int: number of channels in wave file
    :param sample_rate: float (Hz)
    :raises FileExistsError if file exists, and overwrite is off (False)
    """

    num_frames = len(audio)
    compression_type = "NONE"
    compression_name = "not compressed"

    with wave.open(wav_file_path, 'w') as wav_file:
        wav_file.setparams((num_channels, sample_width, sample_rate,
                           num_frames, compression_type, compression_name))

        for sample in audio:
            wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))
