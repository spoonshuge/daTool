import logging
import sys

INFO_LOG_FILENAME = '/var/log/aw_net_test_info.log'
WARNING_LOG_FILENAME = '/var/log/aw_net_test_warn.log'

# set up formatting
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] (%(process)d) %(module)s: %(message)s')

# set up logging to STDOUT for all levels INFO and higher
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.INFO)
sh.setFormatter(formatter)

# create logger object
mylogger = logging.getLogger('MyLogger')
mylogger.setLevel(logging.INFO)
mylogger.addHandler(sh)

# set up logging to a file for all levels INFO and higher
try:
    fh = logging.FileHandler(INFO_LOG_FILENAME)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)

    # create file logger object
    mylogger.addHandler(fh)
except IOError:
    print('It appears you are not on Linux, or do not have access to /var/log/ ...dropping file logging.')

# create shortcut functions
debug = mylogger.debug
info = mylogger.info
warning = mylogger.warning
error = mylogger.error
critical = mylogger.critical
