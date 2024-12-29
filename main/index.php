<?php
$page_id = 0;
include 'contentpages.php';
include '../m_pref.php'
?>

<title><?php echo ($wikiname ?? "SSWiki New Project") ?></title>
<style>
    .MainPage {
    font-family: Arial, sans-serif; /* Шрифт, похожий на используемый */
    background-color: #f9f9f9; /* Светло-серый фон */
    border: 1px solid #ddd; /* Тонкая рамка */
    border-radius: 8px; /* Скругленные углы */
    padding: 20px; /* Внутренние отступы */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Тень для объема */
    max-width: 800px; /* Максимальная ширина */
    margin: 20px auto; /* Центрирование и отступы */
    line-height: 1.6; /* Удобный межстрочный интервал */
    color: #333; /* Тёмно-серый текст */
}

.MainPage h1 {
    font-size: 1.8em; /* Размер заголовка */
    color: #000; /* Чёрный цвет текста заголовка */
    border-bottom: 2px solid #b7b7b7; /* Полоса под заголовком */
    padding-bottom: 5px;
    margin-bottom: 15px;
}

.MainPage img {
    max-width: 100%; /* Подгонка изображения под контейнер */
    border-radius: 8px; /* Скругленные углы изображения */
    margin-bottom: 15px;
}

.MainPage a {
    color: #0066cc; /* Цвет ссылок */
    text-decoration: none; /* Убираем подчеркивание */
}

.MainPage a:hover {
    text-decoration: underline; /* Подчеркивание при наведении */
}

.MainPage p {
    margin: 10px 0; /* Отступы между абзацами */
}
</style>

<h1><?php echo "Добро пожаловать на " . ($wikiname ?? "example wiki!"); ?></h1>
<div class="MainPage"><?php echo ($contentpage_0 ?? "Эта страница не содержит текста."); ?></div>
<?php
if ($userRole === 'verified') {
    echo '<button>Редактировать страницу</button>';
}
?>