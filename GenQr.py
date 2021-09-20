import qrcode

def input_URL():

    input_URL = input("Please enter website address(URL):")

qr = qrcode.QRCode(

    version=1,

    error_correction=qrcode.constants.ERROR_CORRECT_L,

    box_size=15,

    border=4,

)

qr.add_data(input_URL)

qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save("url_qrcode.png")

print(qr.data_list)
