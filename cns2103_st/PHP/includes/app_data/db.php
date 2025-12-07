<?php

$server = "localhost";
$username = "root";
$password = "";
$database = "catuc_st";

$cn = mysqli_connect($server, $username, $password, $database);

if (!$cn) {
    echo mysqli_connect_error() ."Connection Failed";
} 

?>
