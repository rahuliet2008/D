import numpy as np
import logging as log

def print_indexed_names(servers):
    for server in servers:
        print(server[0])

def ask_index(max_index):
    """ask the user for an index and you might sanitize using exception handling"""
    try:
        max_index=int(input("please enter max index: "))
        return max_index # fixture
    except ValueError as e:
        log.error(e)


def print_properties(index, servers):
    try:
        data=servers[index]
        print("name:"+data[0])
        print("IP:"+data[1]+" DNS:"+data[2])
    except IndexError as e:
        log.error(e)

def main():
    log.basicConfig(level=log.INFO)
    servers = [ ["Amsterdam", '192.168.178.3', '255.255.255.0'],
                ["Tokyo", '192.168.178.8', '255.255.255.0'],
                ["Paris",  '192.168.178.12', '255.255.255.0'],
                ["Helsinki",  '192.168.178.145', '255.255.255.0'],
                ["Brussel",  '192.168.178.12', '255.255.255.0']]

    print_indexed_names(servers)
    max_index = 0 # fixture
    index = ask_index(max_index)
    print_properties(index, servers)

if __name__ == "__main__":
    main()