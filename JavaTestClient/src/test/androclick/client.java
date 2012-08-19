package test.androclick;

import java.io.BufferedReader;
import java.io.Reader;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;


class Request extends Thread {
	
	StringEntity s = null;
	
	Request(StringEntity ss){
		s = ss;
	}
	
	public void run() {
		HttpClient httpClient = new DefaultHttpClient();

		try {
			
	        HttpPost request = new HttpPost("http://androclick.herokuapp.com/");
	        request.addHeader("content-type", "application/x-www-form-urlencoded");
	        request.setEntity(this.s);
	        HttpResponse response = httpClient.execute(request);
	        Reader in = new BufferedReader(new InputStreamReader(response.getEntity().getContent(), "UTF-8"));
	        StringBuilder builder= new StringBuilder();
	        char[] buf = new char[1000];
	        int l = 0;
	        while (l >= 0) {
	        	builder.append(buf, 0, l);
	        	l = in.read(buf);
	        }
	        System.out.println(builder.toString());
	    }catch (Exception ex) {
	    	ex.printStackTrace();
	    } finally {
	        httpClient.getConnectionManager().shutdown();
	    }
	}
}

public class client {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			StringEntity[] requestes = {
					// giusta
					new StringEntity("stop_request={\"county\": \"\", \"street\": \"\", \"number\": 3329}"),
					// errata
					new StringEntity("stop_request={\"county\": \"\", \"street\": \"fwfww\", \"number\": 1444}"),
					new StringEntity("stop_request={\"county\": \"ddw\", \"street\": \"\", \"number\": 1444}"),
					new StringEntity("stop_request={\"county\": \"\", \"street\": \"\", \"number\": 144212234}"),
					new StringEntity("location_request={\"county\": \"NAPOLI\", \"street\": \"carlo III\", \"number\": 4432}"),
					// giusta
					new StringEntity("location_request={\"county\": \"NAPOLI\", \"street\": \"carlo III\", \"number\": \"\"}"),
					//errata
					new StringEntity("location_request={\"county\": \"NAPOLI\", \"street\": \"carlo IIIvilwnlkvwnelflne\", \"number\": \"\"}"),
					//giusta
					new StringEntity("line_request={\"line\": \"R2\", \"time\": \"\"}"),
					//errata
					new StringEntity("line_request={\"line\": \"R2wkjefbkjebkwjefbk\", \"time\": \"554\"}"),
					new StringEntity("line_request={\"line\": \"R2wkjefbkjebkwjefbk\", \"time\": \"\"}")
			};
			
			for(StringEntity s : requestes)
				new Request(s).start();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
