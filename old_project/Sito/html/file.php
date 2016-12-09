<?php
	$riga=$_POST['riga'];
	$nome = "/var/www/html/txtfiles/linguette.txt";
	$f = fopen($nome, "w");
	fwrite($f,$riga);
	fclose($f);
	$nome = "/var/www/html/controllo.txt";
	$f = fopen($nome, "w");
	fwrite($f,$riga);
	fclose($f);
?>
