<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN"
            "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<title>uMovies :: Actor</title>
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

<h2>Actor</h2>

<p>
<?php
// -----------------------------------------------------------
// Connect to database
// -----------------------------------------------------------
@$db = new mysqli('localhost', 'uMoviesUser', 'anonymous', 'uMovies');
@$db->set_charset("utf8");

if ($db->connect_errno) {
    echo "<h3>Database Access Error!</h3>";
} else {

    // -------------------------------------------------------
    // Get actor name parameter safely
    // -------------------------------------------------------
    if (!isset($_GET['name']) || trim($_GET['name']) == "") {
        echo "<h3>No Actor Selected</h3>";
        exit();
    }

    $actorName = $db->real_escape_string($_GET['name']);

    // -------------------------------------------------------
    // Fetch actor info (gender)
    // -------------------------------------------------------
    $select = "SELECT * FROM actors WHERE name='$actorName'";
    $result = $db->query($select);

    if (!$result || $result->num_rows == 0) {
        echo "<h3>No Actor to Display</h3>";
    } else {

        $actor = $result->fetch_assoc();

        echo "<h3><span class=\"uTitle\">".$actor['name']."</span></h3>";
        echo "<strong>Gender:</strong> ".$actor['gender']."<br><br>";

        // ---------------------------------------------------
        // Filmography (movies performed in)
        // ---------------------------------------------------
        echo "<strong>Filmography:</strong><br />";

        $select = "SELECT * FROM performed_in 
                   WHERE actor='$actorName'
                   ORDER BY year, movie";

        $films = $db->query($select);

        echo "<table class=\"uMovies\">\n";
        echo "<tr>\n";
        echo "  <th></th>\n";
        echo "  <th>Movie</th>\n";
        echo "  <th>Year</th>\n";
        echo "  <th>Role</th>\n";
        echo "</tr>\n";

        if (!$films || $films->num_rows == 0) {
            echo "<tr><td colspan=\"4\">No Movies to Display</td></tr>";
        } else {
            $i = 1;
            while ($row = $films->fetch_assoc()) {
                $movieName = urlencode($row['movie']);
                $movieYear = urlencode($row['year']);

                echo "<tr class=\"highlight\">";
                echo "  <td>$i</td>";
                echo "  <td><a href=\"movie.php?name=$movieName&year=$movieYear\">".$row['movie']."</a></td>";
                echo "  <td>".$row['year']."</td>";
                echo "  <td>".$row['role']."</td>";
                echo "</tr>\n";

                $i++;
            }
        }

        echo "</table>\n";

        $result->free();
    }

    $db->close();
}
?>
</p>

<p><copyright>Roberto A. Flores &copy; 2027</copyright></p>

</div>
</body>
</html>
