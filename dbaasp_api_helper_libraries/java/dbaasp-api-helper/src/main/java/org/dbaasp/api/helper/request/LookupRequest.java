package org.dbaasp.api.helper.request;

import org.dbaasp.api.helper.LookupType;
import org.dbaasp.api.helper.QueryType;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by mindia on 5/21/16.
 * <p>
 * GET REQUEST
 * <p>
 * ${BASE_URL}/api/v1?query=lookup&lookup_type=target_group&format=json
 * <p>
 * CURL REQUEST
 * <p>
 * curl -v -L -d "query=lookup&lookup_type=target_group&format=json" ${BASE_URL}/api/v1
 */
public class LookupRequest extends AbstractRequest {

    private LookupType lookupType = LookupType.TARGET_OBJECT;

    @Override
    protected Map<String, String> parameters() {
        Map<String, String> params = new HashMap<>();
        params.put("lookup_type", lookupType.getName());
        return params;
    }

    @Override
    protected String queryType() {
        return QueryType.LOOKUP.getName();
    }

    public LookupType getLookupType() {
        return lookupType;
    }

    public void setLookupType(LookupType lookupType) {
        this.lookupType = lookupType;
    }
}
