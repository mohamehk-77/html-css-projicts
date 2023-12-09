from pylatex import Document, Section, Subsection, Command
from pylatex.utils import escape_latex


def add_test_case(doc, title, code):
    with doc.create(Section(title, numbering=False)):
        doc.append(Command('begin', 'verbatim'))
        doc.append(code)
        doc.append(Command('end', 'verbatim'))


doc = Document()

# Task 0
add_test_case(doc, "Task 0: Integers Addition", """
>>> add_integer(2, 3)
5
""")

# Task 1
add_test_case(doc, "Task 1: Divide a Matrix", """
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
""")

# Task 2
add_test_case(doc, "Task 2: Say My Name", """
>>> say_my_name("John", "Smith")
My name is John Smith
""")

# Task 3
add_test_case(doc, "Task 3: Print Square", """
>>> print_square(4)
####
####
####
####
""")

# Task 4
add_test_case(doc, "Task 4: Text Indentation", """
>>> text_indentation("This is a sentence. This is another? And this is the last:")
This is a sentence.
This is another?
And this is the last:
""")

# Task 5
add_test_case(doc, "Task 5: Max Integer - Unittest", """
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

if __name__ == '__main__':
    unittest.main()
""")

doc.generate_pdf("test_cases", clean_tex=True)
