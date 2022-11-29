import sys

sys.path.append("/home/glo-saczkowski/TE_2.0/talent-eng")


class BaseProviderClass:
    """
    Rises error when there is no such method of providing data
    """

    @staticmethod
    def get(item_name: str):

        raise NotImplementedError("get method is not implemented")
