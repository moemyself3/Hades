import pytest
import os
import astropy

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
    pass

def test_make_stack(obj_dir):
    pass

def test_reduce_objects(obj_dir, flat_dir, dark_dir, bkg_method='flat'):
    pass

def test_solve_plates(obj_dir):
    pass
