from config import Configuration
from libraries.utils import Utils

from astropy import units as u
from astropy.coordinates import get_sun, SkyCoord
from astropy.time import Time
from ligo.skymap.postprocess import crossmatch
import numpy as np
import os
import pandas as pd

#from astroplan import Observer
#from astropy.coordinates import AltAz, EarthLocation, HADec
#import astropy_healpix as ah

import logging
logging.getLogger('healpy').setLevel(logging.WARNING)

class Priority:

	@staticmethod
	def field_generator(field_size):

		if os.path.isfile(Configuration.ANALYSIS_DIRECTORY + 'survey_fields.dat') is False or Configuration.FIELD_GENERATION == 'Y':
			Utils.log('Now generating survey fields.', 'info')

			# set up the field data frames and start with the first field
			c = SkyCoord(ra=0.e0, dec=90e0, frame='icrs', unit='deg')
			field_list = pd.DataFrame(data=[['00.000', 90e0, 0e0, c.galactic.l.to_value(), c.galactic.b.to_value(), 'main_survey', 300., 1, 0, 0]], columns=['field_id', 'ra', 'dec', 'l', 'b', 'program', 'exposure_time', 'cadence', 'ephemeris', 'period'])

			# set up the survey field of view
			fov = Configuration.PIXEL_SIZE * Configuration.NUM_PIXELS / 3600.
			field_number = int(np.ceil((90 + Configuration.DEC_LIMIT) / field_size))

			# set up variables necessary for geometry
			deg_to_rad = np.pi / 180.
			field_sep = fov * np.sqrt(2.2 ** 2 + 3.73 ** 2) / 5.0

			# separation of the fields in declination
			declination_strips = 90 - np.arange(0, field_number) * field_sep

			# now loop through and generate the fields
			eo = 0
			for idx in range(1, field_number):
				nfr = np.ceil(360. * np.cos(declination_strips[idx] * deg_to_rad) / field_size)
				ra_sep = 360. / nfr

				if eo == 1:
					ra_off = 0.5 * ra_sep
					eo = 0
				else:
					ra_off = 0.
					eo = 1

				for idy in range(0, int(nfr)):
					# set up the field name with the first hex field
					if len(hex(idx).split('x')[1]) == 1:
						field_1 = '0' + hex(idx).split('x')[1]
					else:
						field_1 = hex(idx).split('x')[1]

					# set up the second hex field
					if len(hex(idy).split('x')[1]) == 1:
						field_2 = '00' + hex(idy).split('x')[1]
					elif len(hex(idy).split('x')[1]) == 2:
						field_2 = '0' + hex(idy).split('x')[1]
					else:
						field_2 = hex(idy).split('x')[1]

					# get the galactic coordinates of the field
					c_idy = SkyCoord(ra=idy * ra_sep + ra_off, dec=declination_strips[idx], frame='icrs', unit='deg')
					if (c_idy.galactic.b.to_value() < 15) or (c_idy.galactic.b.to_value() > -15):
						moon_phase = 1
					else:
						moon_phase = 0

					# set up the series for appending
					field = pd.Series(data=[field_1 + '.' + field_2, idy * ra_sep + ra_off, declination_strips[idx], c_idy.galactic.l.to_value(), c_idy.galactic.b.to_value(), 'main_survey', 300., 1, 0, 0, 0, moon_phase], index=['field_id', 'ra', 'dec', 'l', 'b', 'program', 'exposure_time', 'cadence', 'ephemeris', 'period', 'observations', 'moon_phase'])

					# append the series
					try:
						field_list = field_list._append(field, ignore_index=True)
					except AttributeError:
						field_list = pd.concat([field_list, field.to_frame(1).T], ignore_index=True)

			field_list.to_csv(Configuration.ANALYSIS_DIRECTORY + 'survey_fields.dat', sep=' ', header=True, index=False, float_format='%.3f')

		else:
			# if the file exists already, then just read the field list in
			field_list = pd.read_csv(Configuration.ANALYSIS_DIRECTORY + 'survey_fields.dat', header=0, sep=' ')

		return field_list

	@staticmethod
	def generate_targets(detection_time=None):

		catalog = Configuration.ANALYSIS_DIRECTORY + 'GLADE+.txt'
		delimiter = ' '
		usecols = [2, 8, 9, 32]
		header = None
		names = ['GWGC', 'ra', 'dec', 'dist']
		low_memory = False

		Utils.log('Reading GLADE catalog.', 'info')
		df = pd.read_csv(catalog,
								delimiter=delimiter,
								usecols=usecols,
								header=header,
								names=names,
								low_memory=low_memory)

		Utils.log('Slicing GLADE catalog.', 'info')
		# drop NaNs from catalog
		df = df.dropna()

		# slice catalog by declination
		lim_dec = df.dec > (-90 + Configuration.LATITUDE)
		new_df = df[lim_dec]

		# slice catalog by right ascension
		right_now = detection_time or Time.now()
		right_now = Time(right_now)

		sun = get_sun(right_now)

		horizon = -15 * u.degree
		min_height = 30 * u.degree

		alpha_obs_min = (sun.ra - horizon + min_height).degree
		alpha_obs_max = (sun.ra + horizon - min_height).degree

		circum = 90.0 - abs(new_df.dec) < abs(Configuration.LATITUDE)
		alfa_min = new_df.ra > float(alpha_obs_min)
		alfa_max = new_df.ra <= float(alpha_obs_max)

		case_1 = (alfa_min & alfa_max) | circum
		case_2 = (alfa_min | alfa_max) | circum

		if alpha_obs_max > alpha_obs_min:
			final_df = new_df[case_1]
		else:
			final_df = new_df[case_2]

		return final_df

	@staticmethod
	def sort_field_skymap(survey_fields, skymap, event_name):

		# copy the data frame so we don't ruin the original data
		selected_fields = survey_fields.copy().reset_index(drop=True)

		# get the coordinate values for each survey field in the appropriate units
		field_coords = SkyCoord(selected_fields.ra, selected_fields.dec, unit=u.deg)

		# now crossmatch the survey fields with the sky map probabilities
		cross_match = crossmatch(skymap, field_coords)

		# now move through each survey field and get the integrated area within the field area
		selected_fields['prob'] = cross_match.probdensity

		# sort all survey fields based on the probability strip
		selected_fields = selected_fields.sort_values(by='prob', ascending=False).copy().reset_index(drop=True)
		selected_fields['program'] = 'lvc_alert_' + event_name

		return selected_fields

	@staticmethod
	def sort_galaxy_skymap(catalog, skymap, event_name):

		selected_galaxies = catalog.copy().reset_index(drop=True)

		galaxy_coords = SkyCoord(selected_galaxies.ra, selected_galaxies.dec, unit=u.deg)

		cross_match = crossmatch(skymap, galaxy_coords)

		selected_galaxies['prob'] = cross_match.probdensity

		selected_galaxies = selected_galaxies.sort_values(by='prob', ascending=False).copy().reset_index(drop=True)

		n = 50
		final_galaxies = selected_galaxies.head(n)

		return final_galaxies