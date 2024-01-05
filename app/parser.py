import pywavefront
import quads


def parse(filename: str):
    scene = pywavefront.Wavefront(filename)
    quad_tree = quads.QuadTree(0, 0 ,0)
