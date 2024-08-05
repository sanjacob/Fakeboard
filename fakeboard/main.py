from typing import Generic, TypeVar
from typing_extensions import TypedDict

from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from blackboard.blackboard import (
    BBMembership,
    BBCourse,
    BBCourseContent,
    BBAttachment
)

from . import membership, course, content, attachment


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

app = FastAPI(root_path="/learn/api/public", root_path_in_servers=False)
app.mount("/files", StaticFiles(directory="static"), name="static")

@app.get("/v1/{userId}/courses")
async def get_user_memberships(userId: str) -> Results[BBMembership]:
    result = await membership.get_memberships(userId)

    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"results": result}

@app.get("/v3/courses/{courseId}")
async def get_course(courseId: str) -> BBCourse | None:
    result = await course.get_course(courseId)

    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return result

@app.get("/v1/courses/{courseId}/contents")
async def get_contents(courseId: str) -> Results[BBCourseContent]:
    result = await content.get_contents(courseId)

    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"results": result}

@app.get("/v1/courses/{courseId}/contents/{contentId}/children")
async def get_content_children(courseId: str, contentId: str) -> Results[BBCourseContent]:
    result = await content.get_content_children(courseId, contentId)

    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"results": result}

@app.get("/v1/courses/{courseId}/contents/{contentId}/attachments")
async def get_file_attachments(courseId: str, contentId: str) -> Results[BBAttachment]:
    result = await attachment.get_file_attachments(courseId, contentId)

    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"results": result}

@app.get("/v1/courses/{courseId}/contents/{contentId}/attachments/{attachmentId}/download", response_class=RedirectResponse, status_code=302)
async def download(courseId: str, contentId: str, attachmentId: str) -> None:
    return f"/learn/api/public/files/{courseId}/{attachmentId}"

@app.get("/v1/users/{userId}")
async def get_user(userId: str):
    return {"id": "jsanchez"}

@app.get("/v1/system/version")
async def get_version() -> BBVersion:
    return {
        "learn": {
            "major": 1,
            "minor": 0,
            "patch": 0,
            "build": "dev"
        }
    }
