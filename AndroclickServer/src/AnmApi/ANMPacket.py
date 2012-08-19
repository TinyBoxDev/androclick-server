#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''
from urllib import urlencode;
from bs4 import BeautifulSoup;

EVENT_TARGET_KEY = u'__EVENTTARGET'.encode('utf-8');
EVENT_TARGET_VALUE = u''.encode('utf-8');
EVENT_ARGUMENT_KEY = u'__EVENTARGUMENT'.encode('utf-8');
EVENT_ARGUMENT_VALUE = u''.encode('utf-8');
VIEW_STATE_KEY = u'__VIEWSTATE'.encode('utf-8');
EVENT_VALIDATION_KEY = u'__EVENTVALIDATION'.encode('utf-8');
STOP_NUMBER_KEY = u'TxTNumeroPalina'.encode('utf-8');
LOCATION_KEY = u'ListaLocalità'.encode('utf-8');
STREET_NAME_KEY = u'TxTViaInteresse'.encode('utf-8');
LINE_NUMBER_KEY = u'TxTCAP'.encode('utf-8');
BUTTON_KEY = u'BtnInviaDati'.encode('utf-8');
BUTTON_VALUE = u'Invia Dati'.encode('utf-8');
RESULT_PANEL_KEY = 'PannelloInfoPaline';
VALUE_OF_THE_NODE_KEY = 'value';


def genPacket(eventValidation, viewState, stopNumber, streetName, location, lineNumber):
    pkt = [(EVENT_TARGET_KEY, EVENT_TARGET_VALUE),
           (EVENT_ARGUMENT_KEY, EVENT_ARGUMENT_VALUE),
           (VIEW_STATE_KEY, unicode(viewState).encode('utf-8')),
           (EVENT_VALIDATION_KEY, unicode(eventValidation).encode('utf-8')),
           (STOP_NUMBER_KEY, unicode(stopNumber).encode('utf-8')),
           (LOCATION_KEY, unicode(location).encode('utf-8')),
           (STREET_NAME_KEY, unicode(streetName).encode('utf-8')),
           (LINE_NUMBER_KEY, unicode(lineNumber).encode('utf-8')),
           (BUTTON_KEY, BUTTON_VALUE)];
    
    print("Generated packet: ");
    for item in pkt:
        print item;
    print("\n")
    
    return urlencode(pkt);

class HtmlResponse(object):
    
    _niceHtmlPage = None;
    RECEIVED_ERROR_STRING = "Previsioni in fermata non disponibili.";
    NICE_ERROR_STRING = "It seems infoclick doesn't like you so much. Please try again later!";
    
    def __init__(self, htmlPage):
        self._niceHtmlPage = BeautifulSoup(htmlPage);
    
    def getEventValidation(self):
        return self._extractValueFromNode(self._getElement(EVENT_VALIDATION_KEY));
    
    def getViewState(self):
        return self._extractValueFromNode(self._getElement(VIEW_STATE_KEY));
    
    def getInfoPalina(self):
        infosList = list();
        for info in self._getElement(RESULT_PANEL_KEY).textarea.string.splitlines(True):
            if info!='\r\n':
                infosList.append(info.split('\r\n')[0]);
        
        if len(infosList) == 3 and infosList[2] == self.RECEIVED_ERROR_STRING:
            infosList = [ self.NICE_ERROR_STRING ];
        
        return infosList;
    
    def getStopList(self):
        stopStringList = list();
        for option in self._getElement("ListaTrovati").children:
            if option.string!='\n':
                stopStringList.append(option.string);
        
        return stopStringList;
    
    def _extractValueFromNode(self, node):
        return node[VALUE_OF_THE_NODE_KEY];
        
    def _getElement(self, idToFind):
        return self._niceHtmlPage.find(id=idToFind);


if __name__ == "__main__":    
    html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>
</title><link href="anm.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" language="javascript"> 
 if (document.all){
     document.write('<link href="_ie_Palina.css" rel="stylesheet" type="text/css" />');
    } else {
     document.write('<link href="_moz_Palina.css" rel="stylesheet" type="text/css" />');
    }  
</script>
</head>
<body >
    <form name="form1" method="post" action="Default.aspx" id="form1">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJMjI2NjkyMDEyD2QWAgIDD2QWCAIDDw8WAh4HVmlzaWJsZWhkFggCAw9kFgJmD2QWAgICDw8WAh4EVGV4dAUEMzMyNWRkAgYPZBYCZg9kFgICAg8QZBAVFwpDQVNBTE5VT1ZPFVNBTiBHSU9SR0lPIEEgQ1JFTUFOTw5TQU4gU0VCQVNUSUFOTwhQT1paVU9MSQpDQUxWSVpaQU5PB1BPTExFTkEKVklMTEFSSUNDQQdDQVNPUklBBlFVQVJUTwdQT1JUSUNJDk1BU1NBIERJIFNPTU1BC0NBU0FMTlVPVk8gB01VR05BTk8IUE9MTEVOQSAGTkFQT0xJBk1BUkFOTwZBQ0VSUkEIRVJDT0xBTk8HQ0VSQ09MQQ9UT1JSRSBERUwgR1JFQ08JUElTQ0lOT0xBBVZPTExBCUdJVUdMSUFOTxUXCkNBU0FMTlVPVk8VU0FOIEdJT1JHSU8gQSBDUkVNQU5PDlNBTiBTRUJBU1RJQU5PCFBPWlpVT0xJCkNBTFZJWlpBTk8HUE9MTEVOQQpWSUxMQVJJQ0NBB0NBU09SSUEGUVVBUlRPB1BPUlRJQ0kOTUFTU0EgREkgU09NTUELQ0FTQUxOVU9WTyAHTVVHTkFOTwhQT0xMRU5BIAZOQVBPTEkGTUFSQU5PBkFDRVJSQQhFUkNPTEFOTwdDRVJDT0xBD1RPUlJFIERFTCBHUkVDTwlQSVNDSU5PTEEFVk9MTEEJR0lVR0xJQU5PFCsDF2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnFgECDmQCBw9kFgJmD2QWAgICDw8WAh8BBRlOQVBPTEktVklBLUNJTEVBLUNJVi4gMjUwZGQCCw9kFgJmD2QWAmYPDxYCHgdFbmFibGVkaGRkAgUPZBYEAgMPEGQQFQEZTkFQT0xJLVZJQS1DSUxFQS1DSVYuIDI1MBUBGU5BUE9MSS1WSUEtQ0lMRUEtQ0lWLiAyNTAUKwMBZxYBZmQCBQ8PFgIfAmhkZAIHDw8WAh8AZ2QWCAIDDw8WAh8BBRlOQVBPTEktVklBLUNJTEVBLUNJVi4gMjUwZGQCBw8PFgIfAQVeMjIvMDYvMjAxMiBvcmU6IDA5OjE1OjQyDQpGZXJtYXRhIDMzMjUgDQoNCkxpbmVhIDE4MQkwOToyNg0KTGluZWEgMTgxCTA5OjM3DQpMaW5lYSAxODEJMDk6NDUNCmRkAgkPDxYCHwEFLFN1bGxhIGZlcm1hdGEgdHJhbnNpdGFubzogMTgxLUMzMS1DMzMtQzM2LU43ZGQCCw8PFgIfAGhkZAIJDw8WAh8BBQQzMzI1ZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFFGJ0bkFnZ2lvcm5hUmlzdWx0YXRpIx2lmoxLBG3ZWHV5rWvMq+jLyVc=" />
</div>
<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['form1'];
if (!theForm) {
    theForm = document.form1;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>
<script src="/WebResource.axd?d=5MmRlVAZDIMr5dmCb60HfT6w_wuCZdSnk7MzHnci9ZNUKjJzxcEnbxp27x5RUhBUb4iPhAfnXeJ_KdsC83YsJumKpVs1&amp;t=634722412385664782" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=m2MTn6D-ZhgnIb4DuaNey0cZvTJksTunoXJ9w5Dc6TuCXb4JmD3cX1vSO4_Tind8Kkek3HG5uhDP3dRwy0QmECJuEdTlfgKQ8wnr_0Aonhn-F4Jz_jjrGb1DzN-jsA8iwX5Fk_Mp5RVx22IV6W2YHAVJHak1&amp;t=ffffffff8270033d" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=pUvwc_KQSpzICMOUbIGBh4xvVnb_fdUeB71XoPu0O2Vk0Yt-kp-ujDhXVwEAxlsnGzj2316rHzEk9OpfAw1jSlfx2DkFhe-g0xgIvthIaXnoo9SH1mxH4R_stDTpVrGIUAhf9Ie4EIhOfrFZGbYYizslM_UTMl1JKxPjmyQ-sA7ty8qK0&amp;t=ffffffff8270033d" type="text/javascript"></script>
<div>
    <input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWBALVtIq7AwLmosLADgLMi+f6DgL7gMjOCnZ8HTQEyHzLwrF8zIEX8RSBYtzd" />
</div>
    <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('ScriptManager1', document.getElementById('form1'));
Sys.WebForms.PageRequestManager.getInstance()._updateControls([], [], [], 90);
//]]>
</script>
    <div >
        <div id="PannelloInfoPaline">
              <table border="1" width="430" class="TESTOBOLD" cellpadding="6" cellspacing="0" bordercolor="#FFCC00">  
              <tr>
                <td valign="middle">
                    <table>
                        <tr>
                            <td>Clicca per Aggiornare i risultati --></td>
                            <td><input type="image" name="btnAggiornaRisultati" id="btnAggiornaRisultati" src="reload.png" style="border-color:Black;border-width:1px;border-style:Solid;" /></td>
                        </tr>
                    </table>
                 </td>                  
               </tr>
               <tr>
                <td>
                <hr />
                </td>
               </tr>
               <tr>
                <td align= "center">
                    <span id="LabInfoFermata" style="font-size:Smaller;font-weight:bold;">NAPOLI-VIA-CILEA-CIV. 250</span>
                </td>
               </tr>
                <tr>
                    <td align="center" >
                            <img id="Image1" src="palina.gif" style="border-width:0px;" />
                            <textarea name="TxTDisplay" rows="2" cols="20" readonly="readonly" id="TxTDisplay" class="TabellaPaline" style="font-size:Small;height:95px;width:195px;">22/06/2012 ore: 09:15:42
Fermata 3325 
Linea 181    09:26
Linea 181    09:37
Linea 181    09:45
</textarea>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <span id="LabPassaggiSuPalina">Sulla fermata transitano: 181-C31-C33-C36-N7</span>
                    </td>
                </tr>
                <tr>
                    <td>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <input type="submit" name="BtnCancellaDati" value="Nuova Ricerca" id="BtnCancellaDati" style="font-size:Smaller;" /> 
                    </td>
                </tr>
              </table>
</div>
    </div>
<script type="text/javascript">
//<![CDATA[
Sys.Application.initialize();
//]]>
</script>
</form>
</body>
</html>
'''
    htmlLista = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>

</title><link href="anm.css" rel="stylesheet" type="text/css" />
   
<script type="text/javascript" language="javascript"> 
 if (document.all){
     document.write('<link href="_ie_Palina.css" rel="stylesheet" type="text/css" />');
    } else {
     document.write('<link href="_moz_Palina.css" rel="stylesheet" type="text/css" />');
    }  
</script>
</head>

<body >
    <form name="form1" method="post" action="Default.aspx" id="form1">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJMjI2NjkyMDEyD2QWAgIDD2QWBAIDDw8WAh4HVmlzaWJsZWhkFgQCBg9kFgJmD2QWAgICDxBkEBUXCkNBU0FMTlVPVk8VU0FOIEdJT1JHSU8gQSBDUkVNQU5PDlNBTiBTRUJBU1RJQU5PCFBPWlpVT0xJCkNBTFZJWlpBTk8HUE9MTEVOQQpWSUxMQVJJQ0NBB0NBU09SSUEGUVVBUlRPB1BPUlRJQ0kOTUFTU0EgREkgU09NTUELQ0FTQUxOVU9WTyAHTVVHTkFOTwhQT0xMRU5BIAZOQVBPTEkGTUFSQU5PBkFDRVJSQQhFUkNPTEFOTwdDRVJDT0xBD1RPUlJFIERFTCBHUkVDTwlQSVNDSU5PTEEFVk9MTEEJR0lVR0xJQU5PFRcKQ0FTQUxOVU9WTxVTQU4gR0lPUkdJTyBBIENSRU1BTk8OU0FOIFNFQkFTVElBTk8IUE9aWlVPTEkKQ0FMVklaWkFOTwdQT0xMRU5BClZJTExBUklDQ0EHQ0FTT1JJQQZRVUFSVE8HUE9SVElDSQ5NQVNTQSBESSBTT01NQQtDQVNBTE5VT1ZPIAdNVUdOQU5PCFBPTExFTkEgBk5BUE9MSQZNQVJBTk8GQUNFUlJBCEVSQ09MQU5PB0NFUkNPTEEPVE9SUkUgREVMIEdSRUNPCVBJU0NJTk9MQQVWT0xMQQlHSVVHTElBTk8UKwMXZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cWAQIOZAIKD2QWAmYPZBYCAgIPDxYCHgRUZXh0BQJyMmRkAgUPDxYCHwBnZBYCAgMPEGQQFRMvMTQ0NC0gTkFQT0xJIFBJQVpaQSBHQVJJQkFMREkgU3RhemlvbmUgQ2VudHJhbGU0MTI1NS0gTkFQT0xJIFBJQVpaQSBHQVJJQkFMREkgTU9OVU1FTlRPICAodGFiZWxsb25lKSAxMzI1LSBOQVBPTEkgQ09SU08gVU1CRVJUTyBJIDIwNCAxMzI3LSBOQVBPTEkgQ09SU08gVU1CRVJUTyBJIDE0OCAxMzMwLSBOQVBPTEkgQ09SU08gVU1CRVJUTyBJICA2OCQxNDk0LSBOQVBPTEkgcGlhenphIEJvdmlvIGxhdG8gbW9udGUpMTA4MS0gTkFQT0xJIFZJQSBBR09TVElOTyBERVBSRVRJUyBDSVYuNDA7MTA4My0gTkFQT0xJIFZJQSBBR09TVElOTyBERVBSRVRJUyBBTFRFWlpBIENBTEFUQSBTQU4gTUFSQ083MTMwOS0gTkFQT0xJIFBJQVpaQSBNVU5JQ0lQSU8gYWl1b2xlIGZyLnBhbC5TYW4gR2lhY29tby4yNzE0LSBOQVBPTEkgVklBIFNBTiBDQVJMTyAgR0FMTEVSSUFVTUJFUlRPMcKhKDExNzctIE5BUE9MSSBWSUEgU0FOIENBUkxPIEZSLiBDSVYuMjYvMzI1MTI0My0gTkFQT0xJIFZJQSBWLiBFTUFOVUVMRSBJSUkgRlIuIE1BU0NISU8gQU5HSU9JTk8eMTIzNi0gTkFQT0xJIFZJQSBNRURJTkEgQ0lWLjIzJjE0MzEtIE5BUE9MSSBWSUEgU0FORkVMSUNFIEdVR0xJRUxNTyA3KDE0OTMtIE5BUE9MSSBQSUFaWkEgQk9WSU8gRElSLiBHQVJJQkFMREkgMTMyOS0gTkFQT0xJIENPUlNPIFVNQkVSVE8gSSAxMTcgMTMyOC0gTkFQT0xJIENPUlNPIFVNQkVSVE8gSSAxNzUgMTMyNi0gTkFQT0xJIENPUlNPIFVNQkVSVE8gSSAyNTElMTMyMi0gTkFQT0xJIENPUlNPIFVNQkVSVE8gSSBjaXYuIDM4ORUTLzE0NDQtIE5BUE9MSSBQSUFaWkEgR0FSSUJBTERJIFN0YXppb25lIENlbnRyYWxlNDEyNTUtIE5BUE9MSSBQSUFaWkEgR0FSSUJBTERJIE1PTlVNRU5UTyAgKHRhYmVsbG9uZSkgMTMyNS0gTkFQT0xJIENPUlNPIFVNQkVSVE8gSSAyMDQgMTMyNy0gTkFQT0xJIENPUlNPIFVNQkVSVE8gSSAxNDggMTMzMC0gTkFQT0xJIENPUlNPIFVNQkVSVE8gSSAgNjgkMTQ5NC0gTkFQT0xJIHBpYXp6YSBCb3ZpbyBsYXRvIG1vbnRlKTEwODEtIE5BUE9MSSBWSUEgQUdPU1RJTk8gREVQUkVUSVMgQ0lWLjQwOzEwODMtIE5BUE9MSSBWSUEgQUdPU1RJTk8gREVQUkVUSVMgQUxURVpaQSBDQUxBVEEgU0FOIE1BUkNPNzEzMDktIE5BUE9MSSBQSUFaWkEgTVVOSUNJUElPIGFpdW9sZSBmci5wYWwuU2FuIEdpYWNvbW8uMjcxNC0gTkFQT0xJIFZJQSBTQU4gQ0FSTE8gIEdBTExFUklBVU1CRVJUTzHCoSgxMTc3LSBOQVBPTEkgVklBIFNBTiBDQVJMTyBGUi4gQ0lWLjI2LzMyNTEyNDMtIE5BUE9MSSBWSUEgVi4gRU1BTlVFTEUgSUlJIEZSLiBNQVNDSElPIEFOR0lPSU5PHjEyMzYtIE5BUE9MSSBWSUEgTUVESU5BIENJVi4yMyYxNDMxLSBOQVBPTEkgVklBIFNBTkZFTElDRSBHVUdMSUVMTU8gNygxNDkzLSBOQVBPTEkgUElBWlpBIEJPVklPIERJUi4gR0FSSUJBTERJIDEzMjktIE5BUE9MSSBDT1JTTyBVTUJFUlRPIEkgMTE3IDEzMjgtIE5BUE9MSSBDT1JTTyBVTUJFUlRPIEkgMTc1IDEzMjYtIE5BUE9MSSBDT1JTTyBVTUJFUlRPIEkgMjUxJTEzMjItIE5BUE9MSSBDT1JTTyBVTUJFUlRPIEkgY2l2LiAzODkUKwMTZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkZBlYjc13fyXgD9DovzUWTmSgBQdP" />


<script src="/ScriptResource.axd?d=SvPHQsdErdIPYHzxd7v2H4wNO9csDVVQU0CwkDIPz8uoRN7iURpIOzeHLKcDzMBl9TG5sNqBZ2FRsx3hmZ8LCnVz3QVMXNlkgp2_sf0qK4Xvjb117EzRUFCVUhE48G4kxJvbCnouY6IdehzTwM_mZicm5sU1&amp;t=ffffffffa38e342f" type="text/javascript"></script>
<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWFQKh9df2BQKxj5GdCgKo6Y3lDALamNS3BwLnwP6hCALt28DBBgKK65vVCwKlw9XrAQK06qu2CQKdxsK2AQLs84CXAQKzsNpBAtq92NoGArr+7JIIAqbi5LQKApaVuf4LApjzqZsJAoi5+ekMAr2t97kCAuPwoHgChYyv5gc/JjOkz/HFwlNOeQxVpcTN52pndw==" />
    
    <div >
         
         <div id="PannelloSceltePaline">
    
         <table border="1" width="430" class="TESTOBOLD" cellpadding="6" cellspacing="0" bordercolor="#FFCC00">
            <tr>
                <td>
                    <span id="Label4">Fermate Trovate</span>
                    <br />
                    <select name="ListaTrovati" id="ListaTrovati">
        <option value="1444- NAPOLI PIAZZA GARIBALDI Stazione Centrale">1444- NAPOLI PIAZZA GARIBALDI Stazione Centrale</option>
        <option value="1255- NAPOLI PIAZZA GARIBALDI MONUMENTO  (tabellone)">1255- NAPOLI PIAZZA GARIBALDI MONUMENTO  (tabellone)</option>
        <option value="1325- NAPOLI CORSO UMBERTO I 204">1325- NAPOLI CORSO UMBERTO I 204</option>
        <option value="1327- NAPOLI CORSO UMBERTO I 148">1327- NAPOLI CORSO UMBERTO I 148</option>
        <option value="1330- NAPOLI CORSO UMBERTO I  68">1330- NAPOLI CORSO UMBERTO I  68</option>
        <option value="1494- NAPOLI piazza Bovio lato monte">1494- NAPOLI piazza Bovio lato monte</option>
        <option value="1081- NAPOLI VIA AGOSTINO DEPRETIS CIV.40">1081- NAPOLI VIA AGOSTINO DEPRETIS CIV.40</option>
        <option value="1083- NAPOLI VIA AGOSTINO DEPRETIS ALTEZZA CALATA SAN MARCO">1083- NAPOLI VIA AGOSTINO DEPRETIS ALTEZZA CALATA SAN MARCO</option>
        <option value="1309- NAPOLI PIAZZA MUNICIPIO aiuole fr.pal.San Giacomo">1309- NAPOLI PIAZZA MUNICIPIO aiuole fr.pal.San Giacomo</option>
        <option value="2714- NAPOLI VIA SAN CARLO  GALLERIAUMBERTO1¡">2714- NAPOLI VIA SAN CARLO  GALLERIAUMBERTO1&#161;</option>
        <option value="1177- NAPOLI VIA SAN CARLO FR. CIV.26/32">1177- NAPOLI VIA SAN CARLO FR. CIV.26/32</option>
        <option value="1243- NAPOLI VIA V. EMANUELE III FR. MASCHIO ANGIOINO">1243- NAPOLI VIA V. EMANUELE III FR. MASCHIO ANGIOINO</option>
        <option value="1236- NAPOLI VIA MEDINA CIV.23">1236- NAPOLI VIA MEDINA CIV.23</option>
        <option value="1431- NAPOLI VIA SANFELICE GUGLIELMO 7">1431- NAPOLI VIA SANFELICE GUGLIELMO 7</option>
        <option value="1493- NAPOLI PIAZZA BOVIO DIR. GARIBALDI">1493- NAPOLI PIAZZA BOVIO DIR. GARIBALDI</option>
        <option value="1329- NAPOLI CORSO UMBERTO I 117">1329- NAPOLI CORSO UMBERTO I 117</option>
        <option value="1328- NAPOLI CORSO UMBERTO I 175">1328- NAPOLI CORSO UMBERTO I 175</option>
        <option value="1326- NAPOLI CORSO UMBERTO I 251">1326- NAPOLI CORSO UMBERTO I 251</option>
        <option value="1322- NAPOLI CORSO UMBERTO I civ. 389">1322- NAPOLI CORSO UMBERTO I civ. 389</option>

    </select>
                    <input type="submit" name="BtnScegliIlTrovato" value="Seleziona" id="BtnScegliIlTrovato" />
                </td>
            </tr>
         </table>
        
</div>
        
    </div>
    
    
    

<script type="text/javascript">
//<![CDATA[
Sys.Application.initialize();
//]]>
</script>
</form>
</body>
</html>    
'''
    print genPacket("myValidation", "myState", "myStopNumber", "myStreetName", "myLocation", "myLineName");
    h = HtmlResponse(html);
    
    print h.getInfoPalina();
    print h.getEventValidation();
    print h.getViewState();
    
    h2 = HtmlResponse(htmlLista);
    
    print h2.getStopList();
