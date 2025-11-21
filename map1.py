import folium

"""
El método Map de Folium tiene un único argumento obligatrio llamado location, este es una lista con las
coordenadas (latitud y longitud) que queremos que muestre el mapa al abrirse. Tiene varios otros parámetros
opcionales como zoom_start que controla el nivel de zoom default y va de 0 a 10, o tiles que define el tipo
y la apariencia del mapa
"""
map = folium.Map(location=[19.22, -98.80], zoom_start=5, tiles="https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
attr="OpenTopoMap (CC-BY-SA)")

"""
Es buena práctica crear un objeto FeatureGroup para tener agrupados y accesibles íconos, polígonos y otros
elementos en un mismo lugar, además esto será de ayuda cuando queramos añadir una capa de control al mapa.
"""
fg = folium.FeatureGroup("MyMap")

"""
Para crear un marcador llamamos al método add_child del objeto fg y le pasamos un objeto folium.Marker, que recibe
tres argumentos en su constructor: una coordenada en forma de lista o tupla, un popup, es decir un pequeño texto que 
se mostrará al hacer clic en el marcador y un objeto folium.Icon, en cuyo constructor podemos especificar de manera 
opcional un nombre de color, si no especificamos ninguno será azul por defecto
"""
my_marker = folium.Marker(location=[38.2, -99.1], popup="¡Hola, soy un marcador!", icon=folium.Icon(color="green"))
fg.add_child(my_marker)

#Ahora añadimos el featureGroup al mapa
map.add_child(fg)
map.save("map1.html")