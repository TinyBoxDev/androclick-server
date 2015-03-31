var mockForecast = '<?xml version="1.0" encoding="utf-8"?><ArrayOfPrevisione xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://m.anm.it/srv/"><Previsione><id>3129</id><nome>SEMMOLA-OSPEDALE PASCALE-LAB. ANALISI CARDILLO FRA</nome><time>14.49</time><linea>C41</linea><timeMin>5</timeMin></Previsione><Previsione><id>3129</id><nome>SEMMOLA-OSPEDALE PASCALE-LAB. ANALISI CARDILLO FRA</nome><time>14.52</time><linea>165</linea><timeMin>8</timeMin></Previsione><Previsione><id>3129</id><nome>SEMMOLA-OSPEDALE PASCALE-LAB. ANALISI CARDILLO FRA</nome><time>14.53</time><linea>C44</linea><timeMin>9</timeMin></Previsione></ArrayOfPrevisione>'

exports.Forecast = mockForecast;

var mockInvalidForecast = '<?xml version="1.0" encoding="utf-8"?><ArrayOfPrevisione xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://m.anm.it/srv/"><Previsione><stato>Nessuna informazione alla palina.</stato></Previsione></ArrayOfPrevisione>'

exports.InvalidForecast = mockInvalidForecast;
