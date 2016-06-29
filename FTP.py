#/usr/bin/python

from ftplib import FTP
import ftplib
import sys
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-a","--address",dest="address",help="REMOTE FTP HOST",metavar="REMOTE FTP HOST")
parser.add_option("-r","--remote_file",dest="remote_file",help="REMOTE FILE NAME to download",metavar="REMOTE FILE NAME")
parser.add_option("-l","--local_file",dest="local_file",help="LOCAL FILE NAME to save remote file",metavar="LOCAL FILE NAME")
parser.add_option("-u","--username",dest="username",help="USERNAME",metavar="USERNAME")
parser.add_option("-p","--password",dest="password",help="PASSWORD",metavar="PASSWORD")

(options,args) = parser.parse_args()

if not (options.remote_file and options.local_file and options.address):
    parser.error('REMOTE HOST,LOCAL FILE NAME,' \
            'and REMOTE FILE NAME are Mandatory')

if options.username and not options.password:
    parser.error('PASSWORD is mandatory if USERNAME is present')

ftp = FTP(options.address)
if options.username:
    try:
        ftp.login(options.username,options.password)
    except ftplib.error_perm, e:
        print "Login Failed: %s" % e
        sys.exit(1)
else:
    try:
        ftp.login()
    except ftplib.error_perm,e:
        print "Anonymous Login Failed: %s" % e
        sys.exit(1)

try:
    local_file = open(options.local_file,'wb')
    ftp.retrbinary('RETR %s' % options.remote_file,local_file.write)
finally:
    local_file.close()
    ftp.close()


