from marshmallow import Schema, fields, validate


class CarSchema(Schema):
    id = fields.Integer(required=False)
    model = fields.String(required=True)
    category = fields.String(required=True)
    year_of_manufacture = fields.Integer(required=True)
    description = fields.String(required=True)
    guidelines = fields.String(required=True)
    faqs = fields.Dict(keys=fields.Str(), values=fields.Str())
    current_geotag = fields.String(required=True)
    price = fields.Float(required=True)
    tags = fields.Nested('TagSchema', many=True, required=True)
    reviews = fields.Nested('ReviewSchema', many=True, required=True)
    extras = fields.Nested('ExtraSchema', many=True, required=True)
    features = fields.Nested('TagSchema', many=True, required=True)


class TagSchema(Schema):
    icon = fields.String(required=True)
    name = fields.String(required=True)


class ReviewSchema(Schema):
    name = fields.String(required=True)
    datetime_of_create = fields.DateTime(required=True)
    evaluation = fields.Integer(required=True, validate=validate.Range(min=0, max=5))
    comment = fields.String(required=True)


class ExtraSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Float(required=True, validate=validate.Range(min=0))
