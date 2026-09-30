<?php
declare(strict_types=1);

$EMPFAENGER = 'hello@ordeshop.net';
$ABSENDER    = 'formular@ordeshop.net';   // Postfach beim Hoster anlegen
$ZIEL_OK     = 'danke.html';
$ZIEL_FEHLER = 'anfrage.html?fehler=1';

function weiter(string $ziel): void {
    header('Location: ' . $ziel, true, 303);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    weiter($ZIEL_FEHLER);
}

// Honigtopf: echte Menschen lassen dieses Feld leer
if (($_POST['website_url'] ?? '') !== '') {
    weiter($ZIEL_OK);   // Bot bekommt die Danke-Seite, die Mail geht nicht raus
}

function feld(string $name, int $max = 500): string {
    $wert = trim((string)($_POST[$name] ?? ''));
    $wert = str_replace(["\r", "\n", "\0"], ' ', $wert);
    return mb_substr($wert, 0, $max);
}

$name    = feld('name', 120);
$email   = feld('email', 180);
$betrieb = feld('betrieb', 120);
$telefon = feld('telefon', 60);
$branche = feld('branche', 80);
$seite   = feld('bestehende_seite', 200);
$paket   = feld('paket', 80);
$ok      = isset($_POST['datenschutz']);

$nachricht = trim((string)($_POST['nachricht'] ?? ''));
$nachricht = str_replace("\0", '', $nachricht);
$nachricht = mb_substr($nachricht, 0, 5000);

if ($name === '' || $nachricht === '' || !$ok
    || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    weiter($ZIEL_FEHLER);
}

$betreff = 'Anfrage von ' . $name . ($betrieb !== '' ? ' (' . $betrieb . ')' : '');

$text = "Neue Anfrage ueber ordeshop.net\n\n"
      . "Name:        $name\n"
      . "Betrieb:     $betrieb\n"
      . "E-Mail:      $email\n"
      . "Telefon:     $telefon\n"
      . "Branche:     $branche\n"
      . "Bisher:      $seite\n"
      . "Wunschpaket: $paket\n\n"
      . "Nachricht:\n$nachricht\n\n"
      . "---\n"
      . 'Gesendet: ' . date('d.m.Y H:i') . "\n";

$kopf = [
    'From: ORDE Formular <' . $ABSENDER . '>',
    'Reply-To: ' . $name . ' <' . $email . '>',
    'Content-Type: text/plain; charset=UTF-8',
    'MIME-Version: 1.0',
    'X-Mailer: PHP/' . phpversion(),
];

$betreff_kodiert = '=?UTF-8?B?' . base64_encode($betreff) . '?=';

if (@mail($EMPFAENGER, $betreff_kodiert, $text, implode("\r\n", $kopf))) {
    weiter($ZIEL_OK);
}
weiter($ZIEL_FEHLER);
