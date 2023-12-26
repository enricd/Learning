package org.example;

public class Cat {

    String name;
    int age;

    public void meow() {
        System.out.println("Meoooow");
    }

    public static void staticMeow() {
        System.out.println("This Meooow can be accessed without creating and object, directly from the class itself!");
    }

}
