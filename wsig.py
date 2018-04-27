from tigereye import create_app
from tigereye.configs.product import ProductConfig


aplication = create_app(config=ProductConfig)