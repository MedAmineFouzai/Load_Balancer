from tornado import web,ioloop
import os
class main_request_handler(web.RequestHandler):
    def get(self):
        self.write(f'you are served from server 1 with process {os.getpid()}')
    
def main():
    return web.Application([
        (r'/served',main_request_handler)
    ]) 

if __name__ == "__main__":
    app=main()
    print('listening on port 1111')
    app.listen(1111)
    ioloop.IOLoop.current().start()