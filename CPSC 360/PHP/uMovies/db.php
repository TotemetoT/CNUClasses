<?php
define ("DB_NAME", "uMovies");
define ("DB_HOST", "localhost");

function connectUser() {
    $username = "uMoviesUser";
    $password = "anonymous";

    try {
        $dsn = "mysql:host=".DB_HOST.";dbname=".DB_NAME.";charset=utf8";
        $pdo = new PDO($dsn, $username, $password);

        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        return false;
    }
}

function connectAdmin($password) {
    $username = "uMoviesAdmin";

    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME;
        $pdo = new PDO($dsn, $username, $password);

        // Throw exceptions on errors
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        return $pdo;

    } catch (PDOException $e) {
        // DO NOT reveal actual SQL error to the user
        return false; // admin_login.php checks this
    }
}
?>