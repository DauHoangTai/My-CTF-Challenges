<?php
error_reporting(0);
if (isset($_GET['UA']) && strlen($_GET['UA']) < 135) {
        $User_Agent = $_GET['UA'];
        $ctx = stream_context_create(array(
                "http" => array(
                        "header" => "User-Agent: ".$User_Agent,
                        "timeout" => 1
                )));
        if ( ((int)($User_Agent) === (int)('7_AE_siu_nhan')) || strlen($User_Agent) > strlen(str_repeat('a',500))) {
                if (hash('sha224',$User_Agent) == 0) {
                        $html = file_get_contents("/flag1.txt",false,$ctx);
                        echo $html;
                }
        } else {
                $htmp = file_get_contents('http://34.124.157.127:5005/home.php', false, $ctx); // Change with your ip, not localhost
                echo $htmp;
        }
} else{
        $url = 'https://twitter.com/';
        $path = $_GET['path'] == '' ? ' ' : $_GET['path'];
        if (preg_match("/[a-zA-Z0-9]| /i",$path) && strlen($path) < 7) {
                $url = $path == ' ' ? $url.'taidh_' : $url.$path;
                $ch = curl_init();
                curl_setopt($ch, CURLOPT_URL, $url);
                curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 2);
                $output = curl_exec($ch);
                echo $output;
                curl_close($ch);
        } else {
                die("SSRF isn't that easy （︶︿︶）");
        }
}