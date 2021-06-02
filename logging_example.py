import logging
import sys

# Formatting:
# %(asctime)s - time stamp
# %(name)s - file name from which is logged right now
# %(lineno)d - line number of logging call
# %(levelname)s - logging level
# %(message)s - at call specified msg

# standard values - prints to stderr with level = logging.WARNING (I don't like the format at all)
##logging.basicConfig()

# my standard logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='[%(asctime)s] {%(lineno)d} %(levelname)s: %(message)s')

# print-like logging
##logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='') # '%(message)s' isn't needed if format is an empty string

# only logging to file
##log_filename = 'myProgramLog.txt'
##logging.basicConfig(filename=log_filename, filemode='w', level=logging.DEBUG, format='[%(asctime)s] {%(lineno)d} %(levelname)s: %(message)s') # when not specified filemode is set to 'a'

# logging output to stdout and file
##file_handler = logging.FileHandler(filename='tmp.log')
##stdout_handler = logging.StreamHandler(sys.stdout)
##handlers = [file_handler, stdout_handler]
##
##logging.basicConfig(
##    level=logging.DEBUG, 
##    format='[%(asctime)s] {%(lineno)d} %(levelname)s: %(message)s',
##    handlers=handlers
##)
##
##logger = logging.getLogger('LOGGER_NAME')


##logging.getLogger().setLevel(logging.INFO)
##logging.disable(logging.debug)

logging.debug('Debug Text')
logging.info('Info Text')
logging.warning('Warning Text')
logging.error('Error Text')
logging.critical('Critical Text')
logging.fatal('Fatal Text')
print('normal print')
