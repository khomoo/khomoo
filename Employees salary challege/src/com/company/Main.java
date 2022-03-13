package com.company;
import java.util.Scanner;

public class Main {

    public static void employeesSalaryChallenge() {
        //this line of code below allows the user to input the number of hours worked per week and the money made per hour this will allow us to calculate the employee's gross yearly salary
        Scanner input = new Scanner(System.in);
        System.out.println("Please input the number of hours the employee works per week");
        double hoursPerWeek = input.nextDouble();

        if (hoursPerWeek <= 0){
            System.out.println("Invalid working hours per week for an employee");
        }

        input = new Scanner(System.in);
        System.out.println("Please input the money the employee makes per hour");
        double moneyPerHour = input.nextDouble();

        if (moneyPerHour <= 0){
            System.out.println("Invalid money made per hour for an employee");
        }

        double weeklyPayCheck = hoursPerWeek * moneyPerHour;
        double grossYearlySalary = weeklyPayCheck * 52;
        System.out.print("This is the employee's gross yearly salary "+ grossYearlySalary+" without taking a vacation");


        System.out.println(" Now let us account for the days an employee might take for a vacation ");
        input = new Scanner(System.in);
        System.out.println("Please enter the number of vacation days that an employee might take");
        double vacationDays = input.nextDouble();


        double bonus = vacationDays * moneyPerHour * 8;
        double yearlyPayCheck = bonus - grossYearlySalary;
        System.out.println("Therefore the employee received: "+bonus+"bonus hours");
        System.out.println("This is the amount of money that the employee makes when he/she has taken a vacation"+ yearlyPayCheck+ "since they do not earn anything on vacations");


    }

    public static void main(String[] args) {
        // Now we are calling the employees salary challenge function in the main function so we can be able to run it
        employeesSalaryChallenge();

    }
}
