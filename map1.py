import folium
import pandas as pd

#Creamos un dataframe de pandas
data = pd.read_csv("datasources/volcanoes.csv")
#print(data)

#obtenemos los datos de las columnas LAT y LON y las guardamos en listas nativas de python
latitude: list[float] = list(data["LAT"])
#print( f"\n{latitude}")

longitude: list[float] = list(data["LON"])
#print(f"\n{longitude}")

#Repetimos el procedimiento con la columna ELEV
elevation: list[float] = list(data["ELEV"])
#print(f"\n{longitude}")

#Y una vez más con el nombre:
name: list[float] = list(data["NAME"])
#print(f"\n{name}")

#Creamos una función que reciba la altitud del volcán como parámetro y devuelva un color dependiendo del rango de esta
def color_generator(elevation: float) -> str:
    
    color = ""

    if elevation < 1500:
        color = "green"
    elif (elevation>= 1500 and elevation < 3000):
        color = "orange"
    else: 
        color = "red"
    return color

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
elementos en un mismo lugar, además será de ayuda cuando queramos añadir una capa de control al mapa.
"""
fg = folium.FeatureGroup("MyMap")

#Podemos usar código HTML para estilizar mejor el texto de los popups: esto nos mostrará el nombre, la altura 
# y un link para buscar el volcán en google 
html = """
<ul>
    <li>
        <b>Volcano name:</b>
        <br><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
    </li>
    <li>
        <b>Height</b>: %s m
    </li>
</ul>
"""

"""
Para crear un marcador llamamos al método add_child del objeto fg y le pasamos un objeto folium.Marker, que recibe
tres argumentos en su constructor: una coordenada en forma de lista o tupla, un popup, es decir un pequeño texto que 
se mostrará al hacer clic en el marcador y un objeto folium.Icon, en cuyo constructor podemos especificar de manera 
opcional un nombre de color, si no especificamos ninguno será azul por defecto
"""
#my_marker = folium.Marker(location=[38.2, -99.1], popup="¡Hola, soy un marcador!", icon=folium.Icon(color="green"))
#fg.add_child(my_marker)

"""
Para iterar sobre dos o más listas al mismo tiempo, deberemos crear el número correspondiente de variables iteradoras 
y utilizar la función zip, pasándole todas las listas como argumento, de la siguiente forma:
"""
for lt, ln, el, n in zip(latitude, longitude, elevation, name):
    #Creamos un objeto iframe y le pasamos nuestro html en el constructor: 
    iframe = folium.IFrame(html=html % (n, n, el), width=200, height=100)
    #En el atributo location, creamos una lista con los dos iteradores
    #En el parámetro popup creamos un objeto homónimo, al cual le pasaremos nuestro iframe en el constructor
    print(color_generator(el))
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_generator(el))))


#Ahora añadimos el featureGroup al mapa
map.add_child(fg)
map.add_children
map.save("map1.html")