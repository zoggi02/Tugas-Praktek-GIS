import mapnik
m = mapnik.Map(2000,1700)
m.background = mapnik.Color('steelblue')

#map1
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#fdf704')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Yogi',s)
ds = mapnik.Shapefile(file="countries/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yogi')
m.layers.append(layer)
#map1

#map2
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#ff0000')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Yogi2',s)
ds = mapnik.Shapefile(file="petaindonesia/map.shp")
layer = mapnik.Layer('Indonesia')
layer.datasource = ds
layer.styles.append('Yogi2')
m.layers.append(layer)
#map2

# map3
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#808000')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Turquoise'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Yogi3',s)
ds = mapnik.Shapefile(file="petainggris/map.shp")
layer = mapnik.Layer('Inggris')
layer.datasource = ds
layer.styles.append('Yogi3')
m.layers.append(layer)
#map3

# map4
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#008B8B')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Magenta'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Yogi4',s)
ds = mapnik.Shapefile(file="petasomalia/map.shp")
layer = mapnik.Layer('Somalia')
layer.datasource = ds
layer.styles.append('Yogi4')
m.layers.append(layer)
#map4

# map5
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#4B0082')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Lime'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Yogi5',s)
ds = mapnik.Shapefile(file="petausa/map.shp")
layer = mapnik.Layer('USA')
layer.datasource = ds
layer.styles.append('Yogi5')
m.layers.append(layer)
#map5

m.zoom_all()
mapnik.render_to_file(m,'tugas2.jpeg','jpeg')
print "rendered image to 'tugas2.jpeg'"