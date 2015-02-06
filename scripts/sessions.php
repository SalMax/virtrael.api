<?php
	header('Content-type: text/xml');
	require_once('locale/localization.php');
?>

<Sessions>
  <session id="1">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a VIRTRA-EL!</strong> Ésta es tu primera sesión, así que te explicaremos en qué consistirá tu plan de trabajo. Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="34" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="30" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="101" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="4" type="7" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
	  <exerciseEntry id="5" type="1" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
	  <exerciseEntry id="6" type="25" durationKind="repeat" duration="0" repetitions="4" dependsOn="-1" maxTime="0" />
	  <exerciseEntry id="7" type="102" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
	  <exerciseEntry id="8" type="33" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
	 </exercises>
  </session>
  <session id="2">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la segunda sesión!</strong> En esta sesión te vamos a proponer una serie de ejercicios para medir tu nivel actual de memoria, atención, razonamiento y planificación. Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="8" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="17" durationKind="repeat" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
	  <exerciseEntry id="3" type="11" durationKind="repeat" duration="0" repetitions="6" dependsOn="-1" maxTime="0" />
	  <exerciseEntry id="4" type="12" durationKind="repeat" duration="0" repetitions="6" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="5" type="19" durationKind="notime" duration="0" repetitions="1" dependsOn="1" maxTime="180" />
      <exerciseEntry id="6" type="6" durationKind="repeat" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
	 </exercises>
  </session>
  <session id="3">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la tercera sesión!</strong> En esta sesión te proponemos ejercicios de memoria (Lista de recados), atención (Globos) y planificación (Compra de regalos). Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="2" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="4" durationKind="time" duration="10" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="16" durationKind="time" duration="12" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="4" type="18" durationKind="notime" duration="0" repetitions="1" dependsOn="1" maxTime="180" />
	 </exercises>
  </session>
  <session id="4">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la cuarta sesión!</strong> En esta sesión te proponemos ejercicios de atención (Búsqueda de objetos) y razonamiento. Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="9" durationKind="time" duration="15" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="14" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="11" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="4" type="12" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="5" type="13" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="6" type="15" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
	 </exercises>
  </session>
  <session id="5">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la quinta sesión!</strong> En esta sesión te proponemos ejercicios de memoria visual (Recuerda las imágenes), planificación (Compra de regalos) y memoria (Bolsa de objetos). Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="3" durationKind="time" duration="12" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="16" durationKind="time" duration="12" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="5" durationKind="time" duration="10" repetitions="1" dependsOn="-1" maxTime="0" />
	 </exercises>
  </session>
  <session id="6">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la sexta sesión!</strong> En esta sesión te proponemos ejercicios de memoria verbal (Lista de recados) y atención (Globos y Búsqueda de objetos). Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="2" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="4" durationKind="time" duration="10" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="9" durationKind="time" duration="12" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="4" type="18" durationKind="notime" duration="0" repetitions="1" dependsOn="1" maxTime="48" />
	 </exercises>
  </session>
  <session id="7">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la séptima sesión!</strong> En esta sesión te proponemos ejercicios de razonamiento y planificación (Compra de regalos). Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="11" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="12" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="13" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="4" type="15" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="5" type="16" durationKind="time" duration="15" repetitions="1" dependsOn="1" maxTime="180" />
	 </exercises>
  </session>
  <session id="8">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la octava sesión!</strong> En esta sesión te proponemos ejercicios de memoria visual (Recuerda las imágenes), memoria de trabajo (Bolsa de objetos) y atención (Búsqueda de objetos). Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="3" durationKind="time" duration="12" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="5" durationKind="time" duration="10" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="9" durationKind="time" duration="12" repetitions="1" dependsOn="-1" maxTime="0" />
	 </exercises>
  </session>
  <session id="9">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la novena sesión!</strong> En esta sesión te proponemos ejercicios de memoria verbal (Lista de recados) y razonamiento. Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="2" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="11" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="12" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="4" type="13" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="5" type="14" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="6" type="15" durationKind="repeat" duration="0" repetitions="5" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="7" type="18" durationKind="notime" duration="0" repetitions="1" dependsOn="1" maxTime="180" />
	 </exercises>
  </session>
  <session id="10">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la décima sesión!</strong> En esta sesión te proponemos ejercicios de atención (Búsqueda de objetos), planificación (Compra de regalos) y atención (Globos). Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="9" durationKind="time" duration="15" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="16" durationKind="time" duration="12" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="4" durationKind="time" duration="10" repetitions="1" dependsOn="-1" maxTime="0" />
	 </exercises>
  </session>
  <session id="11">
  	<description><![CDATA[<?php echo _('<strong>¡Bienvenido a la undécima sesión!</strong> En esta sesión te proponemos ejercicios de memoria de trabajo (Bolsa de objetos), memoria visual (Recuerda las imágenes) y realidad virtual. Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="5" durationKind="time" duration="10" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="3" durationKind="time" duration="12" repetitions="1" dependsOn="-1" maxTime="0" />
	 </exercises>
  </session>
  <session id="12">
  	<description><![CDATA[<?php echo _('<strong>¡Ésta es la duodécima sesión!</strong> Te vamos a proponer unos ejercicios para medir tu nivel actual de memoria, atención, razonamiento. Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
    <exercises>
      <exerciseEntry id="1" type="7" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="1" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="3" type="11" durationKind="repeat" duration="0" repetitions="6" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="4" type="12" durationKind="repeat" duration="0" repetitions="6" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="5" type="25" durationKind="repeat" duration="0" repetitions="4" dependsOn="-1" maxTime="0" />
	 </exercises>
  </session>
  <session id="13">
  	<description><![CDATA[<?php echo _('<strong>¡Ésta es la treceava sesión!</strong> En ella te proponemos una serie de ejercicios para medir tu nivel actual de memoria, atención y planificación. Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
  	<exercises>
  	  <exerciseEntry id="1" type="8" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
  	  <exerciseEntry id="2" type="17" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
  	  <exerciseEntry id="3" type="19" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="4" type="6" durationKind="repeat" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
  	</exercises>
  </session>
  <session id="14">
  	<description><![CDATA[<?php echo _('<strong>¡Ésta es la catorceava sesión!</strong> En ella te proponemos una serie de ejercicios de realidad virtual. Por favor, trata de realizar la <strong>sesión completa</strong> sin interrumpirla.'); ?>]]></description>
  	<exercises>
  	  <exerciseEntry id="1" type="20" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
      <exerciseEntry id="2" type="21" durationKind="notime" duration="0" repetitions="1" dependsOn="-1" maxTime="0" />
  	</exercises>
  </session>
</Sessions>
