import java.util.Scanner;

public class DisneyWorldParkEvaluator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Which attraction are you most excited about?");
        System.out.println("1. Star Wars");
        System.out.println("2. Avatar");
        System.out.println("3. Tron");
        System.out.println("4. Guardians of the Galaxy");

        System.out.print("Enter the number of your choice: ");
        int choice = scanner.nextInt();

        String bestPark = "";

        switch (choice) {
            case 1:
                bestPark = "Hollywood Studios";
                break;
            case 2:
                bestPark = "Animal Kingdom";
                break;
            case 3:
                bestPark = "Magic Kingdom";
                break;
            case 4:
                bestPark = "Epcot";
                break;
            default:
                System.out.println("Invalid choice. Please enter a number between 1 and 4.");
                System.exit(0);
        }

        System.out.println("The best Disney World park for you is: " + bestPark);
    }
}