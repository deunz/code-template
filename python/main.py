#!/usr/bin/python
import logging, logging.config
import yaml
__author__ = 'Deunz'


class MyLogging(object):
    @staticmethod
    def setup_logging(log_config='./conf/logging.yaml'):
        with open(log_config) as f:
            my_config = yaml.load(f.read())
            logging.config.dictConfig(my_config)



class Test(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def my_event(self):
        self.logger.debug("hello")


if __name__ == '__main__':
    MyLogging.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Start program")
    t = Test()
    t.my_event()