import math

import pywavefront
from quads import QuadTree


def parse(filename: str) -> QuadTree:
    scene = pywavefront.Wavefront(filename)
    min_x = min(vertex[0] for vertex in scene.vertices)
    max_x = min(vertex[0] for vertex in scene.vertices)
    min_y = min(vertex[1] for vertex in scene.vertices)
    max_y = min(vertex[1] for vertex in scene.vertices)

    quad_tree = QuadTree((0, 0), math.ceil(max_x - min_x), math.ceil(max_y - min_y))

    for vertex in scene.vertices:
        quad_tree.insert((vertex[0], vertex[1]))

    return quad_tree
