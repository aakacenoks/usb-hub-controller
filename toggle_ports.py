import brainstem
from datetime import datetime
from brainstem.result import Result

import sys
import argparse


class ArgumentParser(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._port = None
        self._enable = None
        self._output = sys.stderr

    @property
    def port(self):
        return self._port

    @property
    def enable(self):
        return self._enable

    def print_usage(self):
        return self._parser.print_usage(self._output)

    def print_help(self):
        return self._parser.print_help(self._output)

    def parse_arguments(self, args):
        self._parser.add_argument("-p", "--port", help="Port to enable/disable", type=int, metavar='',
                                  choices={0, 1, 2, 3, 4, 5, 6, 7})
        self._parser.add_argument("-e", "--enable", help="Enable(True)/Disable(False) ", type=eval, metavar='',
                                  choices={True, False})
        args = self._parser.parse_args(args[1:])
        self._port = args.port
        if args.enable is None:
            raise Exception("Please specify --enable=True or --enable=False")
        else:
            self._enable = args.enable


def log(message):
    dt = datetime.now()
    timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
    print("[" + timestamp + "] " + str(message))


def toggle_port(stem, enable, port):
    if enable:
        log("Enabling port " + str(port))
        stem.usb.setPortEnable(port)
    else:
        log("Disabling port " + str(port))
        stem.usb.setPortDisable(port)


def main(argv):
    try:
        log(argv)
        args = ArgumentParser()
        if args.parse_arguments(argv):
            return 1

        stem = brainstem.stem.USBHub3p()
        result = stem.discoverAndConnect(1)

        if result == Result.NO_ERROR:
            if args.port is None:
                for port in range(0, 8):
                    toggle_port(stem, args.enable, port)
            else:
                toggle_port(stem, args.enable, args.port)
        else:
            log("Error Connecting to USBHub3p(). Make sure you are using the correct module object")
        stem.disconnect()
        log("Done.")

    except IOError as e:
        log("Exception - IOError: ", e)
        return 2
    except SystemExit as e:
        return 3
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
