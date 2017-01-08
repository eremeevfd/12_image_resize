import argparse
from PIL import Image
import os.path


def create_argument_parser():
    parser = argparse.ArgumentParser(description='Resize an image')
    parser.add_argument('input', help='path to original image')
    parser.add_argument('--output', help='path to resized image')
    parser.add_argument('--width', type=int, help='new width of image')
    parser.add_argument('--height', type=int, help='new height of image')
    parser.add_argument('--scale', type=float, help='new scale of image')
    return parser


def parse_arguments(parser):
    arguments = parser.parse_args()
    return arguments


def open_image(path_to_image):
    if os.path.exists(path_to_image):
        return Image.open(path_to_image)
    else:
        exit('Error: No such image')


def save_image(image, path):
    image.save(path)


def calculate_image_proportions(image):
    return image.size[0] / image.size[1]


def resize_image_using_scale(scale, original_image):
    return original_image.resize((int(scale * original_image.size[0]),
                                  int(scale * original_image.size[1])))


def warn_if_new_proportions_not_matching(original_image, resized_image):
    if not calculate_image_proportions(original_image) == calculate_image_proportions(resized_image):
        print('You are changing proportions of picture!')


def resizing_controller(arguments, original_image):
    if arguments.scale:
        if arguments.width or arguments.height:
            exit('Error: using scale and width/height together')
        else:
            return resize_image_using_scale(arguments.scale, original_image)
    elif arguments.height and arguments.width:
        return original_image.resize((arguments.height, arguments.width))
    elif arguments.height:
        original_image_scale = calculate_image_proportions(original_image)
        return original_image.resize((arguments.height, int(arguments.height / original_image_scale)))
    elif arguments.width:
        original_image_scale = calculate_image_proportions(original_image)
        return original_image.resize((int(arguments.width * original_image_scale), arguments.width))


def get_extension():
    return os.path.splitext(path_to_original)[1]


def get_name_of_original_image():
    return os.path.splitext(os.path.basename(os.path.abspath(path_to_original)))[0]


def get_original_image_absolute_path(path_to_original):
    return os.path.abspath(path_to_original)


def get_original_image_directory_name(absolute_path):
    return os.path.dirname(absolute_path)


def get_path_ro_result_image_in_original_image_dir(path_to_original):
    original_image_absolute_path = get_original_image_absolute_path(path_to_original)
    original_image_directory_name = get_original_image_directory_name(original_image_absolute_path)
    return os.path.join(original_image_directory_name)


def get_resized_image_name_with_new_properties(original_name, resized_image, extension):
    return '{original_name}__{height}x{width}{extension}'.format(
                                                                original_name=original_name,
                                                                height=resized_image.size[0],
                                                                width=resized_image.size[1],
                                                                extension=extension
                                                                )


def resize_image(path_to_original, path_to_result):
    original_image = open_image(path_to_original)
    extension = get_extension()
    original_name = get_name_of_original_image()
    resized_image = resizing_controller(arguments, original_image)
    resized_name = get_resized_image_name_with_new_properties(original_name, resized_image, extension)
    if path_to_result:
        path_to_result = os.path.join(path_to_result, resized_name)
    else:
        path_to_result = os.path.join(get_path_ro_result_image_in_original_image_dir(path_to_original), resized_name)
    warn_if_new_proportions_not_matching(original_image, resized_image)
    save_image(resized_image, path_to_result)


if __name__ == '__main__':
    parser = create_argument_parser()
    arguments = parse_arguments(parser)
    path_to_original = arguments.input
    if arguments.output:
        resize_image(path_to_original, arguments.output)
    else:
        resize_image(path_to_original, None)

