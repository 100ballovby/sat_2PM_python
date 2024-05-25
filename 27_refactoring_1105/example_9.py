def load_image(path):
	with open(path, 'rb') as file:
		fb = file.load()
	img = image_lib.parse(fb)
	return img


def crop_image(img, width, height):
	...
	return img


def get_img_thumbnail(img, resolution=100):
	...
	return img



