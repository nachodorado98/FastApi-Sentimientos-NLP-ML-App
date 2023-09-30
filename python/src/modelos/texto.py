from pydantic import BaseModel

class Texto(BaseModel):

	texto:str

	class Config:

		json_schema_extra={"example":{"texto":"Hello! I'm very happy today."}}