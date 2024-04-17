from rest_framework.pagination import PageNumberPagination


class ListPaginator(PageNumberPagination):
    page_size = 4  # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания количества элементов на странице
    max_page_size = 4  # Максимальное количество элементов на странице
