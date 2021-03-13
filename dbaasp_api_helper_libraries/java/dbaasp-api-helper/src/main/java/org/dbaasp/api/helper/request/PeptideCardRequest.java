package org.dbaasp.api.helper.request;

import org.dbaasp.api.helper.QueryType;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by mindia on 5/21/16.
 * <p>
 * GET REQUEST
 * <p>
 * ${BASE_URL}/api/v1?query=peptide_card&peptide_id=107&format=json
 *<p>
 * CURL REQUEST
 * <p>
 * curl -v -L -d "query=peptide_card&peptide_id=107&format=json" ${BASE_URL}/api/v1
 */
public class PeptideCardRequest extends AbstractRequest {

    private Integer peptideId = 0;

    @Override
    protected Map<String, String> parameters() {
        Map<String, String> params = new HashMap<>();
        params.put("peptide_id", peptideId.toString());
        return params;
    }

    @Override
    protected String queryType() {
        return QueryType.PEPTIDE_CARD.getName();
    }

    public Integer getPeptideId() {
        return peptideId;
    }

    public void setPeptideId(Integer peptideId) {
        this.peptideId = peptideId;
    }
}
