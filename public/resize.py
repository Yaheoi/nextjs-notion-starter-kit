from PIL import Image

def compress_image(input_image_path, output_image_path, width, height):
    with Image.open(input_image_path) as image:
        new_width = width
        new_height = height
        resized_image = image.resize((new_width, new_height))
        resized_image.save(output_image_path)
        return resized_image

if __name__ == '__main__':

    input_image_path = 'tree_icon.png'
    px = 128
    output_image_path = 'tree_icon-' + str(px) + 'x' + str(px) + '.png'
    compress_image(input_image_path, output_image_path, px, px)

    px = 192
    output_image_path = 'tree_icon-' + str(px) + 'x' + str(px) + '.png'
    compress_image(input_image_path, output_image_path, px, px)

    px = 48
    output_image_path = 'tree_icon-' + str(px) + 'x' + str(px) + '.png'
    ico = compress_image(input_image_path, output_image_path, px, px)
    ico.save('tree_icon.ico')
