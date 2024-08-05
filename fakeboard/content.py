from blackboard.blackboard import (
    BBCourseContent,
    BBAvailability,
    BBContentHandler
)

from . import db


def _create_content(courseId, contentId):
    content = db["courses"][courseId]["content"][contentId]
    return BBCourseContent(
        id=contentId,
        title=content["title"],
        body=content["body"],
        created=content["created"],
        modified="2024-01-01T12:30:00.000Z",
        hasChildren=len(content["children"]) > 0,
        availability=BBAvailability(available="Yes"),
        contentHandler=BBContentHandler(id=content["type"])
    )


async def get_contents(courseId):
    courses = db["courses"]

    if courseId in courses:
        contents = courses[courseId]["content"]
        return [_create_content(courseId, id) for id in contents]
    return None


async def get_content_children(courseId, contentId):
    courses = db["courses"]

    if courseId in courses:
        content = courses[courseId]["content"]

        if contentId in content:
            children = content[contentId]["children"]
            return [_create_content(courseId, id) for id in children]
    return None
