""" Module: urls

URLs for the Tornado handlers.

"""
import tornado.web

url_patterns = [
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "/var/www"}),
        (r"/", tornado.web.RedirectHandler, {"url": "/static/summary.pdf"}),
        ]
