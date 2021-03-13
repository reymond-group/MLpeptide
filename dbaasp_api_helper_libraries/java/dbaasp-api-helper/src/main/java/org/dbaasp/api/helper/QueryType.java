package org.dbaasp.api.helper;

import java.util.Arrays;
import java.util.List;

import static org.dbaasp.api.helper.FormatType.*;

/**
 * Created by mindia on 4/6/16.
 */
public enum QueryType {

    PEPTIDE_CARD("peptide_card", new String[]{JSON.getName(), XML.getName(), FASTA.getName()}),
    SEARCH("search", new String[]{JSON.getName(), XML.getName(), FASTA.getName()}),
    RANKING_SEARCH("ranking_search", new String[]{JSON.getName(), XML.getName(), FASTA.getName()}),
    LOOKUP("lookup", new String[]{JSON.getName(), XML.getName(), TAB.getName()});

    private String name;

    private List<String> formats;

    QueryType(String name, String[] formats) {
        this.name = name;
        this.formats = Arrays.asList(formats);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<String> getFormats() {
        return formats;
    }

    public void setFormats(List<String> formats) {
        this.formats = formats;
    }

    public static QueryType getByName(String name) {

        for (QueryType type : QueryType.values()) {
            if (type.getName().equals(name)) {
                return type;
            }
        }
        return null;
    }
}
