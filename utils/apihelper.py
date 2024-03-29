import functools


def validate_serializer(serializer):
    '''data checker'''
    def validate(view_method):
        @functools.wraps(view_method)
        def handle(*args, **kwargs):
            self = args[0]
            request = args[1]
            seri = serializer(data=request.data)
            if seri.is_valid():
                request.data = seri.data
                request.serializer = seri
                return view_method(*args, **kwargs)
            else:
                return self.invalid_serializer(seri)

        return handle

    return validate


def FormatResponse(data=None):
    return {"error": None, "data": data}
