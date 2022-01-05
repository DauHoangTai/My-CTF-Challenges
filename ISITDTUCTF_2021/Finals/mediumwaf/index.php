<?php 

show_source(__FILE__);

$xss = $_GET['xss'];
$xss = preg_replace('/[\x00-\x1F\x7F-\xFF]/', '', $xss);
$tmpxss = $xss;
do
{
    $xss = $tmpxss;
    $tmpxss = urldecode($xss);
} while($tmpxss != $xss);


do
{
    $xss = $tmpxss;
    $tmpxss = html_entity_decode($xss, ENT_QUOTES | ENT_HTML5, 'UTF-8');
} while($tmpxss != $xss);


$valid = true;
if(preg_match("/\<\w+.*on.*=.*/si", $xss))
{
    $valid = false;
}

if(preg_match("/\s+/", $xss))
{
    $valid = false;
}

if(preg_match("/\<\w+.*src=.*/si", $xss))
{
    $valid = false;
}

if(preg_match("/\<\w+.*href=.*/si", $xss))
{
    $valid = false;
}

if(preg_match("/\<script.*/si", $xss))
{
    $valid = false;
}

if(preg_match("/\<object.*/si", $xss))
{
        $valid = false;
}

if($valid == true)
{
    echo $_GET['xss'];
}
else
{
    echo "WAF block";
}

?>