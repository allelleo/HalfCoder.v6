from app.api.v1.models import (
    User, Profile, Politic, Rating,
    RatingPerWeek, RatingPerMonth
)

from app.adapter.auth.schemas import RegistrationSchema

from app.api.v1.utils.unique import unique_username, unique_email

import app.adapter.auth.exceptions as E

from tortoise.transactions import in_transaction

ok = lambda uuid, email: {
    'status': 201,
    'message': {
        'ru': 'Регистрация прошла успешно',
        'en': 'Registration was successful'
    },
    'uuid': str(uuid),
    'email': email,
}


async def registration(model: RegistrationSchema):
    if not await unique_username(User, model.username):
        raise E.UsernameUniqueHTTPException
    if not await unique_email(User, model.email):
        raise E.EmailUniqueHTTPException

    try:
        async with in_transaction() as transaction:
            profile = Profile()
            await profile.save(using_db=transaction)
            politic = Politic()
            await politic.save(using_db=transaction)
            rating = Rating()
            await rating.save(using_db=transaction)
            rating_per_week = RatingPerWeek()
            await rating_per_week.save(using_db=transaction)
            rating_per_month = RatingPerMonth()
            await rating_per_month.save(using_db=transaction)

            user = User(
                email=model.email,
                username=model.username,
                first_name=model.first_name,
                last_name=model.last_name,
                profile=profile,
                politic=politic,
                rating=rating,
                ratingWeek=rating_per_week,
                ratingMonth=rating_per_month
            )
            await user.set_password(model.password)
            await user.save(using_db=transaction)

            return ok(user.uuid, user.email)

    except Exception as e:
        print(e)
        raise E.DataBaseHTTPException
