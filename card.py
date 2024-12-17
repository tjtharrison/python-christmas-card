"""Script to build digital Christmas card."""
from PIL import Image, ImageDraw, ImageFont

IMAGE_HEIGHT = 5000
IMAGE_WIDTH = 5000

CHRISTMAS_TREE_COLOUR = (26, 222, 51)


def build_background(image_height, image_width, pos=0):
    """
    Build a background image with a Christmas tree and a pot

    Args:
        image_height (int): The height of the image
        image_width (int): The width of the image
        pos (int): The position of item in the gif

    Returns:
        Image: The image with the Christmas tree and pot.

    """
    # Use pillow to create a new image with the image_url in the middle
    background = Image.new("RGB", (image_width, image_height), (255, 255, 0))

    # Add orange wallpaper
    draw = ImageDraw.Draw(background)
    draw.rectangle([000, 000, image_height, (image_height / 100) * 80], fill="orange")

    # Every 1% horizontal, add a vertical line
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

    # Add pink wall hanging
    draw.rectangle(
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
    # Add text to wall hanging
    font = ImageFont.truetype("docs/Audiowide-Regular.ttf", 200)
    draw.text(
        ((image_width / 100) * 16, (image_height / 100) * 21),
        "%%%%%%%%%%%",
        (255, 255, 255),
        font=font,
    )
    draw.text(
        ((image_width / 100) * 16, (image_height / 100) * 26),
        "%       HOME       %",
        (255, 255, 255),
        font=font,
    )
    draw.text(
        ((image_width / 100) * 16, (image_height / 100) * 31),
        "%      SWEET      %",
        (255, 255, 255),
        font=font,
    )
    draw.text(
        ((image_width / 100) * 16, (image_height / 100) * 36),
        "%       HOME       %",
        (255, 255, 255),
        font=font,
    )
    draw.text(
        ((image_width / 100) * 16, (image_height / 100) * 40),
        "%%%%%%%%%%%",
        (255, 255, 255),
        font=font,
    )

    # Add Tele box
    draw.rectangle(
        [
            (image_width / 100) * 3,
            (image_width / 100) * 53,
            (image_height / 100) * 49,
            (image_width / 100) * 74,
        ],
        fill="black",
    )
    # Draw tele back
    draw.rectangle(
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
    # Draw tele legs
    draw.rectangle(
        [
            (image_width / 100) * 5,
            (image_height / 100) * 78,
            (image_width / 100) * 5.2,
            (image_height / 100) * 87.5,
        ],
        fill="black",
    )
    draw.rectangle(
        [
            (image_width / 100) * 49.5,
            (image_height / 100) * 78,
            (image_width / 100) * 49.7,
            (image_height / 100) * 87.5,
        ],
        fill="black",
    )

    # Add screen
    draw.rectangle(
        [
            (image_width / 100) * 7,
            (image_width / 100) * 57,
            (image_height / 100) * 38,
            (image_width / 100) * 76,
        ],
        fill=(89, 92, 208),
    )
    # Add buttons
    draw.ellipse(
        (
            (image_width / 100) * 43,
            (image_height / 100) * 63,
            (image_width / 100) * 44,
            (image_height / 100) * 64,
        ),
        fill="red",
        outline=(0, 0, 0),
    )
    draw.ellipse(
        (
            (image_width / 100) * 42,
            (image_height / 100) * 69,
            (image_width / 100) * 45,
            (image_height / 100) * 72,
        ),
        fill="black",
        outline=(0, 0, 0),
    )
    draw.ellipse(
        (
            (image_width / 100) * 42,
            (image_height / 100) * 73,
            (image_width / 100) * 45,
            (image_height / 100) * 76,
        ),
        fill="black",
        outline=(0, 0, 0),
    )

    # Add Christmas tree
    draw.polygon(
        [
            (image_width / 100) * 70,
            (image_height / 100) * 20,
            (image_width / 100) * 90,
            (image_height / 100) * 20,
            (image_width / 100) * 80,
            (image_height / 100) * 5,
        ],
        fill=CHRISTMAS_TREE_COLOUR,
    )
    draw.polygon(
        [
            (image_width / 100) * 70,
            (image_height / 100) * 35,
            (image_width / 100) * 90,
            (image_height / 100) * 35,
            (image_width / 100) * 80,
            (image_height / 100) * 15,
        ],
        fill=CHRISTMAS_TREE_COLOUR,
    )
    draw.polygon(
        [
            (image_width / 100) * 65,
            (image_height / 100) * 55,
            (image_width / 100) * 95,
            (image_height / 100) * 55,
            (image_width / 100) * 80,
            (image_height / 100) * 30,
        ],
        fill=CHRISTMAS_TREE_COLOUR,
    )
    draw.polygon(
        [
            (image_width / 100) * 60,
            (image_height / 100) * 75,
            (image_width / 100) * 98,
            (image_height / 100) * 75,
            (image_width / 100) * 80,
            (image_height / 100) * 40,
        ],
        fill=CHRISTMAS_TREE_COLOUR,
    )

    # Draw tree trunk
    draw.rectangle(
        [
            (image_width / 100) * 75,
            (image_height / 100) * 75,
            (image_width / 100) * 85,
            (image_height / 100) * 80,
        ],
        fill="brown",
    )

    # Draw red pot
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

    # Draw baubles
    if pos % 2 == 0:
        light_group_1 = "yellow"
        light_group_2 = "white"
    else:
        light_group_1 = "white"
        light_group_2 = "yellow"

    # row 1
    draw.ellipse(
        (
            (image_width / 100) * 70,
            (image_height / 100) * 20,
            (image_width / 100) * 75,
            (image_height / 100) * 25,
        ),
        fill=light_group_1,
        outline="black",
    )
    draw.ellipse(
        (
            (image_width / 100) * 85,
            (image_height / 100) * 20,
            (image_width / 100) * 90,
            (image_height / 100) * 25,
        ),
        fill=light_group_2,
        outline="black",
    )
    # row 2
    draw.ellipse(
        (
            (image_width / 100) * 70,
            (image_height / 100) * 35,
            (image_width / 100) * 75,
            (image_height / 100) * 40,
        ),
        fill=light_group_2,
        outline="black",
    )
    draw.ellipse(
        (
            (image_width / 100) * 85,
            (image_height / 100) * 35,
            (image_width / 100) * 90,
            (image_height / 100) * 40,
        ),
        fill=light_group_1,
        outline="black",
    )
    # row 3
    draw.ellipse(
        (
            (image_width / 100) * 65,
            (image_height / 100) * 55,
            (image_width / 100) * 70,
            (image_height / 100) * 60,
        ),
        fill=light_group_1,
        outline="black",
    )
    draw.ellipse(
        (
            (image_width / 100) * 90,
            (image_height / 100) * 55,
            (image_width / 100) * 95,
            (image_height / 100) * 60,
        ),
        fill=light_group_2,
        outline="black",
    )
    # row 4
    draw.ellipse(
        (
            (image_width / 100) * 60,
            (image_height / 100) * 75,
            (image_width / 100) * 65,
            (image_height / 100) * 80,
        ),
        fill=light_group_2,
        outline="black",
    )
    draw.ellipse(
        (
            (image_width / 100) * 95,
            (image_height / 100) * 75,
            (image_width / 100) * 100,
            (image_height / 100) * 80,
        ),
        fill=light_group_1,
        outline="black",
    )

    return background


def build_image():
    """
    Build the image.
    """

    images = []
    for pos in range(1, 4):
        image = build_background(IMAGE_HEIGHT, IMAGE_WIDTH, pos)
        images.append(image)

    images[0].save(
        "background.gif", save_all=True, append_images=images[1:], loop=0, duration=100
    )


if __name__ == "__main__":
    build_image()
