class Configuration:

	MACHINE = 'epimetheus'

	WORKING_DIR = '/home/epimetheus/Downloads/2024-06-16/grb240615a/align/'
	OBJECT = 'grb240615a'
	FIELD_RA = 326.1413
	FIELD_DEC = 38.5948

	CAMERA = 'PL16803'				# The name of the camera that took the image data
	LATITUDE = 25.995789			# The latitude of the observatory
	LONGITUDE = -97.568956			# The longitude of the observatory
	HEIGHT = 11.5					# The elevation of the observatory above sea level [m]

	BKG_METHOD = 'flat'
	BOX_SIZE = (50, 50)
	COMBINE_METHOD = 'median'
	DILATE_SIZE = 25
	DTYPE = 'float32'
	FILTER_SIZE = (3, 3)
	MEM_LIMIT = 32e9
	NPIXELS = 3
	SIGMA_BKG = 3.0
	SIGMA_SRC = 5.0
	
	#AIRMASS_METHOD = 'ky1998'
	CATALOG = 'gaia-cone'			# The query catalog [gaia-cone, gaia-square]
	#CATALOG_F1 = 'r'
	#CATALOG_F2 = 'i'
	#PHOT_F1 = 'r'
	#PHOT_F2 = 'i'
	RAD_AN_IN = 17					# The annulus inner radius for photometry [px]
	RAD_AN_OUT = 20					# The annulus outer radius for photometry [px]
	RAD_AP = 14						# The aperture radius for photometry [px]
	RAD_SOLVE = 1					# The constraining radius for plate solving [deg]
	RAD_QUERY = 1					# The search radius for querying catalogs [deg]