#!/usr/bin/env python
"""
    Converts a raster image to an ellipsified version
"""

__author__ = "Brian Hooper"
__copyright__ = "Copyright (c) 2018 Brian Hooper"
__license__ = "MIT"
__version__ = "0.2"
__email__ = "brian_hooper@msn.com"

import Parse
import Draw
from ast import literal_eval as make_tuple


def parse_from_file(filename):
    points = []

    file = open(filename + ".jpg.txt", "r")
    lines = file.readlines()
    parser = Parse.Parse(filename + ".jpg")

    for line in lines:
        points.append(make_tuple(line))

    color_points = parser.get_all_colors(points)

    draw_image(filename, color_points, parser.width, parser.height)

    file.close()


def parse_image(filename):
    # Set options for parser
    parser = Parse.Parse(filename + ".jpg")
    parser.threshold = 18
    parser.precision = 3
    parser.minimum_size = 6

    # Parse the image
    points = parser.evaluate_image()

    # Draw the parsed image
    draw_image(filename, points, parser.width, parser.height)


def draw_image(filename, points, width, height):
    if len(points) > 0:
        drawer = Draw
        drawer.draw_image(points, filename + "_output.png", width, height)


def main():
    parse_from_file("gtr")


if __name__ == "__main__":
    main()
