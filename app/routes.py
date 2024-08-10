"""Modulo que contiene toda la lógica de las funciones view para las URLs de la
aplicación web Flask para lógos."""

# Modulos necesarios para escribir la lógica de las funciones view.
import os
import glob
import sympy
from flask import render_template, flash, redirect, url_for, session
from forms import ArgInitial, PremisesForm, ArgDerivation

from app import app

# Modulo del motor inferencial lógos.
from app.logosengine import isvalidarg

# Modulo de asistencia para la traducción de funciones lógos a LaTeX.
from app.logos2latex import logos2latex

@app.route('/')
@app.route('/index')
def index():
    """Lógica a ejecutar cuando el cliente solicita la URL del índice."""
    return render_template('index.html', title='Inicio')

@app.route('/ejemplos')
def ejemplos():
    """Lógica a ejecutar cuando el cliente solicita la URL de los ejemplos."""
    return render_template('ejemplos.html', title='Ejemplos')

@app.route('/argmeta', methods=['GET', 'POST'])
def argf1():
    """Lógica a ejecutar para la URL de metadatos del argumento."""
    form = ArgInitial()
    if form.validate_on_submit():
        session['ognprems'] = int(form.nprems.data)
        session['vars'] = form.vars.data.split(",")
        return redirect(url_for('argf2'))
    return render_template('argfmetadata.html', title='Derivar argumento',
            form=form)

@app.route('/argpremises', methods=['GET', 'POST'])
def argf2():
    """Lógica a ejecutar para la URL de premisas del argumento."""
    files = glob.glob('app/static/temprops/*')
    for file in files:
        os.remove(file)
    ognprems = session.get('ognprems', None)
    varlist = session.get('vars', None)
    prems = []
    props = []

    for i in range(int(ognprems)):
        props.append({"name": str(i)})

    form = PremisesForm(props=props)

    if form.validate_on_submit():
        for i, prop in enumerate(form.props):
            latexpremise = logos2latex(prop.data["prop"], varlist)
            sympy.preview("$" + latexpremise + "$",
                viewer='file', filename='app/static/temprops/p'+str(i+1)+'.png')
            prems.append(prop.data["prop"])
        session['prems'] = prems
        session['refs'] = []
        session['rinfs'] = []
        session['index'] = 1

        return redirect(url_for('argf3'))

    return render_template('argfpremises.html', title='Derivar argumento',
        form=form)

@app.route('/argverify', methods=['GET', 'POST'])
def argf3():
    """Lógica a ejecutar para la URL del formulario de verificación."""
    prems = session.get('prems', None)
    ognprems = session.get('ognprems', None)
    ind = session.get('index', None)
    varlist = session.get('vars', None)
    refs = session.get('refs')
    rinfs = session.get('rinfs')

    form = ArgDerivation()

    if form.validate_on_submit():
        iprems = form.refs.data.split(",")
        iprems = [int(i) for i in iprems]
        temprems = []

        for i in iprems:
            temprems.append(prems[i-1])

        newproplatex = logos2latex(form.prop.data, varlist)

        if isvalidarg(temprems, form.prop.data, varlist):
            sympy.preview("$" + newproplatex + "$",
                    viewer='file',
                    filename='app/static/temprops/p'+str(ognprems+ind)+'.png')
            session['index'] = ind + 1
            prems.append(form.prop.data)
            session['prems'] = prems
            refs.append(form.refs.data)
            session['refs'] = refs
            rinfs.append(form.reginf.data)
            session['rinfs'] = rinfs
            flash("true")
        else:
            sympy.preview("$" + newproplatex + "$",
                    viewer='file', filename='app/static/temprops/mal.png')
            flash("false")
            flash(form.prop.data)
            flash(form.refs.data)
            flash(form.reginf.data)

        return redirect(url_for('argf3'))

    return render_template('argfverify.html', title='Derivar argumento',
            prems=prems, ognprems=ognprems, refs=refs, rinfs=rinfs, form=form)
