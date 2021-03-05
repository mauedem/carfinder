from marshmallow import Schema, fields, validate


class TripSchema(Schema):
    trip_id = fields.Integer(required=False)
    start_datetime = fields.DateTime(required=True)
    estimated_end_date = fields.DateTime(required=True)
    car_id = fields.Integer(required=True)
    price_amount = fields.Float(required=True)
