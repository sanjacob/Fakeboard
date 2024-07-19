from typing import Generic, TypeVar
from typing_extensions import TypedDict

from fastapi import FastAPI

from blackboard.blackboard import (
    BBMembership,
    BBCourse,
    BBCourseContent,
    BBAttachment
)

T = TypeVar("T")

class Results(Generic[T], TypedDict):
    results: list[T]

class SemVer(TypedDict):
    major: int
    minor: int
    patch: int
    build: str

class BBVersion(TypedDict):
    learn: SemVer


# Fakeboard API

app = FastAPI()

api = "/learn/api/public/"

@app.get(api + "v1/{userId}/courses")
async def get_user_memberships() -> Results[BBMembership]:
    return {"results": []}

@app.get(api + "v3/courses/{courseId}")
async def get_courses() -> BBCourse | Results[BBCourse]:
    return {"results": []}

@app.get(api + "v1/courses/{courseId}/contents/{contentId}")
async def get_contents() -> BBCourseContent | Results[BBCourseContent]:
    return {"results": []}

@app.get(api + "v1/courses/{courseId}/contents/{contentId}/children")
async def get_content_children() -> Results[BBCourseContent]:
    return {"results": []}

@app.get(api + "v1/courses/{courseId}/contents/{contentId}/attachments/{attachmentId}")
async def get_file_attachments() -> BBAttachment | Results[BBAttachment]:
    return {"results": []}

@app.get(api + "v1/system/version")
async def get_version() -> BBVersion:
    return {
        "learn": {
            "major": 1,
            "minor": 0,
            "patch": 0,
            "build": "dev"
        }
    }
