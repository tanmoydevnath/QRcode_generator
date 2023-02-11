import qrcode
from PIL import Image
data = input("Enter the text or URL: ")
qr_color = input("Enter the QR color:")
bg_color = input("Enter the Background color: ")

name = input("Enter a name for your QR: ")
qr = qrcode.QRCode(version = 1,
                   error_correction= qrcode.constants.ERROR_CORRECT_H, box_size=8, border= 1)
qr.add_data(data)
qr.make(fit = True)
img=qr.make_image(fill_color=qr_color, back_color=bg_color)
img.save(name+".png")