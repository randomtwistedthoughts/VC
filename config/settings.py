from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = ""
    version: str = "0.1.0"
    max_agent_steps: int = 10

    class Config:
        env_file = ".env"

settings = Settings()
  
  
