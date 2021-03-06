import sys
from StaticApiLibrary import AcceptanceTestLibrary
from util.dynamiclibrary import DynamicApi


if __name__ == '__main__':
    from robotremoteserver import RobotRemoteServer

    _library = DynamicApi(AcceptanceTestLibrary(), False, False)
    RobotRemoteServer(_library, *sys.argv[1:])
