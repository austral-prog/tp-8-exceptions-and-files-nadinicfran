import os
import unittest

from exercise_10_log_parser import parse_log


class TestParseLog(unittest.TestCase):

    def setUp(self):
        self.filename = "test_tp8_10_tmp.log"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def _write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)

    def test_ejemplo_basico(self):
        self._write(
            "INFO: servidor iniciado\n"
            "ERROR: no se puede conectar\n"
            "INFO: reintentando\n"
            "WARN: lento\n"
        )
        self.assertEqual(
            {
                "INFO": ["servidor iniciado", "reintentando"],
                "ERROR": ["no se puede conectar"],
                "WARN": ["lento"],
            },
            parse_log(self.filename),
        )

    def test_un_solo_nivel(self):
        self._write("DEBUG: paso 1\nDEBUG: paso 2\n")
        self.assertEqual(
            {"DEBUG": ["paso 1", "paso 2"]},
            parse_log(self.filename),
        )

    def test_strip_en_nivel_y_mensaje(self):
        self._write("  INFO : hola mundo  \n")
        self.assertEqual({"INFO": ["hola mundo"]}, parse_log(self.filename))

    def test_ignora_lineas_vacias(self):
        self._write("INFO: a\n\n   \nINFO: b\n")
        self.assertEqual({"INFO": ["a", "b"]}, parse_log(self.filename))

    def test_linea_invalida_sin_dos_puntos(self):
        self._write("INFO: ok\nesto no es un log\n")
        with self.assertRaises(ValueError):
            parse_log(self.filename)

    def test_archivo_vacio_retorna_dict_vacio(self):
        self._write("")
        self.assertEqual({}, parse_log(self.filename))

    def test_archivo_no_existe(self):
        with self.assertRaises(FileNotFoundError):
            parse_log("archivo_que_no_existe_tp8_10.log")

    def test_mensaje_con_dos_puntos(self):
        # El mensaje puede contener ':' -> solo split en el primer ':'
        self._write("INFO: hora 10:30\n")
        self.assertEqual({"INFO": ["hora 10:30"]}, parse_log(self.filename))


if __name__ == "__main__":
    unittest.main()
