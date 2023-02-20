# Importing library
import qrcode
import image

# Data to encode
data = input("Enter the text/URL :")

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,box_size = 40,border = 3)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'white',back_color = 'black')

i=input("Enter the image file name:")
img.save(i)

