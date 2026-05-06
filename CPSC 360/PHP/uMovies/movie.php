<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN"
            "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<title>uMovies :: Movie</title>
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

<h2>Movie</h2>

<p>
<?php
// ----------------------------------------------------------------------
// Connect (MySQLi version, matching instructor starter code)
// ----------------------------------------------------------------------
@$moviesdb = new mysqli('localhost','uMoviesUser','anonymous','uMovies');
@$moviesdb->set_charset("utf8");

if ($moviesdb->connect_errno) {
    echo '<h3>Database Access Error!</h3>';
} 
else 
{
    // ------------------------------------------------------------------
    // Get parameters safely
    // ------------------------------------------------------------------
    $movieName = isset($_GET['name']) ? $moviesdb->real_escape_string($_GET['name']) : "";
    $movieYear = isset($_GET['year']) ? intval($_GET['year']) : 0;

    if ($movieName == "") {
        echo "<h3>No Movie Selected</h3>";
        exit();
    }

    // ------------------------------------------------------------------
    // Select the movie (name + year)
    // ------------------------------------------------------------------
    $select = "SELECT * FROM movies WHERE name='$movieName'";
    if ($movieYear != 0) {
        $select .= " AND year=$movieYear";
    }

    $result = $moviesdb->query($select);
    if (!$result || $result->num_rows == 0) {
        echo "<h3>No Movie to Display</h3>";
    }
    else 
    {
        $movie = $result->fetch_assoc();

        echo "<h3><span class=\"uTitle\">".$movie['name']."</span> (".$movie['year'].")</h3>";

        // ------------------------------------------------------------------
        // Directors
        // ------------------------------------------------------------------
        echo "<strong>Directed by: </strong>";

        $select = 'SELECT * FROM directed_by WHERE movie="'.$movie['name'].'" AND year='.$movie['year'];
        $dirs = $moviesdb->query($select);

        if (!$dirs || $dirs->num_rows == 0) {
            echo "<em>No director listed</em><br />";
        } 
        else 
        {
            echo "<span class=\"uDirector\">";
            $count = $dirs->num_rows;
            while ($row = $dirs->fetch_assoc()) {
                echo '<a href="director.php?name='.$row['director'].'">'.$row['director'].'</a>';
                if (--$count > 0) echo ", ";
            }
            echo "</span><br />";
        }

        // ------------------------------------------------------------------
        // Cast + roles
        // ------------------------------------------------------------------
        echo "<br><strong>Cast:</strong><br/>";
        echo "<table class=\"uMovies\">\n";
        echo "<tr>\n";
        echo "<th></th>";
        echo "<th><a href=\"movie.php?name=".$movie['name']."&year=".$movie['year']."&order=name\">Name</a></th>";
        echo "<th><a href=\"movie.php?name=".$movie['name']."&year=".$movie['year']."&order=role\">Role</a></th>";
        echo "</tr>\n";

        // Sorting
        $order = "";
        if (isset($_GET['order']) && ($_GET['order'] == 'name' || $_GET['order'] == 'role')) {
            $order = " ORDER BY ".$_GET['order'];
        }

        $select = 'SELECT * FROM performed_in WHERE movie="'.$movie['name'].'" AND year='.$movie['year'].$order;
        $cast = $moviesdb->query($select);

        if (!$cast || $cast->num_rows == 0) {
            echo "<tr><td colspan=\"3\">No Actors to Display</td></tr>";
        }
        else {
            $i = 1;
            while ($row = $cast->fetch_assoc()) {
                echo "<tr class=\"highlight\">";
                echo "<td>".$i."</td>";
                echo "<td><a href=\"actor.php?name=".$row['actor']."\">".$row['actor']."</a></td>";
                echo "<td>".$row['role']."</td>";
                echo "</tr>\n";
                $i++;
            }
        }

        echo "</table>\n";

        $result->free();
    }

    $moviesdb->close();
}
?>
</p>

<p><copyright>Roberto A. Flores &copy; 2027</copyright></p>
</div>

</body>
</html>
