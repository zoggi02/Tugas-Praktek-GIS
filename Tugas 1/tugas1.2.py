import mapnik
m = mapnik.Map(600,300)
m.background = mapnik.Color('blue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#09f704')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Yogi',s)
ds = mapnik.Shapefile(file="sungaiindonesia/IND_SNG_polyline.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yogi')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'2.jpeg','jpeg')
print "rendered image to '2.jpeg'"