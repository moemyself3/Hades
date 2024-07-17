import pytest
import os
from pathlib import Path

import numpy as np
from astropy.nddata import CCDData
from astropy.io import fits
import ccdproc

@pytest.fixture(scope="session")
def fit_files(tmp_path_factory):
    # Make directories for fit files
    #  needs data, wcs, and align
    fit_files_path = tmp_path_factory.mktemp("data")
    wcs_path = fit_files_path / "wcs"
    wcs_path.mkdir()
    align_path = fit_files_path / "align"
    align_path.mkdir()
    
    # Make fit file data
    hdu = example_hdu()
    print(f"Making file path: {fit_files_path}")
    _ = [hdu.writeto(fit_files_path / f"ccd-{i}.fit") for i in range(3)]

    _ = [hdu.writeto(wcs_path / f"wcs-{i}.fit") for i in range(3)]

    print(f"Scanning Directory: {fit_files_path}")
    with os.scandir(fit_files_path) as iterable_items:
        print("Name\tType")
        for entry in iterable_items:
            if entry.is_dir():
                entry_type = "dir"
            elif entry.is_file():
                entry_type = "file"
            else:
                entry_type = None
            print(f"{entry.name}\t{entry_type}")
    
    return fit_files_path

def example_ccd_data():
    return CCDData(np.random.rand(2,2), unit="adu")

def example_header_with_wcs():
    path = Path(os.getcwd())
    path = path / 'tests'/ 'example_header.txt'
    with open(path, 'r') as file:
        data = file.read()
    header = fits.Header()
    header = header.fromstring(data)
    return header

def example_hdu():
    hdu = fits.PrimaryHDU(example_ccd_data(), example_header_with_wcs())
    return hdu
