from config import Configuration

import glob
import logging
import os
import shutil

class Utils:

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

		# create the logger
		logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', filename=Configuration.LOG_DIRECTORY + 'main.log', filemode='a')
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