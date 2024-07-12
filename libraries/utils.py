from config import Configuration

import glob
import logging
import os
import shutil

class Utils:

	@staticmethod
	def config_camera(name='PL16803'):
		''' This function returns a dictionary of parameters related to a given camera.

		:parameter name [string] - The name of the camera

		:return params [dictionary] - The parameters of the camera

			dx [float] - The number of pixels along the camera's x-axis
			dy [float] - The number of pixels along the camera's y-axis
			gain [float] - The gain of the camera [ADU/e]
			inverse_gain [float] - The inverse gain of the camera [e/ADU]
			pixel_size [float] - The angular size of the pixel projected into the sky [arcsec/px]
			read_noise [float] - The readout noise of the camera [ADU]

		'''

		params = {}

		if name == 'PL16803':
			dx = 4096
			dy = 4096
			gain = 0.72
			inverse_gain = 1.39
			pixel_size = 0.6305
			read_noise = 11.4			

		elif name == 'ST8300':
			dx = 3352
			dy = 2532
			gain = 2.48
			inverse_gain = 0.403
			pixel_size = None
			read_noise = 28.5

		elif name == 'TOROS':
			dx = 10560
			dy = 10560
			gain = None
			inverse_gain = None
			pixel_size = 0.468
			read_noise = None

		else:
			dx = 4096
			dy = 4096
			gain = 0.72
			inverse_gain = 1.39
			pixel_size = 0.6305
			read_noise = 11.4

		params['dx'] = dx
		params['dy'] = dy
		params['gain'] = gain
		params['inverse_gain'] = inverse_gain
		params['pixel_size'] = pixel_size
		params['read_noise'] = read_noise

		return params

	@staticmethod
	def config_observatory(name='CTMO'):
		''' This function returns a dictionary of parameters related to a given camera.

		:parameter name [string] - The name of the observatory

		:return params [dictionary] - The parameters of the observatory

			declination_limit [float] - The limiting declination in the sky accessable to the observatory [deg]
			elevation [int] - The elevation of the observatory above sea level [m]
			latitude [float] - The latitude of the observatory
			longitude [float] - The longitude of the observatory

		'''

		params = {}

		if name == 'CTMO':
			declination_limit = -40.00
			elevation = 11.5
			latitude = 25.995789
			longitude = -97.568956

		elif name == 'Macon':
			declination_limit = 33.84
			elevation = 4650
			latitude = -24.62055556
			longitude = -67.32833333

		elif name == 'OAFA':
			declination_limit = None
			elevation = 2420
			latitude = -31.8023
			longitude = -69.3265

		else:
			declination_limit = -40.00
			elevation = 11.5
			latitude = 25.995789
			longitude = -97.568956

		params['declination_limit'] = declination_limit
		params['elevation'] = elevation
		params['latitude'] = latitude
		params['longitude'] = longitude

		return params

	@staticmethod
	def create_directories(main_dir):

		raw_dir = os.path.join(main_dir, 'raw')
		if not os.path.exists(raw_dir):
			os.mkdir(raw_dir)

		cal_dir = os.path.join(main_dir, 'cal')
		if not os.path.exists(cal_dir):
			os.mkdir(cal_dir)

		wcs_dir = os.path.join(main_dir, 'wcs')
		if not os.path.exists(wcs_dir):
			os.mkdir(wcs_dir)

		align_dir = os.path.join(main_dir, 'align')
		if not os.path.exists(align_dir):
			os.mkdir(align_dir)

		os.chdir(main_dir)

		for item in glob.glob('*.fit'):

			old_item_path = os.path.join(main_dir, item)
			new_item_path = os.path.join(raw_dir, item)

			shutil.move(old_item_path, new_item_path)

		return raw_dir, cal_dir, wcs_dir, align_dir

	@staticmethod
	def log(statement, level):

		log_path = Configuration.MAIN_DIR + 'logs/main.log'

		# create the logger
		logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', filename=log_path, filemode='a')
		logger = logging.getLogger()

		if not getattr(logger, 'handler_set', None):
			logger.setLevel(logging.DEBUG)

			# create console handler and set level to debug
			ch = logging.StreamHandler()
			ch.setLevel(logging.DEBUG)

			# create the formatter
			formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

			# add formatter to ch
			ch.setFormatter(formatter)

			# add ch to logger
			logger.addHandler(ch)

			# 'set' Handler
			logger.handler_set = True

		if level == 'info':
			logger.info(statement)

		if level == 'debug':
			logger.debug(statement)

		if level == 'warning':
			logger.warning(statement)

		if level == 'error':
			logger.error(statement)

		if level == 'critical':
			logger.error(statement)

	@staticmethod
	def setup_hades(main_dir):

		# alerts
		alerts_dir = os.path.join(main_dir, 'alerts/')
		if not os.path.exists(alerts_dir):
			os.mkdir(alerts_dir)

		# alerts > gw
		alerts_gw_dir = os.path.join(alerts_dir, 'gw/')
		if not os.path.exists(alerts_gw_dir):
			os.mkdir(alerts_gw_dir)

		# alerts > gw > json
		alerts_gw_json_dir = os.path.join(alerts_gw_dir, 'json/')
		if not os.path.exists(alerts_gw_json_dir):
			os.mkdir(alerts_gw_json_dir)

		# alerts > gw > moc
		alerts_gw_moc_dir = os.path.join(alerts_gw_dir, 'moc/')
		if not os.path.exists(alerts_gw_moc_dir):
			os.mkdir(alerts_gw_moc_dir)

		# alerts > gw > skymap
		alerts_gw_skymap_dir = os.path.join(alerts_gw_dir, 'skymap/')
		if not os.path.exists(alerts_gw_skymap_dir):
			os.mkdir(alerts_gw_skymap_dir)

		# analysis
		analysis_dir = os.path.join(main_dir, 'analysis/')
		if not os.path.exists(analysis_dir):
			os.mkdir(analysis_dir)

		# analysis > survey
		analysis_survey_dir = os.path.join(analysis_dir, 'survey/')
		if not os.path.exists(analysis_survey_dir):
			os.mkdir(analysis_survey_dir)

		# analysis > gw
		analysis_gw_dir = os.path.join(analysis_dir, 'gw/')
		if not os.path.exists(analysis_gw_dir):
			os.mkdir(analysis_gw_dir)

		# analysis > gw > fields
		analysis_gw_fields_dir = os.path.join(analysis_gw_dir, 'fields/')
		if not os.path.exists(analysis_gw_fields_dir):
			os.mkdir(analysis_gw_fields_dir)

		# analysis > gw > galaxies
		analysis_gw_galaxies_dir = os.path.join(analysis_gw_dir, 'galaxies/')
		if not os.path.exists(analysis_gw_galaxies_dir):
			os.mkdir(analysis_gw_galaxies_dir)

		# logs
		log_dir = os.path.join(main_dir, 'logs/')
		if not os.path.exists(log_dir):
			os.mkdir(log_dir)