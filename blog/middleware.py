import json
import logging

from django.utils.deprecation import MiddlewareMixin
from django.http.response import JsonResponse

logg = logging.getLogger("second_logger")

class UserActivityMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        meta_headers = request.META
        request_dictionary = None
        request_method = request.method
        path_info = meta_headers.get('PATH_INFO')
        view_function = str(view_func)
        view_arguments = str(view_args)
        view_keyword_arguments = str(view_kwargs)
        remote_address = meta_headers.get('REMOTE_ADDR')
        if request.method == 'GET':
            request_dictionary = request.GET
        if request.method == 'POST':
            request_dictionary = dict(request.POST)
        log_message = "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(
            "[PATH_URL]", path_info, 
            "[request_method]".upper(), request_method,
            "[view_function]".upper(), view_function,
            "[view_arguments]".upper(), view_arguments,
            "[view_keyword_arguments]".upper(), view_keyword_arguments,
            "[remote_address]".upper(), remote_address,
            "[meta_headers]".upper(), meta_headers, 
            "[request_dictionary]".upper(), request_dictionary)
        logg.info(log_message)
        