import pyqrcode
import png
from pyqrcode import QRCode

QRString = "https://youtu.be/R-bI0AhSyU0"

url = pyqrcode.create(QRString)

url.png(r'qr.png', scale=8)