import qrcode

def generate_qr_code(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    text = lines[0].strip()
    filename = lines[1].strip()

    image = qrcode.make(text)
    image.save(filename)

    print("QR code generated successfully!")


generate_qr_code("name.txt")