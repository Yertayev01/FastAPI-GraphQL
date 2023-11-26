# Import pydantic BaseSettigns module.
from pydantic_settings import BaseSettings

# Define the Settings class which inherits from BaseSettings
class Settings(BaseSettings):
    # Define properties corresponding to environment variables
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    
    app_version: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    swagger_username: str
    swagger_password: str

settings = Settings(
        database_name="fastapi_grapql",
        database_username="postgres",
        database_password="postgres",
        # database_hostname="0.tcp.jp.ngrok.io",
        # database_port="19536",
        database_hostname="localhost",
        database_port="5432",
        app_version="1.0.0",
        secret_key="*",
        algorithm="HS256",
        access_token_expire_minutes=720,
        swagger_username="swagger_user",
        swagger_password="swagger_password"
)



# Define the Config inner class with the path to the environment file
class Config:
        env_file = ".env"