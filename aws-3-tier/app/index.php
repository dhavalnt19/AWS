<?php
$conn = new mysqli("DB_ENDPOINT", "admin", "password", "mydb");

if ($conn->connect_error) {
    die("Connection failed");
}

echo "Connected to RDS successfully!";
?>
