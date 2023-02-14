import cv2
# читаем наше изображение
image = cv2.imread("vk_qr.png")
# инициализируем cv2 QRCode detector
detector = cv2.QRCodeDetector()
# определяем qr и декодируем его
data, p_array, b_qrcode = detector.detectAndDecode(image)
# if there is a QR code print the data
if p_array is not None:
    print("Закодировано:", data)
else:
    print("Кажется тут нету QR")
