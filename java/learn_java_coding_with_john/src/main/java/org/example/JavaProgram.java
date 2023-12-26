package org.example;

public class JavaProgram {

    public static void main(String[] args) {

        int myInt = 7;
        double shoeSize = 9.5;
        char myInitial = 'J';

        String myName = "John";

        System.out.println(myName.length());

        double result = myInt * shoeSize;

        System.out.println(myInt * shoeSize);

        printName("Enric", 3);

        String name = getName("Enric", 3);

        for (int i = 0; i < 5; i++) {
            System.out.println("I'm in the loop!");
        }

        Cat myCat = new Cat();
        myCat.name = "Fred";
        myCat.age = 6;

        Cat anotherCat = new Cat();
        anotherCat.name = "Stella";
        anotherCat.age = 8;

        System.out.println(myCat.name);

        Cat.staticMeow();
        myCat.staticMeow();

    }

    private static void printName(String name, int number) {
        System.out.println("My name is " + name);
    }

    private static String getName(String name, int number) {

        if (name.equals("John") & number == 3) {
            System.out.println("This guy is awesome");
        }
        else if (name.equals("Enric")) {
            System.out.println("Hello " + name);
        }
        else {
            System.out.println("I don't know this guy");
        }

        return "My name is " + name;
    }

}