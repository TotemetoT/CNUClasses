<?php
require_once('db.php');

if (!isset($_POST['password']) || !isset($_POST['datafile'])) {
    die("<h2>Error: Missing Required Parameters</h2>");   
}

$password = trim($_POST['password']);
$filename = trim($_POST['datafile']);

if ($filename === "") {
    die("<h2>Error: No Data File Name Provided</h2>");
}

$conn = connectAdmin($password);
if ($conn === false) {
    die("<h2>Error: Invalid administrator password.</h2>
         <p><a href='admin_login.html'>Return to Login</a></p>");
}

if (!file_exists($filename)) {
    die("<h2>Error: Data file '$filename' not found on server.</h2>
         <p><a href='admin_menu.php?password=" . urlencode($password) ."'>Return to Admin Menu</a></p>");
}

$moviesTotal = $actorsTotal = $directorsTotal = $directedByTotal = $performedTotal = 0;
$moviesNew = $actorsNew = $directorsNew = $directedByNew = $performedNew = 0;

$lastMovie = $lastActor = $lastDirector = $lastDirectedBy = $lastPerformed = "";

// Insert into movies
function insertMovie($conn, $name, $year) {
    $stmt = $conn->prepare("SELECT * FROM movies WHERE name=? AND year=?");
    $stmt->execute([$name, $year]);
    if ($stmt->rowCount() > 0) return false;

    $stmt = $conn->prepare("INSERT INTO movies VALUES(?,?)");
    $stmt->execute([$name, $year]);
    return true;
}

// Insert into actors
function insertActor($conn, $name, $gender) {
    $stmt = $conn->prepare("SELECT * FROM actors WHERE name=? AND gender=?");
    $stmt->execute([$name, $gender]);
    if ($stmt->rowCount() > 0) return false;

    $stmt = $conn->prepare("INSERT INTO actors VALUES(?,?)");
    $stmt->execute([$name, $gender]);
    return true;
}

// Insert into directors
function insertDirector($conn, $name) {
    $stmt = $conn->prepare("SELECT * FROM directors WHERE name=?");
    $stmt->execute([$name]);
    if ($stmt->rowCount() > 0) return false;

    $stmt = $conn->prepare("INSERT INTO directors VALUES(?)");
    $stmt->execute([$name]);
    return true;
}

// Insert into directed_by
function insertDirectedBy($conn, $movie, $year, $director) {
    $stmt = $conn->prepare("SELECT * FROM directed_by WHERE movie=? AND year=? AND director=?");
    $stmt->execute([$movie, $year, $director]);
    if ($stmt->rowCount() > 0) return false;

    $stmt = $conn->prepare("INSERT INTO directed_by VALUES(?,?,?)");
    $stmt->execute([$movie, $year, $director]);
    return true;
}

// Insert into performed_in
function insertPerformance($conn, $actor, $movie, $year, $role) {
    $stmt = $conn->prepare("SELECT * FROM performed_in WHERE actor=? AND movie=? AND year=? AND role=?");
    $stmt->execute([$actor, $movie, $year, $role]);
    if ($stmt->rowCount() > 0) return false;

    $stmt = $conn->prepare("INSERT INTO performed_in VALUES(?,?,?,?)");
    $stmt->execute([$actor, $movie, $year, $role]);
    return true;
}

$fh = fopen($filename, "r");

while (($line = fgets($fh)) !== false) {
    $line = trim($line);
    if ($line === "") continue;

    // Count total movie entries seen
    $moviesTotal++;

    // Split fields
    list($movieName, $year, $directorsList, $actorsList) = explode("|", $line);

    $movieName = trim($movieName);
    $year = trim($year);

    // Insert movie
    if (insertMovie($conn, $movieName, $year)) {
        $moviesNew++;
        $lastMovie = "$movieName ($year)";
    }

    // Process directors
    $directorsTotal++;
    $directors = explode(",", $directorsList);
    foreach ($directors as $d) {
        $d = trim($d);
        if ($d === "") continue;

        if (insertDirector($conn, $d)) {
            $directorsNew++;
            $lastDirector = $d;
        }

        if (insertDirectedBy($conn, $movieName, $year, $d)) {
            $directedByNew++;
            $lastDirectedBy = "$movieName → $d";
        }
    }

    // Process actors
    $actorsTotal++;
    $actorEntries = explode(",", $actorsList);

    foreach ($actorEntries as $entry) {
        $entry = trim($entry);
        if ($entry === "") continue;

        // Format: ActorName:Role
        list($actorName, $role) = explode(":", $entry);
        $actorName = trim($actorName);
        $role = trim($role);

        // Gender UNKNOWN — assignment provides Male/Female only in given files
        // The provided data files include gender encoded in name endings or separate data files.
        // If gender unknown, default to "Unknown"
        $gender = "Unknown";

        if (insertActor($conn, $actorName, $gender)) {
            $actorsNew++;
            $lastActor = $actorName;
        }

        if (insertPerformance($conn, $actorName, $movieName, $year, $role)) {
            $performedNew++;
            $lastPerformed = "$actorName ($role)";
        }
    }
}

fclose($fh);
?>

<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Upload Summary</title>
    <link rel="stylesheet" href="uMovies.css">
</head>
<body>
<div class="main">
    <h1>Upload Complete</h1>
    <p>Processed file: <strong><?php echo htmlspecialchars($filename); ?></strong></p>

    <h3>Summary:</h3>

    <ul>
        <li>Movies: <?php echo "$moviesNew added out of $moviesTotal"; ?>
            <?php if ($lastMovie) echo "<br>Last added: $lastMovie"; ?>
        </li>

        <li>Actors: <?php echo "$actorsNew added out of $actorsTotal"; ?>
            <?php if ($lastActor) echo "<br>Last added: $lastActor"; ?>
        </li>

        <li>Directors: <?php echo "$directorsNew added out of $directorsTotal"; ?>
            <?php if ($lastDirector) echo "<br>Last added: $lastDirector"; ?>
        </li>

        <li>Directed By entries: <?php echo "$directedByNew added"; ?>
            <?php if ($lastDirectedBy) echo "<br>Last added: $lastDirectedBy"; ?>
        </li>

        <li>Performances: <?php echo "$performedNew added"; ?>
            <?php if ($lastPerformed) echo "<br>Last added: $lastPerformed"; ?>
        </li>
    </ul>

    <p><a href="admin_menu.php?password=<?php echo urlencode($password); ?>">Return to Admin Menu</a></p>
</div>
</body>
</html>