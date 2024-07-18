import pytest
import os
import astropy
import numpy as np

from pathlib import Path
from libraries.reducer import Reducer

def test_align_frames_bad_path():
    bad_path = 'qweruiopasdfjkl;'
    with pytest.raises(FileNotFoundError):
        Reducer.align_frames(bad_path)

def test_align_frames(obj_dir):
   assert isinstance(Reducer.align_frames(obj_dir), list)
   aligned_frames = os.listdir(obj_dir / 'align')
   print(f"aligned frames dir: {aligned_frames}")
   assert len(os.listdir(obj_dir / 'align')) > 0

def test_make_dark(dark_dir, helper):
    assert isinstance(Reducer.make_dark(dark_dir), astropy.nddata.CCDData)
    helper.show_files(dark_dir)

def test_make_flat(flat_dir, dark_dir, helper):
    assert isinstance(Reducer.make_flat(flat_dir, dark_dir), astropy.nddata.CCDData)
    helper.show_files(flat_dir)

def test_make_mask(object_frame):
    mask, boxes = Reducer.make_mask(object_frame)
    assert isinstance(mask, np.ndarray)
    assert isinstance(boxes, dict)

def test_make_stack(obj_dir):
    assert isinstance(Reducer.make_stack(obj_dir), astropy.nddata.CCDData)

def test_reduce_objects(obj_dir, flat_dir, dark_dir, bkg_method='flat'):
    assert isinstance(Reducer.reduce_objects(obj_dir, flat_dir, dark_dir,  bkg_method), list)

def test_solve_plates(obj_dir):
    assert isinstance(Reducer.solve_plates(obj_dir), list)
