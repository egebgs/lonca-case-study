from datetime import datetime
from bson import ObjectId


class Product:
    def __init__(self, stock_code, color, discounted_price, images, is_discounted,
                 name, price, price_unit, product_type, quantity, sample_size,
                 series, status, fabric, model_measurements, product_measurements):
        self._id = ObjectId()
        self.stock_code = stock_code
        self.color = color
        self.discounted_price = discounted_price
        self.images = images
        self.is_discounted = is_discounted
        self.name = name
        self.price = price
        self.price_unit = price_unit
        self.product_type = product_type
        self.quantity = quantity
        self.sample_size = sample_size
        self.series = series
        self.status = status
        self.fabric = fabric
        self.model_measurements = model_measurements
        self.product_measurements = product_measurements
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "_id": self._id,
            "stock_code": self.stock_code,
            "color": self.color,
            "discounted_price": self.discounted_price,
            "images": self.images,
            "is_discounted": self.is_discounted,
            "name": self.name,
            "price": self.price,
            "price_unit": self.price_unit,
            "product_type": self.product_type,
            "quantity": self.quantity,
            "sample_size": self.sample_size,
            "series": self.series,
            "status": self.status,
            "fabric": self.fabric,
            "model_measurements": self.model_measurements,
            "product_measurements": self.product_measurements,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
