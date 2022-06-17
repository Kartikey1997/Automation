import os
import logging
from _datetime import datetime

class LogGen:

    @staticmethod
    def loggen():
        time_now = datetime.now().strftime("%d-%m-%Y--%I:%M %p")
        logger = logging.getLogger()
        path = "./logs/"
        date_folder = datetime.now().strftime("%d-%m-%Y")
        new_path = os.path.join(path,date_folder)
        try:
            os.mkdir(new_path)

        except FileExistsError or FileNotFoundError:
            fhandler = logging.FileHandler(filename=new_path+"/"+"Autolog-"+time_now+".log",
                                       mode="w")
            formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)

        else:
            fhandler = logging.FileHandler(filename=new_path + "/" + "Autolog-" + time_now + ".log",
                                           mode="w")
            formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)

        return logger
