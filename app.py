from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Renderizamos la plantilla "index.html"
    return render_template('index.html')

if __name__ == '__main__':
    # Arrancamos la aplicación en modo debug
    app.run(debug=True)
