from singleton import Singleton


class StringUtils(metaclass=Singleton):
    @staticmethod
    def split_by(string, what_to_change):
        change = string.split(what_to_change)
        return change
