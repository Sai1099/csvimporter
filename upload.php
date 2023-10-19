<?php

// Connect to database
$db = new PDO('mongodb://localhost:27017;dbname=sai;dbcollection=orginalphone', 'root', '');

// Get data from database
$sql = 'SELECT * FROM users';
$result = $db->query($sql);

// Populate text fields with data from database
$name = $result->fetchColumn(1);
$gmail = $result->fetchColumn(2);
$role = $result->fetchColumn(3);
$gender = $result->fetchColumn(4);

?>

<html>
<head>
  <title>Database-Driven Text Fields</title>
</head>
<body>
  <h1>Database-Driven Text Fields</h1>

  <form action="backend.php" method="post">
    <input type="text" name="name" value="<?php echo $name; ?>" placeholder="Name">
    <input type="text" name="gmail" value="<?php echo $gmail; ?>" placeholder="Gmail">
    <input type="text" name="role" value="<?php echo $role; ?>" placeholder="Role">
    <input type="text" name="gender" value="<?php echo $gender; ?>" placeholder="Gender">

    <input type="submit" value="Submit">
  </form>
</body>
</html>
