package org.dbaasp.api.helper.request;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;
import com.mashape.unirest.request.HttpRequestWithBody;
import org.dbaasp.api.helper.FormatType;

import java.util.Map;

/**
 * Created by mindia on 5/21/16.
 */
public abstract class AbstractRequest {


    private FormatType formatType = FormatType.JSON;

    private static final String BASE_URL = "https://dbaasp.org/api/v1";

    public String request() {

        try {
            HttpRequestWithBody request = Unirest.post(BASE_URL);

            request = request.queryString("query", queryType());
            request = request.queryString("format", formatType.getName());

            for (Map.Entry<String, String> keyValue : parameters().entrySet()) {
                if (keyValue.getValue() != null && !keyValue.getValue().isEmpty())
                    request = request.queryString(keyValue.getKey(), keyValue.getValue());
            }
            HttpResponse<String> response = request.asString();

            return response.getBody();

        } catch (UnirestException e) {
            e.printStackTrace();
        }
        return null;
    }

    protected String getValue(Object o) {
        if (o != null) {
            return o.toString();
        }
        return null;
    }

    protected abstract Map<String, String> parameters();

    protected abstract String queryType();

    public void setFormatType(FormatType formatType) {
        this.formatType = formatType;
    }
}
