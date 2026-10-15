<?php
$harga = 250_000;
$qty = 3;
$diskon = 0.15;

$total = $harga * $qty;
$bayar = $total - ($total * $diskon);
$ongkir = $bayar >= 500_000 ? "gratis" : 20_000;

echo "total belanja: Rp " . number_format($total) . "\n";
echo "setelah diskon = Rp " . number_format($bayar) . "\n";
echo "ongkir = " . $ongkir;