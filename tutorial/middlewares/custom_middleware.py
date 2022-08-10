from django.utils.deprecation import MiddlewareMixin


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('before: {{{{{{{ simple_middleware }}}}}}}', request)
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print('after: <<<<<<<< simple_middleware >>>>>>>>', response)
        return response

    return middleware


class MyMiddleware:

    def __init__(self, next_layer=None):
        """We allow next_layer to be None because old-style middlewares
        won't accept any argument.
        """
        print('__init__')
        self.get_response = next_layer

    def process_request(self, request):
        """Let's handle old-style request processing here, as usual."""
        print('process_request')
        # Do something with request
        # Probably return None
        # Or return an HttpResponse in some cases

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('process_view')

    def process_response(self, request, response):
        """Let's handle old-style response processing here, as usual."""
        print('process_response')
        # Do something with response, possibly using request.
        return response

    def __call__(self, request):
        """Handle new-style middleware here."""
        print('__call__')
        response = self.process_request(request)
        if response is None:
            print('response is None')
            # If process_request returned None, we must call the next middleware or
            # the view. Note that here, we are sure that self.get_response is not
            # None because this method is executed only in new-style middlewares.
            response = self.get_response(request)
        print('out side of if')
        response = self.process_response(request, response)
        return response

class MyMiddleware2:

    def __init__(self, next_layer=None):
        """We allow next_layer to be None because old-style middlewares
        won't accept any argument.
        """
        print('MyMiddleware2: __init__')
        self.get_response = next_layer

    def process_request(self, request):
        """Let's handle old-style request processing here, as usual."""
        print('MyMiddleware2: process_request')
        # Do something with request
        # Probably return None
        # Or return an HttpResponse in some cases

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('MyMiddleware2: process_view')

    def process_response(self, request, response):
        """Let's handle old-style response processing here, as usual."""
        print('MyMiddleware2: process_response')
        # Do something with response, possibly using request.
        return response

    def __call__(self, request):
        """Handle new-style middleware here."""
        # print('MyMiddleware2: __call__')
        response = self.process_request(request)
        if response is None:
            print('MyMiddleware2: response is None')
            # If process_request returned None, we must call the next middleware or
            # the view. Note that here, we are sure that self.get_response is not
            # None because this method is executed only in new-style middlewares.
            response = self.get_response(request)
        print('MyMiddleware2: out side of if')
        response = self.process_response(request, response)
        return response
