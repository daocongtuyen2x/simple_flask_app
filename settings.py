# initialize Redis connection settings
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# initialize constants used to control image spatial dimensions and
# data type
IMAGE_WIDTH = 120
IMAGE_HEIGHT = 120
IMAGE_CHANS = 1
IMAGE_DTYPE = "float32"

# initialize constants used for server queuing
IMAGE_QUEUE = "image_queue"
BATCH_SIZE = 1
SERVER_SLEEP = 0.5
CLIENT_SLEEP = 0.5