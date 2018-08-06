import java.util.Scanner;
public class test{
    public static void main(String[] args) {
        System.out.print("This is a test.");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Pleasr enter your name");
        String name = scanner.next();
        System.out.printf("Hello %s\n",name);
    }
}