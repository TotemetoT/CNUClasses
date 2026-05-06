<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN"
            "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<title>uMovies :: Director</title>
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

<h2>Director</h2>

<p>
<?php
// ------------------------------------------------------------
// Connect to database
// ------------------------------------------------------------
@$db = new mysqli('localhost', 'uMoviesUser', 'anonymous', 'uMovies');
@$db->set_charset("utf8");

if ($db->connect_errno) {
    echo "<h3>Database Access Error!</h3>";
}
else {

    // --------------------------------------------------------
    // Check director name passed in URL
    // --------------------------------------------------------
    if (!isset($_GET['name']) || trim($_GET['name']) == "") {
        echo "<h3>No Director Selected</h3>";
        exit();
    }

    $directorName = $db->real_escape_string($_GET['name']);

    // --------------------------------------------------------
    // Fetch director record
    // --------------------------------------------------------
    $select = "SELECT * FROM directors WHERE name='$directorName'";
    $result = $db->query($select);

    if (!$result || $result->num_rows == 0) {
        echo "<h3>No Director to Display</h3>";
    }
    else {

        $director = $result->fetch_assoc();

        echo "<h3><span class=\"uTitle\">" . $director['name'] . "</span></h3>";

        // --------------------------------------------------------
        // Filmography (movies they directed)
        // --------------------------------------------------------
        echo "<strong>Filmography:</strong><br />";

        $select = "SELECT * FROM directed_by 
                   WHERE director='$directorName'
                   ORDER BY year, movie";

        $films = $db->query($select);

        echo "<table class=\"uMovies\">\n";
        echo "<tr>\n";
        echo "  <th></th>\n";
        echo "  <th>Movie</th>\n";
        echo "  <th>Year</th>\n";
        echo "</tr>\n";

        if (!$films || $films->num_rows == 0) {
            echo "<tr><td colspan=\"3\">No Movies to Display</td></tr>";
        }
        else {
            $i = 1;
            while ($row = $films->fetch_assoc()) {
                $movieName = urlencode($row['movie']);
                $movieYear = urlencode($row['year']);

                echo "<tr class=\"highlight\">";
                echo "  <td>$i</td>";
                echo "  <td><a href=\"movie.php?name=$movieName&year=$movieYear\">" . $row['movie'] . "</a></td>";
                echo "  <td>" . $row['year'] . "</td>";
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
