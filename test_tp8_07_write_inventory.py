import os
import unittest

from exercise_07_write_inventory import write_inventory


class TestWriteInventory(unittest.TestCase):

    def setUp(self):
        self.filename = "test_tp8_07_tmp.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def _read(self):
        with open(self.filename, "r") as f:
            return f.read()

    def test_escribe_ordenado_alfabeticamente(self):
        write_inventory(self.filename, {"wood": 10, "coal": 3, "iron": 7})
        self.assertEqual("coal:3\niron:7\nwood:10\n", self._read())

    def test_diccionario_vacio_crea_archivo_vacio(self):
        write_inventory(self.filename, {})
        self.assertTrue(os.path.exists(self.filename))
        self.assertEqual("", self._read())

    def test_sobreescribe_contenido_previo(self):
        with open(self.filename, "w") as f:
            f.write("viejo contenido\n")
        write_inventory(self.filename, {"a": 1})
        self.assertEqual("a:1\n", self._read())

    def test_retorna_none(self):
        result = write_inventory(self.filename, {"x": 1})
        self.assertIsNone(result)

    def test_un_solo_item(self):
        write_inventory(self.filename, {"diamond": 5})
        self.assertEqual("diamond:5\n", self._read())


if __name__ == "__main__":
    unittest.main()
