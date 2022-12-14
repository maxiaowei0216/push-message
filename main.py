import argparse

from server.qywx import QYWX
from server.server import Server


def push_msg(obj: Server, msg: str):
    obj.push(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', type=str, help="Specify which server to be used to push message.")
    parser.add_argument('-m', '--message', help='Message')

    args = parser.parse_args()

    if args.server.upper() == 'QYWX':
        s = QYWX()
    else:
        s = Server()

    push_msg(s, args.message)
