"""Script to build digital Christmas card."""

from PIL import Image, ImageDraw, ImageFont

IMAGE_HEIGHT = 5000
IMAGE_WIDTH = 5000

CHRISTMAS_TREE_COLOUR = (26, 222, 51)


def draw_rectangle(draw, coords, fill, width=0, outline=None):
    """
    Draw a rectangle on the image.

    Args:
        draw (ImageDraw): The ImageDraw object to draw on.
        coords (list): The coordinates of the rectangle.
        fill (str): The fill colour of the rectangle.
        width (int): The width of the rectangle.
        outline (str): The outline colour of the rectangle.
    """
    draw.rectangle(coords, fill=fill, width=width, outline=outline)


def draw_ellipse(draw, coords, fill, outline=None):
    """
    Draw an ellipse on the image.

    Args:
        draw (ImageDraw): The ImageDraw object to draw on.
        coords (list): The coordinates of the ellipse.
        fill (str): The fill colour of the ellipse.
        outline (str): The outline colour of the ellipse.
    """
    draw.ellipse(coords, fill=fill, outline=outline)


def draw_text(draw, coords, text, font, fill=(255, 255, 255)):
    """
    Draw text on the image.

    Args:
        draw (ImageDraw): The ImageDraw object to draw on.
        coords (list): The coordinates of the text.
        text (str): The text to draw.
        font (ImageFont): The font to use.
        fill (str): The fill colour of the text.
    """
    draw.text(coords, text, fill, font=font)


def draw_television(draw, image_width, image_height):
    """
    Draw a television on the image.

    Args:
        draw (ImageDraw): The ImageDraw object to draw on.
        image_width (int): The width of the image.
        image_height (int): The height of the image.
    """

    draw_rectangle(
        draw,
        [
            (image_width / 100) * 3,
            (image_width / 100) * 53,
            (image_height / 100) * 49,
            (image_width / 100) * 74,
        ],
        fill="black",
    )
    draw_rectangle(
        draw,
        [
            (image_width / 100) * 5,
            (image_width / 100) * 55,
            (image_height / 100) * 50,
            (image_width / 100) * 78,
        ],
        fill=(206, 198, 209),
        width=10,
        outline="black",
    )
    draw_rectangle(
        draw,
        [
            (image_width / 100) * 5,
            (image_height / 100) * 78,
            (image_width / 100) * 5.2,
            (image_height / 100) * 87.5,
        ],
        fill="black",
    )
    draw_rectangle(
        draw,
        [
            (image_width / 100) * 49.5,
            (image_height / 100) * 78,
            (image_width / 100) * 49.7,
            (image_height / 100) * 87.5,
        ],
        fill="black",
    )
    draw_rectangle(
        draw,
        [
            (image_width / 100) * 7,
            (image_width / 100) * 57,
            (image_height / 100) * 38,
            (image_width / 100) * 76,
        ],
        fill=(89, 92, 208),
    )
    draw_ellipse(
        draw,
        (
            (image_width / 100) * 43,
            (image_height / 100) * 63,
            (image_width / 100) * 44,
            (image_height / 100) * 64,
        ),
        fill="red",
        outline=(0, 0, 0),
    )
    draw_ellipse(
        draw,
        (
            (image_width / 100) * 42,
            (image_height / 100) * 69,
            (image_width / 100) * 45,
            (image_height / 100) * 72,
        ),
        fill="black",
        outline=(0, 0, 0),
    )
    draw_ellipse(
        draw,
        (
            (image_width / 100) * 42,
            (image_height / 100) * 73,
            (image_width / 100) * 45,
            (image_height / 100) * 76,
        ),
        fill="black",
        outline=(0, 0, 0),
    )


def draw_hanging_frame(draw, image_width, image_height):
    """
    Draw a hanging frame on the image.

    Args:
        draw (ImageDraw): The ImageDraw object to draw on.
        image_width (int): The width of the image.
        image_height (int): The height of the image.
    """
    draw_rectangle(
        draw,
        [
            (image_width / 100) * 15,
            (image_width / 100) * 20,
            (image_height / 100) * 55,
            (image_width / 100) * 45,
        ],
        fill=(217, 41, 209),
        width=10,
        outline="blue",
    )

    font = ImageFont.truetype("docs/Audiowide-Regular.ttf", 200)
    texts = [
        "%%%%%%%%%%%",
        "%       HOME       %",
        "%      SWEET      %",
        "%       HOME       %",
        "%%%%%%%%%%%",
    ]
    for i, text in enumerate(texts):
        draw_text(
            draw,
            ((image_width / 100) * 16, (image_height / 100) * (21 + i * 5)),
            text,
            font,
        )


def draw_christmas_tree(draw, image_width, image_height):
    """
    Draw a Christmas tree on the image.

    Args:
        draw (ImageDraw): The ImageDraw object to draw on.
        image_width (int): The width of the image.
        image_height (int): The height of the image.
    """
    tree_coords = [
        [70, 20, 90, 20, 80, 5],
        [70, 35, 90, 35, 80, 15],
        [65, 55, 95, 55, 80, 30],
        [60, 75, 98, 75, 80, 40],
    ]
    for coords in tree_coords:
        draw.polygon(
            [
                (image_width / 100) * coords[0],
                (image_height / 100) * coords[1],
                (image_width / 100) * coords[2],
                (image_height / 100) * coords[3],
                (image_width / 100) * coords[4],
                (image_height / 100) * coords[5],
            ],
            fill=CHRISTMAS_TREE_COLOUR,
        )
    draw_rectangle(
        draw,
        [
            (image_width / 100) * 75,
            (image_height / 100) * 75,
            (image_width / 100) * 85,
            (image_height / 100) * 80,
        ],
        fill="brown",
    )
    draw.polygon(
        [
            (image_width / 100) * 60,
            (image_height / 100) * 80,
            (image_width / 100) * 98,
            (image_height / 100) * 80,
            (image_width / 100) * 90,
            (image_height / 100) * 95,
            (image_width / 100) * 68,
            (image_height / 100) * 95,
        ],
        fill="red",
    )


def draw_baubles(draw, image_width, image_height, light_group_1, light_group_2):
    """
    Draw baubles on the Christmas tree, flashing colours.

    Args:
        draw (ImageDraw): The ImageDraw object to draw on.
        image_width (int): The width of the image.
        image_height (int): The height of the image.
        light_group_1 (str): The colour of the first group of lights.
        light_group_2 (str): The colour of the second group of lights.
    """
    bauble_coords = [
        [70, 20, 75, 25, light_group_1],
        [85, 20, 90, 25, light_group_2],
        [70, 35, 75, 40, light_group_2],
        [85, 35, 90, 40, light_group_1],
        [65, 55, 70, 60, light_group_1],
        [90, 55, 95, 60, light_group_2],
        [60, 75, 65, 80, light_group_2],
        [95, 75, 100, 80, light_group_1],
    ]
    for x1, y1, x2, y2, fill in bauble_coords:
        draw_ellipse(
            draw,
            [
                (image_width / 100) * x1,
                (image_height / 100) * y1,
                (image_width / 100) * x2,
                (image_height / 100) * y2,
            ],
            fill=fill,
            outline="black",
        )


def draw_background(draw, image_width, image_height):
    """
    Draw the background of the image.

    Args:
        draw (ImageDraw): The ImageDraw object to draw on.
        image_width (int): The width of the image.
        image_height (int): The height of the image.
    """
    draw_rectangle(draw, [0, 0, image_height, (image_height / 100) * 80], fill="orange")

    for i in range(0, 100):
        draw.line(
            [
                (image_width / 100) * i,
                0,
                (image_width / 100) * i,
                (image_height / 100) * 80,
            ],
            fill="black",
        )


def build_image(image_height, image_width, pos=0):
    """
    Build a christmas image with a Christmas tree and a pot.

    Args:
        image_height (int): The height of the image
        image_width (int): The width of the image
        pos (int): The position of item in the gif

    Returns:
        Image: The image with the Christmas tree and pot.

    """
    background = Image.new("RGB", (image_width, image_height), (255, 255, 0))
    draw = ImageDraw.Draw(background)

    draw_background(draw, image_width, image_height)

    draw_hanging_frame(draw, image_width, image_height)

    draw_television(draw, image_width, image_height)

    draw_christmas_tree(draw, image_width, image_height)

    light_group_1 = "yellow" if pos % 2 == 0 else "white"
    light_group_2 = "white" if pos % 2 == 0 else "yellow"
    draw_baubles(draw, image_width, image_height, light_group_1, light_group_2)

    return background


def build_gif():
    """Build the images and create gif."""
    images = []
    for pos in range(1, 4):
        image = build_image(IMAGE_HEIGHT, IMAGE_WIDTH, pos)
        images.append(image)

    images[0].save(
        "merry_christmas.gif",
        save_all=True,
        append_images=images[1:],
        loop=0,
        duration=100,
    )


if __name__ == "__main__":
    build_gif()
