from blackboard.blackboard import (
    BBCourse,
    BBLocale,
    BBEnrollment,
    BBAvailability
)

from . import db


def _create_course(courseId):
    course = db["courses"][courseId]

    return BBCourse(
        id=f"ID-{courseId}",
        courseId=courseId,
        name=course["name"],
        description=course["description"],
        created="2024-01-01T12:30:00.000Z",
        modified="2024-01-01T12:30:00.000Z",
        availability=BBAvailability(available="Yes"),
        enrollment=BBEnrollment(type="")
    )


async def get_course(courseId):
    courses = db["courses"]

    if courseId in courses:
        return _create_course(courseId)
    return None