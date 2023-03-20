from typing import NewType
from PyQt6.QtCore import QThread

method = NewType('method', int)

class Updater(QThread):
    __methods_dict = {}

    def __init__(self) -> None:
        super().__init__()
        """Executes the methods added to it when runed."""
    
    def run(self)-> None:
        [method() for method in self.__methods_dict.values()]
        self.quit()

    def add_method_on_timer_updater(self, methodKey: str, method_whitout_parameters: method) -> None:
        self.__methods_dict[methodKey] = method_whitout_parameters

    def remove_method(self, method_key: str) -> str:
        return self.__methods_dict.pop(method_key)

    def start_updater(self)-> None:
        self.start()



