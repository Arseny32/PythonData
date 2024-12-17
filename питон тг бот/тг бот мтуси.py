bot_token='7818687146:AAHeZdrqoXRXMhkMIVcnbH13TZ_UkkQnEbE'
URL = "https://api.telegram.org/bot%s/" #% BOT_TOKEN='7742537641:AAGFiPBr1osSD8l8f41wgltuDSApuy1AOb8'
MyURL = "https://example.com/hook"

api = requests.Session()
application = tornado.web.Application([
    (r"/", Handler),
])
if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_term_handler)
    try:
        set_hook = api.get(URL + "setWebhook?url=%s" % MyURL)
        if set_hook.status_code != 200:
            logging.error("Can't set hook: %s. Quit." % set_hook.text)
            exit(1)
        application.listen(8888)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        signal_term_handler(signal.SIGTERM, None)
