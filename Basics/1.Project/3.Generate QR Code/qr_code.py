import qrcode as qr

# Create a normal QR code

img = qr.make('https://github.com/Parag-deb')
img.save('normal_qr.png')

