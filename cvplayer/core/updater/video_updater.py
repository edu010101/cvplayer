from .time_updater import TimeUpdater
import time
import queue
from typing import NewType

method = NewType('method', int)
positive_int = NewType('positive_int', int)

class VideoUpdater(TimeUpdater):
    __time_updater_boolean = False
    __signal_updater_boolean = False
    __running = False

    def __init__(self, video_fps: float = 29.97, time_interval: positive_int = 0) -> None:
        super().__init__(time_interval)
        self.tasks_queue = queue.Queue()
        self.time_beetwen_frames = 1 / video_fps
        self.__time_updater_methods_dict = {}
        self.__signal_updater_methods_dict = {}

    def add_task(self, task) -> None:
        if self.__running == False:
            self.tasks_queue.put(task)
            self.start()
        elif self.__running == True:
            self.tasks_queue.put(task)
        
    def start_signal_updater(self) -> None:
        self.__time_updater_boolean = False
        self.__signal_updater_boolean = True
        self.add_task( self.__signal_updater_methods_dict)
    
    def start_time_updater(self) -> None:
        self.__time_updater_boolean = True
        self.__signal_updater_boolean = False
        self.add_task( self.__time_updater_methods_dict)

    def stop_time_updater(self) -> None:
        self.__time_updater_boolean = False

    def run(self) -> None:
        self.__running = True
        while self.tasks_queue.empty() == False:
            task = self.tasks_queue.get()
            for task_method in task.values():
                task_method()
            if self.__time_updater_boolean:
                start = time.time()
                self.tasks_queue.put( self.__time_updater_methods_dict)
                time.sleep(max(0, self.time_beetwen_frames - (time.time() - start)))
        self.__running = False

    def add_method_on_timer_updater(self, methodKey: str, method_whitout_parameters: method) -> None:
        self.__time_updater_methods_dict[methodKey] = method_whitout_parameters
    
    def add_method_on_signal_updater(self, methodKey: str, method_whitout_parameters: method) -> None:
        self.__signal_updater_methods_dict[methodKey] = method_whitout_parameters
    
    def remove_method_from_time_updater(self, method_key: str) -> str:
        return self.__time_updater_methods_dict.pop(method_key)
    
    def remove_method_from_signal_updater(self, method_key: str) -> str:
        return self.__signal_updater_methods_dict.pop(method_key)

    def is_time_updater_running(self) -> bool:
        return self.__time_updater_boolean