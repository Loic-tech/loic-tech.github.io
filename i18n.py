# -*- coding: utf-8 -*-
f='index.html'
h=open(f,encoding='utf-8').read()
miss=[]
def rep(old,new):
    global h
    if old not in h:
        miss.append(old[:70])
        return
    h=h.replace(old,new)

# add data-en="X" attribute to an opening tag matched by full element OR opening-tag
def attr(open_tag, en):
    rep(open_tag, open_tag[:-1]+' data-en="'+en+'">' if open_tag.endswith('>') else open_tag)

# ---- NAV ----
rep('<a href="#about">À propos</a>','<a href="#about" data-en="About">À propos</a>')
rep('<a href="#experience">Expérience</a>','<a href="#experience" data-en="Experience">Expérience</a>')
rep('<a href="#projects">Réalisations</a>','<a href="#projects" data-en="Projects">Réalisations</a>')
rep('<a href="#skills">Compétences</a>','<a href="#skills" data-en="Skills">Compétences</a>')
rep('<button class="theme-btn" id="themeBtn" title="Changer de thème">🌙</button>',
    '<button class="lang-btn" id="langBtn" title="Language">EN</button><button class="theme-btn" id="themeBtn" title="Changer de thème / Toggle theme">🌙</button>')

# ---- HERO ----
rep('<div class="hero-badge reveal"><span class="status-dot"></span>Disponible · Paris, Île-de-France</div>',
    '<div class="hero-badge reveal"><span class="status-dot"></span><span data-en="Available · Paris, France">Disponible · Paris, Île-de-France</span></div>')
rep('<h1 class="reveal d1">Bonjour, je suis<br><span class="grad">Loïc Gnagoh</span></h1>',
    '<h1 class="reveal d1"><span data-en="Hi, I\'m">Bonjour, je suis</span><br><span class="grad">Loïc Gnagoh</span></h1>')
rep('<p class="lead reveal d3">Développeur Java Full-Stack confirmé. Je conçois et fais évoluer des applications d\'entreprise critiques — APIs, microservices et messaging — pour de grands groupes comme le Crédit Agricole et Renault.</p>',
    '<p class="lead reveal d3" data-en="Senior Java Full-Stack developer. I design and evolve business-critical applications — APIs, microservices and messaging — for major groups such as Crédit Agricole and Renault.">Développeur Java Full-Stack confirmé. Je conçois et fais évoluer des applications d\'entreprise critiques — APIs, microservices et messaging — pour de grands groupes comme le Crédit Agricole et Renault.</p>')
rep('<a href="#contact" class="btn btn-primary">Me contacter →</a>','<a href="#contact" class="btn btn-primary" data-en="Get in touch →">Me contacter →</a>')
rep('<a href="#experience" class="btn btn-ghost">Voir mon parcours</a>','<a href="#experience" class="btn btn-ghost" data-en="See my journey">Voir mon parcours</a>')
rep('<div class="lbl">ans d\'expérience</div>','<div class="lbl" data-en="years of experience">ans d\'expérience</div>')
rep('<div class="lbl">grands groupes</div>','<div class="lbl" data-en="major companies">grands groupes</div>')
rep('<div class="lbl">alternants encadrés</div>','<div class="lbl" data-en="juniors mentored">alternants encadrés</div>')

# ---- ABOUT ----
rep('<span class="eyebrow reveal">01 — À propos</span>','<span class="eyebrow reveal" data-en="01 — About">01 — À propos</span>')
rep('<h2 class="title reveal d1">Du code propre,<br>des systèmes qui tiennent.</h2>','<h2 class="title reveal d1" data-en="Clean code,<br>systems that hold.">Du code propre,<br>des systèmes qui tiennent.</h2>')
rep('<p class="section-sub reveal d2">Spécialisé dans les architectures Java / Spring Boot, j\'interviens sur l\'ensemble du cycle de vie applicatif dans des environnements Agile et DevOps.</p>','<p class="section-sub reveal d2" data-en="Specialized in Java / Spring Boot architectures, I work across the full application lifecycle in Agile and DevOps environments.">Spécialisé dans les architectures Java / Spring Boot, j\'interviens sur l\'ensemble du cycle de vie applicatif dans des environnements Agile et DevOps.</p>')
rep('<p>Développeur Java Full-Stack confirmé, je conçois, développe et maintiens des applications d\'entreprise critiques au sein de grands groupes (Crédit Agricole, Renault).</p>','<p data-en="Senior Java Full-Stack developer, I design, build and maintain business-critical applications within major groups (Crédit Agricole, Renault).">Développeur Java Full-Stack confirmé, je conçois, développe et maintiens des applications d\'entreprise critiques au sein de grands groupes (Crédit Agricole, Renault).</p>')
rep('<p>Expert des architectures Java / Spring Boot, des APIs RESTful, des microservices et du messaging (Kafka, MQ), je travaille de bout en bout : conception, développement, déploiement (Docker, Kubernetes, Cloud) et support de production.</p>','<p data-en="Expert in Java / Spring Boot architectures, RESTful APIs, microservices and messaging (Kafka, MQ), I work end-to-end: design, development, deployment (Docker, Kubernetes, Cloud) and production support.">Expert des architectures Java / Spring Boot, des APIs RESTful, des microservices et du messaging (Kafka, MQ), je travaille de bout en bout : conception, développement, déploiement (Docker, Kubernetes, Cloud) et support de production.</p>')
rep('<p>Soucieux de la qualité du code, de la sécurité et de la performance, j\'accompagne aussi mes pairs — revues de code, montée en compétence — et je contribue à l\'amélioration continue des solutions. J\'intègre les outils IA modernes (Claude Code, Codex) dans mon flux de développement.</p>','<p data-en="Committed to code quality, security and performance, I also mentor my peers — code reviews, upskilling — and contribute to the continuous improvement of solutions. I integrate modern AI tools (Claude Code, Codex) into my development workflow.">Soucieux de la qualité du code, de la sécurité et de la performance, j\'accompagne aussi mes pairs — revues de code, montée en compétence — et je contribue à l\'amélioration continue des solutions. J\'intègre les outils IA modernes (Claude Code, Codex) dans mon flux de développement.</p>')
rep('<div class="t">Architecture Hexagonale / DDD</div>','<div class="t" data-en="Hexagonal Architecture / DDD">Architecture Hexagonale / DDD</div>')
rep('<div class="s">Diplôme validé avec mention · 2021</div>','<div class="s" data-en="Degree obtained with honors · 2021">Diplôme validé avec mention · 2021</div>')
rep('<div class="t">Langues</div>','<div class="t" data-en="Languages">Langues</div>')
rep('<div class="s">Français natif · Anglais opérationnel</div>','<div class="s" data-en="Native French · Working English">Français natif · Anglais opérationnel</div>')

# ---- EXPERIENCE ----
rep('<span class="eyebrow reveal">02 — Parcours</span>','<span class="eyebrow reveal" data-en="02 — Journey">02 — Parcours</span>')
rep('<h2 class="title reveal d1">Expérience professionnelle</h2>','<h2 class="title reveal d1" data-en="Professional experience">Expérience professionnelle</h2>')
rep('<p class="section-sub reveal d2">Cinq années à concevoir des applications critiques pour des leaders de la banque et de l\'industrie.</p>','<p class="section-sub reveal d2" data-en="Five years building critical applications for banking and industry leaders.">Cinq années à concevoir des applications critiques pour des leaders de la banque et de l\'industrie.</p>')
rep('<span class="tl-role">Développeur Java</span>','<span class="tl-role" data-en="Java Developer">Développeur Java</span>')
rep('<span class="tl-date">Avr. 2024 — Présent</span>','<span class="tl-date" data-en="Apr. 2024 — Present">Avr. 2024 — Présent</span>')
rep('<div class="tl-company">VINCI Energies · CDI — pour le <b>Crédit Agricole</b></div>','<div class="tl-company" data-en="VINCI Energies · Permanent — for <b>Crédit Agricole</b>">VINCI Energies · CDI — pour le <b>Crédit Agricole</b></div>')
rep('<li>Conception et développement d\'APIs RESTful avec Java & Spring Boot pour le SI bancaire.</li>','<li data-en="Design and development of RESTful APIs with Java &amp; Spring Boot for the banking IS.">Conception et développement d\'APIs RESTful avec Java & Spring Boot pour le SI bancaire.</li>')
rep('<li>Développement et maintenance de microservices ; études techniques et analyses d\'impacts.</li>','<li data-en="Development and maintenance of microservices; technical studies and impact analyses.">Développement et maintenance de microservices ; études techniques et analyses d\'impacts.</li>')
rep('<li>Diagnostic et résolution des incidents de production (support applicatif).</li>','<li data-en="Diagnosis and resolution of production incidents (application support).">Diagnostic et résolution des incidents de production (support applicatif).</li>')
rep('<li>Déploiements Docker / Kubernetes ; gestion des bases PostgreSQL.</li>','<li data-en="Docker / Kubernetes deployments; PostgreSQL database management.">Déploiements Docker / Kubernetes ; gestion des bases PostgreSQL.</li>')
rep('<li>Contribution à la qualité, la sécurité du code et l\'amélioration continue.</li>','<li data-en="Contribution to code quality, security and continuous improvement.">Contribution à la qualité, la sécurité du code et l\'amélioration continue.</li>')
rep('<span class="tl-role">Développeur Java / Angular</span>','<span class="tl-role" data-en="Java / Angular Developer">Développeur Java / Angular</span>')
rep('<span class="tl-date">Fév. 2022 — Avr. 2024</span>','<span class="tl-date" data-en="Feb. 2022 — Apr. 2024">Fév. 2022 — Avr. 2024</span>')
rep('<div class="tl-company">EXTIA · CDI — pour le <b>Groupe Renault</b></div>','<div class="tl-company" data-en="EXTIA · Permanent — for <b>Renault Group</b>">EXTIA · CDI — pour le <b>Groupe Renault</b></div>')
rep('<li>Analyse des besoins, conception et développement de fonctionnalités Full-Stack.</li>','<li data-en="Requirements analysis, design and development of Full-Stack features.">Analyse des besoins, conception et développement de fonctionnalités Full-Stack.</li>')
rep('<li>Migration applicative Java & Angular ; documentation des APIs.</li>','<li data-en="Java &amp; Angular application migration; API documentation.">Migration applicative Java & Angular ; documentation des APIs.</li>')
rep('<li>Migration Cloud AWS → GCP & monitoring (Dynatrace).</li>','<li data-en="Cloud migration AWS → GCP &amp; monitoring (Dynatrace).">Migration Cloud AWS → GCP & monitoring (Dynatrace).</li>')
rep('<li>Mise en place de pipelines CI/CD ; déploiements Kubernetes.</li>','<li data-en="CI/CD pipeline setup; Kubernetes deployments.">Mise en place de pipelines CI/CD ; déploiements Kubernetes.</li>')
rep('<li>Encadrement technique de 2 alternants (revues de code, montée en compétence).</li>','<li data-en="Technical mentoring of 2 work-study students (code reviews, upskilling).">Encadrement technique de 2 alternants (revues de code, montée en compétence).</li>')
rep('<li>Dashboards (Power BI / Spotfire) ; usage d\'outils IA (Claude Code, Codex).</li>','<li data-en="Dashboards (Power BI / Spotfire); use of AI tools (Claude Code, Codex).">Dashboards (Power BI / Spotfire) ; usage d\'outils IA (Claude Code, Codex).</li>')
rep('<span class="tl-date">Juil. — Déc. 2021</span>','<span class="tl-date" data-en="Jul. — Dec. 2021">Juil. — Déc. 2021</span>')
rep('<div class="tl-company">SWConsulting · CDD — pour <b>Benchmark Consulting</b> (Canada)</div>','<div class="tl-company" data-en="SWConsulting · Fixed-term — for <b>Benchmark Consulting</b> (Canada)">SWConsulting · CDD — pour <b>Benchmark Consulting</b> (Canada)</div>')
rep('<li>Analyse des besoins et développement des fonctionnalités.</li>','<li data-en="Requirements analysis and feature development.">Analyse des besoins et développement des fonctionnalités.</li>')
rep('<li>Correction des bugs ; Sprint Review.</li>','<li data-en="Bug fixing; Sprint Review.">Correction des bugs ; Sprint Review.</li>')

# ---- PROJECTS ----
rep('<span class="eyebrow reveal">03 — Réalisations</span>','<span class="eyebrow reveal" data-en="03 — Projects">03 — Réalisations</span>')
rep('<h2 class="title reveal d1">Projets &amp; réalisations</h2>','<h2 class="title reveal d1" data-en="Projects &amp; achievements">Projets &amp; réalisations</h2>')
rep('<p class="section-sub reveal d2">Des plateformes que j\'ai conçues et développées de bout en bout.</p>','<p class="section-sub reveal d2" data-en="Platforms I designed and built end-to-end.">Des plateformes que j\'ai conçues et développées de bout en bout.</p>')
rep('<span class="proj-kind">🌍 Plateforme web · ONG</span>','<span class="proj-kind" data-en="🌍 Web platform · NGO">🌍 Plateforme web · ONG</span>')
rep('<span class="proj-status"><span class="status-dot"></span>En ligne</span>','<span class="proj-status"><span class="status-dot"></span><span data-en="Online">En ligne</span></span>')
rep('<p class="proj-desc">Plateforme web de la communauté CFC Europe — une ONG, non rattachée à une église, réunissant des membres issus de différentes églises. Elle permet d\'adhérer tout en restant membre de son église, puis de devenir <b>missionnaire bénévole</b> lors des activités menées en Côte d\'Ivoire et dans les autres pays d\'intervention.</p>','<p class="proj-desc" data-en="Web platform for the CFC Europe community — an NGO, not affiliated with any church, bringing together members from different churches. It lets you join while remaining a member of your own church, then become a <b>volunteer missionary</b> during activities carried out in Côte d\'Ivoire and other countries of operation.">Plateforme web de la communauté CFC Europe — une ONG, non rattachée à une église, réunissant des membres issus de différentes églises. Elle permet d\'adhérer tout en restant membre de son église, puis de devenir <b>missionnaire bénévole</b> lors des activités menées en Côte d\'Ivoire et dans les autres pays d\'intervention.</p>')
rep('<span>👥 Adhésion des membres</span>','<span data-en="👥 Member registration">👥 Adhésion des membres</span>')
rep('<span>🙌 Engagement missionnaire bénévole</span>','<span data-en="🙌 Volunteer missionary engagement">🙌 Engagement missionnaire bénévole</span>')
rep('<span>🗺️ Activités multi-pays</span>','<span data-en="🗺️ Multi-country activities">🗺️ Activités multi-pays</span>')
rep('rel="noopener">Voir la plateforme <span class="arr">↗</span></a>','rel="noopener"><span data-en="View the platform">Voir la plateforme</span> <span class="arr">↗</span></a>')

# ---- SKILLS ----
rep('<h2 class="title reveal d1">Compétences techniques</h2>','<h2 class="title reveal d1" data-en="Technical skills">Compétences techniques</h2>')
rep('<p class="section-sub reveal d2">Les langages, frameworks et outils que j\'utilise au quotidien.</p>','<p class="section-sub reveal d2" data-en="The languages, frameworks and tools I use daily.">Les langages, frameworks et outils que j\'utilise au quotidien.</p>')
rep('<h3>Langages</h3>','<h3 data-en="Languages">Langages</h3>')
rep('<h3>Messaging & Données</h3>','<h3 data-en="Messaging &amp; Data">Messaging & Données</h3>')
rep('<h3>Qualité & Méthodo</h3>','<h3 data-en="Quality &amp; Methodology">Qualité & Méthodo</h3>')
rep('<span class="tag">Tests unitaires & intégration</span>','<span class="tag" data-en="Unit &amp; integration tests">Tests unitaires & intégration</span>')
rep('<span class="tag">Audit de code</span>','<span class="tag" data-en="Code audit">Audit de code</span>')
rep('<span class="tag">Supervision</span>','<span class="tag" data-en="Monitoring">Supervision</span>')

# ---- CONTACT + FOOTER ----
rep('<h2>Travaillons ensemble.</h2>','<h2 data-en="Let\'s work together.">Travaillons ensemble.</h2>')
rep('<p>Une opportunité, un projet ou simplement envie d\'échanger ? Je réponds rapidement.</p>','<p data-en="An opportunity, a project, or simply want to chat? I reply quickly.">Une opportunité, un projet ou simplement envie d\'échanger ? Je réponds rapidement.</p>')
rep('<footer>Conçu avec <b>♥</b> par Loïc Gnagoh · <span id="year"></span> · <b>Java Full-Stack Developer</b></footer>','<footer><span data-en="Designed with <b>♥</b> by Loïc Gnagoh">Conçu avec <b>♥</b> par Loïc Gnagoh</span> · <span id="year"></span> · <b>Java Full-Stack Developer</b></footer>')

# ---- CSS for lang button ----
rep('.theme-btn:hover{transform:translateY(-2px) rotate(12deg);border-color:var(--accent);box-shadow:0 0 20px var(--glow)}',
    '.theme-btn:hover{transform:translateY(-2px) rotate(12deg);border-color:var(--accent);box-shadow:0 0 20px var(--glow)}\n.lang-btn{height:42px;min-width:42px;padding:0 13px;border-radius:12px;border:1px solid var(--border-strong);background:var(--surface);color:var(--text);cursor:pointer;font-family:\'JetBrains Mono\',monospace;font-weight:600;font-size:.82rem;letter-spacing:.04em;transition:.3s}\n.lang-btn:hover{transform:translateY(-2px);border-color:var(--accent);box-shadow:0 0 20px var(--glow)}')

# ---- JS for language toggle ----
rep("tBtn.addEventListener('click',()=>{theme=theme==='dark'?'light':'dark';setTheme(theme);});",
    "tBtn.addEventListener('click',()=>{theme=theme==='dark'?'light':'dark';setTheme(theme);});\n"
    "// language toggle\n"
    "const langBtn=document.getElementById('langBtn');let lang='fr';\n"
    "function applyLang(l){lang=l;document.querySelectorAll('[data-en]').forEach(el=>{if(el.dataset.fr===undefined)el.dataset.fr=el.innerHTML;el.innerHTML=(l==='en')?el.dataset.en:el.dataset.fr;});document.documentElement.lang=l;langBtn.textContent=(l==='en')?'FR':'EN';}\n"
    "langBtn.addEventListener('click',()=>applyLang(lang==='en'?'fr':'en'));\n"
    "applyLang('fr');")

open(f,'w',encoding='utf-8').write(h)
print('MISSING (%d):'%len(miss))
for m in miss: print(' -',m)
print('data-en count:', h.count('data-en='))
