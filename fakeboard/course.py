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
        id=courseId,
        courseId=courseId,
        name=course["name"],
        created=course["created"],
        availability=BBAvailability(available="Yes"),
        enrollment=BBEnrollment(type="")
    )


async def get_course(courseId):
    courses = db["courses"]

    if courseId in courses:
        return _create_course(courseId)
    return None
