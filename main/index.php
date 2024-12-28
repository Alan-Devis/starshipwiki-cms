<?php
$page_id = 0;
include 'contentpages.php';
include 'Extensions/ext_Parsedown.php';
?>

<h1><?php echo "Добро пожаловать на " . ($wikiname ?? "Please, setup variable $wikiname"); ?></h1>
<div class="MainPage"><?php echo ($contentpage_0); ?></div>