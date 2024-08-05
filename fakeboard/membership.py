from blackboard.blackboard import (
    BBMembership,
    BBAvailability
)

from . import db


def _create_membership(userId, membership):
    courseId = membership["course"]
    course = db["courses"][courseId]

    return BBMembership(
        id=f"ID-{userId}-{courseId}",
        userId=userId,
        courseId=courseId,
        created=membership["created"],
        availability=BBAvailability(available="Yes")
    )


async def get_memberships(userId):
    memberships = db["memberships"]

    if userId in memberships:
        return [_create_membership(userId, m) for m in memberships[userId]]
    return None
