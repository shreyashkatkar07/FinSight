from abc import ABC
from abc import abstractmethod


class OCRProvider(ABC):

    @abstractmethod
    def extract_text(
        self,
        *,
        image_path: str,
    ) -> str:
        pass