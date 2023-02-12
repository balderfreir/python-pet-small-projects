import pyqrcode
import png
link = "https://vk.com/ds_python"
qr_code = pyqrcode.create(link)
qr_code.png("vk_qr.png", scale=5)
