#!/usr/bin/python3

"""A tiny Python program to check that httpd is running.
Try running this program from the command line like this:
  python3 check_webserver.py
"""
import subprocess

def checkhttpd():
    try:
        cmd = 'ps -A | grep httpd'
        subprocess.run(cmd, check=True, shell=True)

    except subprocess.CalledProcessError:
        print("Please wait while we start the apache server")
        try:
            start_server = """#!/bin/bash
              sudo yum install httpd -y
              sudo systemctl enable httpd
              sudo service httpd start"""

            subprocess.run(start_server, check=True, shell=True)
            print("Serevr is now running please check webserver ip address")

        except subprocess.CalledProcessError:
            print("Something went wrong and the web server did not start")




# Define a main() function.
def main():
    checkhttpd()


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()