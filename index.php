<?php
$page_id = 0;
include 'main/contentpages.php';
include 'm_pref.php'
?>

<head>
    <title><?php echo ($wikinametitle ?? "SSWiki New Project") ?></title>
</head>

<body>
    <header>
        <img src="<?php echo $wikiImageHeader ?>" alt="Логотип вики-проекта">
    </header>
    <hr>
    <h1><?php echo ($pagename0 ?? "Заглавная страница") ?></h1>
    <hr>
    <h1><?php echo "Добро пожаловать на " . ($wikiname ?? "example wiki!"); ?></h1>
    <div class="MainPage"><?php echo ($contentpage_0 ?? "Эта страница не содержит текста."); ?></div>
    <?php
    if ($userRole === 'verified') {
        echo '<button>Редактировать страницу</button>';
    }
    ?>
</body>