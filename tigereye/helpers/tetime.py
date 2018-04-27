from datetime import datetime

DEFAULT_DATETIME_FORMAT = '%Y%m%d%H%H%S'
SIMPLE_DATETIME_FORMAT = '%Y-%m-%d-%H-%H-%S'

def now():
    return datetime.now().strftime('%Y%m%d%H%M%S')