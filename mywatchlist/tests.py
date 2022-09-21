from django.test import TestCase
from django.test import Client

class TestingTugas(TestCase):
    def testing_html(self):
        html_response = Client().get("/mywatchlist/html/")
        self.assertEqual(html_response.status_code, 200)

    def testing_xml(self):
        xml_response = Client().get("/mywatchlist/xml/")
        self.assertEqual(xml_response.status_code, 200)

    def testing_json(self):
        json_response = Client().get("/mywatchlist/json/")
        self.assertEqual(json_response.status_code, 200)
