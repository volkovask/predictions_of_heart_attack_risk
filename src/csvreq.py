from pydantic import BaseModel


class CSVRequest(BaseModel):
    file_path: str
