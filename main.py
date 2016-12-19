#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Database import Database
import urllib.request, argparse, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', help='Database hostname', type=str, default='localhost')
    parser.add_argument('-u', '--username', help='Database user', type=str, required=True)
    parser.add_argument('-p', '--password', help='User password', type=str)
    parser.add_argument('-P', '--port', help='Database port', type=str, default='3306')
    parser.add_argument('-d', '--database', help='Database name', type=str, required=True)
    parser.add_argument('-D', '--directory', help='Output folder', type=str, default='output')
    parser.add_argument('-T', '--table', help='Database table name', type=str, required=True)
    parser.add_argument('-C', '--column', help='Table column name', type=str, required=True)
    args = parser.parse_args()
    db = Database(args.username, args.password, args.host, args.port, args.database)
    if not os.path.exists(args.directory):
        os.makedirs(args.directory)
    path = args.directory + '/'
    for link in db.get_link(args.table, args.column):
        try:
            urllib.request.urlretrieve(link, path+link.split('/')[-1])
        except:
            print ('Failed to open : {}'.format(link))

if __name__ == '__main__':
        main()
