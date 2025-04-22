from flask import Blueprint, render_template, request, redirect, url_for
from utils.di_container import container

tariff_bp = Blueprint("tariff_bp", __name__)
tariff_service = container.tariff_service


@tariff_bp.route("/")
def index():
    tariffs = tariff_service.get_all_tariffs()
    return render_template("tariffs/index.html", tariffs=tariffs)


@tariff_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        tariff_service.create_tariff(name, price)
        return redirect(url_for("tariff_bp.index"))
    return render_template("tariffs/create.html")


@tariff_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    tariff = tariff_service.get_tariff(id)
    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        tariff_service.update_tariff(id, name=name, price=price)
        return redirect(url_for("tariff_bp.index"))
    return render_template("tariffs/edit.html", tariff=tariff)


@tariff_bp.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    tariff = tariff_service.get_tariff(id)
    if request.method == "POST":
        tariff_service.delete_tariff(id)
        return redirect(url_for("tariff_bp.index"))
    return render_template("tariffs/delete.html", tariff=tariff)
