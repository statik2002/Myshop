def stat_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('launch before view')
        print(request.headers)
        print(request.scheme)
        print(request.body)
        print(request.path)
        print(request.path_info)
        print(request.method)
        print(request.encoding)
        print(request.content_type)
        print(request.content_params)
        print(request.GET)
        print(request.POST)
        print(request.COOKIES)
        print(request.META)

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print('launch after view')
        print(response)

        return response

    return middleware