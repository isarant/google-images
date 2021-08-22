from __init__ import init_args
from __init__ import get_driver
from __init__ import init_search
from __init__ import create_folder
from __init__ import download_all_current_page_images
import logging.config

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logger = logging.getLogger('__name__')
    args=init_args()
    driver=get_driver()
    init_search(driver,args.search_text,args.image_size)
    create_folder(args.folder_name)
    logger.info(f" You have download {download_all_current_page_images(driver,args.num_images,args.folder_name)} Images")
    driver.close()
