import pandas as pd
from datetime import datetime

try:
    # Excel dosyasını oku
    df = pd.read_excel('Rate sheet.xlsx')
    
    # Verileri HTML tablosuna çevir
    html_table = df.to_html(index=False, classes='table table-dark table-hover', border=0)

    # Senin orijinal şık tasarımın (İngilizce)
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Turkish Cargo Toronto - Rate Lookup</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #0a0a0f; color: #f0f0f0; padding: 40px 20px; }}
        .container {{ max-width: 1000px; margin: auto; background: #16161e; padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
        h2 {{ color: #ff3e3e; font-weight: 700; margin-bottom: 20px; border-left: 5px solid #ff3e3e; padding-left: 15px; }}
        .header-img {{ width: 100%; border-radius: 10px; margin-bottom: 25px; object-fit: cover; height: 250px; }}
        .table {{ color: #e0e0e0; border-color: #2d2d3d; }}
        .table-dark {{ background-color: #16161e; }}
        .last-update {{ font-size: 0.85rem; color: #888; margin-top: 20px; text-align: right; }}
    </style>
</head>
<body>
    <div class="container">
        <img src="Turkish-Cargo-800x450.jpg" class="header-img" alt="Turkish Cargo">
        <h2>Toronto Rate Lookup</h2>
        <div class="table-responsive">
            {html_table}
        </div>
        <p class="last-update">Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (EST)</p>
    </div>
</body>
</html>
"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Successfully updated index.html with stylish theme!")

except Exception as e:
    print(f"Error: {e}")
