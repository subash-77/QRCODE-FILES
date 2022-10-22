import qrcode
from PIL import Image

img_bg = Image.open('kannansb.jpg')

qr = qrcode.QRCode(box_size=2)
qr.add_data('Boommer Uncles')
qr.make()
img_qr = qr.make_image()

pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])

img_bg.paste(img_qr, pos)
img_bg.save('kannansbout.jpg')
