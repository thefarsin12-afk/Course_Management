from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

class CustomPagination(PageNumberPagination):

    page_size = 5

    page_query_param = "page_num"

class CustomLimitOffset(LimitOffsetPagination):

    default_limit = 5

    limit_query_param = "limit"

    offset_query_param = "offset"    