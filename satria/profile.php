<?php
$nama = "Satria Maulana";
$umur = "17";
$sekolah = "SMKN 2 Bandung";
$citacita = "suaminya Kafka";
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
    <link rel="stylesheet" href="style.css">
</head>         
<body>
    <div>
        <h1>Hi There</h1>
            <br>
            <h2>
            <label for="">Perkenalkan, nama saya <?= $nama ?></label>
            <br>
            <label for="">Umur saya adalah  <?= $umur ?></label>
            <br>
            <label for="">Saya ber-sekolah  di <?= $sekolah ?></label>
            <br>
            <label for="">Cita-cita saya adalah menjadi <?= $citacita ?></label>
            </h2>
        <br>
        <a href="index.php">-----Hal Utama-----</a>
    </div>
</body>
</html>