import mapnik

m = mapnik.Map(2000,1000)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
r.symbols.append(polygon_symbolizer)

s.rules.append(r)
m.append_style('Yogi',s)
ds = mapnik.Shapefile(file="INDONESIA_PROP.shp")
layer = mapnik.Layer('indonesia')
layer.datasource = ds
layer.styles.append('Yogi')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[nama]'), 'DejaVu Sans Bold',3,mapnik.Color('red'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
point_sym.opacity = 0.5
point_sym.file = ()
r.symbols.append(point_sym)

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
r.symbols.append(line_symbolizer)
point = mapnik.PointSymbolizer()
r.symbols.append(point)
s.rules.append(r)

m.append_style('Yogi',s)
POSTGIS_TABLE = dict(
	host='localhost',
	port=5433,
	user='postgres',
	password="zoggi",
	dbname='kelasgis',

	table='(select ST_Buffer(ST_Centroid(geom),1) as geom, point from praktek) as praktek',
)
ds = mapnik.PostGIS(**POSTGIS_TABLE)
layer = mapnik.Layer('indonesia')
layer.datasource = ds 
layer.styles.append('Yogi')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m,'indonesia.pdf','pdf')
print "rendered image to 'indonesia.pdf"