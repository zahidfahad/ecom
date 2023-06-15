from rest_framework.exceptions import APIException

class APIERROR(APIException):
    status_code = 400
    default_code = 400
    default_detail = 'Error'