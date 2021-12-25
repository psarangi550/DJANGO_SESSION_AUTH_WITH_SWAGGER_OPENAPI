from rest_framework.pagination import PageNumberPagination

class EmployeePagination(PageNumberPagination):
    page_size=15
    page_size_query_params ="page_size"
    max_page_size=20

    