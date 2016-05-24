# TIY Palindrome Boolean

## Introduction

This module determines whether a user-provided string is a palindrome (i.e. string of characters that can be written the same forward and reverse). The program ignores all punctuation, capitalization, and white space.

The program accepts "" as a palindrome, as well as any string of numbers that looks like a palindrome (e.g. 10301).

The `palindrome_text_reader.py` accepts a text files as an input, provided on directly following the program call on the terminal prompt. The program will test blank lines and return that they are a palindrome, so they should be omitted.

## Dependancies

There are no dependancies for this module. The program is called from the terminal prompt and runs a single iteration before completing. Alternately, there is a text_reader module that can determine palidromes contained in a text file. This program is called from the terminal prompt, followed by the name (or path) of the text file.

## Structure

There are five files associated with this module:
  `README.md` is this file;
  `palindrome.py` is the base program that prompts users for a word to test;
  `palindrome_text_reader.py` is the modified program that parses line-by-line through a text file and tests each line;
  `palindrome_test.py` is a testing program, only for debugging purposes;
  `text.rtf` is a text file, also used for debugging purposes.
