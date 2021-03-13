package org.dbaasp.api.helper.request;

import org.dbaasp.api.helper.Complexity;
import org.dbaasp.api.helper.MathOperationTypes;
import org.dbaasp.api.helper.QueryType;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by mindia on 5/21/16.
 * <p>
 * GET REQUEST
 * <p>
 * ${BASE_URL}/api/v1?query=ranking_search&target_species_id=3232&activity_measure_id=72&operation=<=&activity=0.5&format=json
 * <p>
 * CURL REQUEST
 * <p>
 * curl -v -L -d "query=ranking_search&target_species_id=3232&activity_measure_id=72&operation=<=&activity=0.5&format=json" ${BASE_URL}/api/v1
 */
public class RankingSearchRequest extends AbstractRequest {

    private Integer targetSpeciesId = 0;
    private Integer activityMeasureId = 0;
    private String operation = MathOperationTypes.LESS.getOperation();
    private Float activity = 0.0f;

    //only monomer support at this time
    private String complexity = Complexity.MONOMER.getComplexity();


    @Override
    protected Map<String, String> parameters() {
        Map<String, String> params = new HashMap<>();
        params.put("complexity", getValue(complexity));
        params.put("target_species_id", getValue(targetSpeciesId));
        params.put("activity_measure_id", getValue(activityMeasureId));
        params.put("operation", getValue(operation));
        params.put("activity", getValue(activity));
        return params;
    }

    @Override
    protected String queryType() {
        return QueryType.RANKING_SEARCH.getName();
    }

    public Integer getTargetSpeciesId() {
        return targetSpeciesId;
    }

    public void setTargetSpeciesId(Integer targetSpeciesId) {
        this.targetSpeciesId = targetSpeciesId;
    }

    public Integer getActivityMeasureId() {
        return activityMeasureId;
    }

    public void setActivityMeasureId(Integer activityMeasureId) {
        this.activityMeasureId = activityMeasureId;
    }

    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public Float getActivity() {
        return activity;
    }

    public void setActivity(Float activity) {
        this.activity = activity;
    }

    public String getComplexity() {
        return complexity;
    }

    public void setComplexity(String complexity) {
        this.complexity = complexity;
    }
}
