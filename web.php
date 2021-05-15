<?php
//Fichero para realizar la cache de los datos, especifica la ruta (path) del directorio que desees utilizar.
//Recuerda que el directorio para la cache debe tener permisos de escritura.
$PathFicheroCacheDatos = $_SERVER['DOCUMENT_ROOT'].'/directorio_cache/3768.txt';
include_once($PathFicheroCacheDatos);

if($JsonCache && $LastUpdate > time() - 3600)
{
$WeatherArray = unserialize(stripcslashes($JsonCache));
}
else
{
$WeatherJson = file_get_contents('https://api.tutiempo.net/json/?lan=es&apid={Clave API}&lid=3768');
$WeatherArray = json_decode($WeatherJson,true);
//Guardamos cache
$JsonCachear = addslashes(serialize($WeatherArray));
$TextoCachearDatos = '<?php $LastUpdate = '.time().'; $JsonCache = \''.$JsonCachear.'\'; ?>';
$fp = @fopen($PathFicheroCacheDatos,"w");
fwrite($fp,$TextoCachearDatos);
fclose($fp);
}

$MesesName = array('-','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre');

$WeatherPrint = '<div id="WeatherTutiempo">
<div class="header">
<h2>El tiempo en '.$WeatherArray['locality']['name'].'</h2>
<p>Pronóstico 7 días | El tiempo por Tutiempo.net</p>
</div>';

//Salida días
for($i = 1; $i <= 7; $i++)
{
list($anio,$mes,$dia) = explode("-",$WeatherArray['day'.$i]['date']);
$WeatherPrint .= '<div class="daydata">
<h3 class="date">'.$dia.' de '.$MesesName[$mes].' de '.$anio.'</h3>
<p class="it"><img alt="'.$WeatherArray['day'.$i]['text'].'" title="'.$WeatherArray['day'.$i]['text'].'" height="50" src="https://v5i.tutiempo.net/wi/01/50/'.$WeatherArray['day'.$i]['icon'].'.png" width="50">'.$WeatherArray['day'.$i]['temperature_max'].'&deg;C<br>'.$WeatherArray['day'.$i]['temperature_min'].'&deg;C</p>
<p class="wind"><img alt="'.$WeatherArray['day'.$i]['wind_direction'].'" title="'.$WeatherArray['day'.$i]['wind_direction'].'" height="50" src="https://v5i.tutiempo.net/wd/big/black/'.$WeatherArray['day'.$i]['icon_wind'].'.png" width="50">'.$WeatherArray['day'.$i]['wind'].' km/h</p>
<p class="oc">Humedad: '.$WeatherArray['day'.$i]['humidity'].'%<br>Salida sol: '.$WeatherArray['day'.$i]['sunrise'].'<br>Puesta sol: '.$WeatherArray['day'.$i]['sunset'].'</p>
<p class="moon"><img alt="" height="50" src="https://v5i.tutiempo.net/wmi/02/'.$WeatherArray['day'.$i]['moon_phases_icon'].'.png" width="50">Salida luna: '.$WeatherArray['day'.$i]['moonrise'].'<br>Puesta luna: '.$WeatherArray['day'.$i]['moonset'].'</p>
</div>';
}

$WeatherPrint .= '<p class="linkTT"><a href="'.$WeatherArray['locality']['url_weather_forecast_15_days'].'" target="_blank" rel="nofollow">Predicción 15 días</a></p><div class="header" style="padding-top:20px;"><h2>El tiempo por horas en '.$WeatherArray['locality']['name'].'</h2><p>Próximas 24 horas | Datos de Tutiempo.net</p></div>';

//Salida horas
for($i = 1; $i <= 25; $i++)
{
list($anio,$mes,$dia) = explode("-",$WeatherArray['hour_hour']['hour'.$i]['date']);
$WeatherPrint .= '<div class="daydata">';
if($WeatherArray['hour_hour']['hour'.$i]['date'] != $FechaPuesta){$WeatherPrint .= '<h3 class="date">'.$dia.' de '.$MesesName[$mes].' de '.$anio.'</h3>'; $FechaPuesta = $WeatherArray['hour_hour']['hour'.$i]['date'];}
$WeatherPrint .= '<p class="time"><strong>'.$WeatherArray['hour_hour']['hour'.$i]['hour_data'].'</strong> | '.$WeatherArray['hour_hour']['hour'.$i]['text'].'</p>
<p class="wind"><img alt="'.$WeatherArray['hour_hour']['hour'.$i]['text'].'" title="'.$WeatherArray['hour_hour']['hour'.$i]['text'].'" height="50" src="https://v5i.tutiempo.net/wi/01/50/'.$WeatherArray['hour_hour']['hour'.$i]['icon'].'.png" width="50">'.$WeatherArray['hour_hour']['hour'.$i]['temperature'].'&deg;C</p>
<p class="wind"><img alt="'.$WeatherArray['hour_hour']['hour'.$i]['wind_direction'].'" title="'.$WeatherArray['hour_hour']['hour'.$i]['wind_direction'].'" height="50" src="https://v5i.tutiempo.net/wd/big/black/'.$WeatherArray['hour_hour']['hour'.$i]['icon_wind'].'.png" width="50">'.$WeatherArray['hour_hour']['hour'.$i]['wind'].' km/h</p>
<p class="oc" style="line-height:25px;">Humedad: '.$WeatherArray['hour_hour']['hour'.$i]['humidity'].'%<br>Presión: '.$WeatherArray['hour_hour']['hour'.$i]['pressure'].' hPa</p>
</div>';
}

$WeatherPrint .= '<p class="linkTT"><a href="'.$WeatherArray['locality']['url_hourly_forecast'].'" target="_blank" rel="nofollow">Ver pronóstico por horas 14 días</a></p></div>';

?><!DOCTYPE html>
<html lang="es" class="pretty-scrollbar">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<meta name="author" content="Tutiempo Network, S.L." />
<meta name="distribution" content="global" />
<meta name="lang" content="es" />
<title>Ejemplo API - JSON - PHP - Tutiempo.net</title>
<style>
html,body{width:100%;height:100%;padding:10px;margin:0}
body{margin:0;padding:0;font-family:sans-serif,Arial,Helvetica;font-size:14px;color:#555555;background:#f9f9f9;}
#WeatherTutiempo{all:initial;*{all:unset;}}
#WeatherTutiempo{font-family:sans-serif,Arial,Helvetica;font-size:14px;}
#WeatherTutiempo a{text-decoration:none; color:#0086b3;}
#WeatherTutiempo a:hover{color:black;}
#WeatherTutiempo p{margin:0;padding:5px; padding-left:0; padding-right:0;}
#WeatherTutiempo .header{clear:both;float:none;}
#WeatherTutiempo .header h2{margin:0;margin-top:10px;}
#WeatherTutiempo .header p{margin:0;}
#WeatherTutiempo .date{margin:0;padding-top:10px;padding-bottom:5px;clear:both;float:none;}
#WeatherTutiempo .daydata{clear:both;float:none;}
#WeatherTutiempo .it{line-height:25px; float:left; margin-right:20px;height:50px;white-space:nowrap;}
#WeatherTutiempo .it img{float:left;margin-right:10px;}
#WeatherTutiempo .wind{float:left; margin-right:20px;line-height:50px;height:50px;white-space:nowrap;}
#WeatherTutiempo .wind img{float:left;margin-right:10px;}
#WeatherTutiempo .oc{float:left; margin-right:20px;height:50px;}
#WeatherTutiempo .moon{line-height:25px;float:left; height:50px;white-space:nowrap;}
#WeatherTutiempo .moon img{float:left;margin-right:10px;}
#WeatherTutiempo .time{margin:0; padding:0;clear:both;float:none;padding-top:10px;padding-bottom:5px;}
#WeatherTutiempo .linkTT{clear: both; float: none;}
</style>
</head>
<body>
<?php print $WeatherPrint; ?>
</body>
</html>
