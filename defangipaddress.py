def defang_ip_address(ip):
    # чеб будем клеит строку?
    sep = '[.]'
    # разбиваем входящий апи по точке
    split_ip = ip.split('.')
    # возвращаем модифицированную строку
    return sep.join(split_ip)

print(defang_ip_address('255.255.255.0'))