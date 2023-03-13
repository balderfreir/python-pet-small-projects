import numpy as np

# Радиус земли в км
r = 6371
# Конвертация из градусов в радианы
def deg_to_rad(degrees):
    return degrees * (np.pi / 180)

# непосредственно считаем расстояние между двумя точками
def dist_calculate(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat2 - lat1)
    d_lon = deg_to_rad(lon2 - lon1)
    a = np.sin(d_lat / 2) ** 2 + np.cos(deg_to_rad(lat1)) * \
        np.cos(deg_to_rad(lat2)) * np.sin(d_lon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return r * c


Red_sqr = 55.7539, 37.6208
Ermitazh = 59.9398, 30.3146
Tbilisy = 41.6941, 44.8337
Tokio = 35.6895, 139.692
print(dist_calculate(*Red_sqr, *Ermitazh))
print(dist_calculate(*Red_sqr, *Tbilisy))
print(dist_calculate(*Red_sqr, *Tokio))
