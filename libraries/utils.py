'''
Utils class

'''

from config import Configuration

import glob
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