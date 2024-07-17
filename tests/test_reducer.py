import pytest
import os

from pathlib import Path

from libraries.reducer import Reducer

def test_align_frames_bad_path():
    obj_dir = 'qweruiopasdfjkl;'
    with pytest.raises(FileNotFoundError):
        Reducer.align_frames(obj_dir)

def test_align_frames(fit_files):
   assert isinstance(Reducer.align_frames(fit_files), list)
   aligned_frames = os.listdir(fit_files / 'align')
   print(f"aligned frames dir: {aligned_frames}")
   assert len(os.listdir(fit_files / 'align')) > 0
