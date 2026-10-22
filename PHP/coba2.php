<?php
$nim = "I.2610920";
$nama = "Muhammad Samy";
$umur = 21;
$nilai = 100;
$status = TRUE;

echo "NIM : ".$nim. "<br>";
echo "Nama : $nama<br>";
print "Umur : ". $umur;
print "<br>";
printf ("Nilai :%3f<br>", $nilai);
if ($status)
    echo "Status: Aktif";
else
    echo "Status: Tidak Aktif";
?>