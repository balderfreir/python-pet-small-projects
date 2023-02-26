import speedtest

st = speedtest.Speedtest()
option = int(input('Чего желаем знать?   \n'
                   '1 - Скорость скачивания \n'
                   '2 - Скорость загрузки   \n'
                   'Ответ: '))
if option == 1:
    print(st.download() / 1024 / 1024)
elif option == 2:
    print(st.upload() / 1024 / 1024)
else:
    print("Введите 1 или 2")
