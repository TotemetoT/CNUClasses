<?php
require_once('db.php');

$password = null;
if (isset($_REQUEST['password'])) {
    $password = trim($_REQUEST['password']);
}

if (empty($password)) {
    echo "<!doctype html>
        <html>
        <head><meta charset='utf-8'><title>Admin Access Required</title></head>
        <body>
            <h2>Administrator password not provided.</h2>
            <p><a href='admin_login.html'>Return to Login</a></p>
        </body>
        </html>";
    exit();
}

$conn = connectAdmin($password);
if ($conn === false) {
    // Invalid password — do not leak DB error details
    echo "<!doctype html>
    <html>
      <head>
        <meta charset='utf-8'>
        <title>Invalid Password</title>
        <link rel='stylesheet' type='text/css' href='uMovies.css'>
      </head>
      <body>
        <div class='main'>
          <h2>Invalid administrator password.</h2>
          <p>The password you provided is not valid.</p>
          <p><a href='admin_login.html'>Return to Login</a></p>
        </div>
      </body>
    </html>";
    exit();
}
?>

<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>uMovies — Administrator Menu</title>
  <link rel="stylesheet" href="uMovies.css">
  <script>
    // Client-side checks and confirmations
    function validateUploadForm() {
      const fname = document.getElementById('datafile').value.trim();
      if (fname === "") {
        alert("Please enter a data file name before uploading.");
        return false;
      }
      return confirm("Are you sure you want to upload the file: " + fname + " ?");
    }

    function confirmDeleteAll() {
      return confirm("This will DELETE ALL RECORDS in the uMovies database. Are you sure?");
    }
  </script>
  <style>
    /* minimal inline styles to keep layout tidy if CSS is missing */
    .admin-box { max-width:700px; margin:30px auto; padding:18px; border-radius:8px; background:#fff; box-shadow:0 1px 4px rgba(0,0,0,0.1); }
    .admin-actions { display:flex; gap:18px; flex-wrap:wrap; }
    .admin-panel { flex:1 1 300px; padding:12px; border:1px solid #ddd; border-radius:6px; }
    .admin-panel h3 { margin-top:0; }
    .small { font-size:0.9em; color:#555; }
  </style>
</head>
<body>
  <div class="admin-box">
    <h1>uMovies — Administrator Menu</h1>
    <p class="small">You are logged in as <strong>uMoviesAdmin</strong>. Keep this page private while you administrate the data.</p>

    <div class="admin-actions">
      <!-- Upload Panel -->
      <div class="admin-panel">
        <h3>Upload movie data file</h3>
        <p class="small">Enter the name of a text data file (for example: <code>uMovies_1.txt</code>) that is present on the server.</p>

        <form method="post" action="upload.php" onsubmit="return validateUploadForm();">
          <label for="datafile">Data file name:</label><br>
          <input type="text" id="datafile" name="datafile" placeholder="uMovies_all.txt" style="width:100%; padding:8px; margin-top:6px;"><br><br>

          <!-- Pass the admin password forward -->
          <input type="hidden" name="password" value="<?php echo htmlspecialchars($password, ENT_QUOTES); ?>">

          <input type="submit" value="Upload File">
        </form>
      </div>

      <!-- Delete Panel -->
      <div class="admin-panel">
        <h3>Delete all records</h3>
        <p class="small">This will remove all rows from <code>performed_in</code>, <code>directed_by</code>, <code>movies</code>, <code>actors</code>, and <code>directors</code>.</p>

        <form method="post" action="delete.php" onsubmit="return confirmDeleteAll();">
          <!-- Pass the admin password forward -->
          <input type="hidden" name="password" value="<?php echo htmlspecialchars($password, ENT_QUOTES); ?>">

          <input type="submit" value="Delete All Records">
        </form>
      </div>
    </div>

    <hr style="margin:18px 0;">

    <p>
      <a href="index.html">Return to Public Portal</a> |
      <a href="admin_login.html">Log out</a>
    </p>
  </div>
</body>
</html>