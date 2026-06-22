from abc import ABC, abstractmethod

from apps.artifacts.models import Artifact


class BaseParser(ABC):

    @abstractmethod
    def parse(
        self,
        artifact: Artifact,
    ):
        pass