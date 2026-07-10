import xml.etree.ElementTree as et

from app.book import Book
from app.serializer.base import BaseSerializer


class XmlSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        root = et.Element("book")

        title = et.SubElement(root, "title")
        title.text = book.title

        content = et.SubElement(root, "content")
        content.text = book.content

        return et.tostring(root, encoding="unicode")
