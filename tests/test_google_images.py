#test__init__.py
import os

import pytest
import src.google_images 
from src.google_images import get_driver
from src.google_images import create_folder
from src.google_images import init_search
from src.google_images import download_all_current_page_images
import shutil

Test_folder_name='Test_folder'
var_drive_test=get_driver()

def setup_module(module):
    try:
        shutil.rmtree(Test_folder_name)
    except:
        pass
    
    print('************* SETUP *****************')


@pytest.fixture()
def drive_test():
    return var_drive_test
#    return get_driver()


@pytest.mark.parametrize('folder_name, expected_output', [ (Test_folder_name, True)] )
def test_init_search(folder_name,expected_output):
    assert create_folder(folder_name)
    assert os.path.exists(folder_name)==expected_output

def test_get_driver(drive_test):
    assert drive_test != None

def test_init_search(drive_test):
    search_text='cat'
    image_size=src.google_images.dict_Image_Size['Icon']
    assert init_search(drive_test,search_text,image_size)
   

def test_download_all_current_page_images(drive_test):
    maxcount=10
    assert download_all_current_page_images(drive_test,maxcount,Test_folder_name,maxerrorcount=2) > 0

def teardown_module(module):
    var_drive_test.close()
    try:
        #print(os.rmdir(Test_folder_name))
        shutil.rmtree(Test_folder_name)
    except:
        pass
    print('************* TEARDOWN *****************')
