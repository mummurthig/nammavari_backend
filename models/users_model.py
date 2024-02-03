from pydantic import BaseModel

class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    mobile_number: str
    user_dob: str
    place: str