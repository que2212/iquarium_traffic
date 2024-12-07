<?php

require_once('db.php');

$login = $_POST['login'];
$pass = $_POST['pass'];
$email = $_POST['email'];


$sql = "INSERT INTO 'users'(login,pass,email) VALUES('$login','$pass','$email')";

// $conn -> query($sql);

if( $conn -> query($query) === TRUE){
    echo "regist ";
}else {
    echo "error" . $conn -> error;
}
