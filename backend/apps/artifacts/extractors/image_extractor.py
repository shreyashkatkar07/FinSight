from .base import BaseExtractor

class ImageExtractor(BaseExtractor):

    def extract(
        self,
        *,
        artifact,
    ) -> str:

        return """
            Paid Successfully

            ₹250

            To Zomato

            26 June 2026

            UPI Ref 123456
        """