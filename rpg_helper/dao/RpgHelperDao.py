import abc
import logging
from typing import List
from rpg_helper.models.Inventory import Inventory
InventoryList = List[Inventory]

class RpgHelperDao(metaclass=abc.ABCMeta):
    def __init__(self):
        self.data = []

    @abc.abstractmethod
    def add_inventory(self, user: str, user_id: str, channel_id: str, item: str):
        logging.error(msg='This is not implemented')
        pass

    @abc.abstractmethod
    def get_user_inventory(self, user_id: str, channel_id: str) -> InventoryList:
        logging.error(msg='This is not implemented')
        pass

    @abc.abstractmethod
    def remove_inventory(self, channel_id: str, user_id: str, item: str):
        logging.error(msg='This is not implemented')
        pass

    @abc.abstractmethod
    def add_stat(self, channel_id: str, user_id: str, stat_name: str, value: int):
        logging.error(msg='This is not implemented')
        pass

    @abc.abstractmethod
    def update_stat(self, channel_id: str, user_id: str, statname: str, value: int):
        logging.error(msg='This is not implemented')
        pass

    @abc.abstractmethod
    def remove_stat(self, channel_id: str, user_id: str, stat_name: str):
        logging.error(msg='This is not implemented')
        pass
