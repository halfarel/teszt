class Cuboid():
    """
    This class can calculate the surface, and volume of a cuboid with given height, width and depth.
    """


    # utility function
    def volumeCuboid( l , h , w ):
        return (l * h * w)

    def surfaceAreaCuboid( l , h , w ):
        return (2 * l * w + 2 * w * h + 2 * l * h)

    # driver function
    l = 2
    h = 3
    w = 4
    print("Volume =" , volumeCuboid(l, h, w))
    print("Total Surface Area =", surfaceAreaCuboid(l, h, w))