from .time_updater import TimeUpdater
import time
from typing import NewType

method = NewType('method', int)
positive_int = NewType('positive_int', int)

class VideoUpdater(TimeUpdater):
    __time_updater_boolean = False
    __signal_updater_boolean = False
    __time_updater_methods_dict = {}
    __signal_updater_methods_dict = {}

    def __init__(self, video_fps: float = 29.97, time_interval: positive_int = 0) -> None:
        super().__init__(time_interval)
        self.time_beetwen_frames = 1 / video_fps
            
    def start_time_updater(self) -> None:
        self.quit()
        self.__time_updater_boolean = True
        self.__signal_updater_boolean = False
        self.start()
    
    def stop_time_updater(self) -> None:
        self.quit()
        self.__time_updater_boolean = False
        ####Extremamente perigoso!, concertar isso
        now = time.time()
        while self.isFinished() == False and now + 0.2 > time.time():  
            continue
        
    def start_signal_updater(self) -> None:
        self.stop_time_updater()
        self.__time_updater_boolean = False
        self.__signal_updater_boolean = True
        self.start()
    
    def __run_time_updater(self) -> None:
        while self.__time_updater_boolean:
            start = time.time()
            for method in self.__time_updater_methods_dict.values():
                method()
            
            time.sleep(max(0, self.time_beetwen_frames - (time.time() - start)))
        
    
    def __run_signal_updater(self) -> None:
        [method() for method in self.__signal_updater_methods_dict.values()]
        self.quit()

    def run(self) -> None:
        if self.__time_updater_boolean:
            self.__run_time_updater()
        elif self.__signal_updater_boolean:
            self.__run_signal_updater()

    def add_method_on_timer_updater(self, methodKey: str, method_whitout_parameters: method) -> None:
        self.__time_updater_methods_dict[methodKey] = method_whitout_parameters
    
    def add_method_on_signal_updater(self, methodKey: str, method_whitout_parameters: method) -> None:
        self.__signal_updater_methods_dict[methodKey] = method_whitout_parameters
    
    def remove_method_from_time_updater(self, method_key: str) -> str:
        return self.__time_updater_methods_dict.pop(method_key)
    
    def remove_method_from_signal_updater(self, method_key: str) -> str:
        return self.__signal_updater_methods_dict.pop(method_key)