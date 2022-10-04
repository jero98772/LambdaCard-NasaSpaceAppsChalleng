import folium

m = folium.Map(location=[6.256405968932449, -75.59835591123756])


folium.Marker(
    [6.176375,-75.5600386], popup="<i>Node 0</i>", tooltip="Node 0"
).add_to(m)
m.save("index.html")
