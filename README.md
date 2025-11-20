📦 Project Setup
1. Clone repository
git clone https://github.com/alexhayadela/10tothe6_TFG_2025_AlexDeLaHaya.git
cd 10tothe6_TFG_2025

2. Install Python

Requiere Python 3.10+

3. Install dependencies
pip install -r requirements.txt

🔐 Environment variables

Crea un archivo .env en la raíz del proyecto:

EMAIL_USER=example@gmail.com
EMAIL_PASSWORD=asdf asdf adsf asdf
EMAIL_TARGET_USER=example2@gmail.com


La contraseña debe ser una App Password (contraseña de aplicación) de Google.

📌 ¿Cómo obtener tu App Password para Gmail?

➡️ Guía oficial de Google:
https://support.google.com/accounts/answer/185833

🔒 GitHub Secrets (para la automatización)

En GitHub:

Settings → Secrets and variables → Actions → New repository secret

Agrega estos secretos con los mismos valores que tu .env:

EMAIL_USER

EMAIL_PASSWORD

EMAIL_TARGET_USER

➡️ Guía:
https://docs.github.com/en/actions/security-guides/encrypted-secrets

📬 First Deliverable: Email Automation
Pipeline

Fetch RSS desde Expansión:

Mercados, Ahorro, Empresas

Filtrar noticias relevantes (título, contenido, regex, keywords, etc.)

Convertir a HTML

Insertar imagen

Enviar email automáticamente

Todo esto se ejecuta tanto localmente como mediante GitHub Actions.

🧩 Example HTML Template (newsletter_example.html)

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>10^6, Noticias y consejos diarios para invertir</title>
<style>
  /* Safe email styles (fallback) */
  body {
      margin:0;
      padding:0;
      background-color:#ffffff;
      font-family: Arial, Helvetica, sans-serif;
  }

  .container {
      max-width:650px;
      margin:30px auto;         
      background-color:#f0f0f0;   
      border-radius:12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      padding: 30px;
      text-align: left;
  }
  .header {
      text-align:center;
      margin-bottom:25px;        
  }
  h1 {
      text-align:center;
      color:navy;
      font-size: 30px;
      margin-top:0;
      margin-bottom:25px;
  }
  .news-item {
      margin-bottom: 20px;
      border-bottom:1px solid #eee;
      padding-bottom: 15px;
  }
  h2 {
      color:darkblue;
      font-size: 18px;
      margin-bottom: 5px;
      margin-top:0;
  }
  p {
      font-size: 14px;
      line-height:1.6;
      color:#111;
      margin:0 0 8px 0;
  }
  .footer{
      text-align:center;
      margin-top:30px;
      font-size:12px;
      color:darkslategray;
  }
</style>
</head>
<body>
  <div class="container">
    <div class="header">
      <img src="imgs/freakbob.png" alt="freakbob" width="479" height="242" style="display:block; margin:0 auto; border-radius:6px;">
    </div>
    <h1>Noticias relevantes de hoy</h1>

    <div class="news-item">
      <h2>1. El Ibex se deja un 0,8% en la semana y pierde los 16.000 puntos</h2>
      <p>Jornada de caídas generalizadas en las Bolsas europeas, con las tecnológicas en el punto de mira de los inversores.
         <a href="https://www.expansion.com/mercados/cronica-bolsa/2025/11/07/690d9751e5fdea4f2a8b45a1.html" target="_blank">See more</a>
      </p>
    </div>

    <div class="news-item">
      <h2>2. Cómo ajustar las carteras para limitar los riesgos de corrección</h2>
      <p>Los analistas consultados coinciden en los ajustes recomendados para añadir mayor protección a las carteras.
         <a href="https://www.expansion.com/mercados/2025/11/07/690c94fde5fdea54648b457d.html" target="_blank">See more</a>
      </p>
    </div>

    <div class="footer">
      <p>Alex De La Haya © 2025 | Daily Market Insights</p>
    </div>

  </div>
</body>
</html>
"""


🔁 Automation (GitHub Actions)

El workflow se ejecuta cada día y envía el email automáticamente.

Cron en .github/workflows/daily.yml:

🧑‍💻 Author

Alex De La Haya Gutiérrez
