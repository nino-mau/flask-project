import os
import uuid

import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()


class CloudinaryService:
    def __init__(
        self,
        cloud_name: str = os.getenv("CLOUDINARY_NAME") or "",
        api_key: str = os.getenv("CLOUDINARY_API_KEY") or "",
        api_secret: str = os.getenv("CLOUDINARY_API_SECRET") or "",
    ):
        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
        )

    def upload(self, file_to_upload):
        if hasattr(file_to_upload, "filename"):
            return cloudinary.uploader.upload(
                file_to_upload,
                folder="flask_app_uploads/",
                public_id=file_to_upload.filename,
                display_name=file_to_upload.filename,
            )
        else:
            return cloudinary.uploader.upload(
                file_to_upload,
                folder="flask_app_uploads/",
                public_id=str(uuid.uuid4()),
                display_name=str(uuid.uuid4()),
            )
