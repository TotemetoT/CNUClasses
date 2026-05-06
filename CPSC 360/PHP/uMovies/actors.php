<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN"
            "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<title>uMovies :: Actors</title>
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

<h2>Browsing All Actors</h2>

<p>
<?php
// ----------------------------------------------------------------------
// Connect to database
// ----------------------------------------------------------------------
@$actorsdb = new mysqli('localhost','uMoviesUser','anonymous','uMovies');
@$actorsdb->set_charset("utf8");

if ($actorsdb->connect_errno) {
    echo "<h3>Database Access Error!</h3>";
}
else {

    // ---------------------------------------------------------
    // Sorting logic
    // ---------------------------------------------------------
    $order = "";
    if (isset($_GET['order']) && ($_GET['order'] == 'name' || $_GET['order'] == 'gender')) {
        $order = " ORDER BY " . $_GET['order'];
    }

    // Retrieve all actors
    $select = "SELECT * FROM actors" . $order;
    $result = $actorsdb->query($select);

    echo "<table class=\"uMovies\">\n";
    echo "<tr>\n";
    echo "  <th></th>\n";
    echo "  <th><a href=\"actors.php?order=name\">Name</a></th>\n";
    echo "  <th><a href=\"actors.php?order=gender\">Gender</a></th>\n";
    echo "</tr>\n";

    if ($result->num_rows == 0) {
        echo "<tr><td colspan=\"3\">No Actors to Display</td></tr>";
    }
    else {
        $i = 1;
        while ($row = $result->fetch_assoc()) {
            $actorSafe = urlencode($row['name']);
            echo "<tr class=\"highlight\">";
            echo "  <td>$i</td>";
            echo "  <td><a href=\"actor.php?name=$actorSafe\">".$row['name']."</a></td>";
            echo "  <td>".$row['gender']."</td>";
            echo "</tr>\n";
            $i++;
        }
    }

    echo "</table>\n";

    $result->free();
    $actorsdb->close();
}
?>
</p>

<p><copyright>Roberto A. Flores &copy; 2027</copyright></p>
</div>

</body>
</html>
