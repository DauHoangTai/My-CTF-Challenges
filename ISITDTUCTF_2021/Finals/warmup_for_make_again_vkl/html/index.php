<?php
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    if (preg_replace('/[^\W]+\((?R)?\)/',NULL,$cmd) === '') {
        if (preg_match("/[3-9`~!@#\$%^&*\-=+.,;?'\"\[\]\{\}\\\\]|\([2]|\_[a-g]|0|1|pcntl|high|var|root|len|func|flo|contents|count|cmp|get|head|replace|local/i",$cmd) || substr_count($cmd,'ext') > 1 || substr_count($cmd,'scan') > 1 || strlen($cmd) > 45) {
            die("¯\_(ツ)_/¯");
        } else {
            eval($cmd.";");
        }
    } else {
        die('Just think simple please ( ͡° ͜ʖ ͡°)');
    }
} else {
    highlight_file(__FILE__);
}

?>
