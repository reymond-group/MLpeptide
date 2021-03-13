package org.dbaasp.api.helper;

import org.dbaasp.api.helper.request.LookupRequest;
import org.dbaasp.api.helper.request.PeptideCardRequest;
import org.dbaasp.api.helper.request.RankingSearchRequest;
import org.dbaasp.api.helper.request.SearchRequest;

/**
 * Created by mindia on 5/21/16.
 */
public class APICaller {

    public static void main(String... args) {


        PeptideCardRequest peptideCardRequest = new PeptideCardRequest();
        peptideCardRequest.setPeptideId(8);
        peptideCardRequest.setFormatType(FormatType.XML);

//        System.out.print(peptideCardRequest.request());

        LookupRequest lookupRequest = new LookupRequest();
        lookupRequest.setLookupType(LookupType.C_TERMINUS);
        lookupRequest.setFormatType(FormatType.XML);

//        System.out.print(lookupRequest.request());

        SearchRequest searchRequest = new SearchRequest();
//        searchRequest.setSynthesisType(36);
//        searchRequest.setTargetGroupId(790);
//        searchRequest.setKingdomId(52);
        searchRequest.setFormatType(FormatType.JSON);
        searchRequest.setBondId("all_bond");

        System.out.print(searchRequest.request());

        RankingSearchRequest rankingSearchRequest = new RankingSearchRequest();
        rankingSearchRequest.setTargetSpeciesId(3232);
        rankingSearchRequest.setActivityMeasureId(72);
        rankingSearchRequest.setActivity(100f);
        rankingSearchRequest.setFormatType(FormatType.XML);

//        System.out.print(rankingSearchRequest.request());

    }
}
