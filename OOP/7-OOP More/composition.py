# inheritance provides 'is-a' relation
# composition provides 'has-a' relation


class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        return "Engine Started"


class Driver:
    def __init__(self) -> None:
        pass


# Car Has an Engine
# Car Have Drives
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        print(self.engine.start())


toyota = Car()
toyota.start()
