import xml.etree.ElementTree as ET

from app.book import Book
from app.serializer.base import BaseSerializer


class XmlSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")

        title = ET.SubElement(root, "title")
        title.text = book.title

        content = ET.SubElement(root, "content")
        content.text = book.content

        return ET.tostring(root, encoding="unicode")
