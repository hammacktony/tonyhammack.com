''' Load User Middleware'''


class MiddlewareTest:
    ''' Middleware class which loads the current user into the request '''

    def __init__(self, Request):
        ''' Inject Any Dependencies From The Service Container '''
        self.request = Request

    def before(self):
        ''' Run This Middleware Before The Route Executes '''
        print('running before')
        self.request.path = 'test/middleware/before/ran'
        print('request path', self.request.path)

    def after(self):
        ''' Run This Middleware After The Route Executes '''
        pass

    def load_user(self, request):
        ''' Load user into the request '''
        request.set_user(Auth(request).user())
