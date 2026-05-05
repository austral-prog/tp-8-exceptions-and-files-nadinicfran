import os
import unittest

from exercise_05_csv_to_dict import csv_to_dict


class TestCsvToDict(unittest.TestCase):

    def setUp(self):
        self.filename = "test_tp8_05_tmp.csv"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def _write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)

    def test_ejemplo_basico(self):
        self._write("name,age,city\nAlice,30,Buenos Aires\nBob,25,Rosario\n")
        self.assertEqual(
            [
                {"name": "Alice", "age": 30, "city": "Buenos Aires"},
                {"name": "Bob", "age": 25, "city": "Rosario"},
            ],
            csv_to_dict(self.filename),
        )

    def test_age_es_int(self):
        self._write("name,age,city\nAlice,30,BA\n")
        data = csv_to_dict(self.filename)
        self.assertIsInstance(data[0]["age"], int)

    def test_solo_header_retorna_lista_vacia(self):
        self._write("name,age,city\n")
        self.assertEqual([], csv_to_dict(self.filename))

    def test_archivo_vacio(self):
        self._write("")
        self.assertEqual([], csv_to_dict(self.filename))

    def test_una_fila(self):
        self._write("name,age,city\nCarla,40,Cordoba\n")
        self.assertEqual(
            [{"name": "Carla", "age": 40, "city": "Cordoba"}],
            csv_to_dict(self.filename),
        )

    def test_archivo_no_existe(self):
        with self.assertRaises(FileNotFoundError):
            csv_to_dict("archivo_que_no_existe_tp8_05.csv")


if __name__ == "__main__":
    unittest.main()
