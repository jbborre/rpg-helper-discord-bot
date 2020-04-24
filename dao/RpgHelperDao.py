import abc


class RpgHelperDao(metaclass=abc.ABCMeta):
    def __init__(self):
        self.data = []

    @abc.abstractmethod
    def add_inventory(self, user: str, channel: str, item: str):
        print('This is not implemented')
        pass

    @abc.abstractmethod
    def remove_inventory(self, user: str, item: str):
        print('This is not implemented')
        pass

    @abc.abstractmethod
    def add_stat(self, user: str, statName: str, value: int):
        print('This is not implemented')
        pass

    @abc.abstractmethod
    def update_stat(self, user: str, statName: str, value: int):
        print('This is not implemented')
        pass

    @abc.abstractmethod
    def remove_stat(self, user: str, statName: str):
        print('This is not implemented')
        pass
