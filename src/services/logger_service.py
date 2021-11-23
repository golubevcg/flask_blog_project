import logging
import logging.handlers as handlers
import re

logging.basicConfig(
     filename='flask_blog.log',
     level=logging.INFO,
     format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s',
     datefmt='%H:%M:%S'
 )

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)

log_handler = (handlers
               .TimedRotatingFileHandler(
                                        'flask_blog.log',
                                        when='D',
                                        interval=1
                                        )
               )
log_handler.suffix = "%d_%m_%Y"
log_handler.extMatch = re.compile(r"^\d{8}$")
log_handler.setLevel(logging.INFO)

logging.getLogger('').addHandler(console)
logging.getLogger('').addHandler(log_handler)


main_logger = logging.getLogger('main_logger')
