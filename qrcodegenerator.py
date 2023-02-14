import pyqrcode
# Ссылка для кодировани
link = "https://vk.com/ds_python"
# Получаем код из 0 и 1
qr_code = pyqrcode.create(link)
# Преобразуем в png
qr_code.png("vk_qr.png", scale=5)
