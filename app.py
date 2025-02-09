from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess, sys

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # run df -h and put in output
        dfout = subprocess.check_output(["df", "-h"])
        self.wfile.write(dfout)
        #run free -h and put in output
        dfout = subprocess.check_output(["free", "-h"])
        self.wfile.write("**********\n".encode())
        self.wfile.write("Memory stats:\n".encode())
        self.wfile.write(dfout)
        self.wfile.write("**********\n".encode())
        #run ps -aef and put in output
        dfout = subprocess.check_output(["ps", "-aef"])
        self.wfile.write("List of running processes:\n".encode())
        self.wfile.write(dfout)
        self.wfile.write("**********\n".encode())
        #run lsblk and put in output
        dfout = subprocess.check_output(["lsblk"])
        self.wfile.write("List of Block devices:\n".encode())
        self.wfile.write(dfout)
        self.wfile.write("**********\n".encode())
        self.wfile.write(b'''
          ##         .
    ## ## ##        ==
 ## ## ## ## ##    ===
/"""""""""""""""""\___/ ===
{                       /  ===-
\______ O           __/
 \    \         __/
  \____\_______/


Hello from Docker!
''')

def run():
    print('Starting server...')
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print('Server started!')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
