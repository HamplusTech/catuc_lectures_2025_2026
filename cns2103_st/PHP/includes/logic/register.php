<?php
require "includes/app_data/db.php";

if(isset($_POST['register'])) {
    $fullname = $_POST['fullname'];
    $username = $_POST['username'];
    $password = $_POST['password'];
    $phone = $_POST['phone'];
    $gender = $_POST['gender'];

    $stmt = "INSERT INTO users (username,gender, fullname, phone, password) VALUES ('$username', '$gender', '$fullname', '$phone', '$password')";
    $cmd = mysqli_query($cn, $stmt);

    if ($cmd) {
        $msg =  "User registered successfully";
    } else {
        echo mysqli_query_error($cn);
    }
}
