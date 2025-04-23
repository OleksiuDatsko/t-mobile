from flask import Blueprint, render_template, request, redirect, url_for
from utils.di_container import container

subscriber_bp = Blueprint("subscriber_bp", __name__)
subscriber_service = container.subscriber_service
tariff_service = container.tariff_service


@subscriber_bp.route("/")
def index():
    subscribers = container.subscriber_repo.get_all()
    return render_template("subscribers/index.html", subscribers=subscribers)


@subscriber_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone_number"]
        tariff_plan_id = int(request.form["tariff_plan_id"])
        subscriber_service.create_subscriber(name, tariff_plan_id, phone)
        return redirect(url_for("subscriber_bp.index"))
    tariffs = tariff_service.get_all_tariffs()
    return render_template("subscribers/create.html", tariffs=tariffs)


@subscriber_bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    subscriber = subscriber_service.get_subscriber(id)
    if request.method == "POST":
        subscriber.name = request.form["name"]
        subscriber.phone_number = request.form["phone_number"]
        subscriber.tariff_plan_id = int(request.form["tariff_plan_id"])
        container.subscriber_repo.update(subscriber)
        return redirect(url_for("subscriber_bp.index"))
    tariffs = tariff_service.get_all_tariffs()
    return render_template("subscribers/edit.html", subscriber=subscriber, tariffs=tariffs)


@subscriber_bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    subscriber = subscriber_service.get_subscriber(id)
    if request.method == "POST":
        container.subscriber_repo.delete(subscriber)
        return redirect(url_for("subscriber_bp.index"))
    return render_template("subscribers/delete.html", subscriber=subscriber)
