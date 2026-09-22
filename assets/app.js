
(function(){
  const OFFER = 'https://lkzq.cc/644450';
  const toast = document.createElement('div');
  toast.className = 'toast';
  document.body.appendChild(toast);
  function showToast(msg){ toast.textContent = msg; toast.classList.add('show'); setTimeout(()=>toast.classList.remove('show'),2200); }
  document.querySelectorAll('a[href="https://lkzq.cc/644450"]').forEach(a=>{
    a.addEventListener('click',()=>{ try{ ym(106419573,'reachGoal','offer_click'); }catch(e){} });
  });
  const copy = document.getElementById('copyPromo');
  if(copy) copy.addEventListener('click', async()=>{
    const code = copy.dataset.code || 'PIXELWIN';
    try{ await navigator.clipboard.writeText(code); showToast('Промокод PIXELWIN скопирован'); }catch(e){ showToast('Скопируйте код: PIXELWIN'); }
  });
  const dGrid = document.getElementById('demoGrid');
  const sGrid = document.getElementById('signalGrid');
  if(!dGrid || !sGrid) return;
  const gamePanel = dGrid.closest('[data-demo-lang]') || dGrid.closest('.game-panel') || document.body;
  const balanceBox = document.getElementById('balanceBox');
  const profitBox = document.getElementById('profitBox');
  const statusBox = document.getElementById('gameStatus');
  const resetBalanceBtn = document.getElementById('resetBalanceBtn');
  const betInput = document.getElementById('betInput');
  const minesSelect = document.getElementById('minesSelect');
  const multBox = document.getElementById('multBox');
  const playBtn = document.getElementById('playBtn');
  const signalBtn = document.getElementById('signalBtn');
  if(!playBtn || !signalBtn || !betInput || !minesSelect || !multBox) return;

  const DEMO_LANG = (gamePanel.dataset.demoLang || document.documentElement.lang || 'ru').slice(0,2).toLowerCase();
  const CURRENCY = gamePanel.dataset.currency || '₽';
  const LOCALE = gamePanel.dataset.locale || document.documentElement.lang || 'ru-RU';
  const START_BALANCE = Math.max(0, Math.round(Number(gamePanel.dataset.startBalance) || 5000));
  const DEFAULT_BET = Math.max(1, Math.round(Number(gamePanel.dataset.defaultBet) || 100));
  const MIN_BET = Math.max(1, Math.round(Number(gamePanel.dataset.minBet) || 10));
  const BALANCE_KEY = gamePanel.dataset.storageKey || ('minesDemoBalance:' + DEMO_LANG);
  const TEXT = {
    ru:{cell:'Клетка ', bet:'СДЕЛАТЬ СТАВКУ', cashout:'ЗАБРАТЬ ', saved:'Баланс сохраняется в браузере. Сделайте демо-ставку и заберите выигрыш до бомбы.', lost:'Бомба забрала ставку {bet}. Баланс уже сохранён.', bomb:'Бомба! Ставка списана с демо-баланса', opened:'Открыто безопасных клеток: {opened}. Можно продолжить риск или забрать выигрыш.', noBalance:'Недостаточно демо-баланса', lower:'Уменьшите ставку или сбросьте баланс до {start}.', started:'Раунд начался, ставка списана', betSaved:'Ставка {bet} списана. Ищите безопасные клетки.', winAdded:'Выигрыш {win} добавлен к балансу', cashed:'Вы забрали {win}. Баланс сохранён в localStorage.', openOne:'Откройте хотя бы одну клетку', reset:'Демо-баланс сброшен', signal:'Сигнал создан: проверьте безопасные шаги в демо'},
    en:{cell:'Cell ', bet:'PLACE BET', cashout:'CASH OUT ', saved:'The balance is saved in this browser. Place a demo bet and cash out before a bomb.', lost:'A bomb took the {bet} bet. The balance is already saved.', bomb:'Bomb! The bet was deducted from the demo balance', opened:'Safe tiles opened: {opened}. Keep risking or cash out.', noBalance:'Not enough demo balance', lower:'Lower the bet or reset the balance to {start}.', started:'Round started, bet deducted', betSaved:'Bet {bet} deducted. Find safe tiles.', winAdded:'Win {win} added to balance', cashed:'You cashed out {win}. Balance saved in localStorage.', openOne:'Open at least one tile', reset:'Demo balance reset', signal:'Signal created: check safe steps in the demo'},
    es:{cell:'Casilla ', bet:'APOSTAR', cashout:'COBRAR ', saved:'El saldo se guarda en este navegador. Haz una apuesta demo y cobra antes de una bomba.', lost:'Una bomba quitó la apuesta de {bet}. El saldo ya está guardado.', bomb:'¡Bomba! La apuesta se descontó del saldo demo', opened:'Casillas seguras abiertas: {opened}. Puedes arriesgar más o cobrar.', noBalance:'Saldo demo insuficiente', lower:'Reduce la apuesta o reinicia el saldo a {start}.', started:'Ronda iniciada, apuesta descontada', betSaved:'Apuesta {bet} descontada. Busca casillas seguras.', winAdded:'Ganancia {win} añadida al saldo', cashed:'Cobraste {win}. Saldo guardado en localStorage.', openOne:'Abre al menos una casilla', reset:'Saldo demo reiniciado', signal:'Señal creada: revisa pasos seguros en la demo'},
    de:{cell:'Feld ', bet:'EINSATZ SETZEN', cashout:'AUSZAHLEN ', saved:'Das Guthaben wird in diesem Browser gespeichert. Setzen Sie demo und zahlen Sie vor einer Bombe aus.', lost:'Eine Bombe nahm den Einsatz {bet}. Das Guthaben ist gespeichert.', bomb:'Bombe! Der Einsatz wurde vom Demo-Guthaben abgezogen', opened:'Sichere Felder geöffnet: {opened}. Weiter riskieren oder auszahlen.', noBalance:'Nicht genug Demo-Guthaben', lower:'Senken Sie den Einsatz oder setzen Sie das Guthaben auf {start} zurück.', started:'Runde gestartet, Einsatz abgezogen', betSaved:'Einsatz {bet} abgezogen. Finden Sie sichere Felder.', winAdded:'Gewinn {win} zum Guthaben hinzugefügt', cashed:'Sie haben {win} ausgezahlt. Guthaben in localStorage gespeichert.', openOne:'Öffnen Sie mindestens ein Feld', reset:'Demo-Guthaben zurückgesetzt', signal:'Signal erstellt: sichere Schritte in der Demo prüfen'},
    ph:{cell:'Tile ', bet:'PLACE BET', cashout:'CASH OUT ', saved:'Naka-save ang balance sa browser na ito. Mag-demo bet at mag-cash out bago ang bomba.', lost:'Kinuha ng bomba ang {bet} bet. Naka-save na ang balance.', bomb:'Bomba! Nabawas ang bet sa demo balance', opened:'Safe tiles opened: {opened}. Pwede pang mag-risk o mag-cash out.', noBalance:'Kulang ang demo balance', lower:'Ibaba ang bet o i-reset ang balance sa {start}.', started:'Nagsimula ang round, nabawas ang bet', betSaved:'Nabawas ang bet na {bet}. Hanapin ang safe tiles.', winAdded:'Win na {win} idinagdag sa balance', cashed:'Na-cash out mo ang {win}. Naka-save ang balance sa localStorage.', openOne:'Magbukas muna ng isang tile', reset:'Na-reset ang demo balance', signal:'Signal created: tingnan ang safe steps sa demo'}
  };
  const L = TEXT[DEMO_LANG] || TEXT.ru;
  let mines = [], opened = 0, playing = false, bet = DEFAULT_BET, balance = loadBalance(), currentWin = 0;
  if(balanceBox) balanceBox.dataset.currency = CURRENCY;
  if(profitBox) profitBox.dataset.currency = CURRENCY;
  betInput.value = DEFAULT_BET;
  betInput.min = MIN_BET;
  function readStorage(key){ try{ return window.localStorage ? localStorage.getItem(key) : null; }catch(e){ return null; } }
  function writeStorage(key,value){ try{ if(window.localStorage) localStorage.setItem(key, value); }catch(e){} }
  function loadBalance(){ const saved = Number(readStorage(BALANCE_KEY)); return Number.isFinite(saved) && saved >= 0 ? Math.round(saved) : START_BALANCE; }
  function saveBalance(){ writeStorage(BALANCE_KEY, String(balance)); }
  function msg(key, data){ return (L[key] || TEXT.ru[key] || '').replace(/\{(\w+)\}/g, function(_, k){ return data && data[k] !== undefined ? data[k] : ''; }); }
  function money(n){ try{ return Math.max(0, Math.round(n)).toLocaleString(LOCALE); }catch(e){ return String(Math.max(0, Math.round(n))); } }
  function setStatus(text){ if(statusBox) statusBox.textContent = text; }
  function updateWallet(){ if(balanceBox) balanceBox.textContent = money(balance); if(profitBox) profitBox.textContent = money(currentWin); saveBalance(); }
  function countMines(){ return parseInt(minesSelect.value,10)||3; }
  function multiplier(m,s){ let x=1; for(let i=0;i<s;i++) x *= (25-i)/(25-m-i); return x*.97; }
  function board(){ mines=[]; const m=countMines(); while(mines.length<m){ const r=Math.floor(Math.random()*25); if(!mines.includes(r)) mines.push(r); } }
  function render(){
    dGrid.innerHTML=''; sGrid.innerHTML='';
    for(let i=0;i<25;i++){
      const c=document.createElement('button'); c.type='button'; c.className='cell'; c.setAttribute('aria-label',msg('cell')+(i+1)); c.addEventListener('click',function(){ clickCell(i,c); }); dGrid.appendChild(c);
      const sc=document.createElement('div'); sc.className='cell'; sGrid.appendChild(sc);
    }
  }
  function reset(){ opened=0; playing=false; currentWin=0; multBox.textContent='x1.00'; playBtn.textContent=msg('bet'); setStatus(msg('saved')); updateWallet(); board(); render(); }
  function loseRound(c){ c.classList.add('mine'); c.textContent='💣'; currentWin=0; updateWallet(); setStatus(msg('lost',{bet:money(bet)})); showToast(msg('bomb')); setTimeout(reset,950); }
  function clickCell(i,c){
    if(!playing || c.classList.contains('safe') || c.classList.contains('mine')) return;
    if(mines.includes(i)){ loseRound(c); return; }
    opened++; c.classList.add('safe'); c.textContent='💎'; const x=multiplier(countMines(),opened); currentWin=Math.round(bet*x); multBox.textContent='x'+x.toFixed(2); if(profitBox) profitBox.textContent=money(currentWin); playBtn.textContent=msg('cashout')+money(currentWin); setStatus(msg('opened',{opened:opened}));
  }
  playBtn.addEventListener('click',function(){
    if(!playing){
      bet=Math.max(MIN_BET, Math.round(parseFloat(betInput.value)||DEFAULT_BET));
      betInput.value=bet;
      if(bet>balance){ showToast(msg('noBalance')); setStatus(msg('lower',{start:money(START_BALANCE)})); return; }
      balance-=bet; currentWin=0; playing=true; opened=0; board(); render(); updateWallet(); showToast(msg('started')); setStatus(msg('betSaved',{bet:money(bet)})); playBtn.textContent=msg('cashout')+'0';
    }
    else if(opened>0){ balance+=currentWin; showToast(msg('winAdded',{win:money(currentWin)})); setStatus(msg('cashed',{win:money(currentWin)})); reset(); }
    else showToast(msg('openOne'));
  });
  if(resetBalanceBtn) resetBalanceBtn.addEventListener('click',function(){ balance=START_BALANCE; currentWin=0; updateWallet(); reset(); showToast(msg('reset')); });
  signalBtn.addEventListener('click',function(){
    if(!mines.length) board();
    Array.from(sGrid.children).forEach(function(c){ c.className='cell'; c.textContent=''; });
    const safe=[]; for(let i=0;i<25;i++) if(!mines.includes(i)) safe.push(i);
    for(let n=0;n<3 && safe.length;n++){ const pos=safe.splice(Math.floor(Math.random()*safe.length),1)[0]; const c=sGrid.children[pos]; if(c){ c.classList.add('safe'); c.textContent='⭐'; } }
    showToast(msg('signal'));
  });
  reset();
})();

(function(){
  const sidebar = document.querySelector('.sidebar');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.sidebar .nav');
  if(!sidebar || !toggle || !nav) return;
  let isOpen = sidebar.classList.contains('menu-open');
  let raf = 0;
  function setOpen(open){
    if(isOpen === open) return;
    isOpen = open;
    if(raf) cancelAnimationFrame(raf);
    raf = requestAnimationFrame(function(){
      sidebar.classList.toggle('menu-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  nav.querySelectorAll('.nav-subtoggle').forEach(function(btn){
    const group = btn.closest('.nav-group');
    if(!group) return;
    btn.setAttribute('aria-expanded', group.classList.contains('open') ? 'true' : 'false');
    btn.addEventListener('click', function(e){
      e.preventDefault();
      e.stopPropagation();
      const open = !group.classList.contains('open');
      group.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  toggle.addEventListener('click', function(e){
    e.stopPropagation();
    setOpen(!isOpen);
  }, {passive:true});
  nav.addEventListener('click', function(e){ if(e.target.closest('a')) setOpen(false); });
  document.addEventListener('click', function(e){ if(isOpen && !sidebar.contains(e.target)) setOpen(false); }, {passive:true});
  document.addEventListener('keydown', function(e){ if(isOpen && e.key === 'Escape') setOpen(false); });
  window.addEventListener('resize', function(){ if(isOpen && window.innerWidth > 820) setOpen(false); }, {passive:true});
})();

(function(){
  const switchers = Array.from(document.querySelectorAll('[data-lang-switcher]'));
  if(!switchers.length) return;
  function setOpen(box, open){
    if(box.classList.contains('open') === open) return;
    const toggle = box.querySelector('.lang-switcher-toggle');
    box.classList.toggle('open', open);
    if(toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  switchers.forEach(function(box){
    const toggle = box.querySelector('.lang-switcher-toggle');
    if(!toggle) return;
    toggle.addEventListener('click', function(e){
      e.stopPropagation();
      setOpen(box, !box.classList.contains('open'));
    }, {passive:true});
    box.addEventListener('click', function(e){ if(e.target.closest('.lang-options a')) setOpen(box, false); });
  });
  document.addEventListener('click', function(e){
    switchers.forEach(function(box){ if(box.classList.contains('open') && !box.contains(e.target)) setOpen(box, false); });
  }, {passive:true});
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape') switchers.forEach(function(box){ setOpen(box, false); });
  });
})();

(function(){
  const root = document.documentElement;
  const storageKey = 'minesneonTheme';
  const buttons = Array.from(document.querySelectorAll('[data-theme-toggle]'));
  if(!buttons.length) return;
  const meta = document.querySelector('meta[name="theme-color"]');
  function savedTheme(){ try{return localStorage.getItem(storageKey);}catch(e){return null;} }
  function storeTheme(theme){ try{localStorage.setItem(storageKey, theme);}catch(e){} }
  function applyTheme(theme){
    const light = theme === 'light';
    if(light) root.setAttribute('data-theme','light'); else root.removeAttribute('data-theme');
    if(meta) meta.setAttribute('content', light ? '#eef8ff' : '#050403');
    buttons.forEach(function(btn){
      btn.setAttribute('aria-pressed', light ? 'true' : 'false');
      const icon = btn.querySelector('.theme-toggle__icon');
      const text = btn.querySelector('.theme-toggle__text');
      if(icon) icon.textContent = light ? '☾' : '☀';
      if(text) text.textContent = light ? 'Темная тема' : 'Светлая тема';
    });
  }
  applyTheme(savedTheme() === 'light' ? 'light' : 'dark');
  buttons.forEach(function(btn){
    btn.addEventListener('click', function(){
      const next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      storeTheme(next);
      applyTheme(next);
    });
  });
})();

