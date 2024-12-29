<?php
$page_id = 0;
include 'main/contentpages.php';
include 'm_pref.php'
?>

<title><?php echo ($wikinametitle ?? "SSWiki New Project") ?></title>

<h1><?php echo "Добро пожаловать на " . ($wikiname ?? "example wiki!"); ?></h1>
<div class="MainPage"><?php echo ($contentpage_0 ?? "Эта страница не содержит текста."); ?></div>
<?php
if ($userRole === 'verified') {
    echo '<button>Редактировать страницу</button>';
}
?>