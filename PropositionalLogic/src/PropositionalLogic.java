import java.util.Scanner;
import java.util.Stack;
import java.util.ArrayList;
import java.util.HashMap;

public class PropositionalLogic {

    // Logical operations
    public static boolean and(boolean a, boolean b) {
        return a && b;
    }

    public static boolean or(boolean a, boolean b) {
        return a || b;
    }

    public static boolean not(boolean a) {
        return !a;
    }

    public static boolean implication(boolean a, boolean b) {
        return !a || b;
    }

    public static boolean biconditional(boolean a, boolean b) {
        return a == b;
    }

    // Method to evaluate postfix expression
    public static boolean evaluatePostfix(String[] postfix, boolean[] values, HashMap<String, Integer> variableMap) {
        Stack<Boolean> stack = new Stack<>();
        for (String token : postfix) {
            if (variableMap.containsKey(token)) {
                stack.push(values[variableMap.get(token)]);
            } else {
                switch (token) {
                    case "AND":
                        stack.push(and(stack.pop(), stack.pop()));
                        break;
                    case "OR":
                        stack.push(or(stack.pop(), stack.pop()));
                        break;
                    case "NOT":
                        stack.push(not(stack.pop()));
                        break;
                    case "->":
                        boolean right = stack.pop();
                        boolean left = stack.pop();
                        stack.push(implication(left, right));
                        break;
                    case "<->":
                        stack.push(biconditional(stack.pop(), stack.pop()));
                        break;
                    default:
                        System.out.println("Invalid token in expression: " + token);
                        return false;
                }
            }
        }
        return stack.pop();
    }

    // Convert infix to postfix using Shunting Yard Algorithm
    public static String[] infixToPostfix(String expression) {
        ArrayList<String> output = new ArrayList<>();
        Stack<String> operators = new Stack<>();
        String[] tokens = expression.split(" ");

        for (String token : tokens) {
            if (token.matches("[A-Z]")) { // Matches any variable (A, B, C, ...)
                output.add(token);
            } else if (token.equals("AND") || token.equals("OR") || token.equals("->") || token.equals("<->")) {
                while (!operators.isEmpty() && precedence(operators.peek()) >= precedence(token)) {
                    output.add(operators.pop());
                }
                operators.push(token);
            } else if (token.equals("NOT")) {
                operators.push(token);
            } else if (token.equals("(")) {
                operators.push(token);
            } else if (token.equals(")")) {
                while (!operators.isEmpty() && !operators.peek().equals("(")) {
                    output.add(operators.pop());
                }
                if (!operators.isEmpty() && operators.peek().equals("(")) {
                    operators.pop();
                }
            }
        }

        while (!operators.isEmpty()) {
            output.add(operators.pop());
        }

        return output.toArray(new String[0]);
    }

    // Define precedence for logical operators
    public static int precedence(String operator) {
        switch (operator) {
            case "NOT" -> {
                return 3;
            }
            case "AND" -> {
                return 2;
            }
            case "OR" -> {
                return 1;
            }
            case "->", "<->" -> {
                return 0;
            }
            default -> {
                return -1;
            }
        }
    }

    // Generate and print the truth table for the expression
    public static void generateTruthTable(String expression, int numVariables) {
        // Map variables to indices (e.g., A -> 0, B -> 1, etc.)
        HashMap<String, Integer> variableMap = new HashMap<>();
        for (int i = 0; i < numVariables; i++) {
            variableMap.put(String.valueOf((char) ('A' + i)), i);
        }

        // Convert infix to postfix
        String[] postfix = infixToPostfix(expression);

        // Generate combinations for the truth values based on the number of variables
        int rows = (int) Math.pow(2, numVariables);
        boolean[][] table = new boolean[rows][numVariables];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < numVariables; j++) {
                table[i][j] = (i / (int) Math.pow(2, numVariables - j - 1)) % 2 == 0;
            }
        }

        // Print the table header
        StringBuilder header = new StringBuilder();
        for (int i = 0; i < numVariables; i++) {
            header.append((char) ('A' + i)).append("\t");
        }
        header.append("Result");
        System.out.println(header);

        // Print a separator line
        for (int i = 0; i < header.length(); i++) {
            System.out.print("-");
        }
        System.out.println();

        // Evaluate the expression for each row and print the result
        for (boolean[] row : table) {
            StringBuilder rowStr = new StringBuilder();
            for (boolean value : row) {
                rowStr.append(value ? "T" : "F").append("\t");
            }
            boolean result = evaluatePostfix(postfix, row, variableMap);
            rowStr.append(result ? "T" : "F");
            System.out.println(rowStr);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a logical expression (e.g., '( A AND B ) OR C' or 'A -> ( B AND C )'):");
        String expression = scanner.nextLine();

        System.out.println("Enter the number of variables in your expression (e.g., 2 for A, B):");
        int numVariables = scanner.nextInt();

        // Generate and print the truth table for the given expression
        generateTruthTable(expression, numVariables);
    }
}
