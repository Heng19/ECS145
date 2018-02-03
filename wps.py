
# client for the server for remote versions of the w and ps commands
# user can check load on machine without logging in (or even without
# having an account on the remote machine)
# usage:
# python wps.py remotehostname port_num {w,ps}
# e.g. python wps.py nimbus.org 8888 w would cause the server at
# nimbus.org on port 8888 to run the UNIX w command there, and send the
# output of the command back to the client here
import socket,sys

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = sys.argv[1]
    port = int(sys.argv[2])
    s.connect((host,port))
    # send w or ps command to server
    s.send(sys.argv[3])

    # create "file-like object" flo
    flo = s.makefile('r',0) # read-only, unbuffered
    # now can call readlines() on flo, and also use the fact that
    # that stdout is a file-like object too
    sys.stdout.writelines(flo.readlines())

if __name__ == '__main__':
    main()
