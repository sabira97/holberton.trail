from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
        <head>
            <title>Deniz mənzərəsi</title>
        </head>
        <body>
            <h1>Salam, xoş gəlmisiniz!</h1>
            <h2>“Deniz” — Qısa Tanıtım Mətni</h2>
            <p>“Deniz” adında simvolik mənanızın dərinliyinə dalın — Türk mədəniyyətində dənizin sonsuzluğunu, gücünü və genişliyini ifadə edən bu uniseks ad, həm kişilərə, həm də qadınlara xas ola bilər. Tarixə və müasirliyə toxunan qısa təqdimat, sayta canlılıq qatacaq.</p>
            <ul>
                <li>Deniz Baykal – Türk siyasətçilərindən biri</li>
                <li>Deniz Öncü – Peşəkar motosikletçi</li>
                <li>Deniz Kılıçlı – Türk basketbolçu</li>
            </ul>
            <hr>
            <p>
                <i>
                    Dəniz bir okeanla əlaqəli böyük, adətən duzlu su hövzəsidir. <br>
                    Termin tez-tez okean termini ilə əvəz olunur. <br>
                    Okeanlar Yer səthinin 70%-ni əhatə edir. 1,338 milyard km³ torpaq sahəsini əhatə edərək dünya su ehtiyatlarının 96,5%-ni təşkil edir. <br>
                    Lakin dəniz suyunun tərkibində orta hesabla 3,5% duz olduğu üçün hazırda bahalı təmizləmə üsullarından istifadə etmədən ondan içməli su kimi istifadə etmək mümkün deyil.
                </i>
            </p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(port=5022, debug=True)
