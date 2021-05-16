from mc_api.components import *

def testblock(coordinates, interface=None):

    if not interface:
        return interface

    if type(coordinates) is tuple:
        coordinates = Coordinates(*coordinates)

    # TODO: here
    cmd = Command('execute', coordinates).to_str()
    response = interface.post(cmd)

    return response

    