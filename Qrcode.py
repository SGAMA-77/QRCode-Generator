import qrcode

linkedIn_profile = "https://www.linkedin.com/in/phophi-sigama-7ba192236"

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

qr.add_data(linkedIn_profile)
qr.make()

qr_img = qr.make_image(fill_color = 'black', back_color = 'white')

qr_img.save('linkedIn Profile.png')