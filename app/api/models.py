from pydantic import BaseModel
from typing import List, Optional


class StudentIn(BaseModel):
    name: str
    genre: str
    learning: int
    city: str
    university_id: List[int]


class StudentOut(StudentIn):
    id: int


class StudentUpdate(StudentIn):
    name: Optional[str] = None
    genre: Optional[str] = None
    learning: Optional[str] = None
    city: Optional[str] = None
    university_id: Optional[List[int]] = None