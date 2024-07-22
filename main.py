from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio_tarros = tarros * 9000
        descuento = 0

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = precio_tarros * (1 - descuento)
        descuento_aplicado = precio_tarros * descuento

        resultado = {
            'nombre': nombre,
            'precio_tarros': precio_tarros,
            'descuento_aplicado': descuento_aplicado,
            'total_con_descuento': total_con_descuento
        }

        return render_template('ejercicio1.html', resultado=resultado, nombre=nombre, precio_tarros=precio_tarros,
                               descuento_aplicado=descuento_aplicado, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html', resultado=None)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuarios = {
            "juan": "admin",
            "pepe": "user"
        }
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario in usuarios and usuarios[usuario] == password:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == "pepe":
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html', mensaje=None)


if __name__ == '__main__':
    app.run(debug=True)
