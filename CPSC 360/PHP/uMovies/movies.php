<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN"
            "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<title>uMovies :: Movies</title>
<style type="text/css">
@import url(uMovies.css);
</style>
</head>
<body>

<div id="links">
<a href="./">Home<span> Access the database of movies, actors and directors. Free to all!</span></a>
<a href="admin_login.html">Administrator<span> Administrator access. Password required.</span></a>
</div>

<div id="content">
<h1>uMovies&trade;</h1>
<p>
Welcome to <em>uMovies</em>, your destination for information on 
<a href="movies.php">movies</a>, 
<a href="actors.php">actors</a>, 
and <a href="directors.php">directors</a>.
</p>

<h2>Browsing All Movies</h2>

<p>
<?php
// -------------------------------------------------------------
// Connect to database
// -------------------------------------------------------------
@$moviesdb = new mysqli('localhost','uMoviesUser','anonymous','uMovies');
@$moviesdb->set_charset("utf8");

if ($moviesdb->connect_errno) {
    echo '<h3>Database Access Error!</h3>';
}
else {

    // ---------------------------------------------------------
    // Sorting
    // ---------------------------------------------------------
    $order = "";
    if (isset($_GET['order']) && ($_GET['order'] === 'name' || $_GET['order'] === 'year')) {
        $order = " ORDER BY " . $_GET['order'];
    }

    $select = "SELECT * FROM movies" . $order;
    $result = $moviesdb->query($select);
    $rows   = $result->num_rows;

    echo "<table class='uMovies'>\n";
    echo "<tr>\n";
    echo "<th></th>";
    echo "<th><a href='movies.php?order=name'>Name</a></th>";
    echo "<th><a href='movies.php?order=year'>Release Year</a></th>";
    echo "</tr>\n";

    // ---------------------------------------------------------
    // No movies?
    // ---------------------------------------------------------
    if ($rows == 0) {
        echo "<tr><td colspan='3'>No Movies to Display</td></tr>\n";
    }
    else {
        // -----------------------------------------------------
        // Display movies
        // -----------------------------------------------------
        $count = 1;
        while ($row = $result->fetch_assoc()) {

            // IMPORTANT: include BOTH name & year for movie.php
            $mName = urlencode($row['name']);
            $mYear = urlencode($row['year']);

            echo "<tr class='highlight'>";
            echo "<td>".$count."</td>";
            echo "<td><a href='movie.php?name=$mName&year=$mYear'>".$row['name']."</a></td>";
            echo "<td>".$row['year']."</td>";
            echo "</tr>\n";
            $count++;
        }
    }

    echo "</table>\n";

    $result->free();
    $moviesdb->close();
}
?>
</p>

<p><copyright>Roberto A. Flores &copy; 2027</copyright></p>
</div>

</body>
</html>
