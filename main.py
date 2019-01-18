import tornado.ioloop
import tornado.web

import jwt

# TODO create a secret
SECRET = ""


class AcquireHandler(tornado.web.RequestHandler):
    def get(self):
        unit_id = self.get_argument("unit_id")
        # unit_secret = self.get_argument("unit_secret")

        token = jwt.encode(
            {
                "unit_id": unit_id
            },
            SECRET,
            algorithm="HS256"
        )
        token = token.decode("utf-8")
        print("Token generated: %s" % token)

        self.write({"token": token})


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/acquire", AcquireHandler)
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
