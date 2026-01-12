<!DOCTYPE html>
<html>
<head>
    <title>KRUTIK_HIRUDKAR_v2.0</title>
    <style>
        body {
            background-color: #05070a;
            color: #e0e0e0;
            font-family: 'Courier New', Courier, monospace;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .terminal {
            width: 600px;
            border: 2px solid #1a1a1a;
            background: #0d1117;
            box-shadow: 15px 15px 0px #0056b3;
            padding: 25px;
            position: relative;
        }

        .terminal::before {
            content: "● ● ● profile_metadata.sys";
            position: absolute;
            top: -25px;
            left: 0;
            font-size: 12px;
            color: #00d2ff;
        }

        h1 {
            color: #00d2ff;
            font-size: 1.5rem;
            border-bottom: 1px solid #333;
            padding-bottom: 10px;
            margin-top: 0;
        }

        .data-row {
            margin: 12px 0;
            display: flex;
        }

        .label {
            color: #58a6ff;
            width: 140px;
            font-weight: bold;
        }

        .bar-container {
            border: 1px solid #333;
            width: 100%;
            height: 18px;
            margin-top: 20px;
            position: relative;
            background: #05070a;
        }

        #progress-fill {
            background-color: #00d2ff;
            height: 100%;
            width: 0%;
            transition: width 1.5s cubic-bezier(0.1, 0.7, 1.0, 0.1);
        }

        .status-box {
            background: #161b22;
            padding: 15px;
            border-left: 4px solid #00d2ff;
            margin-top: 25px;
            font-size: 14px;
            line-height: 1.5;
        }

        .pizza-tag {
            background: #238636;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
        }
    </style>
</head>
<body>

<div class="terminal">
    <h1>> KRUTIK_HIRUDKAR_PROFILE</h1>
    
    <div class="data-row">
        <span class="label">LOCATION:</span> <span>India 🇮🇳</span>
    </div>
    <div class="data-row">
        <span class="label">AGE:</span> <span>20</span>
    </div>
    <div class="data-row">
        <span class="label">FAV_SUBJECT:</span> <span>Math 📐</span>
    </div>
    <div class="data-row">
        <span class="label">HOBBY:</span> <span>Exploring new things 🔍</span>
    </div>
    <div class="data-row">
        <span class="label">FUEL:</span> <span class="pizza-tag">Pizza 🍕</span>
    </div>

    <div class="bar-container">
        <div id="progress-fill"></div>
    </div>
    <div style="font-size: 11px; color: #888; margin-top: 5px;">
        ENGINEERING_GOAL: Becoming a good engineer [65%]
    </div>

    <div class="status-box" id="status"></div>
</div>

<script>
    const myData = {
        name: "Krutik Hirudkar",
        status: "Architecting AI-native solutions with a focus on Agentic workflows and system resilience. Currently 65% through mastering Python for MLOps while debugging the future, one 'vibe' at a time. 🚀💻",
        progress: 65
    };

    function initProfile() {
        const bar = document.getElementById('progress-fill');
        setTimeout(() => {
            bar.style.width = myData.progress + "%";
        }, 300);

        document.getElementById('status').innerText = myData.status;
    }

    window.onload = initProfile;
</script>

</body>
</html>
