class Configuration:

	MACHINE = 'epimetheus'

	MAIN_DIRECTORY = '/home/epimetheus/Downloads/hades/'
	ALERTS_DIRECTORY = MAIN_DIRECTORY + 'alerts/'
	ANALYSIS_DIRECTORY = MAIN_DIRECTORY + 'analysis/'
	LOG_DIRECTORY = MAIN_DIRECTORY + 'logs/'
	QUERIES_DIRECTORY = MAIN_DIRECTORY + 'queries/'

	CLIENT_ID = 'client_id'
	CLIENT_SECRET = 'client_secret'

	AVAILABLE_TOPICS = ['igwn.gwalert',
						'gcn.notices.icecube.lvk_nu_track_search',
						'gcn.notices.swift.bat.guano',
						'gcn.classic.text.FERMI_GBM_ALERT',
						'gcn.classic.text.FERMI_GBM_FIN_POS',
						'gcn.classic.text.FERMI_GBM_FLT_POS',
						'gcn.classic.text.FERMI_GBM_GND_POS',
						'gcn.classic.text.FERMI_GBM_POS_TEST',
						'gcn.classic.text.FERMI_GBM_SUBTHRESH',
						'gcn.classic.text.FERMI_LAT_MONITOR',
						'gcn.classic.text.FERMI_LAT_OFFLINE',
						'gcn.classic.text.FERMI_LAT_POS_TEST',
						'gcn.classic.text.FERMI_POINTDIR',
						'gcn.classic.text.ICECUBE_ASTROTRACK_BRONZE',
						'gcn.classic.text.ICECUBE_ASTROTRACK_GOLD',
						'gcn.classic.text.ICECUBE_CASCADE',
						'gcn.classic.text.SWIFT_ACTUAL_POINTDIR',
						'gcn.classic.text.SWIFT_BAT_GRB_LC',
						'gcn.classic.text.SWIFT_BAT_GRB_POS_ACK',
						'gcn.classic.text.SWIFT_BAT_GRB_POS_TEST',
						'gcn.classic.text.SWIFT_BAT_QL_POS',
						'gcn.classic.text.SWIFT_BAT_SCALEDMAP',
						'gcn.classic.text.SWIFT_BAT_TRANS',
						'gcn.classic.text.SWIFT_FOM_OBS',
						'gcn.classic.text.SWIFT_POINTDIR',
						'gcn.classic.text.SWIFT_SC_SLEW',
						'gcn.classic.text.SWIFT_TOO_FOM',
						'gcn.classic.text.SWIFT_TOO_SC_SLEW',
						'gcn.classic.text.SWIFT_UVOT_DBURST',
						'gcn.classic.text.SWIFT_UVOT_DBURST_PROC',
						'gcn.classic.text.SWIFT_UVOT_EMERGENCY',
						'gcn.classic.text.SWIFT_UVOT_FCHART',
						'gcn.classic.text.SWIFT_UVOT_FCHART_PROC',
						'gcn.classic.text.SWIFT_UVOT_POS',
						'gcn.classic.text.SWIFT_UVOT_POS_NACK',
						'gcn.classic.text.SWIFT_XRT_CENTROID',
						'gcn.classic.text.SWIFT_XRT_IMAGE',
						'gcn.classic.text.SWIFT_XRT_IMAGE_PROC',
						'gcn.classic.text.SWIFT_XRT_LC',
						'gcn.classic.text.SWIFT_XRT_POSITION',
						'gcn.classic.text.SWIFT_XRT_SPECTRUM',
						'gcn.classic.text.SWIFT_XRT_SPECTRUM_PROC',
						'gcn.classic.text.SWIFT_XRT_SPER',
						'gcn.classic.text.SWIFT_XRT_SPER_PROC',
						'gcn.classic.text.SWIFT_XRT_THRESHPIX',
						'gcn.classic.text.SWIFT_XRT_THRESHPIX_PROC']

	WORKING_DIR = '/home/epimetheus/Downloads/2024-06-16/grb240615a/align/'
	OBJECT = 'grb240615a'
	FIELD_RA = 326.1413
	FIELD_DEC = 38.5948

	LATITUDE = 25.995789			# The latitude of the observatory
	LONGITUDE = -97.568956			# The longitude of the observatory
	ELEVATION = 11.5				# The elevation of the observatory above sea level [m]

	CAMERA = 'PL16803'				# The name of the camera that took the image data
	PIXEL_SIZE = 0.6305				# The plate scale of the optical system [arcsec/px]
	DEC_LIMIT = -40.00				# The declination limit of the telescope [deg]

	AIRMASS_METHOD = 'ky1998'
	BKG_METHOD = 'flat'
	BOX_SIZE = (50, 50)
	CATALOG = 'gaia-cone'			# The query catalog [gaia-cone, gaia-square]
	CATALOG_F1 = 'r'
	CATALOG_F2 = 'i'
	COMBINE_METHOD = 'median'
	DILATE_SIZE = 25
	DTYPE = 'float32'
	FILTER_SIZE = (3, 3)
	MEM_LIMIT = 32e9
	NPIXELS = 3
	PHOT_F1 = 'r'
	PHOT_F2 = 'i'
	RAD_AN_IN = 17					# The annulus inner radius for photometry [px]
	RAD_AN_OUT = 20					# The annulus outer radius for photometry [px]
	RAD_AP = 14						# The aperture radius for photometry [px]
	RAD_SOLVE = 1					# The constraining radius for plate solving [deg]
	RAD_QUERY = 1					# The search radius for querying catalogs [deg]
	SIGMA_BKG = 3.0
	SIGMA_SRC = 5.0