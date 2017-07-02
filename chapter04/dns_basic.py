#coding=utf-8

import argparse
# dnspython
import dns.resolver

def lookup(name):
    for qtype in 'A', 'AAA', 'CNAME', 'MX', 'NS':
        answer = resolver.query(name, qtype, raise_on_no_answer=Fasle)
        if answer.rrset is not None:
            print(answer.rrset)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolve a name using DNS')
    parser.add_argument('name', help='name that you want to look uo in DNS')
    lookup(parser.parse_args().name)