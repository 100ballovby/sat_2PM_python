from example_9 import load_image, crop_image, get_img_thumbnail

image = load_image('~/.../.../assets/logo.png')
image = crop_image(image, 400, 500)
thumb = get_img_thumbnail(image)

# если бы у меня был класс Image:
from example_9 import Image

image = Image('~/.../.../assets/logo.png')
image.crop(400, 500)
thumb = image.thumbnail()
