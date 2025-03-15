from flask import Flask, render_template, request

app = Flask(__name__)

categories = ["Rent/House", "Food", "Transport", "Fun", "Bills", "Savings"]

@app.route("/", methods=["GET", "POST"])
def budget():
    print("Rendering template...")  

    if request.method == "POST":
        total_money = float(request.form.get("income", 0))

        budget = {category: float(request.form.get(f"budget_{category}", 0)) for category in categories}
        spent = {category: float(request.form.get(f"spent_{category}", 0)) for category in categories}

        total_budget = sum(budget.values())
        total_spent = sum(spent.values())
        money_left = total_money - total_spent

        savings = total_money - total_spent
        saved_percent = round((savings / total_money) * 100, 2) if total_money > 0 else 0
        spent_percent = round((total_spent / total_money) * 100, 2) if total_money > 0 else 0

        return render_template(
            "index.html",
            categories=categories,
            total_money=total_money,
            total_budget=total_budget,
            total_spent=total_spent,
            money_left=money_left,
            budget=budget,
            spent=spent,
            savings=savings,
            saved_percent=saved_percent,
            spent_percent=spent_percent
        )

    return render_template("index.html", categories=categories, total_money=None)


@app.route("/favicon.ico")
def favicon():
    return "", 204  

if __name__ == "__main__":
    app.run(debug=True)

