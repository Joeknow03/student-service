import os
import httpx

UNIVERSITY_SERVICE_HOST_URL = 'http://localhost:8020/api/v1/university/'

def is_university_present(university_id: int):
    return True