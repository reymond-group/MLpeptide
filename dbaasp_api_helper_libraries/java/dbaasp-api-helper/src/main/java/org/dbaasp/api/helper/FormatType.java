package org.dbaasp.api.helper;

/**
 * Created by mindia on 4/6/16.
 */
public enum FormatType {

    XML("xml"),
    JSON("json"),
    FASTA("fasta"),
    TAB("tab");

    private String name;

    FormatType(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public static FormatType getByName(String name) {

        for (FormatType type : FormatType.values()) {
            if (type.getName().equals(name)) {
                return type;
            }
        }
        return null;
    }
}
