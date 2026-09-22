from pathlib import Path
import json
import re

ROOT = Path('mines-seo-site')
SITE = 'https://minesneon.ru/'
LANGS = ('ru', 'en', 'es', 'de', 'ph')
HTML_LANG = {'ru': 'ru', 'en': 'en', 'es': 'es', 'de': 'de', 'ph': 'fil'}
HREFLANG = {'ru': 'ru', 'en': 'en', 'es': 'es', 'de': 'de', 'ph': 'fil'}

CORE_FILES = {
    'index': {'ru': 'index.html', 'en': 'index-en.html', 'es': 'index-es.html', 'de': 'index-de.html', 'ph': 'index-ph.html'},
    'promo': {'ru': 'promo.html', 'en': 'promo-en.html', 'es': 'promo-es.html', 'de': 'promo-de.html', 'ph': 'promo-ph.html'},
    'strategies-main': {'ru': 'strategies.html', 'en': 'strategies-main-en.html', 'es': 'strategies-main-es.html', 'de': 'strategies-main-de.html', 'ph': 'strategies-main-ph.html'},
    'faq': {'ru': 'faq.html', 'en': 'faq-en.html', 'es': 'faq-es.html', 'de': 'faq-de.html', 'ph': 'faq-ph.html'},
    'apk': {'ru': 'apk.html', 'en': 'apk-en.html', 'es': 'apk-es.html', 'de': 'apk-de.html', 'ph': 'apk-ph.html'},
    'other': {'ru': 'other.html', 'en': 'other-en.html', 'es': 'other-es.html', 'de': 'other-de.html', 'ph': 'other-ph.html'},
}

GUIDE_SLUGS = ('home', 'demo', 'bonus', 'promocode', 'registration', 'strategies', 'download', 'analog', 'hack', 'mines-game')

SEO = {
    'index': {
        'ru': ('Мины играть онлайн бесплатно — Mines demo 5×5 и сигналы', 'Играйте в мины онлайн бесплатно: демо Mines 5×5, баланс в браузере, сигналы безопасных клеток, стратегии и бонус PIXELWIN 500% для старта.', 'мины играть онлайн, играть в мины бесплатно, mines demo, mines сигналы, бот мины, mines casino, PIXELWIN'),
        'en': ('Play Mines Online Free — 5x5 Demo Game and Signals', 'Play Mines online for free with a 5x5 demo board, saved practice balance, safe-cell signals, strategy tips and PIXELWIN 500% bonus guide.', 'play mines online, mines demo, mines free, mines signals, mines bot, mines casino, PIXELWIN'),
        'es': ('Jugar Mines Online Gratis — Demo 5x5 y Señales', 'Juega Mines online gratis con demo 5x5, saldo guardado, señales de casillas seguras, estrategias y guía del bono PIXELWIN 500%.', 'jugar mines online, mines gratis, mines demo, señales mines, bot mines, casino mines, PIXELWIN'),
        'de': ('Mines Online Kostenlos Spielen — 5x5 Demo und Signale', 'Spielen Sie Mines online kostenlos mit 5x5 Demo, gespeichertem Übungsguthaben, sicheren Signalen, Strategien und PIXELWIN 500% Bonus.', 'Mines online spielen, Mines kostenlos, Mines Demo, Mines Signale, Mines Bot, Mines Casino, PIXELWIN'),
        'ph': ('Play Mines Online Free — 5x5 Demo Game at Signals', 'Maglaro ng Mines online free gamit ang 5x5 demo, saved practice balance, safe-cell signals, strategy tips at PIXELWIN 500% bonus guide.', 'play mines online, mines demo, mines free, mines signals, mines bot, mines casino, PIXELWIN'),
    },
    'promo': {
        'ru': ('Mines промокод PIXELWIN — бонус 500% для игры в мины', 'Актуальный промокод Mines PIXELWIN: как активировать VIP бонус 500%, увеличить депозит и начать играть в мины на деньги ответственнее.', 'mines промокод, промокод PIXELWIN, mines бонус 500, мины на деньги, mines casino'),
        'en': ('Mines Promo Code PIXELWIN — 500% Bonus for Mines', 'Use the Mines promo code PIXELWIN to activate a VIP 500% bonus, boost your deposit and start real-money Mines with smarter limits.', 'mines promo code, PIXELWIN promo, mines bonus 500, mines real money, mines casino'),
        'es': ('Código Promo Mines PIXELWIN — Bono 500% para Mines', 'Usa el código promo Mines PIXELWIN para activar un bono VIP 500%, ampliar el depósito y jugar Mines con límites más seguros.', 'código promo mines, PIXELWIN, bono mines 500, mines dinero real, casino mines'),
        'de': ('Mines Promo-Code PIXELWIN — 500% Bonus für Mines', 'Nutzen Sie den Mines Promo-Code PIXELWIN für den VIP Bonus 500%, mehr Startguthaben und verantwortliches Mines Echtgeld-Spiel.', 'Mines Promo Code, PIXELWIN, Mines Bonus 500, Mines Echtgeld, Mines Casino'),
        'ph': ('Mines Promo Code PIXELWIN — 500% Bonus for Mines', 'Gamitin ang Mines promo code PIXELWIN para ma-activate ang VIP 500% bonus, dagdagan ang deposit at maglaro nang may smart limits.', 'mines promo code, PIXELWIN promo, mines bonus 500, mines real money, mines casino'),
    },
    'strategies-main': {
        'ru': ('Стратегии Mines — Safe Step, Зигзаг, RTP и риск-менеджмент', 'Лучшие стратегии Mines для демо и реальной игры: Safe Step, Зигзаг, охотник, RTP, лимиты ставок и честный взгляд на сигналы.', 'стратегии mines, тактика mines, safe step, mines rtp, mines сигналы, риск менеджмент'),
        'en': ('Mines Strategies — Safe Step, Zigzag, RTP and Risk Control', 'Learn Mines strategies for demo and real play: Safe Step, Zigzag, hunter mode, RTP basics, bet limits and responsible signal use.', 'mines strategies, mines tactic, safe step, mines rtp, mines signals, risk management'),
        'es': ('Estrategias Mines — Safe Step, Zigzag, RTP y Control de Riesgo', 'Aprende estrategias Mines para demo y juego real: Safe Step, Zigzag, modo cazador, RTP, límites de apuesta y uso responsable de señales.', 'estrategias mines, táctica mines, safe step, mines rtp, señales mines, gestión de riesgo'),
        'de': ('Mines Strategien — Safe Step, Zigzag, RTP und Risikokontrolle', 'Lernen Sie Mines Strategien für Demo und Echtgeld: Safe Step, Zigzag, Hunter-Modus, RTP, Einsatzlimits und verantwortliche Signale.', 'Mines Strategien, Mines Taktik, Safe Step, Mines RTP, Mines Signale, Risikomanagement'),
        'ph': ('Mines Strategies — Safe Step, Zigzag, RTP at Risk Control', 'Alamin ang Mines strategies para sa demo at real play: Safe Step, Zigzag, hunter mode, RTP basics, bet limits at responsible signals.', 'mines strategies, mines tactic, safe step, mines rtp, mines signals, risk management'),
    },
    'strategies': {
        'ru': ('Стратегии Mines гайд — тактики, лимиты и безопасный cashout', 'Подробный гайд по стратегиям Mines: выбор мин, безопасные шаги, лимиты ставок, cashout, RTP и почему сигналы не дают гарантий.', 'стратегии mines гайд, тактики mines, безопасные шаги, cashout mines, лимиты ставок'),
        'en': ('Mines Strategy Guide — Tactics, Limits and Safe Cashout', 'Detailed Mines strategy guide: mine count, safe steps, bet limits, cashout timing, RTP and why signals never guarantee profit.', 'mines strategy guide, mines tactics, safe steps, mines cashout, betting limits'),
        'es': ('Guía de Estrategias Mines — Tácticas, Límites y Cashout', 'Guía detallada de estrategias Mines: número de minas, pasos seguros, límites, cashout, RTP y por qué las señales no garantizan ganancias.', 'guía estrategias mines, tácticas mines, pasos seguros, cashout mines, límites apuestas'),
        'de': ('Mines Strategie Guide — Taktiken, Limits und Sicherer Cashout', 'Detaillierter Mines Strategie-Guide: Minenanzahl, sichere Schritte, Einsatzlimits, Cashout, RTP und warum Signale nichts garantieren.', 'Mines Strategie Guide, Mines Taktiken, sichere Schritte, Mines Cashout, Einsatzlimits'),
        'ph': ('Mines Strategy Guide — Tactics, Limits at Safe Cashout', 'Detailed Mines strategy guide: mine count, safe steps, bet limits, cashout timing, RTP at bakit hindi guaranteed ang signals.', 'mines strategy guide, mines tactics, safe steps, mines cashout, betting limits'),
    },
    'faq': {
        'ru': ('Mines отзывы и FAQ — честность, выплаты, сигналы и демо', 'Ответы на вопросы про Mines: реальные отзывы, честность RNG, выплаты, демо-режим, сигналы, промокод PIXELWIN и безопасный старт.', 'mines отзывы, mines faq, mines выплаты, честность mines, mines демо, mines сигналы'),
        'en': ('Mines Reviews and FAQ — Fairness, Payouts, Signals and Demo', 'Mines FAQ with clear answers about reviews, RNG fairness, payouts, demo mode, signals, PIXELWIN promo code and safer first steps.', 'mines reviews, mines faq, mines payouts, mines fairness, mines demo, mines signals'),
        'es': ('Opiniones Mines y FAQ — Justicia, Pagos, Señales y Demo', 'FAQ de Mines con respuestas sobre opiniones, justicia RNG, pagos, demo, señales, código PIXELWIN y primeros pasos más seguros.', 'opiniones mines, faq mines, pagos mines, justicia mines, mines demo, señales mines'),
        'de': ('Mines Bewertungen und FAQ — Fairness, Auszahlungen und Demo', 'Mines FAQ mit Antworten zu Bewertungen, RNG-Fairness, Auszahlungen, Demo, Signalen, PIXELWIN Promo-Code und sicherem Start.', 'Mines Bewertungen, Mines FAQ, Mines Auszahlungen, Mines Fairness, Mines Demo, Mines Signale'),
        'ph': ('Mines Reviews at FAQ — Fairness, Payouts, Signals at Demo', 'Mines FAQ na may sagot tungkol sa reviews, RNG fairness, payouts, demo mode, signals, PIXELWIN promo code at safer first steps.', 'mines reviews, mines faq, mines payouts, mines fairness, mines demo, mines signals'),
    },
    'apk': {
        'ru': ('Mines скачать на телефон — APK, PWA, Android и iPhone', 'Как скачать Mines безопасно: APK или PWA, установка на Android Chrome и iPhone Safari, быстрый доступ к демо, сигналам и бонусу.', 'mines скачать, скачать mines apk, mines pwa, mines android, mines iphone, приложение mines'),
        'en': ('Download Mines on Mobile — APK, PWA, Android and iPhone', 'How to download Mines safely: APK or PWA install, Android Chrome, iPhone Safari and quick access to demo, signals and bonus pages.', 'download mines, mines apk, mines pwa, mines android, mines iphone, mines app'),
        'es': ('Descargar Mines en Móvil — APK, PWA, Android y iPhone', 'Cómo descargar Mines con seguridad: APK o PWA, instalación en Android Chrome y iPhone Safari, acceso rápido a demo, señales y bono.', 'descargar mines, mines apk, mines pwa, mines android, mines iphone, app mines'),
        'de': ('Mines Herunterladen — APK, PWA, Android und iPhone', 'So laden Sie Mines sicher herunter: APK oder PWA, Installation in Android Chrome und iPhone Safari, schneller Zugriff auf Demo und Bonus.', 'Mines herunterladen, Mines APK, Mines PWA, Mines Android, Mines iPhone, Mines App'),
        'ph': ('Download Mines sa Mobile — APK, PWA, Android at iPhone', 'Paano ligtas i-download ang Mines: APK o PWA install, Android Chrome, iPhone Safari at quick access sa demo, signals at bonus.', 'download mines, mines apk, mines pwa, mines android, mines iphone, mines app'),
    },
    'other': {
        'ru': ('Аналоги Mines — Lucky Jet, Aviator, Rocket Queen и краш-игры', 'Подборка игр похожих на Mines: Lucky Jet, Aviator, Speed and Cash, Rocket Queen, crash-форматы, коэффициенты и советы по риску.', 'аналоги mines, игры похожие на mines, lucky jet, aviator, rocket queen, краш игры'),
        'en': ('Mines Alternatives — Lucky Jet, Aviator, Rocket Queen and Crash Games', 'Explore games like Mines: Lucky Jet, Aviator, Speed and Cash, Rocket Queen, crash mechanics, multipliers and risk-control tips.', 'mines alternatives, games like mines, lucky jet, aviator, rocket queen, crash games'),
        'es': ('Alternativas a Mines — Lucky Jet, Aviator, Rocket Queen y Crash Games', 'Explora juegos parecidos a Mines: Lucky Jet, Aviator, Speed and Cash, Rocket Queen, mecánicas crash, multiplicadores y riesgo.', 'alternativas mines, juegos como mines, lucky jet, aviator, rocket queen, juegos crash'),
        'de': ('Mines Alternativen — Lucky Jet, Aviator, Rocket Queen und Crash Games', 'Entdecken Sie Spiele wie Mines: Lucky Jet, Aviator, Speed and Cash, Rocket Queen, Crash-Mechaniken, Multiplikatoren und Risiko-Tipps.', 'Mines Alternativen, Spiele wie Mines, Lucky Jet, Aviator, Rocket Queen, Crash Games'),
        'ph': ('Mines Alternatives — Lucky Jet, Aviator, Rocket Queen at Crash Games', 'Tingnan ang games like Mines: Lucky Jet, Aviator, Speed and Cash, Rocket Queen, crash mechanics, multipliers at risk-control tips.', 'mines alternatives, games like mines, lucky jet, aviator, rocket queen, crash games'),
    },
    'home': {
        'ru': ('Mines игра — обзор, правила и как играть на деньги', 'Полный обзор Mines: правила поля 5×5, мины и звёзды, cashout, множители, демо-практика и переход к игре на деньги.', 'mines игра, mines обзор, как играть в mines, mines на деньги, правила mines'),
        'en': ('Mines Game Review — Rules, Real Money Play and Tips', 'Complete Mines game review: 5x5 board rules, mines and stars, cashout, multipliers, demo practice and real-money play tips.', 'mines game, mines review, how to play mines, mines real money, mines rules'),
        'es': ('Juego Mines — Reseña, Reglas y Cómo Jugar con Dinero', 'Reseña completa de Mines: reglas del tablero 5x5, minas y estrellas, cashout, multiplicadores, demo y juego con dinero real.', 'juego mines, reseña mines, cómo jugar mines, mines dinero real, reglas mines'),
        'de': ('Mines Spiel — Test, Regeln und Echtgeld Tipps', 'Vollständiger Mines Test: 5x5 Regeln, Minen und Sterne, Cashout, Multiplikatoren, Demo-Übung und Echtgeld-Tipps.', 'Mines Spiel, Mines Test, Mines Regeln, Mines Echtgeld, Mines Anleitung'),
        'ph': ('Mines Game Review — Rules, Real Money Play at Tips', 'Complete Mines game review: 5x5 board rules, mines and stars, cashout, multipliers, demo practice at real-money tips.', 'mines game, mines review, how to play mines, mines real money, mines rules'),
    },
    'demo': {
        'ru': ('Mines demo бесплатно — играть в мины без депозита', 'Запустите Mines demo бесплатно: тренировка на поле 5×5, выбор мин, безопасные клетки, демо-баланс и понимание коэффициентов.', 'mines demo, mines бесплатно, играть в мины без депозита, демо mines, mines 5x5'),
        'en': ('Mines Demo Free — Play Mines Without Deposit', 'Start the free Mines demo: 5x5 practice board, mines selection, safe tiles, demo balance and multiplier learning without deposit.', 'mines demo, mines free, play mines no deposit, free mines game, mines 5x5'),
        'es': ('Mines Demo Gratis — Jugar Mines Sin Depósito', 'Inicia la demo gratis de Mines: tablero 5x5, selección de minas, casillas seguras, saldo demo y multiplicadores sin depósito.', 'mines demo, mines gratis, jugar mines sin depósito, juego mines gratis, mines 5x5'),
        'de': ('Mines Demo Kostenlos — Ohne Einzahlung Spielen', 'Starten Sie die kostenlose Mines Demo: 5x5 Feld, Minenauswahl, sichere Felder, Demo-Guthaben und Multiplikatoren ohne Einzahlung.', 'Mines Demo, Mines kostenlos, Mines ohne Einzahlung, kostenloses Mines Spiel, Mines 5x5'),
        'ph': ('Mines Demo Free — Play Mines Without Deposit', 'Simulan ang free Mines demo: 5x5 practice board, mines selection, safe tiles, demo balance at multipliers nang walang deposit.', 'mines demo, mines free, play mines no deposit, free mines game, mines 5x5'),
    },
    'bonus': {
        'ru': ('Mines бонус 500% — как получить PIXELWIN для игры', 'Разбор бонуса Mines 500%: промокод PIXELWIN, условия активации, депозит, лимиты и как использовать бонус ответственно.', 'mines бонус, бонус mines 500, PIXELWIN бонус, mines депозит, бонус казино mines'),
        'en': ('Mines Bonus 500% — How to Claim PIXELWIN Offer', 'Mines 500% bonus guide: PIXELWIN promo code, activation steps, deposit tips, limits and responsible bonus use.', 'mines bonus, mines 500 bonus, PIXELWIN bonus, mines deposit, mines casino bonus'),
        'es': ('Bono Mines 500% — Cómo Reclamar PIXELWIN', 'Guía del bono Mines 500%: código PIXELWIN, pasos de activación, depósito, límites y uso responsable del bono.', 'bono mines, bono mines 500, bono PIXELWIN, depósito mines, bono casino mines'),
        'de': ('Mines Bonus 500% — So Holen Sie PIXELWIN', 'Mines 500% Bonus Anleitung: PIXELWIN Promo-Code, Aktivierung, Einzahlung, Limits und verantwortliche Bonusnutzung.', 'Mines Bonus, Mines 500 Bonus, PIXELWIN Bonus, Mines Einzahlung, Mines Casino Bonus'),
        'ph': ('Mines Bonus 500% — How to Claim PIXELWIN Offer', 'Mines 500% bonus guide: PIXELWIN promo code, activation steps, deposit tips, limits at responsible bonus use.', 'mines bonus, mines 500 bonus, PIXELWIN bonus, mines deposit, mines casino bonus'),
    },
    'promocode': {
        'ru': ('Промокод Mines PIXELWIN — VIP код на бонус 500%', 'Как применить промокод Mines PIXELWIN: регистрация, активация VIP кода, бонус 500%, депозит и советы для безопасного старта.', 'промокод mines, PIXELWIN код, mines vip код, mines бонус 500, промокод казино'),
        'en': ('Mines Promo Code PIXELWIN — VIP Code for 500% Bonus', 'How to use Mines promo code PIXELWIN: registration, VIP code activation, 500% bonus, deposit tips and safer start checklist.', 'mines promo code, PIXELWIN code, mines vip code, mines 500 bonus, casino promo code'),
        'es': ('Código Promocional Mines PIXELWIN — VIP 500%', 'Cómo usar el código Mines PIXELWIN: registro, activación VIP, bono 500%, depósito y consejos para empezar con seguridad.', 'código promocional mines, código PIXELWIN, código vip mines, bono mines 500, promo casino'),
        'de': ('Mines Promo-Code PIXELWIN — VIP Code für 500% Bonus', 'So nutzen Sie den Mines Promo-Code PIXELWIN: Registrierung, VIP Aktivierung, 500% Bonus, Einzahlung und sicherer Start.', 'Mines Promo Code, PIXELWIN Code, Mines VIP Code, Mines 500 Bonus, Casino Promo Code'),
        'ph': ('Mines Promo Code PIXELWIN — VIP Code for 500% Bonus', 'Paano gamitin ang Mines promo code PIXELWIN: registration, VIP activation, 500% bonus, deposit tips at safer start checklist.', 'mines promo code, PIXELWIN code, mines vip code, mines 500 bonus, casino promo code'),
    },
    'registration': {
        'ru': ('Mines регистрация — создать аккаунт и активировать бонус', 'Пошаговая регистрация в Mines casino: создание аккаунта, промокод PIXELWIN, верификация, депозит и безопасные настройки.', 'mines регистрация, зарегистрироваться mines, аккаунт mines, PIXELWIN регистрация, mines casino'),
        'en': ('Mines Registration — Create Account and Activate Bonus', 'Step-by-step Mines casino registration: account setup, PIXELWIN promo code, verification, deposit and safer account settings.', 'mines registration, sign up mines, mines account, PIXELWIN registration, mines casino'),
        'es': ('Registro Mines — Crear Cuenta y Activar Bono', 'Registro paso a paso en Mines casino: crear cuenta, código PIXELWIN, verificación, depósito y ajustes de seguridad.', 'registro mines, crear cuenta mines, cuenta mines, PIXELWIN registro, casino mines'),
        'de': ('Mines Registrierung — Konto Erstellen und Bonus Aktivieren', 'Schrittweise Mines Casino Registrierung: Konto erstellen, PIXELWIN Promo-Code, Verifizierung, Einzahlung und Sicherheitseinstellungen.', 'Mines Registrierung, Mines anmelden, Mines Konto, PIXELWIN Registrierung, Mines Casino'),
        'ph': ('Mines Registration — Create Account and Activate Bonus', 'Step-by-step Mines casino registration: account setup, PIXELWIN promo code, verification, deposit at safer account settings.', 'mines registration, sign up mines, mines account, PIXELWIN registration, mines casino'),
    },
    'download': {
        'ru': ('Mines download — скачать APK или установить PWA', 'Инструкция Mines download: безопасная установка APK/PWA, Android, iOS, быстрый запуск демо-игры, сигналов и страницы бонуса.', 'mines download, mines apk, скачать mines, mines pwa, mines android, mines ios'),
        'en': ('Mines Download — Install APK or PWA Safely', 'Mines download guide: safe APK/PWA installation, Android, iOS, quick launch of demo game, signals and bonus page.', 'mines download, mines apk, download mines, mines pwa, mines android, mines ios'),
        'es': ('Mines Download — Instalar APK o PWA con Seguridad', 'Guía Mines download: instalación segura APK/PWA, Android, iOS, acceso rápido a demo, señales y bono.', 'mines download, mines apk, descargar mines, mines pwa, mines android, mines ios'),
        'de': ('Mines Download — APK oder PWA Sicher Installieren', 'Mines Download Anleitung: sichere APK/PWA Installation, Android, iOS, schneller Start von Demo, Signalen und Bonusseite.', 'Mines Download, Mines APK, Mines herunterladen, Mines PWA, Mines Android, Mines iOS'),
        'ph': ('Mines Download — Install APK or PWA Safely', 'Mines download guide: safe APK/PWA installation, Android, iOS, quick launch ng demo game, signals at bonus page.', 'mines download, mines apk, download mines, mines pwa, mines android, mines ios'),
    },
    'analog': {
        'ru': ('Аналоги Mines — лучшие игры похожие на мины онлайн', 'Сравнение аналогов Mines: crash-игры, поля с риском, множители, Lucky Jet, Aviator и советы по выбору безопасного формата.', 'аналоги mines, игры похожие на мины, mines alternatives, lucky jet, aviator, crash игры'),
        'en': ('Mines Alternatives — Best Games Like Mines Online', 'Compare Mines alternatives: crash games, risk-grid formats, multipliers, Lucky Jet, Aviator and tips for choosing safer formats.', 'mines alternatives, games like mines, mines similar games, lucky jet, aviator, crash games'),
        'es': ('Alternativas Mines — Mejores Juegos Parecidos a Mines', 'Compara alternativas a Mines: juegos crash, formatos de riesgo, multiplicadores, Lucky Jet, Aviator y consejos de elección.', 'alternativas mines, juegos parecidos a mines, juegos similares mines, lucky jet, aviator, juegos crash'),
        'de': ('Mines Alternativen — Beste Spiele Wie Mines Online', 'Vergleichen Sie Mines Alternativen: Crash Games, Risiko-Raster, Multiplikatoren, Lucky Jet, Aviator und Tipps zur Auswahl.', 'Mines Alternativen, Spiele wie Mines, ähnliche Mines Spiele, Lucky Jet, Aviator, Crash Games'),
        'ph': ('Mines Alternatives — Best Games Like Mines Online', 'Compare Mines alternatives: crash games, risk-grid formats, multipliers, Lucky Jet, Aviator at tips sa safer formats.', 'mines alternatives, games like mines, mines similar games, lucky jet, aviator, crash games'),
    },
    'hack': {
        'ru': ('Mines predictor и взлом — правда о сигналах и ботах', 'Честный разбор Mines predictor, ботов и запросов на взлом: почему гарантий нет, как работают сигналы и как снижать риск.', 'mines predictor, mines взлом, бот mines, mines сигналы, predictor mines, mines hack'),
        'en': ('Mines Predictor and Hack — Truth About Signals and Bots', 'Honest guide to Mines predictor tools, bots and hack claims: why guarantees do not exist, how signals work and how to reduce risk.', 'mines predictor, mines hack, mines bot, mines signals, predictor mines, mines safe cells'),
        'es': ('Mines Predictor y Hack — Verdad Sobre Señales y Bots', 'Guía honesta sobre Mines predictor, bots y supuestos hacks: por qué no hay garantías, cómo funcionan las señales y cómo reducir riesgo.', 'mines predictor, mines hack, bot mines, señales mines, predictor mines, casillas seguras'),
        'de': ('Mines Predictor und Hack — Wahrheit über Signale und Bots', 'Ehrlicher Guide zu Mines Predictor, Bots und Hack-Behauptungen: keine Garantien, Signal-Logik und Risikoreduzierung.', 'Mines Predictor, Mines Hack, Mines Bot, Mines Signale, Predictor Mines, sichere Felder'),
        'ph': ('Mines Predictor and Hack — Truth About Signals and Bots', 'Honest guide sa Mines predictor tools, bots at hack claims: bakit walang guarantees, paano gumagana signals at paano bawasan risk.', 'mines predictor, mines hack, mines bot, mines signals, predictor mines, mines safe cells'),
    },
    'mines-game': {
        'ru': ('Игра Mines онлайн — правила, демо, стратегии и бонус', 'Игра Mines онлайн: правила поля, выбор количества мин, cashout, демо-режим, стратегии, сигналы и бонус PIXELWIN для старта.', 'игра mines, mines онлайн, правила mines, mines demo, mines стратегии, mines бонус'),
        'en': ('Mines Game Online — Rules, Demo, Strategies and Bonus', 'Mines game online guide: board rules, mine count, cashout, demo mode, strategies, signals and PIXELWIN bonus for a smarter start.', 'mines game online, mines rules, mines demo, mines strategies, mines bonus, play mines'),
        'es': ('Juego Mines Online — Reglas, Demo, Estrategias y Bono', 'Guía del juego Mines online: reglas, número de minas, cashout, demo, estrategias, señales y bono PIXELWIN para empezar mejor.', 'juego mines online, reglas mines, mines demo, estrategias mines, bono mines, jugar mines'),
        'de': ('Mines Spiel Online — Regeln, Demo, Strategien und Bonus', 'Mines Spiel Online Guide: Regeln, Minenanzahl, Cashout, Demo-Modus, Strategien, Signale und PIXELWIN Bonus für den Start.', 'Mines Spiel online, Mines Regeln, Mines Demo, Mines Strategien, Mines Bonus, Mines spielen'),
        'ph': ('Mines Game Online — Rules, Demo, Strategies at Bonus', 'Mines game online guide: board rules, mine count, cashout, demo mode, strategies, signals at PIXELWIN bonus for smarter start.', 'mines game online, mines rules, mines demo, mines strategies, mines bonus, play mines'),
    },
}


def page_info(path: Path):
    name = path.name
    for slug, by_lang in CORE_FILES.items():
        for lang, filename in by_lang.items():
            if name == filename:
                return slug, lang
    match = re.fullmatch(r'(.+)-(ru|en|es|de|ph)\.html', name)
    if match and match.group(1) in GUIDE_SLUGS:
        return match.group(1), match.group(2)
    return None, None


def esc_attr(value: str) -> str:
    return value.replace('&', '&').replace('"', '"').replace('<', '<').replace('>', '>')


def replace_meta(text: str, name: str, content: str) -> str:
    tag = f'<meta name="{name}" content="{esc_attr(content)}">'
    if re.search(rf'<meta\s+name=["\']{re.escape(name)}["\'][^>]*>', text, re.I):
        return re.sub(rf'<meta\s+name=["\']{re.escape(name)}["\'][^>]*>', tag, text, count=1, flags=re.I)
    return re.sub(r'(<meta\s+name=["\']robots["\'][^>]*>)', tag + '\n  \\1', text, count=1, flags=re.I)


def replace_property(text: str, prop: str, content: str) -> str:
    tag = f'<meta property="{prop}" content="{esc_attr(content)}">'
    return re.sub(rf'<meta\s+property=["\']{re.escape(prop)}["\'][^>]*>', tag, text, count=1, flags=re.I)


def replace_twitter(text: str, name: str, content: str) -> str:
    tag = f'<meta name="{name}" content="{esc_attr(content)}">'
    return re.sub(rf'<meta\s+name=["\']{re.escape(name)}["\'][^>]*>', tag, text, count=1, flags=re.I)


def update_json_ld(text: str, title: str, desc: str):
    def repl(match):
        raw = match.group(1)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return match.group(0)
        if 'headline' in data:
            data['headline'] = title
        if 'name' in data:
            data['name'] = title
        data['description'] = desc
        return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'
    return re.sub(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', repl, text, count=1, flags=re.S | re.I)


def optimize_file(path: Path):
    slug, lang = page_info(path)
    if not slug or slug not in SEO:
        return False, None
    title, desc, keywords = SEO[slug][lang]
    text = path.read_text(encoding='utf-8-sig')
    text = re.sub(r'<html\s+lang=["\'][^"\']+["\']', f'<html lang="{HTML_LANG[lang]}"', text, count=1, flags=re.I)
    text = re.sub(r'<title>.*?</title>', f'<title>{esc_attr(title)}</title>', text, count=1, flags=re.S | re.I)
    text = replace_meta(text, 'description', desc)
    text = replace_meta(text, 'keywords', keywords)
    text = replace_property(text, 'og:title', title)
    text = replace_property(text, 'og:description', desc)
    text = replace_twitter(text, 'twitter:title', title)
    text = replace_twitter(text, 'twitter:description', desc)
    text = update_json_ld(text, title, desc)
    path.write_text(text, encoding='utf-8')
    return True, (title, desc, keywords)


def main():
    updated = 0
    report = []
    for path in sorted(ROOT.glob('*.html')):
        ok, meta = optimize_file(path)
        if ok:
            updated += 1
            title, desc, keywords = meta
            report.append((path.name, len(title), len(desc), len(keywords)))
    print(f'updated seo files: {updated}')
    too_long = [r for r in report if r[1] > 70 or r[2] > 165]
    missing = []
    for path in sorted(ROOT.glob('*.html')):
        text = path.read_text(encoding='utf-8')
        if '<meta name="description"' not in text or '<meta name="keywords"' not in text:
            missing.append(path.name)
    print('too_long:', too_long if too_long else 'none')
    print('missing_meta:', missing if missing else 'none')
    print('sample report:')
    for item in report[:12]:
        print(item)

if __name__ == '__main__':
    main()
