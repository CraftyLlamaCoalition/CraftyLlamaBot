from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str = Field()


if __name__ == "__main__":
    print(Settings().model_dump())
