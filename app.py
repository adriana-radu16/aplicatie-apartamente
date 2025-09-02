from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import scraper
import io

app = Flask(__name__)

@app.route("/")
def index():
    city = request.args.get("city", "Târgoviște")
    listings = scraper.get_listings(city)
    return render_template("index.html", listings=listings, city=city)

@app.route("/export")
def export():
    city = request.args.get("city", "Târgoviște")
    listings = scraper.get_listings(city)
    df = pd.DataFrame(listings)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    return send_file(output, as_attachment=True, download_name="anunturi.xlsx")

if __name__ == "__main__":
    app.run(debug=True)
