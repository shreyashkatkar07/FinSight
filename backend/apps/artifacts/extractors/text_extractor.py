from .base import BaseExtractor


class TextExtractor(BaseExtractor):

    def extract(
        self,
        *,
        artifact,
    ) -> str:

        return artifact.storage_path