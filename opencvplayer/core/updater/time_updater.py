import time
from typing import NewType
from .updater import Updater

positive_int = NewType('positive_int', int)

class TimeUpdater(Updater):
    run_updater = False

    def __init__(self, time_interval: positive_int = 1) -> None:
        super().__init__()
        """Executes the methods in a loop with a time interval in seconds."""
        self.time_interval = time_interval
    
    def run(self)-> None:
        while self.run_updater:
            for method in self.__methods_dict.values():
                method()
            time.sleep(self.time_interval)

    def start_updater(self)-> None:
        self.run_updater = True
        self.start()
    
    def stop_updater(self)-> None:
        self.run_updater = False
        self.quit()
    
    def set_time_interval(self, time_interval: positive_int)-> None:
        self.time_interval = time_interval

