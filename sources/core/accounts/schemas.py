from marshmallow import Schema, fields, validate


class AccountSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(8, 64))
    personal_data = fields.Nested('PersonalDataSchema', many=False, required=True)


class PersonalDataSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(2, 64))
    last_name = fields.String(required=True, validate=validate.Length(2, 64))
