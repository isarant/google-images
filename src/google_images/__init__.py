import os
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import logging
import urllib.request
import argparse

dict_Image_Size={'Any':1,
            'Large':2,
            'Medium':3,
            'Icon':4

}

logger = logging.getLogger('__name__')

def init_args():
    my_parser = argparse.ArgumentParser(description='Google Search images ')
    my_parser.add_argument("-f","--folder_name", default='cat', type= str, help="Folder Name to save image" )
    my_parser.add_argument("-t","--search_text", default='cat', type= str, help="The text that used in search")
    my_parser.add_argument("-n","--num_images", default=10, type= int, help="The max number of downloaded images")
    my_parser.add_argument("-s","--image_size",  default=1, type=int, help="Images size in google search Any=1 Large=2 Medium=3 Icon=4")
    return my_parser.parse_args()

def create_folder(folder_name):
    """
    create_folder Create a folder for downloaded images

    :param folder_name: Folder Name
    :return: True if folder created succesed othewise return False
    """ 
    try:
        os.mkdir(folder_name)
    except:
        return False
    return True

def get_driver():
    """
    get_diver Create a selenium driver for Chrome browsher

    :return: driver othewise return None
    """ 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #Create Driver for Chrome
    #Goto google image site
    try:
        driver.get('https://www.google.gr/imghp?hl=en&tab=ri&ogbl')
    except WebDriverException:
        print("page down")
        driver.quit()
        return None
    return driver

def init_search(driver,search_text,image_size):
    """
    init_search  Start a google search for images 

    :param driver: driver from function get_driver
    :param search_text: The text who used in google search
    "param image_size: Number , Select image size in google search ,Any=1,Large=2,Medium=3,Icon=4 See the dict_Image_Size List

    :return: if all excecute well return True  othewise return False
    """ 
   
    try:
        #This is only for my browser
        button_iagrre=driver.find_element_by_xpath('//*[@id="L2AGLb"]/div')
        button_iagrre.click()
        time.sleep(1)

        #Write to Search Box 
        search_box=driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
        search_box.send_keys(search_text)
        search_box.send_keys(keys.Keys.ENTER)
    except:
        return False

    #Chosse size of images
    try:
        button_tools=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div/div/div').click()
        time.sleep(1)
        button_size=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[1]/div/div[1]/div/div[1]').click()
        time.sleep(1)

        button_size =driver.find_element_by_xpath(f'//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[{image_size}]').click()
        #button_medium =driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[3]').click()
        #button_icon    =driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[4]').click()
        #button_icon    =driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[4]').click()
        time.sleep(1)
    except:
        return False
    return True

def download_all_current_page_images(driver,maxcount,folder_name,maxerrorcount=2):
    """
    download_all_current_page_images  from then google search page  (See init_search) make click to each image and from image preview at right 
    side to google  get url and download the image.
    Looping untill download maxcountsize of images or untiil there is not other images


    :param driver: driver from function get_driver
    :param maxcount: The max number of images we want to download
    "param folder_name: Folder name to save downloaded images
    "param maxerrorcount: 

    :return: The number of downloaded images
    """ 

    count=1
    filecount=1
    errorcount=0
    while(True):
        try:
            #find next thumbnail image
            logger.debug(f"Try to find thumbnail count {count}")
            image=driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(count)+']/a[1]/div[1]/img')
            logger.debug(f"Find thumbnail count {count}")
            # print(image.get_attribute('innerHTML'))
            
            #Click thubnail image
            image.click()
            logger.debug(f"Click thumbnail count {count}")
            #time.slepep(1)
            
            #Find preview of thubnail image to the right side
            logger.debug(f"Try to find image right side count {count}")
            right_image=driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(count)+']/a[1]')
            logger.debug(f"Find image right side count {count}")
            
            #Get href parameter
            url_image=right_image.get_attribute('href')
            logger.debug(f"Get image right side count {count}")
            #print(url_image)
            
            #Get source image url from big google url
            start = '?imgurl='
            end = '&imgrefurl='
            download_image_url=urllib.parse.unquote(url_image[url_image.find(start)+len(start):url_image.rfind(end)])
            logger.debug(f"Url image {download_image_url}")
            
            
            #Download image from source url
            try:
                localfilename= os.path.join(folder_name,f"{count}.jpg")
                logger.info(f"Download from {download_image_url} to { localfilename}")
                urllib.request.urlretrieve(download_image_url, localfilename)
                logger.info(f"Download Done")
                filecount=filecount+1
            except:
                pass
        except:
            try:
                next= driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
                logger.info("Clicked More Results")
            except:
                pass                
            
            

            #Check if is the end of page
            try:
                next= driver.find_element_by_xpath(f'//*[@id="islrg"]/div[1]/div[{count}]/following-sibling::div')
                id=next.get_attribute('id')
                logger.debug(f"Element id is {id}")
                if id=='islrh':
                    logger.debug(f" Find th end of page")
                errorcount=0
            except:
                errorcount=errorcount+1
                if(errorcount>maxerrorcount):
                    break
        finally:
            count=count+1
            if(filecount>=maxcount):
                break
    return filecount
