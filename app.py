from flask import Flask, render_template, request, redirect, url_for
from kurlar import Kurlar
from combobox import Form

app = Flask(__name__)
app.config["SECRET_KEY"] = 'cairocoders-ednalan'
kurlar = Kurlar()


def get_kur_list():
    return kurlar.get_list()


def get_json():
    return kurlar.get_json()


def get_dictionary():
    return kurlar.get_dictionary()


@app.route("/")
def index():
    form = Form()
    kur_list = get_kur_list()

    form.kur_isim.choices = [(isim, kur_list[isim]) for isim in kur_list]
    form.kur_deger.choices = [("Alış", "Alış"), ("Satış", "Satış"),
                              ("Efektif_alış", "Efektif Alış"),
                              ("Efektif_satış", "Efektif Satış")]
    return render_template("index.html", form=form)


@app.route("/get_data")
def get_data():
    data = get_json()
    return data


if __name__ == "__main__":
    app.run(debug=True)
