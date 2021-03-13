package org.dbaasp.api.helper;

/**
 * Created by mindia on 4/6/16.
 */
public enum LookupType {

    TARGET_OBJECT("target_object"),
    TARGET_GROUP("target_group"),
    N_TERMINUS("n_terminus"),
    C_TERMINUS("c_terminus"),
    SYNTHESIS("synthesis_type"),
    COMPLEXITY("complexity"),
    KINGDOM("kingdom"),
    INTRA_CHAIN_BOND("intra_chain_bond"),
    INTER_CHAIN_BOND("inter_chain_bond"),
    UNUSUAL_AMINO_ACID("unusual_amino_acid"),
    UNIT("unit"),
    ACTIVITY_MEASURE("activity_measure"),
    AUTHOR("author"),
    JOURNAL("journal"),
    TARGET_ACTIVITY("target_species"),
    TARGET_CELL("mammalian_cell"),
    MEDIUM("medium");


    private String name;

    public static LookupType getByName(String name) {

        for (LookupType type : LookupType.values()) {
            if (type.getName().equals(name)) {
                return type;
            }
        }
        return null;
    }

    LookupType(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public static void main(String... args) {
        StringBuilder stringBuilder = new StringBuilder();
        for (LookupType lookupType : LookupType.values()) {
            stringBuilder.append(lookupType.getName() + ", ");
        }
        System.out.print(stringBuilder.toString());
    }
}
