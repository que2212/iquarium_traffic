<?php

$user = 'root';
$password = 'root';
$db = 'users_regist';
$host = 'localhost';
$port = 3306;

$link = mysqli_init();
$success = mysqli_real_connect(
   $link,
   $host,
   $user,
   $password,
   $db,
   $port
);


$conn = mysqli_connect($host, $user, $password, $db);

// if(!$conn){
//     die("connect failed". mysqli_connect_error());
// }else{
//     echo "uspeh";
// }?>