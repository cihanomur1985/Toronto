import pandas as pd
from datetime import datetime

# Read the Excel file
try:
    df = pd.read_excel('Rate sheet.xlsx')
    
    # Convert dataframe to HTML table with Bootstrap classes
    html_table = df.to_html(index=False, classes='table table-hover table-bordered', border=0)

    # The English HTML Template
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toronto Cargo Rate Sheet</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body {{ background-color: #f8f9fa; padding-top: 50px; }}
        .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        h2 {{ color: #d40000; font-weight: bold; margin-bottom: 25px; }}
        .last-update {{ font-size: 0.8rem; color: #6c757d; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
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
    print("Success: index.html has been updated!")

except Exception as e:
    print(f"Error: {e}")
