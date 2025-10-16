class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores


class RAM:
    def __init__(self, size) -> None:
        self.size = size


class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity


# Computer has a CPU
# Computer has a Ram
# Computer has a Hard Drive
class Computer:
    def __init__(self, cpu, ram, hard_drive) -> None:
        self.cpu = CPU(cpu)
        self.ram = RAM(ram)
        self.hard_drive = HardDrive(hard_drive)

    def __repr__(self) -> str:
        return (
            f"This Computer has {self.cpu.cores} cores and {self.ram.size} ram"
            f" with {self.hard_drive.capacity} capacity of hard drive."
        )


linux = Computer(7, 4, 500)
print(linux)
