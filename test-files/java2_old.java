// Facade
class CPU {
    void start() { System.out.println("CPU started"); }
}

class Memory {
    void load() { System.out.println("Memory loaded"); }
}

class Disk {
    void read() { System.out.println("Disk read"); }
}

// Facade
class Computer {
    private CPU cpu = new CPU();
    private Memory memory = new Memory();
    private Disk disk = new Disk();

    void start() {
        cpu.start();
        memory.load();
        disk.read();
    }
}


