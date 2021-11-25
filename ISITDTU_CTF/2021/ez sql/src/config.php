<?php
    $server = 'mysql8';
    $username = 'root';
    $password = '414ba6bef9406cf1c6440e679e68c9ed9af742f9';
    $db = 'main';
    $conn = new mysqli($server, $username, $password, $db);
    if($conn->connect_error){
        die("connect_error: " . $conn->connect_error);
    }
?>