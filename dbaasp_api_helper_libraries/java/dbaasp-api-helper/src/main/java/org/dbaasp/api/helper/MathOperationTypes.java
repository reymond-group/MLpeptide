package org.dbaasp.api.helper;

/**
 * Created by mindia on 4/29/16.
 */
public enum MathOperationTypes {

    EQUALS("="),
    GREATER(">"),
    LESS("<"),
    EQUALS_OR_LESS("<="),
    EQUALS_OR_GREATER(">=");

    public static String getAll() {
        return EQUALS.getOperation() + "," + GREATER.getOperation() + "," + LESS.getOperation() + "," + EQUALS_OR_LESS.getOperation() + "," + EQUALS_OR_GREATER.getOperation();
    }

    private String operation;

    MathOperationTypes(String operation) {
        this.operation = operation;
    }

    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public static MathOperationTypes getByName(String name) {

        for (MathOperationTypes type : MathOperationTypes.values()) {
            if (type.getOperation().equals(name)) {
                return type;
            }
        }
        return null;
    }
}
