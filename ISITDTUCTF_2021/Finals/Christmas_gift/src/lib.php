<?php
if ($_SERVER['REMOTE_ADDR'] === '34.124.157.127') { // Change with your ip, not localhost
    if(isset($_GET['f'])) {
        $f = $_GET['f'] ;
        if (!preg_match("/zip|:\/\//i",$f)) {
            include $f.".php";
        }
    }
} else {
    echo "no IP private";
}