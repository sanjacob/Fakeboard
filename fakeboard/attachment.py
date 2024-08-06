from blackboard.blackboard import BBAttachment

from . import db


def _create_attachment(attachment):
    return BBAttachment(id=attachment["filename"],
                        fileName=attachment["filename"],
                        mimeType=attachment["mimetype"])


async def get_file_attachments(courseId, contentId):
    courses = db["courses"]

    if courseId in courses:
        content = courses[courseId]["content"]

        if contentId in content:
            attachments = content[contentId].get("attachments", [])
            return [_create_attachment(a) for a in attachments]
    return None
