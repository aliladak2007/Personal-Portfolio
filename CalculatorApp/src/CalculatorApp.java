import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import java.util.ArrayList;

public class CalculatorApp extends Application {
    private TextField display;
    private double firstOperand = 0;
    private String operator = "";
    private boolean startNewInput = true;
    private ArrayList<String> history = new ArrayList<>();
    private ListView<String> historyView = new ListView<>();

    @Override
    public void start(Stage primaryStage) {
        // Setting up the display
        display = new TextField();
        display.setEditable(false);
        display.setPrefHeight(50);
        display.setStyle("-fx-font-size: 18px;");

        // Setting up the grid layout for buttons
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);

        // Add display to the grid
        grid.add(display, 0, 0, 5, 1);

        // Number buttons
        Button[] numberButtons = new Button[10];
        for (int i = 0; i < 10; i++) {
            final int num = i;
            numberButtons[i] = new Button(String.valueOf(i));
            numberButtons[i].setPrefSize(50, 50);
            numberButtons[i].setOnAction(e -> appendNumber(num));
        }

        // Operation buttons
        Button btnAdd = new Button("+");
        Button btnSubtract = new Button("-");
        Button btnMultiply = new Button("*");
        Button btnDivide = new Button("/");
        Button btnEquals = new Button("=");
        Button btnClear = new Button("C");
        Button btnDecimal = new Button(".");
        Button btnSin = new Button("sin");
        Button btnCos = new Button("cos");
        Button btnTan = new Button("tan");
        Button btnSinh = new Button("sinh");
        Button btnCosh = new Button("cosh");
        Button btnTanh = new Button("tanh");
        Button btnAsin = new Button("asin");
        Button btnAcos = new Button("acos");
        Button btnAtan = new Button("atan");
        Button btnLog = new Button("log");
        Button btnLn = new Button("ln");
        Button btnSqrt = new Button("√");
        Button btnExp = new Button("exp");
        Button btnPow = new Button("^");
        Button btnToggleSign = new Button("+/-");

        // Set button sizes
        Button[] ops = {btnAdd, btnSubtract, btnMultiply, btnDivide, btnEquals, btnClear, btnDecimal,
                btnSin, btnCos, btnTan, btnSinh, btnCosh, btnTanh,
                btnAsin, btnAcos, btnAtan, btnLog, btnLn, btnSqrt, btnExp, btnPow, btnToggleSign};
        for (Button btn : ops) {
            btn.setPrefSize(50, 50);
        }

        // Add number buttons to the grid
        grid.add(numberButtons[1], 0, 1);
        grid.add(numberButtons[2], 1, 1);
        grid.add(numberButtons[3], 2, 1);
        grid.add(numberButtons[4], 0, 2);
        grid.add(numberButtons[5], 1, 2);
        grid.add(numberButtons[6], 2, 2);
        grid.add(numberButtons[7], 0, 3);
        grid.add(numberButtons[8], 1, 3);
        grid.add(numberButtons[9], 2, 3);
        grid.add(numberButtons[0], 1, 4);

        // Add operation buttons to the grid
        grid.add(btnAdd, 3, 1);
        grid.add(btnSubtract, 3, 2);
        grid.add(btnMultiply, 3, 3);
        grid.add(btnDivide, 3, 4);
        grid.add(btnEquals, 2, 4);
        grid.add(btnClear, 0, 5);
        grid.add(btnDecimal, 1, 5);
        grid.add(btnSin, 0, 6);
        grid.add(btnCos, 1, 6);
        grid.add(btnTan, 2, 6);
        grid.add(btnSinh, 0, 7);
        grid.add(btnCosh, 1, 7);
        grid.add(btnTanh, 2, 7);
        grid.add(btnAsin, 0, 8);
        grid.add(btnAcos, 1, 8);
        grid.add(btnAtan, 2, 8);
        grid.add(btnLog, 0, 9);
        grid.add(btnLn, 1, 9);
        grid.add(btnSqrt, 2, 9);
        grid.add(btnExp, 3, 7);
        grid.add(btnPow, 3, 8);
        grid.add(btnToggleSign, 3, 9);

        // Add event handlers for operations
        btnAdd.setOnAction(e -> setOperator("+"));
        btnSubtract.setOnAction(e -> setOperator("-"));
        btnMultiply.setOnAction(e -> setOperator("*"));
        btnDivide.setOnAction(e -> setOperator("/"));
        btnEquals.setOnAction(e -> calculate());
        btnClear.setOnAction(e -> clear());
        btnDecimal.setOnAction(e -> appendDecimal());
        btnSin.setOnAction(e -> applyFunction("sin"));
        btnCos.setOnAction(e -> applyFunction("cos"));
        btnTan.setOnAction(e -> applyFunction("tan"));
        btnSinh.setOnAction(e -> applyFunction("sinh"));
        btnCosh.setOnAction(e -> applyFunction("cosh"));
        btnTanh.setOnAction(e -> applyFunction("tanh"));
        btnAsin.setOnAction(e -> applyFunction("asin"));
        btnAcos.setOnAction(e -> applyFunction("acos"));
        btnAtan.setOnAction(e -> applyFunction("atan"));
        btnLog.setOnAction(e -> applyFunction("log"));
        btnLn.setOnAction(e -> applyFunction("ln"));
        btnSqrt.setOnAction(e -> applyFunction("sqrt"));
        btnExp.setOnAction(e -> applyFunction("exp"));
        btnPow.setOnAction(e -> setOperator("^"));
        btnToggleSign.setOnAction(e -> toggleSign());

        // Set up the main layout
        BorderPane mainLayout = new BorderPane();
        mainLayout.setTop(display);
        mainLayout.setCenter(grid);
        mainLayout.setRight(historyView);

        // Set up the scene and stage
        Scene scene = new Scene(mainLayout, 600, 600);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Scientific Calculator");
        primaryStage.show();
    }

    // Main method to launch the application
    public static void main(String[] args) {
        launch(args);
    }

    private void appendNumber(int number) {
        if (startNewInput) {
            display.clear();
            startNewInput = false;
        }
        display.appendText(String.valueOf(number));
    }

    private void setOperator(String op) {
        if (!display.getText().isEmpty()) {
            try {
                firstOperand = Double.parseDouble(display.getText());
                operator = op;
                startNewInput = true;
            } catch (NumberFormatException e) {
                display.setText("Error");
                clear();
            }
        }
    }

    private void applyFunction(String func) {
        if (!display.getText().isEmpty()) {
            try {
                double value = Double.parseDouble(display.getText());
                double result;
                switch (func) {
                    case "sin" -> result = Math.sin(Math.toRadians(value));
                    case "cos" -> result = Math.cos(Math.toRadians(value));
                    case "tan" -> result = Math.tan(Math.toRadians(value));
                    case "sinh" -> result = Math.sinh(value);
                    case "cosh" -> result = Math.cosh(value);
                    case "tanh" -> result = Math.tanh(value);
                    case "asin" -> result = Math.toDegrees(Math.asin(value));
                    case "acos" -> result = Math.toDegrees(Math.acos(value));
                    case "atan" -> result = Math.toDegrees(Math.atan(value));
                    case "log" -> result = Math.log10(value);
                    case "ln" -> result = Math.log(value);
                    case "sqrt" -> result = Math.sqrt(value);
                    case "exp" -> result = Math.exp(value);
                    default -> result = 0;
                }
                display.setText(String.valueOf(result));
                addHistory(func + "(" + value + ") = " + result);
                startNewInput = true;
            } catch (NumberFormatException e) {
                display.setText("Error");
                clear();
            }
        }
    }

    private void calculate() {
        if (!display.getText().isEmpty() && !operator.isEmpty()) {
            try {
                double secondOperand = Double.parseDouble(display.getText());
                double result = 0;

                switch (operator) {
                    case "+":
                        result = firstOperand + secondOperand;
                        break;
                    case "-":
                        result = firstOperand - secondOperand;
                        break;
                    case "*":
                        result = firstOperand * secondOperand;
                        break;
                    case "/":
                        if (secondOperand != 0) {
                            result = firstOperand / secondOperand;
                        } else {
                            display.setText("Error");
                            clear();
                            return; // Exit the method when division by zero occurs
                        }
                        break;
                    case "^":
                        result = Math.pow(firstOperand, secondOperand);
                        break;
                    default:
                        display.setText("Error");
                        clear();
                        return; // Exit if the operator is invalid
                }

                display.setText(String.valueOf(result));
                addHistory(firstOperand + " " + operator + " " + secondOperand + " = " + result);
                operator = "";
                startNewInput = true;
            } catch (NumberFormatException e) {
                display.setText("Error");
                clear();
            }
        }
    }

    private void addHistory(String entry) {
        history.add(entry);
        historyView.getItems().setAll(history);
    }

    private void clear() {
        display.clear();
        firstOperand = 0;
        operator = "";
        startNewInput = true;
    }

    private void appendDecimal() {
        if (startNewInput) {
            display.clear();
            startNewInput = false;
        }
        if (!display.getText().contains(".")) {
            display.appendText(".");
        }
    }

    private void toggleSign() {
        if (!display.getText().isEmpty() && !display.getText().equals("Error")) {
            double value = Double.parseDouble(display.getText());
            value = -value;
            display.setText(String.valueOf(value));
        }
    }
}
