import os
import unittest

from exercise_09_merge_files import merge_files


class TestMergeFiles(unittest.TestCase):

    def setUp(self):
        self.file1 = "test_tp8_09_a.txt"
        self.file2 = "test_tp8_09_b.txt"
        self.output = "test_tp8_09_out.txt"

    def tearDown(self):
        for f in (self.file1, self.file2, self.output):
            if os.path.exists(f):
                os.remove(f)

    def _write(self, filename, content):
        with open(filename, "w") as f:
            f.write(content)

    def _read(self, filename):
        with open(filename, "r") as f:
            return f.read()

    def test_concatena_en_orden(self):
        self._write(self.file1, "hola\n")
        self._write(self.file2, "mundo\n")
        merge_files(self.file1, self.file2, self.output)
        self.assertEqual("hola\nmundo\n", self._read(self.output))

    def test_archivos_vacios(self):
        self._write(self.file1, "")
        self._write(self.file2, "")
        merge_files(self.file1, self.file2, self.output)
        self.assertEqual("", self._read(self.output))

    def test_uno_vacio_otro_con_contenido(self):
        self._write(self.file1, "")
        self._write(self.file2, "contenido\n")
        merge_files(self.file1, self.file2, self.output)
        self.assertEqual("contenido\n", self._read(self.output))

    def test_sobreescribe_output(self):
        self._write(self.file1, "nuevo\n")
        self._write(self.file2, "valor\n")
        self._write(self.output, "viejo\n")
        merge_files(self.file1, self.file2, self.output)
        self.assertEqual("nuevo\nvalor\n", self._read(self.output))

    def test_file1_no_existe(self):
        self._write(self.file2, "b\n")
        with self.assertRaises(FileNotFoundError):
            merge_files("no_existe_a.txt", self.file2, self.output)
        self.assertFalse(
            os.path.exists(self.output),
            "El archivo de salida no debe crearse si falta un input",
        )

    def test_file2_no_existe(self):
        self._write(self.file1, "a\n")
        with self.assertRaises(FileNotFoundError):
            merge_files(self.file1, "no_existe_b.txt", self.output)
        self.assertFalse(
            os.path.exists(self.output),
            "El archivo de salida no debe crearse si falta un input",
        )

    def test_retorna_none(self):
        self._write(self.file1, "a\n")
        self._write(self.file2, "b\n")
        self.assertIsNone(merge_files(self.file1, self.file2, self.output))


if __name__ == "__main__":
    unittest.main()
