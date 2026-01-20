# My Introductin

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Krutik Hirudkar | Architect of Resilience</title>
    <style>
        :root {
            --cloud-dancer: #F5F5F0; /* Pantone 2026 Base */
            --lavender: #A78BFA;
            --cyber-lime: #D9F99D;
            --text-obsidian: #1A1A1A;
            --glass-white: rgba(255, 255, 255, 0.6);
        }

        * { box-sizing: border-box; transition: all 0.3s ease; }

        body {
            background-color: var(--cloud-dancer);
            color: var(--text-obsidian);
            font-family: 'Inter', -apple-system, sans-serif;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
            line-height: 1.5;
        }

        .bento-grid {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            grid-auto-rows: minmax(120px, auto);
            gap: 1.5rem;
            max-width: 1100px;
            width: 100%;
        }

        .box {
            background: var(--glass-white);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255,255,255,0.4);
            border-radius: 2.5rem;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.02);
            position: relative;
            overflow: hidden;
        }

        .box:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(167, 139, 250, 0.1);
            background: rgba(255, 255, 255, 0.8);
        }

        /* Identity Block */
        .hero { grid-column: span 4; grid-row: span 2; display: flex; flex-direction: column; justify-content: center; background: linear-gradient(135deg, #fff, var(--cyber-lime)); }
        h1 { font-size: 4rem; margin: 0; letter-spacing: -3px; line-height: 0.9; color: var(--text-obsidian); }
        .tagline { font-size: 1.2rem; color: #555; margin-top: 1.5rem; font-weight: 500; }

        /* Status & Age */
        .age-badge { grid-column: span 2; display: flex; flex-direction: column; align-items: center; justify-content: center; background: var(--lavender); color: white; border-radius: 100px; }
        .age-val { font-size: 5rem; font-weight: 900; }

        /* Professional Vision - 2026 Style */
        .vision { grid-column: span 3; border-bottom: 6px solid var(--lavender); }
        .hot-take { grid-column: span 3; background: #fff; }

        /* The 20-Year-Old Mindset Blocks */
        .flow-state { grid-column: span 2; }
        .fuel { grid-column: span 2; text-align: center; background: #FFF9F5; }
        .contact { grid-column: span 2; background: var(--text-obsidian); color: white; display: flex; align-items: center; justify-content: center; text-decoration: none; font-weight: 700; }
        
        /* Labels & Details */
        h3 { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; color: #888; margin-bottom: 0.75rem; }
        .highlight { color: var(--lavender); font-weight: 700; }

        @media (max-width: 900px) {
            .bento-grid { grid-template-columns: 1fr 1fr; }
            .hero, .vision, .hot-take { grid-column: span 2; }
            h1 { font-size: 2.5rem; }
        }
    </style>
</head>
<body>

    <main class="bento-grid">
        
        <section class="box hero">
            <h3>Human / Engineer / India 🇮🇳</h3>
            <h1>Krutik<br>Hirudkar</h1>
            <p class="tagline">Architecting AI-native resilience for the 2026 landscape. Currently bridging the gap between <span class="highlight">Abstract Math</span> and <span class="highlight">Agentic Workflows</span>.</p>
        </section>

        <!-- 2. The Core Number -->
        <section class="box age-badge">
            <span class="age-val">20</span>
            <span style="text-transform: uppercase; font-weight: 700; opacity: 0.8;">Circles of Growth</span>
        </section>

        <!-- 3. The 2026 Project Focus -->
        <section class="box vision">
            <h3>Vision 2026</h3>
            <p>Developing <strong>"Self-Healing MLOps"</strong>. I believe the next era isn't about more data, but more durable system logic built in Python.</p>
        </section>

        <!-- 4. The Engineering Mindset -->
        <section class="box hot-take">
            <h3>The Hot Take</h3>
            <p>"In 2026, prompt engineering is dead. <strong>Logical Architecture</strong> is the only skill that scales. If you can't sketch the math, you can't build the agent."</p>
        </section>

        <!-- 5. Flow State -->
        <section class="box flow-state">
            <h3>Flow State</h3>
            <p>Fueled by <strong>Synthwave</strong> and a minimalist desk setup. Currently obsessed with finding patterns in non-linear equations.</p>
        </section>

        <!-- 6. Real World Fuel -->
        <section class="box fuel">
            <h3>Carbon-Based Fuel</h3>
            <div style="font-size: 3.5rem;">🍕</div>
            <p style="font-weight: 800; letter-spacing: 2px;">PIZZA</p>
        </section>

        <!-- 7. Call to Action -->
        <a href="https://linkedin.com" class="box contact">
            <div style="text-align: center;">
                <div style="margin-bottom: 4px;">Collaborate / Innovate</div>
                <div style="font-size: 0.7rem; opacity: 0.6;">Reach out via LinkedIn or GitHub</div>
            </div>
        </a>
    </main>

</body>
</html>
