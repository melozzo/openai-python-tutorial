import functools
import os
import openai
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('ai', __name__, url_prefix='/ai')


@bp.route('/completion', methods=('GET', 'POST'))
def aicomplete():
    if request.method == "POST":
        animal = request.form["animal"]
        print(animal)
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        print(response)
        return redirect(url_for("ai.aicomplete", result=response.choices[0].text))

   
    result = request.args.get("result")
    return render_template('ai/completion.html', result=result)

def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.
    Animal: Cat
    Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
    Animal: Dog
    Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
    Animal: {}
    Names:""".format( animal.capitalize() )