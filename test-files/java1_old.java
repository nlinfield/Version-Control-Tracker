import java.util.*;

interface Component {s
    void show();
}



class Leaf implements Component {
    private String name;
    Leaf(String n)
    {
        name = n;
    }

    public void show() {
        System.out.println(name);
    }
}



class Composite implements Component {
    private List<Component> children = new ArrayList<>();

    void add(Component c) { children.add(c); }

    public void show() {
        for (Component c : children) {
            c.show();
        }
    }
}
