from flask import Flask

app = Flask(__name__)

@app.route("/")
def coffee():
    return"""
<html>  
      <head>
        <title>Coffee novleri</title>
      </head>
      <body>
        <h1>Salam, xos gelmisiniz!</h1>
        <h2>"Coffee"-haqqinda qisa metin</h2>
        <p>"Coffee" qovrulmus ve uyudulmus
        "beans"den(qehve gilirlerinden)hazirlanan ickidir.O,Yemen ve Etipoya etrafi bolgelerden genis yayilib ve kofeinin stimullasdirici tesiri ile meshurdur.</p>
        <ul>    
           <li> Coffea arabica (Arabica): Dünya istehsalının təxminən 60%-ni təşkil edir, daha zərif və aromatik dadı vardır, daha az kofein tərkibli olur</li>
           <li> Coffea canephora (Robusta): Arabica’ya nisbətən daha çox kofeinli, daha acı dadlıdır. Daha sərt və ucuzdur, Espresso qarışıqlarında istifadə olunur və daha davamlıdır</li>
           <li> Coffee dünyada su və çayın ardınca ən çox istehlak olunan içkidir. Gündə təxminən 2 milyard fincan içilir</li>
           <li> Coffee qlobal ticarətdə neftdən sonra ikinci yerdə»dir, çox sayda fermer bu işlə məşğuldur</li> 
        </ul>   
        <hr>
        <p> 
                <i> 
                  Coffee qlobal ticarətdə neftdən sonra ikinci yerdə»dir, çox sayda fermer bu işlə məşğuldur. <br>
                  Roast Dərəcələri:<br>
                  Light roast: daha yüksək kofein, zəif dad və aromalar.<br>
                  Medium roast: balanslı dad və aroma.<br>
                  Dark roast: güclü və zəngin dad, daha az kofein.   
                <i>    
            </p>    
        </body>
    </html>
"""
if __name__ == "__main__":
    app.run(debug=True)