import picture_to_wave

def main(image_file: str, wav_file: str):

    try:
        pixels = picture_to_wave.read_image(image_file)
        audio = picture_to_wave.image_to_sound(pixels)
        picture_to_wave.save_wav(wav_file, audio)

    except FileNotFoundError:
        print('File not found')


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
    except picture_to_wave.Image.UnidentifiedImageError:
        print('Invalid image format')
