import httpx
from app.adapter.user.schemas import RegistrationSchema, LoginSchema
from app.settings import AdapterSettings
from app.adapter.user.exceptions import CallServiceHTTPException, NotFoundByUsernameHTTPException, WrongPasswordHTTPException, UsernameUniqueHTTPException, EmailUniqueHTTPException, DataBaseHTTPException
from app.providers import Authentication

class APIClient:
    @staticmethod
    async def call_registration(user: RegistrationSchema):
        print(2)
        async with httpx.AsyncClient() as client:
            try:
                response: httpx.Response = await client.post (
                    url=AdapterSettings.user_service_url + 'api/v1/adapter/auth/registration',
                    json={
                            'username': user.username,
                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'email': user.email,
                            'password': user.password
                    }
                )
            except Exception as e:
                print(e)
                raise CallServiceHTTPException
        return response

    @staticmethod
    async def call_login(user: LoginSchema):
        async with httpx.AsyncClient() as client:
            try:
                response: httpx.Response = await client.post(
                    url=AdapterSettings.user_service_url + 'api/v1/adapter/auth/login',
                    json={
                            'username': user.username,
                            'password': user.password
                    }
                )
            except Exception as e:
                raise CallServiceHTTPException
        return response


class APIProcess:
    @staticmethod
    async def registration(response: httpx.Response):
        if response.status_code != 200:
            print(response.json())

            if response.status_code == 409:
                if response.json()['detail']['message']['en'] == 'Username is already registered':
                    raise UsernameUniqueHTTPException
                if response.json()['detail']['message']['en'] == 'Email is already registered':
                    raise EmailUniqueHTTPException
            elif response.status_code == 500:
                if response.json()['detail']['message']['en'] == 'Unknown error':
                    raise DataBaseHTTPException
                else:
                    raise CallServiceHTTPException
            else:
                raise CallServiceHTTPException
        data: dict = response.json()
        uuid: str = str(data.get('uuid'))
        email: str = str(data.get('email'))

        data.pop('uuid')

        # TODO: Отправить письмо с ссылкой на почту ( uuid )
        return data

    @staticmethod
    async def login(response: httpx.Response, auth: Authentication) -> str:
        if response.status_code != 200:
            if response.status_code == 409:
                if response.json()['detail']['message']['en'] == 'Not found user with this name':
                    raise NotFoundByUsernameHTTPException
                if response.json()['detail']['message']['en'] == 'Wrong password':
                    raise WrongPasswordHTTPException
            else:
                raise CallServiceHTTPException

        user_id: int = response.json()['user_id']
        return auth.login(user_id)
