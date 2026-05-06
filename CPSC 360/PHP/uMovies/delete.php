<?php
// delete.php
// Deletes ALL records from all uMovies tables.

require_once("db.php");

// ------------------------------------------------------------
// 1. Validate password input
// ------------------------------------------------------------
if (!isset($_POST['password'])) {
    die("<h2>Error: No password provided.</h2>
         <p><a href='admin_login.html'>Return to Login</a></p>");
}

$password = trim($_POST['password']);

// ------------------------------------------------------------
// 2. Try connecting as administrator
// ------------------------------------------------------------
$conn = connectAdmin($password);
if ($conn === false) {
    die("<h2>Error: Invalid administrator password.</h2>
         <p><a href='admin_login.html'>Return to Login</a></p>");
}

// ------------------------------------------------------------
// 3. Delete all records from all tables
// ------------------------------------------------------------
try {
    $conn->exec("DELETE FROM performed_in");
    $conn->exec("DELETE FROM directed_by");
    $conn->exec("DELETE FROM movies");
    $conn->exec("DELETE FROM actors");
    $conn->exec("DELETE FROM directors");
} catch (PDOException $e) {
    die("<h2>Error while deleting records.</h2><pre>" . $e->getMessage() . "</pre>");
}

?>
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>All Records Deleted</title>
    <link rel="stylesheet" href="uMovies.css">
</head>
<body>
<div class="main">
    <h1>All Records Deleted</h1>

    <p>All tables in the <strong>uMovies</strong> database have been cleared.</p>

    <p><a href="admin_menu.php?password=<?php echo urlencode($password); ?>">Return to Administrator Menu</a></p>
</div>
</body>
</html>
