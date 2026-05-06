<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN"
            "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<title>uMovies :: Directors</title>
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

<h2>Browsing All Directors</h2>

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
    // Sorting (only "name" is needed for directors)
    // --------------------------------------------------------
    $order = "";
    if (isset($_GET['order']) && $_GET['order'] === 'name') {
        $order = " ORDER BY name";
    }

    // --------------------------------------------------------
    // Query directors
    // --------------------------------------------------------
    $select = "SELECT * FROM directors" . $order;
    $result = $db->query($select);

    echo "<table class=\"uMovies\">\n";
    echo "<tr>\n";
    echo "  <th></th>\n";
    echo "  <th><a href=\"directors.php?order=name\">Name</a></th>\n";
    echo "</tr>\n";

    if (!$result || $result->num_rows == 0) {
        echo "<tr><td colspan=\"2\">No Directors to Display</td></tr>";
    }
    else {
        $i = 1;
        while ($row = $result->fetch_assoc()) {
            $safeName = urlencode($row['name']);
            echo "<tr class=\"highlight\">";
            echo "  <td>$i</td>";
            echo "  <td><a href=\"director.php?name=$safeName\">".$row['name']."</a></td>";
            echo "</tr>\n";
            $i++;
        }
    }

    echo "</table>\n";

    $result->free();
    $db->close();
}
?>
</p>

<p><copyright>Roberto A. Flores &copy; 2027</copyright></p>
</div>

</body>
</html>
