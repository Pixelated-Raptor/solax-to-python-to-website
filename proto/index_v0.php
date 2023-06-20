<html>
<h1>Aktuelle Daten</h1>
<style> table { border: 2px solid black; } </style>
<?php

ini_set('display_errors', 1);
error_reporting(~0);	

	try {
		$dbPDO = new PDO('sqlite:/home/kiwi/project/solar_data.db');
	} catch (Exception $e) {
		echo $e->getMessage();
	}

	try {
		$data = $dbPDO->query("
		SELECT 
		substr(time(time_of_request, 'localtime'), 1, 5) as 'Zeit',
		acpower || ' W',
		yieldtoday || ' kWh',
		yieldtotal || ' MWh',
		feedinenergy || ' kWh',
		consumeenergy || ' kWh',
		batPower || ' W'
		from DOwNLOADED_SOLAX_INFO
		order by time_of_request desc
		limit 13");
	} catch (Exception $e) {
		echo $e->getMessage();
	}
echo "	
<table>
	<tr>
		<th>Zeitstempel</th>
		<th>AC Leistung</th>
		<th>Tagesertrag</th>
		<th>Gesamtertrag</th>
		<th>Einspeisung</th>
		<th>Eigennutzung</th>
		<th>Batterieleistung</th>
	</tr>
";
//Spalte kann per Nummer, Alias oder genauso wie im Select angesprochen werden
foreach($data as $row) {
echo "
<tr>
	<td>{$row[0]}</td>
	
	<td>{$row['acpower || \' W\'']}</td>
	<td>{$row['yieldtoday || \' kWh\'']}</td>
	<td>{$row['yieldtotal || \' MWh\'']}</td>
	<td>{$row['feedinenergy || \' kWh\'']}</td>
	<td>{$row['consumeenergy || \' kWh\'']}</td>
	<td>{$row['batPower || \' W\'']}</td>
</tr>
";
}
echo "</table>";
?>
<?php
$path = "graphs/daily0.png";
echo "<img src=$path>";
?>
</html>
