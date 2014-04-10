import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, WebApp Worldzz!')

app = webapp2.WSGIApplication([('/', MainPage)])