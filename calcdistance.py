import numpy as np

# Радиус земли в км
r = 6371
# Конвертация из градусов в радианы
def deg_to_rad(degrees):
    return degrees * (np.pi/180)
# непосредственно считаем расстояние между двумя точками
def dist_calculate(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat2-lat1)
    d_lon = deg_to_rad(lon2-lon1)
    a = np.sin(d_lat/2)**2 + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(d_lon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return r * c

lat1 = 55.7539
lon1 = 37.6208
lat2 = 59.9398
lon2 = 30.3146
print(dist_calculate(lat1, lon1, lat2, lon2))