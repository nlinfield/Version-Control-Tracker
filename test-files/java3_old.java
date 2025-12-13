

    public class Singleton {

        private static Singleton instance;  // private static variable

        private Singleton() {} //make constructor private

        public static Singleton getInstance() {  //public static method to get the instance
            // creating it if it does not exist
            if (instance == null) {
                instance = new Singleton();
            }
            return instance;

        }

        public void test(){
            System.out.println("test");

        }



        public static void main(String[] args) {

//        Singleton s1 = Singleton.getInstance();
//        Singleton s2 = Singleton.getInstance();
//        System.out.println(s1 == s2);
//        s1.test();
//        s2.test();


//
//        Old o = new Old();
//        o.printOld();
//        New n = new Adapter(o);
//        n.print();


//        Subject subject = new Subject();
//        Observer o1 = new ConcreteObserver("1");
//        Observer o2 = new ConcreteObserver("2");
//        subject.addObserver(o1);
//        subject.addObserver(o2);
//        subject.notifyObservers("OLA");


//        Coffee coffee = new basicCoffee();
//        System.out.println(coffee.getDes());
//        System.out.println(coffee.getPrice());
//
//        coffee = new milk(coffee);
//        System.out.println(coffee.getDes());
//        System.out.println(coffee.getPrice());


//        Animal cat = Factory.getAnimal("cat");
//        Animal dog = Factory.getAnimal("dog");
//
//        cat.speak();
//        dog.speak();



//        UseIterator useIterator = new UseIterator();
//        useIterator.test();
//        useIterator.print();


//        Computer c = new Computer();
//        c.start();


//
//        Light light = new Light();
//        Remote remote = new Remote();
//
//        remote.setCommand(new LightOnCommand(light));
//        remote.pressButton();  // Light ON
//
//        remote.setCommand(new LightOffCommand(light));
//        remote.pressButton();



//         Chess c = new Chess();
//         c.play(g);


//            Composite root = new Composite();
//            root.add(new Leaf("A"));
//            root.add(new Leaf("B"));
//
//            Composite sub = new Composite();
//            sub.add(new Leaf("C"));
//
//            root.add(sub);
//
//            root.show();

        
    }
}