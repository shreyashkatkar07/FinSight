from pathlib import Path

from django.core.files.storage import default_storage
from ninja.files import UploadedFile


class StorageService:

    ARTIFACT_DIRECTORY = "artifacts"

    def save_file(
        self,
        *,
        file: UploadedFile,
    ) -> str:
        file_path = (
            Path(self.ARTIFACT_DIRECTORY)
            / file.name
        )

        return default_storage.save(
            str(file_path),
            file,
        )


storage_service = StorageService()