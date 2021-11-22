import logging
import logging.handlers as handlers
import re

main_logger = logging.getLogger('flask_blog')
main_logger.setLevel(logging.INFO)

log_handler = handlers.TimedRotatingFileHandler('flask_blog.log', when='D', interval=1)
log_handler.suffix = "%d_%m_%Y"
log_handler.extMatch = re.compile(r"^\d{8}$")
log_handler.setLevel(logging.INFO)
main_logger.addHandler(log_handler)
