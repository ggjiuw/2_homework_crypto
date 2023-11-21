import jwt
import settings

def decode(data: str) -> dict:
    decoded_result = jwt.decode(
        data,
        settings.JWT_SECRET,
        algorithms=['HS256'],
        options={
        'verify_signature': False
        }
    )
    return decoded_result