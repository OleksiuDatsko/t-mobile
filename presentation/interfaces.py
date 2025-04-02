from abc import ABC, abstractmethod


class IConsoleInterface(ABC):
    @abstractmethod
    def show_menu(self):
        pass
