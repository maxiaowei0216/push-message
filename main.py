import argparse

from server.qywx import QYWX
from server.server import Server


def push_msg(obj: Server, msg: str):
    obj.push(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('server', type=str, help="Specify which server to be used to push message.")
    parser.add_argument('-m', help='Message')

    args = parser.parse_args()
    server: str = args.server

    if server.upper() == 'QYWX':
        s = QYWX()
    else:
        s = Server()

    push_msg(s, args.m)
