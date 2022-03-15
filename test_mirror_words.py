import unittest

from mirror_words import mirror_words

class TestMirrorWords(unittest.TestCase):
    def test1(self):
        sentence = ""
        self.assertEqual(mirror_words(sentence, len(sentence)), "")

    def test2(self):
        sentence = " "
        self.assertEqual(mirror_words(sentence, len(sentence)), " ")

    def test3(self):
        sentence = ","
        self.assertEqual(mirror_words(sentence, len(sentence)), ",")

    def test4(self):
        sentence = "."
        self.assertEqual(mirror_words(sentence, len(sentence)), ".")

    def test5(self):
        sentence = ".."
        self.assertEqual(mirror_words(sentence, len(sentence)), "..")

    def test6(self):
        sentence = ",."
        self.assertEqual(mirror_words(sentence, len(sentence)), ",.")

    def test7(self):
        sentence = "I"
        self.assertEqual(mirror_words(sentence, len(sentence)), "I")

    def test8(self):
        sentence = "One"
        self.assertEqual(mirror_words(sentence, len(sentence)), "enO")

    def test9(self):
        sentence = "One."
        self.assertEqual(mirror_words(sentence, len(sentence)), "enO.")

    def test10(self):
        sentence = ".One."
        self.assertEqual(mirror_words(sentence, len(sentence)), ".enO.")

    def test11(self):
        sentence = "..One.."
        self.assertEqual(mirror_words(sentence, len(sentence)), "..enO..")

    def test12(self):
        sentence = "One.Two"
        self.assertEqual(mirror_words(sentence, len(sentence)), "enO.owT")

    def test13(self):
        sentence =   ".One.Two."
        self.assertEqual(mirror_words(sentence, len(sentence)), ".enO.owT.")

    def test14(self):
        sentence = "..One..Two.."
        self.assertEqual(mirror_words(sentence, len(sentence)), "..enO..owT..")

    def test15(self):
        sentence = "One two, I three.  Four."
        self.assertEqual(mirror_words(sentence, len(sentence)), "enO owt, I eerht.  ruoF.")

unittest.main()

