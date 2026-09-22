from pathlib import Path
from html import escape
import json

ROOT = Path('mines-seo-site')
ASSETS = ROOT / 'assets'
OFFER = 'https://lkzq.cc/644450'
SITE = 'https://minesneon.ru/'

ASSETS.mkdir(parents=True, exist_ok=True)

pages = {
    'index.html': {
        'active': 'index.html',
        'title': 'Мины играть онлайн бесплатно — Mines demo, бот сигналов и бонус PIXELWIN',
        'description': 'Играйте в мины бесплатно в Mines demo 5×5, тестируйте сигналы, mines бот и стратегии перед переходом в mines casino с бонусом 500% по промокоду PIXELWIN.',
        'keywords': 'мины играть, играть в мины, Mines бесплатно, mines demo, mines демо, mines сигналы, бот мины, mines бот, mines bot, mines free, Mines land, mines взлом, мины на деньги',
        'h1': 'Мины играть онлайн: Mines бесплатно, демо-игра и бот сигналов',
        'lead': 'Тренируйтесь в симуляторе минных ячеек 5×5, проверяйте безопасные шаги и переходите к реальным коэффициентам только после того, как поймёте механику Mines.',
        'content': 'INDEX_CONTENT'
    },
    'promo.html': {
        'active': 'promo.html',
        'title': 'Mines промокоды PIXELWIN — VIP бонус 500% для игры мины на деньги',
        'description': 'Актуальный mines промокод PIXELWIN: получите VIP бонус 500% на депозит, активируйте предложение для Mines casino и начните играть в мины на деньги.',
        'keywords': 'mines промокоды, PIXELWIN, mines casino, мины на деньги, минес, майнес',
        'h1': 'Mines промокоды: VIP бонус 500% по коду PIXELWIN',
        'lead': 'Промокод PIXELWIN создан для игроков, которые хотят перейти из бесплатного режима к реальным ставкам с увеличенным стартовым балансом.',
        'content': 'PROMO_CONTENT'
    },
    'strategies.html': {
        'active': 'strategies.html',
        'title': 'Стратегии Mines: Safe Step, Зигзаг, Охотник, Мартингейл и RTP',
        'description': 'Разбор стратегий Mines: консервативная игра, зигзаг, охотник, мартингейл, RTP и честный подход к сигналам без мифов про mines взлом.',
        'keywords': 'стратегии Mines, mines взлом, Safe Step, Zigzag, Hunter, Martingale, RTP, минес, майнес',
        'h1': 'Стратегии игры Mines: от Safe Step до анализа RTP',
        'lead': 'Ни одна тактика не гарантирует выигрыш, но грамотное управление риском помогает дольше сохранять банкролл и выбирать подходящий коэффициент.',
        'content': 'STRATEGIES_CONTENT'
    },
    'faq.html': {
        'active': 'faq.html',
        'title': 'Mines отзывы и FAQ — честность игры, выплаты, сигналы и демо',
        'description': 'Ответы на частые вопросы про Mines: отзывы игроков, честность алгоритма, выплаты, сигналы, бот, демо-режим и безопасный старт в casino.',
        'keywords': 'mines отзывы, Mines FAQ, выплаты Mines, честность Mines, минес, майнес',
        'h1': 'Mines отзывы и часто задаваемые вопросы',
        'lead': 'Собрали ответы на главные вопросы о честности, выплатах, демо-режиме, сигналах и переходе к игре на реальные коэффициенты.',
        'content': 'FAQ_CONTENT'
    },
    'apk.html': {
        'active': 'apk.html',
        'title': 'Mines скачать на телефон — APK и PWA инструкция для Android и iOS',
        'description': 'Как mines скачать на смартфон: установка PWA, инструкция для Android Chrome и iPhone Safari, быстрый доступ к Mines demo, сигналам и бонусу PIXELWIN.',
        'keywords': 'mines скачать, скачать Mines, APK Mines, PWA Mines, mines бесплатно, минес, майнес',
        'h1': 'Mines скачать: APK/PWA инструкция для телефона',
        'lead': 'Добавьте Mines на главный экран смартфона и запускайте демо-игру, сигналы и страницу бонуса без поиска сайта в браузере.',
        'content': 'APK_CONTENT'
    },
}

nav = [
    ('index.html', 'Демо + сигналы', '🎮'),
    ('promo.html', 'Промокод 500%', '💎'),
    ('strategies.html', 'Стратегии', '📈'),
    ('faq.html', 'FAQ', '❓'),
    ('apk.html', 'Скачать APK', '📲'),
    ('home-en.html', 'Гайды', '📚'),
]

common_cta = f"""
<section class=\"cta-strip\" aria-label=\"Переход в казино\">
  <div>
    <strong>Готовы проверить коэффициенты на реальной платформе?</strong>
    <span>Активируйте PIXELWIN и получите до 500% к депозиту.</span>
  </div>
  <a class=\"btn btn-pulse\" href=\"{OFFER}\" rel=\"nofollow sponsored noopener\" target=\"_blank\">ПЕРЕЙТИ В КАЗИНО</a>
</section>
"""

content_map = {}
content_map['INDEX_CONTENT'] = f"""
<section class=\"hero-grid\">
  <div class=\"panel game-panel\">
    <div class=\"section-kicker\">mines demo • mines free • Mines land</div>
    <h2>Mines demo 5×5 — играть в мины бесплатно</h2>
    <p>Этот режим создан для тех, кто хочет <strong>играть в мины</strong> без депозита: выбирайте ставку, количество бомб и открывайте безопасные клетки. Демо помогает понять, как растёт коэффициент после каждого шага и почему важно вовремя забрать выигрыш.</p>
    <div class=\"demo-wallet\" aria-label=\"Демо баланс игрока\">
      <div>
        <span>Баланс</span>
        <strong id=\"balanceBox\">5 000</strong>
      </div>
      <div>
        <span>Возможный выигрыш</span>
        <strong id=\"profitBox\">0</strong>
      </div>
      <button class=\"wallet-reset\" id=\"resetBalanceBtn\" type=\"button\">Сбросить</button>
    </div>
    <div class=\"game-toolbar\">
      <label>Ставка <input id=\"betInput\" type=\"number\" value=\"100\" min=\"10\" inputmode=\"numeric\"></label>
      <label>Мины <select id=\"minesSelect\"><option>1</option><option selected>3</option><option>5</option><option>10</option></select></label>
      <div class=\"mult\" id=\"multBox\">x1.00</div>
    </div>
    <div class=\"game-status\" id=\"gameStatus\">Баланс сохраняется в браузере. Сделайте демо-ставку и заберите выигрыш до бомбы.</div>
    <div class=\"mines-grid\" id=\"demoGrid\" aria-label=\"Демо поле Mines\"></div>
    <button class=\"btn btn-main\" id=\"playBtn\">СДЕЛАТЬ СТАВКУ</button>
  </div>
  <div class=\"panel signal-panel\">
    <div class=\"section-kicker\">бот мины • mines bot • mines сигналы</div>
    <h2>Mines бот сигналов: безопасные клетки перед раундом</h2>
    <p>Блок сигналов показывает три вероятно безопасные ячейки. Это не <strong>mines взлом</strong> и не гарантия выигрыша, а тренировочный инструмент для анализа паттернов и дисциплины. Используйте его как подсказку, а не как обещание результата.</p>
    <div class=\"mines-grid signal-grid\" id=\"signalGrid\" aria-label=\"Поле сигналов Mines\"></div>
    <button class=\"btn btn-pulse\" id=\"signalBtn\">ПОЛУЧИТЬ СИГНАЛ</button>
    <a class=\"btn btn-ghost\" href=\"promo.html\">ЗАБРАТЬ БОНУС PIXELWIN</a>
  </div>
</section>
<section class=\"seo-block\">
  <h2>Как играть в мины онлайн: demo, сигналы и безопасная тренировка</h2>
  <p><strong>Мины играть</strong> лучше начинать не с депозита, а с понятного демо-режима. Mines demo показывает механику поля 5x5, где игрок открывает минные ячейки, ищет безопасный шаг и следит за ростом коэффициента после каждого успешного открытия. Такой формат помогает спокойно понять, как работает риск, почему количество бомб влияет на выплату и в какой момент разумнее фиксировать результат.</p>
  <p>На этой странице можно <strong>играть в мины</strong> бесплатно, тестировать Mines сигналы и сравнивать разные сценарии без давления реального баланса. Блок сигналов работает как тренировочный mines бот: он подсвечивает вероятно безопасные клетки, чтобы игрок видел логику выбора и учился не нажимать хаотично. Это не mines взлом и не обещание гарантированного выигрыша, а инструмент для анализа, дисциплины и более осознанной игры.</p>
  <p><strong>Mines бесплатно</strong> особенно полезен новичкам, которые только знакомятся с краш-игрой, RTP, коэффициентами и безопасными шагами. Начните с 1-3 мин, открывайте по 2-4 клетки за раунд и следите, как меняется множитель. После нескольких сессий станет понятнее, чем отличается осторожная стратегия от агрессивной игры с большим количеством бомб.</p>
  <ul>
    <li><strong>mines demo</strong> помогает изучить правила без депозита;</li>
    <li><strong>бот мины</strong> показывает подсказки для тренировки безопасных клеток;</li>
    <li><strong>mines bot</strong> и mines сигналы стоит использовать только вместе с лимитами;</li>
    <li><strong>мины на деньги</strong> подходят после практики и понимания риска.</li>
  </ul>
  <p>Если демо-игра уже понятна, а безопасные шаги и коэффициенты не вызывают вопросов, можно переходить к реальному формату. Для старта используйте <a href=\"https://lkzq.cc/644450\" rel=\"nofollow sponsored noopener\" target=\"_blank\">партнёрский переход в mines casino с бонусом PIXELWIN</a>, заранее установите лимит сессии и не играйте без стратегии.</p>
</section>
{common_cta}
"""

content_map['PROMO_CONTENT'] = f"""
<section class=\"promo-hero panel\">
  <div class=\"badge\">VIP BONUS • LIMITED</div>
  <h2>Промокод PIXELWIN</h2>
  <p>Скопируйте код и используйте его при регистрации, чтобы активировать расширенный приветственный бонус для игры Mines.</p>
  <button class=\"promo-code\" id=\"copyPromo\" data-code=\"PIXELWIN\">PIXELWIN</button>
  <a class=\"btn btn-pulse btn-xl\" href=\"{OFFER}\" rel=\"nofollow sponsored noopener\" target=\"_blank\">ЗАБРАТЬ БОНУС 500%</a>
</section>
<section class=\"seo-block\">
  <h2>Mines промокоды: как активировать PIXELWIN и получить бонус 500%</h2>
  <p><strong>Mines промокоды</strong> нужны игрокам, которые хотят перейти от бесплатного демо к реальной игре с увеличенным стартовым балансом. Промокод PIXELWIN открывает VIP-бонус до 500%, поэтому его выгодно использовать перед первым депозитом, особенно если вы планируете тестировать Mines casino, разные коэффициенты и стратегии управления банкроллом.</p>
  <p>Страница промокода создана для игроков, которые уже понимают базовую механику минес: поле 5x5, безопасные клетки, бомбы, cashout и зависимость выплаты от риска. Когда вы переходите в <strong>мины на деньги</strong>, бонус помогает распределить депозит на большее количество коротких раундов. Это снижает давление на одну ставку и позволяет аккуратнее сравнивать тактики Safe Step, зигзаг или игру с повышенным числом мин.</p>
  <p>Чтобы активировать предложение, перейдите по партнёрской ссылке, зарегистрируйтесь, введите <strong>PIXELWIN</strong> в поле промокода и внимательно проверьте условия бонуса. Важно учитывать вейджер, лимиты вывода, минимальный депозит и правила ставок. Бонус не отменяет риск, но делает старт более комфортным для тех, кто играет дисциплинированно.</p>
  <ul>
    <li><strong>PIXELWIN</strong> — основной промокод для VIP-бонуса 500%;</li>
    <li><strong>mines casino</strong> подходит для реальных коэффициентов и быстрых раундов;</li>
    <li><strong>мины на деньги</strong> требуют лимита, стоп-лосса и раннего cashout;</li>
    <li>перед депозитом стоит протестировать Mines demo и сигналы.</li>
  </ul>
  <p>Готовы забрать бонус и проверить реальные коэффициенты? Используйте <a href=\"https://lkzq.cc/644450\" rel=\"nofollow sponsored noopener\" target=\"_blank\">официальный партнёрский редирект с промокодом PIXELWIN</a> и начинайте с небольших ставок, а не с максимального риска.</p>
</section>
{common_cta}
"""

content_map['STRATEGIES_CONTENT'] = f"""
<section class=\"cards\">
  <article class=\"card\"><h2>Консервативная стратегия Safe Step</h2><p><strong>1–3 мины</strong>, 2–3 открытия и ранний cashout. Подходит для новичков, которые хотят снизить дисперсию.</p></article>
  <article class=\"card\"><h2>Зигзаг</h2><p>Открывайте клетки диагонально или Z-образно, не концентрируясь в одном углу поля. Метод дисциплинирует и снижает хаотичные клики.</p></article>
  <article class=\"card\"><h2>Охотник</h2><p><strong>5–10 мин</strong>, минимальная ставка и цель поймать высокий коэффициент. Риск выше, поэтому лимит обязателен.</p></article>
  <article class=\"card\"><h2>Мартингейл</h2><p>Удвоение после проигрыша может быстро съесть банкролл. Используйте только в демо и не считайте систему гарантией.</p></article>
</section>
<section class=\"seo-block\">
  <h2>Стратегии Mines: Safe Step, зигзаг, охотник, мартингейл и RTP</h2>
  <p>Стратегии Mines не дают стопроцентной гарантии выигрыша, но помогают играть осознаннее. В этой краш-игре каждый раунд строится вокруг выбора минных ячеек: чем больше бомб на поле, тем выше коэффициент, но тем меньше безопасных шагов. Поэтому главная задача игрока — не искать мифический <strong>mines взлом</strong>, а контролировать риск, ставку, количество открытий и момент фиксации результата.</p>
  <p><strong>Safe Step</strong> подходит новичкам: выбирайте 1-3 мины, открывайте 2-3 клетки и забирайте небольшой множитель. Стратегия зигзаг помогает структурировать выбор клеток и не нажимать случайно. Охотник — более агрессивный подход с 5-10 минами и минимальной ставкой ради высокого коэффициента. Мартингейл в Mines стоит использовать только в демо, потому что удвоение после проигрыша быстро увеличивает нагрузку на банкролл.</p>
  <p>Опытные игроки дополнительно смотрят на RTP, волатильность, длину сессии и историю собственных решений. Mines сигналы или mines bot могут быть полезны как вспомогательная аналитика, но не должны заменять лимиты. Если инструмент показывает безопасные клетки, воспринимайте это как подсказку для тренировки, а не как гарантированный прогноз.</p>
  <ul>
    <li><strong>Safe Step</strong> — низкий риск и ранний cashout;</li>
    <li><strong>Зигзаг</strong> — дисциплина выбора клеток и контроль темпа;</li>
    <li><strong>Охотник</strong> — высокий риск ради крупного множителя;</li>
    <li><strong>RTP-анализ</strong> — понимание дистанции, а не результата одной ставки.</li>
  </ul>
  <p>После тренировки в демо можно применить выбранную стратегию в реальном Mines casino. Для более комфортного старта активируйте <a href=\"https://lkzq.cc/644450\" rel=\"nofollow sponsored noopener\" target=\"_blank\">бонус PIXELWIN через партнёрскую ссылку</a>, заранее задайте лимит и не повышайте ставку после эмоционального проигрыша.</p>
</section>
{common_cta}
"""

content_map['FAQ_CONTENT'] = f"""
<section class=\"faq-list\">
  <details open><summary><h2>Честная ли игра Mines?</h2></summary><p>В лицензированных казино результат раунда формируется алгоритмом RNG или Provably Fair. Проверяйте правила площадки, лимиты и историю ставок.</p></details>
  <details><summary><h2>Что говорят mines отзывы?</h2></summary><p><strong>Mines отзывы</strong> чаще всего выделяют быстрый темп, простую механику и высокий риск при большом количестве бомб. Положительный опыт связан с лимитами, а негативный — с погоней за коэффициентом.</p></details>
  <details><summary><h2>Сигналы гарантируют выигрыш?</h2></summary><p>Нет. Сигналы — подсказка для тренировки и CRO-элемент, а не гарантия. Используйте их вместе с демо, лимитом ставки и ранним cashout.</p></details>
  <details><summary><h2>Как быстро проходят выплаты?</h2></summary><p>Скорость зависит от casino, метода оплаты и верификации. Перед депозитом изучайте правила вывода, минимальную сумму и комиссии.</p></details>
</section>
<section class=\"seo-block\">
  <h2>Mines FAQ: отзывы, честность игры, выплаты, сигналы и бонусы</h2>
  <p>Раздел FAQ отвечает на главные вопросы игроков, которые изучают <strong>mines отзывы</strong>, демо-режим, сигналы и реальные выплаты. Mines — это быстрая краш-игра с полем 5x5, где результат зависит от выбранных клеток, количества мин и момента cashout. Формат кажется простым, но без лимитов легко начать открывать лишние ячейки ради большего коэффициента и потерять банкролл.</p>
  <p>Честность игры в лицензированных казино обычно обеспечивается RNG или Provably Fair-механикой. Это означает, что результат раунда нельзя узнать заранее и нельзя изменить через сторонний mines bot. Поэтому запросы вроде mines взлом лучше воспринимать критически: безопаснее изучать правила, RTP, условия бонусов и собственную статистику, чем доверять обещаниям гарантированного выигрыша.</p>
  <p>Сигналы Mines могут быть полезны в демо и как вспомогательная подсказка, но они не гарантируют выплату. Если вы используете mines сигналы, сочетайте их с небольшой ставкой, короткой серией открытий и заранее выбранным стоп-лоссом. Перед игрой на реальные деньги обязательно проверьте минимальный депозит, лимиты вывода, сроки обработки заявок и требования верификации.</p>
  <ul>
    <li><strong>mines отзывы</strong> помогают понять опыт других игроков, но не заменяют правила casino;</li>
    <li><strong>Mines demo</strong> нужен для тренировки без депозита;</li>
    <li><strong>mines сигналы</strong> стоит воспринимать как подсказку, а не гарантию;</li>
    <li><strong>мины на деньги</strong> требуют ответственного подхода и лимитов.</li>
  </ul>
  <p>Если вы уже разобрались с FAQ и готовы попробовать реальные коэффициенты, переходите через <a href=\"https://lkzq.cc/644450\" rel=\"nofollow sponsored noopener\" target=\"_blank\">партнёрскую ссылку с промокодом PIXELWIN</a>. Бонус увеличит стартовый баланс, но стратегия и контроль риска остаются главным условием комфортной игры.</p>
</section>
{common_cta}
"""

content_map['APK_CONTENT'] = f"""
<section class=\"cards install-cards\">
  <article class=\"card\"><h2>Android Chrome</h2><ol><li>Откройте сайт в Chrome.</li><li>Нажмите меню ⋮.</li><li>Выберите «Добавить на главный экран» или «Установить приложение».</li></ol></article>
  <article class=\"card\"><h2>iPhone Safari</h2><ol><li>Откройте страницу в Safari.</li><li>Нажмите «Поделиться».</li><li>Выберите «На экран Домой».</li></ol></article>
  <article class=\"card\"><h2>Быстрый доступ</h2><p>PWA открывается как приложение: демо, сигналы, промокод и FAQ остаются под рукой без поиска в браузере.</p></article>
</section>
<section class=\"seo-block\">
  <h2>Как mines скачать и установить без лишнего риска</h2>
  <p>Запрос <strong>mines скачать</strong> часто приводит на сомнительные APK-файлы. Более безопасный вариант — PWA: сайт добавляется на главный экран, работает как приложение и не требует установки неизвестного пакета из стороннего источника.</p>
  <p>Если вам нужен именно APK, скачивайте его только с официальной страницы казино после регистрации. Так вы снижаете риск подмены файла, фишинга и потери доступа к аккаунту.</p>
  <ul>
    <li><strong>Android</strong>: используйте Chrome и функцию установки PWA;</li>
    <li><strong>iOS</strong>: добавляйте сайт через Safari;</li>
    <li><strong>Mines бесплатно</strong>: тестируйте demo до депозита;</li>
    <li><strong>PIXELWIN</strong>: активируйте бонус перед игрой на деньги.</li>
  </ul>
  <p>Установили ярлык и готовы открыть реальные раунды? Перейдите на <a href=\"{OFFER}\" rel=\"nofollow sponsored noopener\" target=\"_blank\">официальную партнёрскую страницу казино</a>, используйте промокод и скачивайте приложение только внутри аккаунта.</p>
</section>
{common_cta}
"""

content_map['OTHER_CONTENT'] = f"""
<section class=\"cards games\">
  <article class=\"card game-card\"><span>🚀</span><h2>Lucky Jet</h2><p>Классический crash с растущим коэффициентом и быстрым cashout.</p><a href=\"{OFFER}\" rel=\"nofollow sponsored noopener\" target=\"_blank\">Открыть</a></article>
  <article class=\"card game-card\"><span>⚡</span><h2>Speed and Cash</h2><p>Динамичный формат для коротких сессий и быстрой фиксации результата.</p><a href=\"{OFFER}\" rel=\"nofollow sponsored noopener\" target=\"_blank\">Открыть</a></article>
  <article class=\"card game-card\"><span>👑</span><h2>Rocket Queen</h2><p>Яркая краш-игра с понятной механикой коэффициента.</p><a href=\"{OFFER}\" rel=\"nofollow sponsored noopener\" target=\"_blank\">Открыть</a></article>
  <article class=\"card game-card\"><span>✈️</span><h2>Aviator</h2><p>Популярный аналог Mines для тех, кто любит управлять моментом выхода.</p><a href=\"{OFFER}\" rel=\"nofollow sponsored noopener\" target=\"_blank\">Открыть</a></article>
</section>
<section class=\"seo-block\">
  <h2>Краш-игры как альтернатива Mines casino</h2>
  <p>Mines привлекает контролем над каждым кликом, а другие краш-игры делают акцент на тайминге: коэффициент растёт, и игрок решает, когда забрать результат. Lucky Jet, Speed and Cash и Rocket Queen подходят тем, кто хочет чередовать форматы и не зацикливаться на одной механике.</p>
  <p>Главный принцип одинаков: не гонитесь за максимальным множителем каждый раунд. Используйте лимиты, фиксируйте небольшой профит и помните, что высокая отдача RTP работает только на длинной дистанции, а не в одной ставке.</p>
  <ul>
    <li>выбирайте игры с понятными правилами;</li>
    <li>сравнивайте волатильность и минимальную ставку;</li>
    <li>тестируйте демо, если оно доступно;</li>
    <li>используйте бонус PIXELWIN для расширения стартового банка.</li>
  </ul>
  <p>Хотите попробовать Mines и соседние краш-форматы на одной площадке? <a href=\"{OFFER}\" rel=\"nofollow sponsored noopener\" target=\"_blank\">Откройте казино через партнёрский редирект</a> и активируйте бонус перед депозитом.</p>
</section>
{common_cta}
"""

style = r'''
:root{
  color-scheme:dark;
  --bg:#070a12;
  --bg-2:#0b1020;
  --surface:#0f172a;
  --surface-2:#111c33;
  --surface-3:#17233d;
  --glass:rgba(15,23,42,.72);
  --glass-strong:rgba(17,28,51,.86);
  --line:rgba(226,232,240,.10);
  --line-strong:rgba(226,232,240,.18);
  --text:#f8fafc;
  --text-soft:#e5edf8;
  --muted:#a8b3c7;
  --muted-2:#77849a;
  --primary:#54f0c1;
  --primary-2:#6ee7f9;
  --violet:#8b7cff;
  --pink:#ff73d2;
  --gold:#ffd166;
  --danger:#ff5d7a;
  --success:#7af0a3;
  --radius-xl:30px;
  --radius:22px;
  --radius-md:18px;
  --radius-sm:14px;
  --shadow-xl:0 32px 90px rgba(0,0,0,.48);
  --shadow:0 20px 54px rgba(0,0,0,.34);
  --shadow-soft:0 12px 34px rgba(0,0,0,.24);
  --container:1140px;
}

*{box-sizing:border-box}
*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;text-rendering:optimizeLegibility}
body{
  margin:0;
  min-width:320px;
  font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
  color:var(--text);
  background:
    radial-gradient(circle at 8% -12%,rgba(84,240,193,.24),transparent 31rem),
    radial-gradient(circle at 96% 0%,rgba(139,124,255,.22),transparent 32rem),
    radial-gradient(circle at 70% 46%,rgba(255,115,210,.08),transparent 28rem),
    linear-gradient(180deg,#070a12 0%,#0b1020 44%,#060912 100%);
  overflow-x:hidden;
  line-height:1.62;
}
body::before{
  content:"";
  position:fixed;
  inset:0;
  pointer-events:none;
  z-index:-1;
  background:
    linear-gradient(rgba(255,255,255,.018) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,255,255,.018) 1px,transparent 1px);
  background-size:44px 44px;
  mask-image:linear-gradient(180deg,rgba(0,0,0,.75),transparent 72%);
}
body::after{
  content:"";
  position:fixed;
  inset:0;
  pointer-events:none;
  z-index:-1;
  background:radial-gradient(circle at 50% 0%,rgba(255,255,255,.08),transparent 38rem);
  mix-blend-mode:screen;
}

a{color:#7cf4d2;text-decoration:none;text-underline-offset:4px;text-decoration-thickness:1px}
a:hover{text-decoration:underline}
button,input,select{font:inherit}
button{-webkit-tap-highlight-color:transparent}

.site{display:grid;grid-template-columns:274px minmax(0,1fr);min-height:100dvh;isolation:isolate}
.sidebar{
  position:sticky;
  top:0;
  height:100dvh;
  padding:22px 17px;
  border-right:1px solid var(--line);
  background:linear-gradient(180deg,rgba(8,12,24,.86),rgba(8,12,24,.72));
  backdrop-filter:blur(22px) saturate(145%);
  -webkit-backdrop-filter:blur(22px) saturate(145%);
  z-index:20;
}
.sidebar::before{
  content:"";
  position:absolute;
  inset:14px 10px auto;
  height:156px;
  border-radius:26px;
  background:linear-gradient(135deg,rgba(84,240,193,.11),rgba(139,124,255,.10));
  filter:blur(0);
  z-index:-1;
}
.brand{
  display:flex;
  align-items:center;
  gap:13px;
  margin-bottom:24px;
  padding:8px 7px;
  color:var(--text);
}
.brand:hover{text-decoration:none}
.brand-logo{
  position:relative;
  display:grid;
  place-items:center;
  flex:0 0 auto;
  width:48px;
  height:48px;
  border-radius:17px;
  background:
    linear-gradient(135deg,rgba(84,240,193,.96),rgba(110,231,249,.82) 48%,rgba(139,124,255,.92));
  color:#06111d;
  box-shadow:0 16px 38px rgba(84,240,193,.18),inset 0 1px 0 rgba(255,255,255,.42);
  font-size:23px;
}
.brand-logo::after{
  content:"";
  position:absolute;
  inset:-5px;
  border:1px solid rgba(84,240,193,.18);
  border-radius:22px;
}
.brand strong{display:block;font-size:20px;letter-spacing:-.035em;color:#fff;line-height:1.05}
.brand span span{display:block;margin-top:3px;color:var(--muted);font-size:12px;line-height:1.25}

.nav{display:grid;gap:9px}
.nav a{
  position:relative;
  min-height:48px;
  display:flex;
  align-items:center;
  gap:11px;
  padding:12px 14px;
  border:1px solid transparent;
  border-radius:17px;
  color:#dce6f5;
  background:rgba(255,255,255,.028);
  transition:transform .18s ease,background .18s ease,border-color .18s ease,color .18s ease,box-shadow .18s ease;
}
.nav a span{display:grid;place-items:center;width:26px;height:26px;border-radius:10px;background:rgba(255,255,255,.055);font-size:15px}
.nav a.active{
  color:#fff;
  border-color:rgba(84,240,193,.24);
  background:linear-gradient(135deg,rgba(84,240,193,.13),rgba(139,124,255,.10));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 12px 28px rgba(0,0,0,.16);
}
.nav a.active::before{
  content:"";
  position:absolute;
  left:-1px;
  top:12px;
  bottom:12px;
  width:3px;
  border-radius:999px;
  background:linear-gradient(180deg,var(--primary),var(--violet));
}
.nav a:hover{transform:translateX(3px);color:#fff;border-color:rgba(255,255,255,.12);background:rgba(255,255,255,.055);text-decoration:none}

.side-cta{
  position:relative;
  margin-top:18px;
  padding:16px;
  overflow:hidden;
  border:1px solid rgba(255,209,102,.22);
  border-radius:22px;
  background:
    linear-gradient(145deg,rgba(255,209,102,.13),rgba(139,124,255,.08)),
    rgba(255,255,255,.035);
  box-shadow:var(--shadow-soft);
}
.side-cta::before{
  content:"";
  position:absolute;
  width:140px;
  height:140px;
  right:-70px;
  top:-70px;
  border-radius:999px;
  background:rgba(255,209,102,.18);
  filter:blur(18px);
}
.side-cta b{position:relative;display:block;margin-bottom:12px;color:#fff;font-size:14px;line-height:1.35}

.main{position:relative;min-width:0}
.main::before{
  content:"";
  position:absolute;
  top:88px;
  right:4vw;
  width:min(44vw,560px);
  height:min(44vw,560px);
  border-radius:999px;
  background:radial-gradient(circle,rgba(84,240,193,.09),transparent 64%);
  pointer-events:none;
  z-index:-1;
}
.topbar{
  position:sticky;
  top:0;
  z-index:10;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:16px;
  min-height:72px;
  padding:12px max(18px,env(safe-area-inset-left)) 12px clamp(18px,4vw,44px);
  padding-right:max(clamp(18px,4vw,44px),env(safe-area-inset-right));
  border-bottom:1px solid var(--line);
  background:rgba(7,10,18,.66);
  backdrop-filter:blur(22px) saturate(160%);
  -webkit-backdrop-filter:blur(22px) saturate(160%);
}
.topbar small{
  display:inline-flex;
  align-items:center;
  gap:10px;
  color:#d2dcec;
  font-size:13px;
  font-weight:650;
  letter-spacing:-.01em;
}
.topbar small::before{
  content:"18+";
  display:inline-flex;
  align-items:center;
  justify-content:center;
  min-width:38px;
  height:30px;
  padding:0 9px;
  border-radius:999px;
  color:#fff;
  background:linear-gradient(135deg,rgba(255,93,122,.22),rgba(255,115,210,.14));
  border:1px solid rgba(255,93,122,.28);
  font-weight:900;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08);
}
.container{width:min(var(--container),100%);margin:0 auto;padding:clamp(22px,4vw,46px)}
.hero{position:relative;padding:14px 0 30px}
.hero::after{
  content:"";
  display:block;
  width:86px;
  height:4px;
  margin-top:22px;
  border-radius:999px;
  background:linear-gradient(90deg,var(--primary),var(--violet),transparent);
}
.section-kicker,.badge{
  display:inline-flex;
  align-items:center;
  gap:8px;
  margin-bottom:13px;
  padding:8px 12px;
  border:1px solid rgba(84,240,193,.22);
  border-radius:999px;
  color:#9af6df;
  background:linear-gradient(135deg,rgba(84,240,193,.105),rgba(110,231,249,.045));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06);
  font-size:11px;
  font-weight:900;
  text-transform:uppercase;
  letter-spacing:.085em;
}
h1{
  margin:0 0 15px;
  max-width:980px;
  font-size:clamp(34px,5.6vw,68px);
  line-height:.99;
  letter-spacing:-.065em;
  color:#fff;
  text-wrap:balance;
}
h2{margin:0 0 12px;font-size:clamp(23px,3.1vw,36px);line-height:1.1;letter-spacing:-.045em;color:#fff;text-wrap:balance}
p{margin:0 0 16px;color:#d8e1ef}
.lead{max-width:840px;color:#b9c6d8;font-size:clamp(17px,2.15vw,22px);line-height:1.58;text-wrap:pretty}

.btn{
  position:relative;
  min-height:50px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:10px;
  padding:14px 19px;
  overflow:hidden;
  border:0;
  border-radius:16px;
  color:#06101d;
  font-weight:950;
  letter-spacing:.012em;
  text-transform:uppercase;
  cursor:pointer;
  touch-action:manipulation;
  text-align:center;
  transform:translateZ(0);
  transition:transform .18s ease,filter .18s ease,box-shadow .18s ease,border-color .18s ease;
}
.btn::before{
  content:"";
  position:absolute;
  inset:0;
  opacity:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.36),transparent);
  transform:translateX(-120%);
  transition:opacity .2s ease,transform .55s ease;
}
.btn:hover::before{opacity:1;transform:translateX(120%)}
.btn:hover{text-decoration:none;transform:translateY(-2px);filter:brightness(1.04)}
.btn-pulse,.btn-main{
  background:linear-gradient(135deg,#5cf0c3 0%,#6ee7f9 46%,#9a8cff 100%);
  box-shadow:0 14px 34px rgba(84,240,193,.20),0 0 0 0 rgba(84,240,193,.26),inset 0 1px 0 rgba(255,255,255,.45);
  animation:pulseLux 2.35s infinite;
}
.btn-ghost{background:rgba(255,255,255,.055);color:#eef5ff;border:1px solid var(--line-strong);box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}
.btn-xl{width:min(100%,430px);min-height:60px;font-size:17px;border-radius:18px}

.panel,.card,.seo-block,.cta-strip{
  position:relative;
  border:1px solid var(--line);
  border-radius:var(--radius-xl);
  background:
    linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.025)),
    linear-gradient(145deg,rgba(17,28,51,.92),rgba(10,16,31,.92));
  box-shadow:var(--shadow),inset 0 1px 0 rgba(255,255,255,.065);
}
.panel::before,.card::before,.seo-block::before,.cta-strip::before{
  content:"";
  position:absolute;
  inset:0;
  border-radius:inherit;
  padding:1px;
  background:linear-gradient(135deg,rgba(84,240,193,.20),rgba(139,124,255,.12),rgba(255,255,255,0));
  mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite:exclude;
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;
  pointer-events:none;
}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.13fr) minmax(min(318px,100%),.87fr);gap:20px;align-items:start}
.panel{padding:clamp(18px,2.6vw,28px)}
.game-panel{overflow:hidden;background:linear-gradient(160deg,rgba(84,240,193,.085),rgba(139,124,255,.07) 38%,rgba(17,28,51,.92)),linear-gradient(145deg,rgba(17,28,51,.95),rgba(8,13,26,.96))}
.game-panel > *{position:relative;z-index:1}
.game-panel::after,.signal-panel::after,.promo-hero::after{
  content:"";
  position:absolute;
  width:210px;
  height:210px;
  right:-82px;
  top:-86px;
  border-radius:999px;
  background:radial-gradient(circle,rgba(84,240,193,.14),transparent 68%);
  pointer-events:none;
}
.signal-panel::after{background:radial-gradient(circle,rgba(139,124,255,.16),transparent 68%)}

.demo-wallet{
  position:relative;
  z-index:1;
  display:grid;
  grid-template-columns:1fr 1fr auto;
  gap:10px;
  margin:18px 0 14px;
  padding:12px;
  border:1px solid rgba(84,240,193,.17);
  border-radius:22px;
  background:linear-gradient(135deg,rgba(84,240,193,.11),rgba(139,124,255,.075)),rgba(4,8,18,.42);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 16px 36px rgba(0,0,0,.18);
}
.demo-wallet div{min-width:0;padding:10px 12px;border-radius:16px;background:rgba(255,255,255,.045);border:1px solid rgba(226,232,240,.09)}
.demo-wallet span{display:block;color:#9eacc3;font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.06em}
.demo-wallet strong{display:block;margin-top:5px;color:#f7fbff;font-size:clamp(20px,3.8vw,30px);line-height:1;font-weight:1000;letter-spacing:-.04em}
.demo-wallet strong::after{content:" ₽";color:#7cf4d2;font-size:.58em;letter-spacing:0}
.wallet-reset{align-self:stretch;min-height:50px;padding:10px 14px;border:1px solid rgba(255,255,255,.12);border-radius:16px;background:rgba(255,255,255,.06);color:#dbe7f6;font-weight:950;cursor:pointer}
.wallet-reset:hover{border-color:rgba(84,240,193,.25);color:#fff;background:rgba(84,240,193,.09)}
.game-toolbar{display:grid;grid-template-columns:1fr 1fr auto;gap:11px;margin:14px 0 10px}
.game-toolbar label{display:grid;gap:7px;color:#aebbd0;font-size:13px;font-weight:750}
.game-toolbar input,.game-toolbar select{
  width:100%;
  min-height:47px;
  border:1px solid rgba(226,232,240,.14);
  border-radius:15px;
  background:rgba(4,8,18,.58);
  color:var(--text);
  padding:10px 13px;
  font-size:16px;
  outline:none;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.04);
}
.game-toolbar input:focus,.game-toolbar select:focus{border-color:rgba(84,240,193,.55);box-shadow:0 0 0 4px rgba(84,240,193,.10),inset 0 1px 0 rgba(255,255,255,.05)}
.mult{
  display:grid;
  place-items:center;
  min-width:88px;
  min-height:47px;
  border-radius:15px;
  background:linear-gradient(135deg,rgba(84,240,193,.14),rgba(110,231,249,.08));
  border:1px solid rgba(84,240,193,.16);
  color:#9af6df;
  font-weight:1000;
}
.game-status{min-height:44px;display:flex;align-items:center;margin:0 0 14px;padding:11px 13px;border:1px solid rgba(110,231,249,.13);border-radius:16px;background:rgba(4,8,18,.38);color:#c8d5e7;font-size:13px;font-weight:750;line-height:1.35}
.mines-grid{width:min(100%,416px);display:grid;grid-template-columns:repeat(5,1fr);gap:clamp(7px,1.45vw,11px);margin:18px auto 20px;padding:10px;border-radius:24px;background:rgba(0,0,0,.13);border:1px solid rgba(226,232,240,.055)}
.cell{
  aspect-ratio:1;
  border:1px solid rgba(226,232,240,.115);
  border-radius:18px;
  background:
    radial-gradient(circle at 32% 22%,rgba(255,255,255,.08),transparent 30%),
    linear-gradient(145deg,#1a2944,#0d1528 72%);
  box-shadow:inset 0 -8px 16px rgba(0,0,0,.25),inset 0 1px 0 rgba(255,255,255,.06),0 9px 18px rgba(0,0,0,.18);
  display:grid;
  place-items:center;
  font-size:clamp(19px,5vw,31px);
  font-weight:950;
  color:#fff;
  cursor:pointer;
  user-select:none;
  transition:transform .16s ease,border-color .16s ease,box-shadow .16s ease,background .16s ease;
}
.cell:hover{transform:translateY(-2px);border-color:rgba(84,240,193,.28);box-shadow:inset 0 -8px 16px rgba(0,0,0,.25),0 12px 26px rgba(84,240,193,.09)}
.cell.safe,.cell.gem{background:linear-gradient(145deg,#62f0c5,#79e8f7 52%,#9c91ff);color:#05101d;box-shadow:0 14px 28px rgba(84,240,193,.20),inset 0 1px 0 rgba(255,255,255,.45)}
.cell.mine{background:linear-gradient(145deg,#ff6b86,#9c2c45);color:#fff;box-shadow:0 14px 28px rgba(255,93,122,.18),inset 0 1px 0 rgba(255,255,255,.18)}
.signal-grid .cell{cursor:default}
.signal-grid .cell:hover{transform:none}

.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.card{padding:23px;overflow:hidden;transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease}
.card:hover{transform:translateY(-3px);border-color:rgba(84,240,193,.20);box-shadow:0 24px 60px rgba(0,0,0,.36)}
.card h2{font-size:24px}.card span{display:inline-grid;place-items:center;width:48px;height:48px;margin-bottom:12px;border-radius:16px;background:rgba(84,240,193,.10);font-size:28px}.card a{font-weight:950}
.seo-block{margin-top:20px;padding:clamp(19px,3vw,32px)}
.seo-block p{color:#d6dfed;text-wrap:pretty}
.seo-block ul{padding-left:20px;color:#d6dfed}.seo-block li{margin:9px 0}.seo-block strong{color:#fff}.seo-block a{font-weight:850}
.cta-strip{
  margin-top:20px;
  padding:20px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:18px;
  overflow:hidden;
  background:
    linear-gradient(135deg,rgba(84,240,193,.14),rgba(139,124,255,.12)),
    rgba(255,255,255,.035);
}
.cta-strip > div{position:relative;z-index:1}.cta-strip strong{display:block;font-size:18px;letter-spacing:-.02em}.cta-strip span{display:block;margin-top:4px;color:var(--muted)}
.promo-hero{text-align:center;display:grid;justify-items:center;gap:14px;overflow:hidden}
.promo-code{
  position:relative;
  min-height:70px;
  padding:12px 30px;
  border:1px dashed rgba(255,209,102,.62);
  border-radius:22px;
  background:linear-gradient(135deg,rgba(255,209,102,.13),rgba(255,255,255,.035));
  color:#ffd166;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 16px 34px rgba(255,209,102,.08);
  font-size:clamp(34px,8vw,60px);
  font-weight:1000;
  letter-spacing:.12em;
  cursor:pointer;
}
.faq-list{display:grid;gap:13px}
.faq-list details{border:1px solid var(--line);border-radius:22px;background:rgba(17,28,51,.72);padding:17px 18px;box-shadow:inset 0 1px 0 rgba(255,255,255,.045)}
.faq-list details[open]{border-color:rgba(84,240,193,.18);background:linear-gradient(180deg,rgba(84,240,193,.06),rgba(17,28,51,.78))}
.faq-list summary{cursor:pointer;list-style:none}.faq-list summary::-webkit-details-marker{display:none}.faq-list summary h2{display:inline;font-size:22px}
.footer{padding:30px clamp(18px,4vw,44px);border-top:1px solid var(--line);color:var(--muted);font-size:13px;background:rgba(0,0,0,.10)}
.toast{position:fixed;left:50%;bottom:max(18px,env(safe-area-inset-bottom));transform:translateX(-50%) translateY(120px);z-index:80;max-width:min(92vw,520px);padding:13px 18px;border-radius:999px;background:#f8fafc;color:#06101d;font-weight:950;transition:.25s;box-shadow:var(--shadow-soft);text-align:center}
.toast.show{transform:translateX(-50%) translateY(0)}

@keyframes pulseLux{
  0%{box-shadow:0 14px 34px rgba(84,240,193,.20),0 0 0 0 rgba(84,240,193,.26),inset 0 1px 0 rgba(255,255,255,.45)}
  68%{box-shadow:0 14px 34px rgba(84,240,193,.20),0 0 0 12px rgba(84,240,193,0),inset 0 1px 0 rgba(255,255,255,.45)}
  100%{box-shadow:0 14px 34px rgba(84,240,193,.20),0 0 0 0 rgba(84,240,193,0),inset 0 1px 0 rgba(255,255,255,.45)}
}

@media (max-width:1080px){
  .site{grid-template-columns:252px minmax(0,1fr)}
  .hero-grid{grid-template-columns:1fr}
}

@media (max-width:980px){
  .site{display:block}
  .sidebar{
    position:relative;
    height:auto;
    padding:12px max(12px,env(safe-area-inset-left)) 9px;
    padding-right:max(12px,env(safe-area-inset-right));
    border-right:0;
    border-bottom:1px solid var(--line);
    background:rgba(7,10,18,.88);
  }
  .sidebar::before{display:none}
  .brand{margin-bottom:10px;padding:3px 2px}.brand-logo{width:42px;height:42px;border-radius:15px;font-size:20px}.brand-logo::after{display:none}.brand strong{font-size:18px}.brand span span{font-size:11px}
  .nav{display:flex;overflow-x:auto;padding:2px 1px 9px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;gap:8px}
  .nav::-webkit-scrollbar{display:none}
  .nav a{flex:0 0 auto;min-height:43px;padding:9px 13px;border-radius:999px;scroll-snap-align:start;font-size:14px;background:rgba(255,255,255,.045);white-space:nowrap}
  .nav a span{width:24px;height:24px;border-radius:999px;font-size:14px}.nav a.active::before{display:none}.nav a:hover{transform:none}
  .side-cta{display:none}
  .topbar{position:relative;min-height:auto;padding:12px max(12px,env(safe-area-inset-right)) 12px max(12px,env(safe-area-inset-left));background:rgba(7,10,18,.78)}
  .topbar small{font-size:12px;line-height:1.35}.topbar small::before{min-width:35px;height:28px}
  .topbar .btn{min-height:45px;padding:11px 14px;font-size:13px;white-space:nowrap;border-radius:14px}
  .cards{grid-template-columns:1fr}.cta-strip{align-items:stretch;flex-direction:column}.cta-strip .btn{width:100%}
}

@media (max-width:640px){
  body{background:linear-gradient(180deg,#070a12 0%,#0a1020 48%,#060912 100%)}
  body::before{background-size:34px 34px;opacity:.75}
  .sidebar{padding-top:10px}
  .brand{gap:10px;margin-bottom:8px}.brand-logo{width:40px;height:40px}.brand span span{max-width:190px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .topbar{display:grid;grid-template-columns:1fr;gap:10px;border-bottom-color:rgba(226,232,240,.08)}
  .topbar small{display:flex;align-items:center;justify-content:flex-start;color:#c6d1e1}
  .topbar .btn{width:100%;min-height:50px}
  .container{padding:19px 12px 24px}
  .hero{padding:7px 0 24px}.hero::after{width:70px;height:3px;margin-top:18px}
  .section-kicker,.badge{font-size:10.5px;letter-spacing:.06em;padding:7px 10px}
  h1{font-size:35px;line-height:1.03;letter-spacing:-.05em}h2{font-size:24px}.lead{font-size:16px;line-height:1.55}
  .panel,.card,.seo-block,.cta-strip{border-radius:22px;box-shadow:0 14px 36px rgba(0,0,0,.30)}
  .panel,.card,.seo-block{padding:16px}.cta-strip{padding:16px}
  .demo-wallet{grid-template-columns:1fr 1fr;padding:10px;border-radius:18px}.wallet-reset{grid-column:1/-1}.demo-wallet div{padding:9px 10px}.game-toolbar{grid-template-columns:1fr 1fr;gap:9px}.mult{grid-column:1/-1}.game-toolbar input,.game-toolbar select{min-height:46px}
  .mines-grid{width:min(100%,362px);gap:7px;margin:16px auto 18px}.cell{border-radius:13px}
  .btn{width:100%;min-height:52px;border-radius:15px}.btn-xl{min-height:58px}.promo-code{width:100%;font-size:34px;letter-spacing:.08em;min-height:64px;border-radius:18px}
  .faq-list details{border-radius:18px;padding:15px}.faq-list summary h2{font-size:20px}
}

@media (max-width:380px){
  h1{font-size:32px}.nav a{font-size:13px;padding-inline:11px}.mines-grid{gap:6px}.cell{border-radius:11px}.container{padding-inline:10px}
}

@media (hover:none){
  .btn:hover,.card:hover,.cell:hover,.nav a:hover{transform:none}
}

@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}
}

/* Multilingual article pages */
.article-hero{padding-bottom:22px}
.lang-switcher{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin-top:22px;
}
.lang-switcher a{
  min-height:44px;
  display:inline-flex;
  align-items:center;
  gap:8px;
  padding:9px 13px;
  border:1px solid rgba(226,232,240,.14);
  border-radius:999px;
  color:#d8e4f4;
  background:rgba(255,255,255,.045);
  font-weight:950;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.045);
}
.lang-switcher a span{color:#9daac0;font-size:12px;font-weight:750;text-transform:none}
.lang-switcher a.active,
.lang-switcher a:hover{
  color:#06101d;
  background:linear-gradient(135deg,#5cf0c3,#6ee7f9 48%,#9a8cff);
  border-color:transparent;
  text-decoration:none;
  box-shadow:0 12px 28px rgba(84,240,193,.18),inset 0 1px 0 rgba(255,255,255,.38);
}
.lang-switcher a.active span,
.lang-switcher a:hover span{color:#102033}
.article-content{font-size:17px;line-height:1.72}
.article-content h2:first-child{margin-top:0}
.article-content h2,.article-content h3,.article-content h4{margin-top:30px}
.article-content h3{font-size:clamp(20px,2.3vw,28px);line-height:1.18;letter-spacing:-.03em;color:#fff}
.article-content h4{font-size:20px;color:#edf5ff}
.article-content hr{height:1px;border:0;margin:28px 0;background:linear-gradient(90deg,transparent,rgba(84,240,193,.28),rgba(139,124,255,.18),transparent)}
.article-content ol,.article-content ul{padding-left:24px}
.article-content li::marker{color:#7cf4d2}
.article-content code{padding:2px 6px;border-radius:8px;background:rgba(255,255,255,.08);color:#9af6df}
@media (max-width:640px){
  .lang-switcher{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:18px}
  .lang-switcher a{justify-content:center;width:100%;padding:9px 10px}
  .lang-switcher a span{display:none}
  .article-content{font-size:16px;line-height:1.68}
  .article-content h2,.article-content h3,.article-content h4{margin-top:24px}
}
'''

app_js = f'''
(function(){{
  const OFFER = '{OFFER}';
  const toast = document.createElement('div');
  toast.className = 'toast';
  document.body.appendChild(toast);
  function showToast(msg){{ toast.textContent = msg; toast.classList.add('show'); setTimeout(()=>toast.classList.remove('show'),2200); }}
  document.querySelectorAll('a[href="{OFFER}"]').forEach(a=>{{
    a.addEventListener('click',()=>{{ try{{ ym(106419573,'reachGoal','offer_click'); }}catch(e){{}} }});
  }});
  const copy = document.getElementById('copyPromo');
  if(copy) copy.addEventListener('click', async()=>{{
    const code = copy.dataset.code || 'PIXELWIN';
    try{{ await navigator.clipboard.writeText(code); showToast('Промокод PIXELWIN скопирован'); }}catch(e){{ showToast('Скопируйте код: PIXELWIN'); }}
  }});
  const dGrid = document.getElementById('demoGrid');
  const sGrid = document.getElementById('signalGrid');
  if(!dGrid || !sGrid) return;
  const balanceBox = document.getElementById('balanceBox');
  const profitBox = document.getElementById('profitBox');
  const statusBox = document.getElementById('gameStatus');
  const resetBalanceBtn = document.getElementById('resetBalanceBtn');
  const betInput = document.getElementById('betInput');
  const minesSelect = document.getElementById('minesSelect');
  const multBox = document.getElementById('multBox');
  const playBtn = document.getElementById('playBtn');
  const BALANCE_KEY = 'minesDemoBalance';
  const START_BALANCE = 5000;
  let mines = [], opened = 0, playing = false, bet = 100, balance = loadBalance(), currentWin = 0;
  function loadBalance(){{ const saved = Number(localStorage.getItem(BALANCE_KEY)); return Number.isFinite(saved) && saved >= 0 ? Math.round(saved) : START_BALANCE; }}
  function saveBalance(){{ localStorage.setItem(BALANCE_KEY, String(balance)); }}
  function money(n){{ return Math.max(0, Math.round(n)).toLocaleString('ru-RU'); }}
  function setStatus(msg){{ if(statusBox) statusBox.textContent = msg; }}
  function updateWallet(){{ if(balanceBox) balanceBox.textContent = money(balance); if(profitBox) profitBox.textContent = money(currentWin); saveBalance(); }}
  function countMines(){{ return parseInt(minesSelect.value,10)||3; }}
  function multiplier(m,s){{ let x=1; for(let i=0;i<s;i++) x *= (25-i)/(25-m-i); return x*.97; }}
  function board(){{ mines=[]; const m=countMines(); while(mines.length<m){{ const r=Math.floor(Math.random()*25); if(!mines.includes(r)) mines.push(r); }} }}
  function render(){{
    dGrid.innerHTML=''; sGrid.innerHTML='';
    for(let i=0;i<25;i++){{
      const c=document.createElement('button'); c.type='button'; c.className='cell'; c.setAttribute('aria-label','Клетка '+(i+1)); c.addEventListener('click',()=>clickCell(i,c)); dGrid.appendChild(c);
      const sc=document.createElement('div'); sc.className='cell'; sGrid.appendChild(sc);
    }}
  }}
  function reset(){{ opened=0; playing=false; currentWin=0; multBox.textContent='x1.00'; playBtn.textContent='СДЕЛАТЬ СТАВКУ'; setStatus('Баланс сохраняется в браузере. Сделайте демо-ставку и заберите выигрыш до бомбы.'); updateWallet(); board(); render(); }}
  function loseRound(c){{ c.classList.add('mine'); c.textContent='💣'; currentWin=0; updateWallet(); setStatus('Бомба забрала ставку '+money(bet)+'. Баланс уже сохранён.'); showToast('Бомба! Ставка списана с демо-баланса'); setTimeout(reset,950); }}
  function clickCell(i,c){{
    if(!playing || c.classList.contains('safe') || c.classList.contains('mine')) return;
    if(mines.includes(i)){{ loseRound(c); return; }}
    opened++; c.classList.add('safe'); c.textContent='💎'; const x=multiplier(countMines(),opened); currentWin=Math.round(bet*x); multBox.textContent='x'+x.toFixed(2); profitBox.textContent=money(currentWin); playBtn.textContent='ЗАБРАТЬ '+money(currentWin); setStatus('Открыто безопасных клеток: '+opened+'. Можно продолжить риск или забрать выигрыш.');
  }}
  playBtn.addEventListener('click',()=>{{
    if(!playing){{
      bet=Math.max(10, Math.round(parseFloat(betInput.value)||100));
      betInput.value=bet;
      if(bet>balance){{ showToast('Недостаточно демо-баланса'); setStatus('Уменьшите ставку или сбросьте баланс до '+money(START_BALANCE)+'.'); return; }}
      balance-=bet; currentWin=0; playing=true; opened=0; board(); render(); updateWallet(); showToast('Раунд начался, ставка списана'); setStatus('Ставка '+money(bet)+' списана. Ищите безопасные клетки.'); playBtn.textContent='ЗАБРАТЬ 0';
    }}
    else if(opened>0){{ balance+=currentWin; showToast('Выигрыш '+money(currentWin)+' добавлен к балансу'); setStatus('Вы забрали '+money(currentWin)+'. Баланс сохранён в localStorage.'); reset(); }}
    else showToast('Откройте хотя бы одну клетку');
  }});
  if(resetBalanceBtn) resetBalanceBtn.addEventListener('click',()=>{{ balance=START_BALANCE; currentWin=0; updateWallet(); reset(); showToast('Демо-баланс сброшен'); }});
  document.getElementById('signalBtn').addEventListener('click',()=>{{
    if(!mines.length) board();
    Array.from(sGrid.children).forEach(c=>{{c.className='cell'; c.textContent='';}});
    const safe=[]; for(let i=0;i<25;i++) if(!mines.includes(i)) safe.push(i);
    for(let n=0;n<3;n++){{ const pos=safe.splice(Math.floor(Math.random()*safe.length),1)[0]; const c=sGrid.children[pos]; c.classList.add('safe'); c.textContent='⭐'; }}
    showToast('Сигнал создан: проверьте безопасные шаги в демо');
  }});
  reset();
}})();
'''

def json_ld(filename, data):
    obj = {
        '@context': 'https://schema.org',
        '@type': 'WebPage',
        'name': data['title'],
        'description': data['description'],
        'url': SITE + filename,
        'inLanguage': 'ru-RU',
        'isPartOf': {'@type': 'WebSite', 'name': 'MinesNeon', 'url': SITE},
        'about': ['Mines', 'краш-игра', 'mines casino', 'промокод PIXELWIN']
    }
    return json.dumps(obj, ensure_ascii=False)

def render_page(filename, data):
    nav_items = []
    for href, label, icon in nav:
        active_class = 'active' if href == data['active'] else ''
        nav_items.append(f'<a class="{active_class}" href="{href}"><span>{icon}</span>{label}</a>')
    nav_html = '\n'.join(nav_items)
    canonical = SITE if filename == 'index.html' else SITE + filename
    content = content_map[data['content']]
    return f'''<!DOCTYPE html>
<html lang="ru" prefix="og: https://ogp.me/ns#">
<head>
  <script type="text/javascript">
    (function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};m[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){{if(document.scripts[j].src===r){{return;}}}}k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}})(window,document,'script','https://mc.yandex.ru/metrika/tag.js?id=106419573','ym');
    ym(106419573,'init',{{ssr:true,webvisor:true,clickmap:true,ecommerce:"dataLayer",referrer:document.referrer,url:location.href,accurateTrackBounce:true,trackLinks:true}});
  </script>
  <noscript><div><img src="https://mc.yandex.ru/watch/106419573" style="position:absolute;left:-9999px;" alt=""></div></noscript>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=5,user-scalable=yes,viewport-fit=cover">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>{escape(data['title'])}</title>
  <meta name="description" content="{escape(data['description'])}">
  <meta name="keywords" content="{escape(data['keywords'])}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#060713">
  <link rel="canonical" href="{canonical}">
  <link rel="manifest" href="site.webmanifest">
  <link rel="stylesheet" href="assets/style.css">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{escape(data['title'])}">
  <meta property="og:description" content="{escape(data['description'])}">
  <meta property="og:site_name" content="MinesNeon">
  <meta property="og:locale" content="ru_RU">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(data['title'])}">
  <meta name="twitter:description" content="{escape(data['description'])}">
  <script type="application/ld+json">{json_ld(filename, data)}</script>
  <script src="https://analytics.ahrefs.com/analytics.js" data-key="5+Aq5cTCiHoUIdAWGMQ1dg" async></script>
</head>
<body>
  <div class="site">
    <aside class="sidebar" aria-label="Основная навигация">
      <a class="brand" href="index.html" aria-label="MinesNeon главная">
        <span class="brand-logo">💣</span><span><strong>MinesNeon</strong><span>Демо • сигналы • бонус</span></span>
      </a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span><b>Меню</b></button>
      <nav class="nav" id="site-nav">{nav_html}</nav>
      <div class="side-cta"><b>PIXELWIN: бонус 500%</b><a class="btn btn-pulse" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">ЗАБРАТЬ БОНУС</a></div>
    </aside>
    <main class="main">
      <header class="topbar">
        <small>Демо Mines · сигналы · бонус PIXELWIN</small>
        <a class="btn btn-pulse" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">ПЕРЕЙТИ В КАЗИНО</a>
      </header>
      <div class="container">
        <section class="hero">
          <div class="section-kicker">MinesNeon SEO Hub</div>
          <h1>{escape(data['h1'])}</h1>
          <p class="lead">{escape(data['lead'])}</p>
        </section>
        {content}
      </div>
      <footer class="footer">
        <p><strong>MinesNeon</strong> — информационный лендинг и демо-симулятор. Материалы не являются финансовой рекомендацией. Азартные игры доступны только пользователям 18+ в регионах, где это разрешено законом.</p>
      </footer>
    </main>
  </div>
  <script src="assets/app.js" defer></script>
</body>
</html>
'''

(ASSETS / 'style.css').write_text(style, encoding='utf-8')
(ASSETS / 'app.js').write_text(app_js, encoding='utf-8')
(ROOT / 'site.webmanifest').write_text(json.dumps({
    'name': 'MinesNeon',
    'short_name': 'Mines',
    'start_url': 'index.html',
    'display': 'standalone',
    'background_color': '#060713',
    'theme_color': '#060713',
    'lang': 'ru-RU'
}, ensure_ascii=False, indent=2), encoding='utf-8')

for filename, data in pages.items():
    (ROOT / filename).write_text(render_page(filename, data), encoding='utf-8')

print('Generated files:')
for path in sorted(ROOT.rglob('*')):
    print(path.as_posix())

