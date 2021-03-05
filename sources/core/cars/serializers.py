from core.accounts.serializers import serialize_account
from core.cars.entities import Car, Tag, Review, Extra


def serialize_car(car: Car) -> dict:
    return dict(
        car_id=car.car_id,
        model=car.model,
        category=car.category,
        year_of_manufacture=car.year_of_manufacture,
        hoster=car.hoster,
        tags=[serialize_tag(tag) for tag in car.tags],
        reviews=[serialize_review(review) for review in car.reviews],
        extras=[serialize_extra(extra) for extra in car.extras],
        description=car.description,
        features=[serialize_tag(tag) for tag in car.features],
        guidelines=car.guidelines,
        faqs=car.faqs,
        current_geotag=car.current_geotag,
        price=car.price,
    )


def serialize_tag(tag: Tag) -> dict:
    return dict(
        icon=tag.icon,
        name=tag.name,
    )


def serialize_review(review: Review) -> dict:
    return dict(
        account=serialize_account(review.account),
        datetime_of_create=review.datetime_of_create,
        evaluation=review.evaluation,
        comment=review.comment,
    )


def serialize_extra(extra: Extra) -> dict:
    return dict(
        name=extra.name,
        description=extra.description,
        price=extra.price,
    )
