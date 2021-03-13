package org.dbaasp.api.helper;

/**
 * Created by mindia on 7/3/16.
 */
public enum Complexity {

    MONOMER("monomer"),
    DIMER("dimer"),
    TWO_PEPTIDE("two_peptide");

    private String complexity;


    public static Complexity getByName(String name) {
        for (Complexity complexityMap : Complexity.values()) {
            if (complexityMap.getComplexity().equals(name)) {
                return complexityMap;
            }
        }
        return null;
    }

    Complexity(String complexity) {
        this.complexity = complexity;
    }

    public String getComplexity() {
        return complexity;
    }

    public void setComplexity(String complexity) {
        this.complexity = complexity;
    }
}
