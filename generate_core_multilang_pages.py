from pathlib import Path
from html import escape
import json

ROOT = Path('mines-seo-site')
SITE = 'https://minesneon.ru/'
OFFER = 'https://lkzq.cc/644450'
LANGS = ['ru', 'en', 'es', 'de', 'ph']

LANG_META = {
    'ru': {'html': 'ru', 'hreflang': 'ru', 'name': 'Русский', 'flag': 'ru', 'change': 'Сменить язык', 'menu': 'Меню', 'brand': 'Демо • сигналы • бонус', 'nav': 'Основная навигация', 'bonus': 'ЗАБРАТЬ БОНУС', 'go': 'ПЕРЕЙТИ В КАЗИНО', 'top': 'Демо Mines · сигналы · бонус PIXELWIN', 'footer': 'информационный лендинг и демо-симулятор. Материалы не являются финансовой рекомендацией. Азартные игры доступны только пользователям 18+ в регионах, где это разрешено законом.'},
    'en': {'html': 'en', 'hreflang': 'en', 'name': 'English', 'flag': 'gb', 'change': 'Change language', 'menu': 'Menu', 'brand': 'Demo • signals • bonus', 'nav': 'Site navigation', 'bonus': 'CLAIM BONUS', 'go': 'GO TO CASINO', 'top': 'Mines demo · signals · PIXELWIN bonus', 'footer': 'informational landing page and demo simulator. Content is not financial advice. Gambling is available only for users 18+ where permitted by law.'},
    'es': {'html': 'es', 'hreflang': 'es', 'name': 'Español', 'flag': 'es', 'change': 'Cambiar idioma', 'menu': 'Menú', 'brand': 'Demo • señales • bono', 'nav': 'Navegación principal', 'bonus': 'RECLAMAR BONO', 'go': 'IR AL CASINO', 'top': 'Demo Mines · señales · bono PIXELWIN', 'footer': 'landing informativa y simulador demo. El contenido no es asesoramiento financiero. Juegos solo para mayores de 18 años donde la ley lo permita.'},
    'de': {'html': 'de', 'hreflang': 'de', 'name': 'Deutsch', 'flag': 'de', 'change': 'Sprache ändern', 'menu': 'Menü', 'brand': 'Demo • Signale • Bonus', 'nav': 'Hauptnavigation', 'bonus': 'BONUS HOLEN', 'go': 'ZUM CASINO', 'top': 'Mines Demo · Signale · PIXELWIN Bonus', 'footer': 'Informationsseite und Demo-Simulator. Inhalte sind keine Finanzberatung. Glücksspiel nur ab 18 Jahren und nur in erlaubten Regionen.'},
    'ph': {'html': 'fil', 'hreflang': 'fil', 'name': 'Filipino', 'flag': 'ph', 'change': 'Palitan ang wika', 'menu': 'Menu', 'brand': 'Demo • signals • bonus', 'nav': 'Pangunahing navigation', 'bonus': 'KUNIN ANG BONUS', 'go': 'PUMUNTA SA CASINO', 'top': 'Mines demo · signals · PIXELWIN bonus', 'footer': 'informational landing page at demo simulator. Hindi financial advice ang content. Para lamang sa 18+ kung pinapayagan ng batas.'},
}

CURRENCY = {
    'ru': {'symbol': '₽', 'code': 'RUB', 'locale': 'ru-RU', 'start': 5000, 'bet': 100, 'min': 10},
    'en': {'symbol': '$', 'code': 'USD', 'locale': 'en-US', 'start': 100, 'bet': 2, 'min': 1},
    'es': {'symbol': '€', 'code': 'EUR', 'locale': 'es-ES', 'start': 100, 'bet': 2, 'min': 1},
    'de': {'symbol': '€', 'code': 'EUR', 'locale': 'de-DE', 'start': 100, 'bet': 2, 'min': 1},
    'ph': {'symbol': '₱', 'code': 'PHP', 'locale': 'en-PH', 'start': 5000, 'bet': 100, 'min': 10},
}

CORE_NAV = {
    'ru': [('index.html','🎮','Демо + сигналы'),('promo.html','💎','Промокод 500%'),('strategies.html','📈','Стратегии'),('faq.html','❓','FAQ'),('apk.html','📲','Скачать APK'),('other.html','🚀','Другие игры')],
    'en': [('index-en.html','🎮','Demo + signals'),('promo-en.html','💎','Promo 500%'),('strategies-main-en.html','📈','Strategies'),('faq-en.html','❓','FAQ'),('apk-en.html','📲','Download APK'),('other-en.html','🚀','Other games')],
    'es': [('index-es.html','🎮','Demo + señales'),('promo-es.html','💎','Promo 500%'),('strategies-main-es.html','📈','Estrategias'),('faq-es.html','❓','FAQ'),('apk-es.html','📲','Descargar APK'),('other-es.html','🚀','Otros juegos')],
    'de': [('index-de.html','🎮','Demo + Signale'),('promo-de.html','💎','Promo 500%'),('strategies-main-de.html','📈','Strategien'),('faq-de.html','❓','FAQ'),('apk-de.html','📲','APK Download'),('other-de.html','🚀','Andere Spiele')],
    'ph': [('index-ph.html','🎮','Demo + signals'),('promo-ph.html','💎','Promo 500%'),('strategies-main-ph.html','📈','Mga strategy'),('faq-ph.html','❓','FAQ'),('apk-ph.html','📲','Download APK'),('other-ph.html','🚀','Iba pang games')],
}

GUIDES = [
    ('home','🏠',{'ru':'Главная','en':'Home','es':'Inicio','de':'Startseite','ph':'Home'}),('demo','🎮',{'ru':'Демо','en':'Demo','es':'Demo','de':'Demo','ph':'Demo'}),('bonus','🎁',{'ru':'Бонус','en':'Bonus','es':'Bono','de':'Bonus','ph':'Bonus'}),('promocode','💎',{'ru':'Промокод','en':'Promo code','es':'Código promo','de':'Promo-Code','ph':'Promo code'}),('registration','📝',{'ru':'Регистрация','en':'Registration','es':'Registro','de':'Registrierung','ph':'Registration'}),('strategies','📈',{'ru':'Стратегии гайда','en':'Guide strategies','es':'Estrategias guía','de':'Guide-Strategien','ph':'Guide strategies'}),('download','📲',{'ru':'Скачать','en':'Download','es':'Descargar','de':'Download','ph':'Download'}),('analog','🧩',{'ru':'Аналоги','en':'Alternatives','es':'Alternativas','de':'Alternativen','ph':'Mga alternatibo'}),('hack','🛡️',{'ru':'Предиктор','en':'Predictor','es':'Predictor','de':'Predictor','ph':'Predictor'}),('mines-game','💣',{'ru':'Игра Mines','en':'Mines game','es':'Juego Mines','de':'Mines Spiel','ph':'Mines game'}),
]
GUIDE_UI = {'ru':('Гайды','Открыть гайды','Скрыть гайды'),'en':('Guides','Open guides','Hide guides'),'es':('Guías','Abrir guías','Ocultar guías'),'de':('Guides','Guides öffnen','Guides ausblenden'),'ph':('Guides','Buksan ang guides','Itago ang guides')}

FILENAME = {
    'index': {'ru':'index.html','en':'index-en.html','es':'index-es.html','de':'index-de.html','ph':'index-ph.html'},
    'promo': {'ru':'promo.html','en':'promo-en.html','es':'promo-es.html','de':'promo-de.html','ph':'promo-ph.html'},
    'strategies': {'ru':'strategies.html','en':'strategies-main-en.html','es':'strategies-main-es.html','de':'strategies-main-de.html','ph':'strategies-main-ph.html'},
    'faq': {'ru':'faq.html','en':'faq-en.html','es':'faq-es.html','de':'faq-de.html','ph':'faq-ph.html'},
    'apk': {'ru':'apk.html','en':'apk-en.html','es':'apk-es.html','de':'apk-de.html','ph':'apk-ph.html'},
    'other': {'ru':'other.html','en':'other-en.html','es':'other-es.html','de':'other-de.html','ph':'other-ph.html'},
}

PAGES = {
 'index': {
  'ru': {'title':'Мины играть онлайн бесплатно — Mines demo, бот сигналов и бонус PIXELWIN','description':'Играйте в мины бесплатно в Mines demo 5×5, тестируйте сигналы, mines бот и стратегии перед переходом в mines casino с бонусом 500% по промокоду PIXELWIN.','keywords':'мины играть, играть в мины, Mines бесплатно, mines demo, mines сигналы, бот мины','h1':'Мины играть онлайн: Mines бесплатно, демо-игра и бот сигналов','lead':'Тренируйтесь в симуляторе минных ячеек 5×5, проверяйте безопасные шаги и переходите к реальным коэффициентам только после понимания механики Mines.','content':'index'},
  'en': {'title':'Play Mines Online Free — Mines demo, signal bot and PIXELWIN bonus','description':'Play Mines free in a 5×5 demo, test safe signals, learn the bot logic and move to real Mines casino only after practice.','keywords':'play mines, mines demo, mines free, mines signals, mines bot','h1':'Play Mines online: free demo, signals and training balance','lead':'Train on a 5×5 Mines field, test safe steps, manage a saved demo balance and learn the mechanics before real coefficients.','content':'index'},
  'es': {'title':'Jugar Mines online gratis — demo, señales y bono PIXELWIN','description':'Juega Mines gratis en demo 5×5, prueba señales seguras y aprende la mecánica antes de pasar al casino con bono.','keywords':'jugar mines, mines demo, mines gratis, señales mines','h1':'Jugar Mines online: demo gratis, señales y saldo de práctica','lead':'Entrena en un tablero 5×5, prueba pasos seguros, usa un saldo demo guardado y entiende la mecánica antes de apostar.','content':'index'},
  'de': {'title':'Mines online kostenlos spielen — Demo, Signale und PIXELWIN Bonus','description':'Spielen Sie Mines kostenlos in der 5×5 Demo, testen Sie Signale und lernen Sie die Mechanik vor echtem Casino-Spiel.','keywords':'Mines spielen, Mines Demo, Mines kostenlos, Mines Signale','h1':'Mines online spielen: kostenlose Demo, Signale und Trainingsguthaben','lead':'Trainieren Sie auf einem 5×5 Feld, testen Sie sichere Schritte und nutzen Sie ein gespeichertes Demo-Guthaben vor echten Einsätzen.','content':'index'},
  'ph': {'title':'Play Mines Online Free — demo, signals at PIXELWIN bonus','description':'Maglaro ng Mines demo 5×5, subukan ang safe signals at aralin ang mechanics bago lumipat sa real casino.','keywords':'play mines, mines demo, mines free, mines signals','h1':'Play Mines online: free demo, signals at practice balance','lead':'Mag-practice sa 5×5 Mines field, subukan ang safe steps at gamitin ang saved demo balance bago real coefficients.','content':'index'},
 },
 'promo': {
  'ru': {'title':'Mines промокоды PIXELWIN — VIP бонус 500%','description':'Актуальный mines промокод PIXELWIN: получите VIP бонус 500% на депозит.','keywords':'mines промокоды, PIXELWIN, mines casino','h1':'Mines промокоды: VIP бонус 500% по коду PIXELWIN','lead':'Промокод PIXELWIN помогает перейти из демо к реальным ставкам с увеличенным стартовым балансом.','content':'promo'},
  'en': {'title':'Mines promo code PIXELWIN — VIP 500% bonus','description':'Use Mines promo code PIXELWIN to claim a VIP 500% deposit bonus.','keywords':'mines promo code, PIXELWIN, mines casino','h1':'Mines promo code: VIP 500% bonus with PIXELWIN','lead':'PIXELWIN helps you move from demo practice to real rounds with a larger starting balance.','content':'promo'},
  'es': {'title':'Código promo Mines PIXELWIN — bono VIP 500%','description':'Usa el código promo PIXELWIN para reclamar un bono VIP de 500%.','keywords':'código promo mines, PIXELWIN, casino mines','h1':'Código promo Mines: bono VIP 500% con PIXELWIN','lead':'PIXELWIN ayuda a pasar de la demo a rondas reales con un saldo inicial mayor.','content':'promo'},
  'de': {'title':'Mines Promo-Code PIXELWIN — VIP Bonus 500%','description':'Nutzen Sie den Promo-Code PIXELWIN für einen VIP Bonus von 500%.','keywords':'Mines Promo Code, PIXELWIN, Mines Casino','h1':'Mines Promo-Code: VIP 500% Bonus mit PIXELWIN','lead':'PIXELWIN erleichtert den Wechsel von der Demo zu echten Runden mit größerem Startguthaben.','content':'promo'},
  'ph': {'title':'Mines promo code PIXELWIN — VIP 500% bonus','description':'Gamitin ang PIXELWIN promo code para sa VIP 500% deposit bonus.','keywords':'mines promo code, PIXELWIN, mines casino','h1':'Mines promo code: VIP 500% bonus gamit ang PIXELWIN','lead':'Tinutulungan ka ng PIXELWIN lumipat mula demo practice papunta sa real rounds na may mas malaking starting balance.','content':'promo'},
 },
 'strategies': {
  'ru': {'title':'Стратегии Mines: Safe Step, Зигзаг, Мартингейл и RTP','description':'Разбор стратегий Mines, RTP и честный подход к сигналам без мифов про взлом.','keywords':'стратегии Mines, Safe Step, Martingale, RTP','h1':'Стратегии игры Mines: от Safe Step до анализа RTP','lead':'Тактики не гарантируют выигрыш, но управление риском помогает сохранять банкролл.','content':'strategies'},
  'en': {'title':'Mines strategies: Safe Step, Zigzag, Martingale and RTP','description':'Learn Mines strategies, RTP basics and responsible use of signals without hack myths.','keywords':'Mines strategies, Safe Step, Martingale, RTP','h1':'Mines strategies: from Safe Step to RTP analysis','lead':'No tactic guarantees profit, but risk control helps protect your bankroll.','content':'strategies'},
  'es': {'title':'Estrategias Mines: Safe Step, Zigzag, Martingala y RTP','description':'Estrategias Mines, RTP y uso responsable de señales sin mitos de hacks.','keywords':'estrategias Mines, Safe Step, Martingala, RTP','h1':'Estrategias Mines: de Safe Step al análisis RTP','lead':'Ninguna táctica garantiza ganancias, pero controlar el riesgo protege el bankroll.','content':'strategies'},
  'de': {'title':'Mines Strategien: Safe Step, Zigzag, Martingale und RTP','description':'Mines Strategien, RTP-Grundlagen und verantwortliche Nutzung von Signalen ohne Hack-Mythen.','keywords':'Mines Strategien, Safe Step, Martingale, RTP','h1':'Mines Strategien: von Safe Step bis RTP-Analyse','lead':'Keine Taktik garantiert Gewinn, aber Risikokontrolle schützt die Bankroll.','content':'strategies'},
  'ph': {'title':'Mines strategies: Safe Step, Zigzag, Martingale at RTP','description':'Alamin ang Mines strategies, RTP basics at responsible signals nang walang hack myths.','keywords':'Mines strategies, Safe Step, Martingale, RTP','h1':'Mines strategies: mula Safe Step hanggang RTP analysis','lead':'Walang guaranteed profit, pero nakakatulong ang risk control para protektahan ang bankroll.','content':'strategies'},
 },
 'faq': {
  'ru': {'title':'Mines отзывы и FAQ — честность игры, выплаты, сигналы и демо','description':'Ответы на частые вопросы про Mines: отзывы, честность, выплаты, сигналы и демо.','keywords':'mines отзывы, Mines FAQ, выплаты Mines','h1':'Mines отзывы и часто задаваемые вопросы','lead':'Ответы о честности, выплатах, демо-режиме, сигналах и безопасном старте.','content':'faq'},
  'en': {'title':'Mines reviews and FAQ — fairness, payouts, signals and demo','description':'Answers about Mines reviews, fairness, payouts, signals, demo mode and safe start.','keywords':'Mines reviews, Mines FAQ, Mines payouts','h1':'Mines reviews and frequently asked questions','lead':'Clear answers about fairness, payouts, demo mode, signals and responsible play.','content':'faq'},
  'es': {'title':'Opiniones y FAQ de Mines — justicia, pagos, señales y demo','description':'Respuestas sobre opiniones Mines, pagos, señales, demo y juego responsable.','keywords':'opiniones Mines, FAQ Mines, pagos Mines','h1':'Opiniones de Mines y preguntas frecuentes','lead':'Respuestas sobre justicia, pagos, demo, señales y juego responsable.','content':'faq'},
  'de': {'title':'Mines Bewertungen und FAQ — Fairness, Auszahlungen, Signale und Demo','description':'Antworten zu Mines Bewertungen, Fairness, Auszahlungen, Signalen und Demo.','keywords':'Mines Bewertungen, Mines FAQ, Auszahlungen','h1':'Mines Bewertungen und häufige Fragen','lead':'Antworten zu Fairness, Auszahlungen, Demo-Modus, Signalen und verantwortlichem Spiel.','content':'faq'},
  'ph': {'title':'Mines reviews at FAQ — fairness, payouts, signals at demo','description':'Mga sagot tungkol sa Mines reviews, fairness, payouts, signals, demo at safe start.','keywords':'Mines reviews, Mines FAQ, Mines payouts','h1':'Mines reviews at madalas na tanong','lead':'Malinaw na sagot tungkol sa fairness, payouts, demo mode, signals at responsible play.','content':'faq'},
 },
 'apk': {
  'ru': {'title':'Mines скачать на телефон — APK и PWA инструкция','description':'Как mines скачать на смартфон: PWA, Android Chrome, iPhone Safari и быстрый доступ.','keywords':'mines скачать, APK Mines, PWA Mines','h1':'Mines скачать: APK/PWA инструкция для телефона','lead':'Добавьте Mines на главный экран и запускайте демо, сигналы и бонус без поиска.','content':'apk'},
  'en': {'title':'Download Mines on mobile — APK and PWA guide','description':'How to download Mines safely: PWA install, Android Chrome, iPhone Safari and quick access.','keywords':'download Mines, Mines APK, Mines PWA','h1':'Download Mines: APK/PWA guide for mobile','lead':'Add Mines to your home screen and open demo, signals and bonus pages faster.','content':'apk'},
  'es': {'title':'Descargar Mines en móvil — guía APK y PWA','description':'Cómo descargar Mines con seguridad: PWA, Android Chrome, iPhone Safari y acceso rápido.','keywords':'descargar Mines, APK Mines, PWA Mines','h1':'Descargar Mines: guía APK/PWA para móvil','lead':'Añade Mines a la pantalla de inicio para abrir demo, señales y bono más rápido.','content':'apk'},
  'de': {'title':'Mines auf dem Handy herunterladen — APK und PWA Anleitung','description':'So laden Sie Mines sicher herunter: PWA, Android Chrome, iPhone Safari und Schnellzugriff.','keywords':'Mines herunterladen, Mines APK, Mines PWA','h1':'Mines herunterladen: APK/PWA Anleitung für Mobilgeräte','lead':'Fügen Sie Mines zum Startbildschirm hinzu und öffnen Sie Demo, Signale und Bonus schneller.','content':'apk'},
  'ph': {'title':'Download Mines sa mobile — APK at PWA guide','description':'Paano ligtas i-download ang Mines: PWA install, Android Chrome, iPhone Safari at quick access.','keywords':'download Mines, Mines APK, Mines PWA','h1':'Download Mines: APK/PWA guide para sa mobile','lead':'Idagdag ang Mines sa home screen para mas mabilis buksan ang demo, signals at bonus.','content':'apk'},
 },
 'other': {
  'ru': {'title':'Другие краш-игры: Lucky Jet, Speed and Cash, Rocket Queen и аналоги Mines','description':'Подборка краш-игр для игроков Mines: Lucky Jet, Speed and Cash, Rocket Queen и Aviator.','keywords':'краш-игры, Lucky Jet, Speed and Cash, Rocket Queen','h1':'Другие краш-игры и аналоги Mines','lead':'Изучите другие быстрые игры с коэффициентами, короткими раундами и управлением риском.','content':'other'},
  'en': {'title':'Other crash games: Lucky Jet, Speed and Cash, Rocket Queen and Mines alternatives','description':'Crash game picks for Mines players: Lucky Jet, Speed and Cash, Rocket Queen and Aviator.','keywords':'crash games, Lucky Jet, Speed and Cash, Rocket Queen','h1':'Other crash games and Mines alternatives','lead':'Explore fast coefficient games with short rounds and familiar risk management.','content':'other'},
  'es': {'title':'Otros crash games: Lucky Jet, Speed and Cash, Rocket Queen y alternativas Mines','description':'Juegos crash para jugadores de Mines: Lucky Jet, Speed and Cash, Rocket Queen y Aviator.','keywords':'juegos crash, Lucky Jet, Speed and Cash, Rocket Queen','h1':'Otros crash games y alternativas a Mines','lead':'Explora juegos rápidos con coeficientes, rondas cortas y gestión de riesgo.','content':'other'},
  'de': {'title':'Andere Crash Games: Lucky Jet, Speed and Cash, Rocket Queen und Mines Alternativen','description':'Crash Games für Mines-Spieler: Lucky Jet, Speed and Cash, Rocket Queen und Aviator.','keywords':'Crash Games, Lucky Jet, Speed and Cash, Rocket Queen','h1':'Andere Crash Games und Mines Alternativen','lead':'Entdecken Sie schnelle Spiele mit Koeffizienten, kurzen Runden und Risikomanagement.','content':'other'},
  'ph': {'title':'Iba pang crash games: Lucky Jet, Speed and Cash, Rocket Queen at Mines alternatives','description':'Crash games para sa Mines players: Lucky Jet, Speed and Cash, Rocket Queen at Aviator.','keywords':'crash games, Lucky Jet, Speed and Cash, Rocket Queen','h1':'Iba pang crash games at Mines alternatives','lead':'Tingnan ang mabilis na coefficient games na may short rounds at risk management.','content':'other'},
 },
}

def t(lang, ru, en, es, de, ph):
    return {'ru': ru, 'en': en, 'es': es, 'de': de, 'ph': ph}[lang]

def cta(lang):
    return f'''<section class="cta-strip" aria-label="{escape(t(lang,'Переход в казино','Go to casino','Ir al casino','Zum Casino','Pumunta sa casino'))}"><div><strong>{escape(t(lang,'Готовы проверить коэффициенты на реальной платформе?','Ready to test real coefficients?','¿Listo para probar coeficientes reales?','Bereit für echte Koeffizienten?','Ready na subukan ang real coefficients?'))}</strong><span>{escape(t(lang,'Активируйте PIXELWIN и получите до 500% к депозиту.','Activate PIXELWIN and get up to 500% on deposit.','Activa PIXELWIN y recibe hasta 500% en el depósito.','Aktivieren Sie PIXELWIN und erhalten Sie bis zu 500% auf die Einzahlung.','I-activate ang PIXELWIN at makakuha ng hanggang 500% sa deposit.'))}</span></div><a class="btn btn-pulse" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(LANG_META[lang]['go'])}</a></section>'''

def content(kind, lang):
    if kind == 'index':
        cur = CURRENCY[lang]
        balance = f"{cur['start']:,}".replace(',', ' ')
        return f'''<section class="hero-grid"><div class="panel game-panel" data-demo-lang="{lang}" data-currency="{escape(cur['symbol'])}" data-locale="{cur['locale']}" data-start-balance="{cur['start']}" data-default-bet="{cur['bet']}" data-min-bet="{cur['min']}" data-storage-key="minesDemoBalance:{lang}:{cur['code']}"><div class="section-kicker">mines demo • mines free • Mines land</div><h2>{escape(t(lang,'Mines demo 5×5 — играть в мины бесплатно','Mines demo 5×5 — play for free','Mines demo 5×5 — jugar gratis','Mines Demo 5×5 — kostenlos spielen','Mines demo 5×5 — play for free'))}</h2><p>{escape(t(lang,'Выбирайте ставку, количество бомб и открывайте безопасные клетки. Баланс сохраняется в браузере через localStorage.','Choose a bet, mines count and open safe tiles. Your demo balance is saved in the browser with localStorage.','Elige apuesta, número de minas y abre casillas seguras. El saldo demo se guarda en el navegador con localStorage.','Wählen Sie Einsatz und Minenanzahl und öffnen Sie sichere Felder. Das Demo-Guthaben wird per localStorage gespeichert.','Pumili ng bet, mines count at buksan ang safe tiles. Naka-save ang demo balance sa browser gamit ang localStorage.'))}</p><div class="demo-wallet" aria-label="Demo balance"><div><span>{escape(t(lang,'Баланс','Balance','Saldo','Guthaben','Balance'))}</span><strong id="balanceBox" data-currency="{escape(cur['symbol'])}">{balance}</strong></div><div><span>{escape(t(lang,'Возможный выигрыш','Possible win','Ganancia posible','Möglicher Gewinn','Possible win'))}</span><strong id="profitBox" data-currency="{escape(cur['symbol'])}">0</strong></div><button class="wallet-reset" id="resetBalanceBtn" type="button">{escape(t(lang,'Сбросить','Reset','Reiniciar','Zurücksetzen','Reset'))}</button></div><div class="game-toolbar"><label>{escape(t(lang,'Ставка','Bet','Apuesta','Einsatz','Bet'))} <input id="betInput" type="number" value="{cur['bet']}" min="{cur['min']}" inputmode="numeric"></label><label>{escape(t(lang,'Мины','Mines','Minas','Minen','Mines'))} <select id="minesSelect"><option>1</option><option selected>3</option><option>5</option><option>10</option></select></label><div class="mult" id="multBox">x1.00</div></div><div class="game-status" id="gameStatus">{escape(t(lang,'Баланс сохраняется в браузере. Сделайте демо-ставку и заберите выигрыш до бомбы.','The balance is saved in this browser. Place a demo bet and cash out before a bomb.','El saldo se guarda en este navegador. Haz una apuesta demo y cobra antes de una bomba.','Das Guthaben wird in diesem Browser gespeichert. Setzen Sie demo und zahlen Sie vor einer Bombe aus.','Naka-save ang balance sa browser na ito. Mag-demo bet at mag-cash out bago ang bomba.'))}</div><div class="demo-grid" id="demoGrid" aria-label="Mines demo grid"></div><button class="btn btn-pulse btn-xl" id="playBtn" type="button">{escape(t(lang,'СДЕЛАТЬ СТАВКУ','PLACE BET','APOSTAR','EINSATZ SETZEN','PLACE BET'))}</button></div><div class="panel signal-panel"><h2>{escape(t(lang,'Mines predictor bot — демо сигнал','Mines predictor bot — demo signal','Mines predictor bot — señal demo','Mines Predictor Bot — Demo-Signal','Mines predictor bot — demo signal'))}</h2><p>{escape(t(lang,'Нажмите кнопку, чтобы подсветить три безопасные клетки для тренировки.','Press the button to highlight three safe training tiles.','Pulsa el botón para resaltar tres casillas seguras de práctica.','Klicken Sie, um drei sichere Trainingsfelder zu markieren.','Pindutin ang button para i-highlight ang tatlong safe training tiles.'))}</p><div class="signal-grid" id="signalGrid" aria-label="Mines signal grid"></div><button class="btn" id="signalBtn" type="button">{escape(t(lang,'ПОЛУЧИТЬ СИГНАЛ','GET SIGNAL','OBTENER SEÑAL','SIGNAL HOLEN','GET SIGNAL'))}</button></div></section>{cta(lang)}'''
    if kind == 'promo':
        return f'''<section class="promo-hero panel"><div class="badge">VIP BONUS • LIMITED</div><h2>{escape(t(lang,'Промокод PIXELWIN','PIXELWIN promo code','Código promo PIXELWIN','PIXELWIN Promo-Code','PIXELWIN promo code'))}</h2><p>{escape(t(lang,'Скопируйте код и используйте его при регистрации для расширенного бонуса.','Copy the code and use it during registration for the extended bonus.','Copia el código y úsalo durante el registro para el bono ampliado.','Kopieren Sie den Code und nutzen Sie ihn bei der Registrierung für den erweiterten Bonus.','Kopyahin ang code at gamitin sa registration para sa extended bonus.'))}</p><button class="promo-code" id="copyPromo" data-code="PIXELWIN">PIXELWIN</button><a class="btn btn-pulse btn-xl" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(LANG_META[lang]['bonus'])}</a></section><section class="seo-block"><h2>{escape(PAGES['promo'][lang]['h1'])}</h2><p>{escape(PAGES['promo'][lang]['lead'])}</p><ul><li>PIXELWIN</li><li>{escape(t(lang,'зарегистрируйтесь через партнёрский редирект','register through the partner redirect','regístrate mediante el enlace de socio','registrieren Sie sich über den Partnerlink','mag-register gamit ang partner redirect'))}</li><li>{escape(t(lang,'начните с малых ставок','start with small bets','empieza con apuestas pequeñas','beginnen Sie mit kleinen Einsätzen','magsimula sa small bets'))}</li></ul></section>{cta(lang)}'''
    if kind == 'strategies':
        return f'''<section class="cards"><article class="card"><h2>Safe Step</h2><p>{escape(t(lang,'1–3 мины, короткая серия и ранний cashout.','1–3 mines, short sequence and early cashout.','1–3 minas, serie corta y cobro temprano.','1–3 Minen, kurze Serie und frühes Cashout.','1–3 mines, short sequence at early cashout.'))}</p></article><article class="card"><h2>Zigzag</h2><p>{escape(t(lang,'Диагональные клики помогают избежать хаотичных решений.','Diagonal clicks help avoid chaotic decisions.','Los clics diagonales ayudan a evitar decisiones caóticas.','Diagonale Klicks helfen gegen chaotische Entscheidungen.','Diagonal clicks help avoid magulong decisions.'))}</p></article><article class="card"><h2>RTP</h2><p>{escape(t(lang,'RTP описывает дистанцию, а не результат одного раунда.','RTP describes long-term return, not one round.','El RTP describe el retorno a largo plazo, no una ronda.','RTP beschreibt langfristige Rendite, nicht eine Runde.','RTP describes long-term return, hindi one round.'))}</p></article></section><section class="seo-block"><h2>{escape(PAGES['strategies'][lang]['h1'])}</h2><p>{escape(PAGES['strategies'][lang]['lead'])}</p></section>{cta(lang)}'''
    if kind == 'faq':
        q1=t(lang,'Честная ли игра Mines?','Is Mines fair?','¿Mines es justo?','Ist Mines fair?','Fair ba ang Mines?')
        a1=t(lang,'В лицензированных казино результат формируется RNG или Provably Fair.','Licensed casinos use RNG or Provably Fair mechanics.','Los casinos con licencia usan RNG o Provably Fair.','Lizenzierte Casinos nutzen RNG oder Provably Fair.','Licensed casinos use RNG o Provably Fair mechanics.')
        return f'''<section class="faq-list"><details open><summary><h2>{escape(q1)}</h2></summary><p>{escape(a1)}</p></details><details><summary><h2>{escape(t(lang,'Сигналы гарантируют выигрыш?','Do signals guarantee wins?','¿Las señales garantizan ganancias?','Garantieren Signale Gewinne?','Guaranteed ba ng signals ang win?'))}</h2></summary><p>{escape(t(lang,'Нет, это тренировочные подсказки, а не гарантия.','No, they are practice hints, not guarantees.','No, son pistas de práctica, no garantías.','Nein, es sind Übungshinweise, keine Garantien.','Hindi, practice hints sila, hindi guarantees.'))}</p></details></section><section class="seo-block"><h2>{escape(PAGES['faq'][lang]['h1'])}</h2><p>{escape(PAGES['faq'][lang]['lead'])}</p></section>{cta(lang)}'''
    if kind == 'apk':
        return f'''<section class="cards install-cards"><article class="card"><h2>Android Chrome</h2><ol><li>{escape(t(lang,'Откройте сайт в Chrome.','Open the site in Chrome.','Abre el sitio en Chrome.','Öffnen Sie die Seite in Chrome.','Buksan ang site sa Chrome.'))}</li><li>{escape(t(lang,'Выберите установку приложения.','Choose install app.','Elige instalar aplicación.','Wählen Sie App installieren.','Piliin ang install app.'))}</li></ol></article><article class="card"><h2>iPhone Safari</h2><ol><li>{escape(t(lang,'Откройте страницу в Safari.','Open the page in Safari.','Abre la página en Safari.','Öffnen Sie die Seite in Safari.','Buksan ang page sa Safari.'))}</li><li>{escape(t(lang,'Добавьте на экран Домой.','Add to Home Screen.','Añade a pantalla de inicio.','Zum Home-Bildschirm hinzufügen.','Add to Home Screen.'))}</li></ol></article></section><section class="seo-block"><h2>{escape(PAGES['apk'][lang]['h1'])}</h2><p>{escape(PAGES['apk'][lang]['lead'])}</p></section>{cta(lang)}'''
    return f'''<section class="cards games"><article class="card game-card"><span>🚀</span><h2>Lucky Jet</h2><p>Crash game with fast cashout.</p><a href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(t(lang,'Открыть','Open','Abrir','Öffnen','Open'))}</a></article><article class="card game-card"><span>⚡</span><h2>Speed and Cash</h2><p>Fast rounds and coefficient control.</p><a href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(t(lang,'Открыть','Open','Abrir','Öffnen','Open'))}</a></article><article class="card game-card"><span>👑</span><h2>Rocket Queen</h2><p>Bright crash format for short sessions.</p><a href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(t(lang,'Открыть','Open','Abrir','Öffnen','Open'))}</a></article></section><section class="seo-block"><h2>{escape(PAGES['other'][lang]['h1'])}</h2><p>{escape(PAGES['other'][lang]['lead'])}</p></section>{cta(lang)}'''

def lang_switcher(kind, current_lang):
    cur = LANG_META[current_lang]
    links = []
    for lang in LANGS:
        m = LANG_META[lang]
        cls = 'active' if lang == current_lang else ''
        aria = ' aria-current="true"' if lang == current_lang else ''
        href = FILENAME[kind][lang]
        links.append(f'<a class="{cls}" hreflang="{m["hreflang"]}" href="{href}"{aria}><span class="lang-flag"><img src="https://flagcdn.com/w40/{m["flag"]}.png" srcset="https://flagcdn.com/w80/{m["flag"]}.png 2x" width="40" height="30" loading="lazy" alt="{escape(m["name"])} flag"></span><span class="lang-code">{lang.upper()}</span><span class="lang-name">{escape(m["name"])}</span></a>')
    return f'<div class="lang-switcher" data-lang-switcher aria-label="Language switcher"><button class="lang-switcher-toggle" type="button" aria-expanded="false"><span class="lang-flag"><img src="https://flagcdn.com/w40/{cur["flag"]}.png" srcset="https://flagcdn.com/w80/{cur["flag"]}.png 2x" width="40" height="30" loading="lazy" alt="{escape(cur["name"])} flag"></span><span class="lang-current"><strong>{escape(cur["name"])}</strong><small>{escape(cur["change"])}</small></span><span class="lang-chevron">⌄</span></button><div class="lang-options">' + ''.join(links) + '</div></div>'

def nav_html(current_file, lang):
    links = [f'<a class="{"active" if href == current_file else ""}" href="{href}"><span>{icon}</span>{escape(label)}</a>' for href, icon, label in CORE_NAV[lang]]
    guides = []
    for slug, icon, labels in GUIDES:
        href = f'{slug}-{lang}.html'
        guides.append(f'<a class="" href="{href}"><span>{icon}</span>{escape(labels[lang])}</a>')
    title, op, close = GUIDE_UI[lang]
    return '<nav class="nav" id="site-nav">' + '\n'.join(links) + f'\n<div class="nav-group guides-group"><button class="nav-subtoggle" type="button" aria-expanded="false" data-open="{escape(op)}" data-close="{escape(close)}"><span>📚</span><b>{escape(title)}</b><i>⌄</i></button><div class="nav-submenu">' + '\n'.join(guides) + '</div></div></nav>'

def json_ld(kind, lang, data, filename):
    return json.dumps({'@context':'https://schema.org','@type':'WebPage','name':data['title'],'description':data['description'],'url':SITE + filename,'inLanguage':LANG_META[lang]['html'],'isPartOf':{'@type':'WebSite','name':'MinesNeon','url':SITE}}, ensure_ascii=False)

def render(kind, lang):
    data = PAGES[kind][lang]
    filename = FILENAME[kind][lang]
    meta = LANG_META[lang]
    canonical = SITE if filename == 'index.html' else SITE + filename
    alternates = ''.join(f'  <link rel="alternate" hreflang="{LANG_META[l]["hreflang"]}" href="{SITE + FILENAME[kind][l]}">\n' for l in LANGS)
    alternates += f'  <link rel="alternate" hreflang="x-default" href="{SITE + FILENAME[kind]["en"]}">\n'
    return f'''<!DOCTYPE html>
<html lang="{meta['html']}" prefix="og: https://ogp.me/ns#">
<head>
  <script type="text/javascript">(function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};m[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){{if(document.scripts[j].src===r){{return;}}}}k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}})(window,document,'script','https://mc.yandex.ru/metrika/tag.js?id=106419573','ym');ym(106419573,'init',{{ssr:true,webvisor:true,clickmap:true,ecommerce:"dataLayer",referrer:document.referrer,url:location.href,accurateTrackBounce:true,trackLinks:true}});</script>
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
{alternates}  <link rel="manifest" href="site.webmanifest">
  <link rel="stylesheet" href="assets/style.css">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{escape(data['title'])}">
  <meta property="og:description" content="{escape(data['description'])}">
  <meta property="og:site_name" content="MinesNeon">
  <script type="application/ld+json">{json_ld(kind, lang, data, filename)}</script>
  <script src="https://analytics.ahrefs.com/analytics.js" data-key="5+Aq5cTCiHoUIdAWGMQ1dg" async></script>
</head>
<body>
  <div class="site">
    <aside class="sidebar" aria-label="{escape(meta['nav'])}">
      <a class="brand" href="{FILENAME['index'][lang]}" aria-label="MinesNeon"><span class="brand-logo">💣</span><span><strong>MinesNeon</strong><span>{escape(meta['brand'])}</span></span></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-open="{escape(meta['menu'])}" data-close="{escape(meta['menu'])}"><span></span><span></span><span></span><b>{escape(meta['menu'])}</b></button>
      {nav_html(filename, lang)}
      <div class="side-cta"><b>PIXELWIN: 500%</b><a class="btn btn-pulse" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(meta['bonus'])}</a></div>
    </aside>
    <main class="main">
      <header class="topbar"><small>{escape(meta['top'])}</small><a class="btn btn-pulse" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(meta['go'])}</a></header>
      <div class="container"><section class="hero article-hero"><div class="section-kicker">MinesNeon SEO Hub</div><h1>{escape(data['h1'])}</h1><p class="lead">{escape(data['lead'])}</p>{lang_switcher(kind, lang)}</section>{content(data['content'], lang)}</div>
      <footer class="footer"><p><strong>MinesNeon</strong> — {escape(meta['footer'])}</p></footer>
    </main>
  </div>
  <script src="assets/app.js" defer></script>
</body>
</html>
'''


def main():
    written = []
    for kind in FILENAME:
        for lang in LANGS:
            path = ROOT / FILENAME[kind][lang]
            path.write_text(render(kind, lang), encoding='utf-8')
            written.append(path.name)
    print('generated core multilingual pages:', len(written))
    print('\n'.join(written))

if __name__ == '__main__':
    main()
