import mapnik
m = mapnik.Map(600,300)
m.background = mapnik.Color('steelblue')
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
ds = mapnik.Shapefile(file="provinsiindonesia/INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yogi')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'1.png','png')
print "rendered image to '1.png'"