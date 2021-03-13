package org.dbaasp.api.helper.request;

import org.dbaasp.api.helper.Complexity;
import org.dbaasp.api.helper.QueryType;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by mindia on 5/21/16.
 * <p>
 * GET REQUEST
 * <p>
 * ${BASE_URL}/api/v1?query=search&target_group_id=790&synthesis_type=36&format=xml
 * <p>
 * CURL REQUEST
 * <p>
 * curl -v -L -d "query=search&target_group_id=790&synthesis_type=36&format=xml" ${BASE_URL}/api/v1
 */
public class SearchRequest extends AbstractRequest {

    private String name;
    private String sequence;
    private Integer nTerminusId;
    private Integer cTerminusId;
    private Integer targetGroupId;
    private Integer targetObjectId;
    private Integer synthesisType;
    private Integer kingdomId;
    private Object bondId;
    private Integer unusualAminoAcidId;
    private Integer authorId;
    private Integer journalId;
    private Integer articleYear;
    private String articleTitle;
    private String complexity = Complexity.MONOMER.getComplexity();


    @Override
    protected Map<String, String> parameters() {
        Map<String, String> params = new HashMap<>();
        params.put("complexity", getValue(complexity));
        params.put("name", getValue(name));
        params.put("sequence", getValue(sequence));
        params.put("n_terminus_id", getValue(nTerminusId));
        params.put("c_terminus_id", getValue(cTerminusId));
        params.put("target_group_id", getValue(targetGroupId));
        params.put("target_object_id", getValue(targetObjectId));
        params.put("synthesis_type", getValue(synthesisType));
        params.put("kingdom_id", getValue(kingdomId));
        params.put("bond_id", getValue(bondId));
        params.put("unusual_amino_acid_id", getValue(unusualAminoAcidId));
        params.put("author_id", getValue(authorId));
        params.put("journal_id", getValue(journalId));
        params.put("article_year", getValue(articleYear));
        params.put("article_title", getValue(articleTitle));
        return params;
    }

    @Override
    protected String queryType() {
        return QueryType.SEARCH.getName();
    }

    public Integer getTargetGroupId() {
        return targetGroupId;
    }

    public void setTargetGroupId(Integer targetGroupId) {
        this.targetGroupId = targetGroupId;
    }

    public Integer getSynthesisType() {
        return synthesisType;
    }

    public void setSynthesisType(Integer synthesisType) {
        this.synthesisType = synthesisType;
    }

    public Integer getTargetObjectId() {
        return targetObjectId;
    }

    public void setTargetObjectId(Integer targetObjectId) {
        this.targetObjectId = targetObjectId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSequence() {
        return sequence;
    }

    public void setSequence(String sequence) {
        this.sequence = sequence;
    }

    public Integer getnTerminusId() {
        return nTerminusId;
    }

    public void setnTerminusId(Integer nTerminusId) {
        this.nTerminusId = nTerminusId;
    }

    public Integer getcTerminusId() {
        return cTerminusId;
    }

    public void setcTerminusId(Integer cTerminusId) {
        this.cTerminusId = cTerminusId;
    }

    public Integer getKingdomId() {
        return kingdomId;
    }

    public void setKingdomId(Integer kingdomId) {
        this.kingdomId = kingdomId;
    }

    public String getComplexity() {
        return complexity;
    }

    public void setComplexity(String complexity) {
        this.complexity = complexity;
    }

    public Object getBondId() {
        return bondId;
    }

    public void setBondId(Object bondId) {
        this.bondId = bondId;
    }

    public Integer getUnusualAminoAcidId() {
        return unusualAminoAcidId;
    }

    public void setUnusualAminoAcidId(Integer unusualAminoAcidId) {
        this.unusualAminoAcidId = unusualAminoAcidId;
    }

    public Integer getAuthorId() {
        return authorId;
    }

    public void setAuthorId(Integer authorId) {
        this.authorId = authorId;
    }

    public Integer getJournalId() {
        return journalId;
    }

    public void setJournalId(Integer journalId) {
        this.journalId = journalId;
    }

    public Integer getArticleYear() {
        return articleYear;
    }

    public void setArticleYear(Integer articleYear) {
        this.articleYear = articleYear;
    }

    public String getArticleTitle() {
        return articleTitle;
    }

    public void setArticleTitle(String articleTitle) {
        this.articleTitle = articleTitle;
    }
}
