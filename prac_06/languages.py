"""
CP1404 - Practicals - Week 6: Classes
"""

from prac_06.programming_langauge import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)

    is_ruby_dynamic = ruby.is_dynamic()
    is_python_dynamic = python.is_dynamic()
    is_visual_basic_dynamic = visual_basic.is_dynamic()

    print("\nThe dynamically typed languages are: ")

    if is_python_dynamic:
        print(python.name)

    if is_ruby_dynamic:
        print(ruby.name)

    if is_visual_basic_dynamic:
        print(visual_basic.name)


main()
