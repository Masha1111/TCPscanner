import sys
import socket
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", type=str, help="начало диапазона")
    parser.add_argument("-e", type=str, help="конец диапазона")
    return parser.parse_args()


def scan(start, end):
    ports = []
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            try:
                sock.connect(('ns.e1.ru', port))
                ports.append(port)
            except socket.timeout or socket.error:
                pass
    return ports


if __name__ == "__main__":
    args = get_args()
    try:
        start = int(args.s)
        end = int(args.e)
    except:
        sys.exit("Некорректный ввод")
    if end < start:
        sys.exit("Некорректный ввод")
    ports = scan(start, end)
    if not ports == []:
        print("Активные порты:")
        for el in ports:
            print(str(el))
