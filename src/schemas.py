from pydantic import BaseModel, Field   

class Asteroid(BaseModel):
    plate: str
    lat: float = Field(description="x", default=42)
    lon: float = Field(description="y", default=69)
