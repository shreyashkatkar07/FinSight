from abc import ABC
from abc import abstractmethod

from apps.artifacts.models import Artifact


class BaseExtractor(ABC):

    @abstractmethod
    def extract(
        self,
        *,
        artifact: Artifact,
    ) -> str:
        pass