<?php
$page_id = 0;
include 'contentpages.php';
include '../m_pref.php'
include 'cascad_stylesheet/divs.css'
?>

<h1><?php echo "Добро пожаловать на " . ($wikiname ?? "example wiki!"); ?></h1>
<div class="MainPage"><?php echo ($contentpage_0 ?? "Эта страница не содержит текста."); ?></div>
<?php
if ($userRole === 'verified') {
    echo '<button>Редактировать страницу</button>';
}
?>