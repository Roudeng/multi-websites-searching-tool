from flask import Flask, render_template, request


app = Flask(__name__)

SEARCH_ENGINES = {
    "momo": "https://www.momoshop.com.tw/search/searchShop.jsp?keyword={}",
    "pchome": "https://24h.pchome.com.tw/search/?q={}",
    "shopee": "https://shopee.tw/search?keyword={}",
    "yahoo": "https://tw.buy.yahoo.com/search/product?p={}",
    "costco": "https://www.costco.com.tw/search?searchOption=tw-search-all&text={}"
}


@app.route("/", methods=["GET", "POST"])
def index():
    keyword = ""
    search_links = []
    if request.method == "POST":
        keyword = request.form["keyword"]
        selected_sites = request.form.getlist("sites")
        search_links = [
            SEARCH_ENGINES[site].format(keyword) for site in selected_sites
        ]
    return render_template("index.html", keyword=keyword, links=search_links, sites=SEARCH_ENGINES)

if __name__ == "__main__":
    app.run(debug=True)
