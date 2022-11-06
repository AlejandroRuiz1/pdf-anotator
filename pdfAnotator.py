#!/usr/bin/env python

import argparse
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

width, height = letter

class File:
    def __init__(self, filename, location) -> None:
        self.filename = filename
        self.location = location

'''
    def function to calculate vertical distance between slides for a given number of slides
    set page margins 
    place images of slides offset to the right by a variable amount 
'''
class Page:
    def __init__(self, width: int, height: int, number_of_slides: int, number_of_lines: int) -> None:
        self.width = width 
        self.height = height
        self.number_of_slides = number_of_slides
        self.number_of_lines = number_of_lines

def calculateDims(width, height, number_of_slides, number_of_lines):
    page_area = width * height

def annotate(path):
    c = canvas.Canvas(pagesize=letter)

def getArgs():
    argParser = argparse.ArgumentParser(
        description="Converts PDF slides to annotateable PDF"
    ) 
    argParser.add_argument("filename", type=Path, help="Name of PDF file to import")
    argParser.add_argument("-O", "--output", type=str, help="Output filename for PDF")
    argParser.add_argument("-W", "--width", type=int, help="Width of paper", default=8)
    argParser.add_argument( "-H", "--height", type=int, help="Height of paper", default=11)
    argParser.add_argument("-S", "--slides", type=int, help="Number of slides per page", default=3)
    return argParser.parse_args()

def main():
    args = getArgs()

    print("Hello!")


if __name__ == '__main__':
    main()


# the page parameters will be obtained from user input
# either argparse or a simple gui with buttons
