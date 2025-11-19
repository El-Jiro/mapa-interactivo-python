import folium

"""
El método Map de Folium tiene un único argumento obligatrio llamado location, este es una lista con las
coordenadas (latitud y longitud) que queremos que muestre el mapa al abrirse. Tiene varios otros parámetros
opcionales como zoom_start que controla el nivel de zoom default y va de 0 a 10, o tiles que define el tipo
y la apariencia del mapa
"""
map = folium.Map(location=[19.22, -98.80], zoom_start=5, tiles="Stamen Terrain")
map.save("map1.html")