<?php
require_once("db.php");

if (!isset($_POST['password'])) {
    die("<h2>Error: No Password Provided</h2>");
}

$password = trim($_POST["password"]);
$conn = connectAdmin($password);

if ($conn === false) {
    echo "
        <html>
            <head>
                <title>Invalid Password</title>
                <link rel='stylesheet' type='text/css' href='uMovies.css'>
            </head>
            <body>
                <div class='main'>
                    <h2>Invalid administrator password.</h2>
                    <p>The password you entered is incorrect.</p>
                    <p><a href='admin_login.html'>Return to Login</a></p>
                </div>
            </body>
        </html>";
    exit();
}

header("Location: admin_menu.php?password=" . urlencode($password));
exit();
?>