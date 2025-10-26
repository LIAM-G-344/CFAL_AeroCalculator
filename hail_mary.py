#Liam Griesacker copyright 2025
#most of this i wrote but it gave me some error because the solvers return dictonaries and kept retruning a weird error
#so i fed it into chad gpt and told it to fix it and it did and it also organized this prittey well so, imma take it. any
#code written by chad gpt is marked accordingly


import panel as pn
from bokeh.io import curdoc
from pygasflow.solvers import (
    isentropic_solver,
    normal_shockwave_solver,
    oblique_shockwave_solver,
    conical_shockwave_solver,
    fanno_solver,
    rayleigh_solver
)

pn.extension()

# Solver perameter lists
iso_p1_choice = ["m", "pressure", "density", "temperature", "crit_area_sub", "crit_area_super", "mach_angle", "prandtl_meyer"]
normal_p1_choice = ["pressure", "temperature", "density", "total_pressure", "mu", "md"]
fanno_p1_choice = ["m", "pressure", "density", "temperature", "total_pressure_sub", "total_pressure_super", "velocity", "friction_sub", "friction_super", "entropy_sub", "entropy_super"]
ray_p1_choice = ["m", "pressure", "density", "velocity", "temperature_sub", "temperature_super", "total_pressure_sub", "total_pressure_super", "total_temperature_sub", "total_temperature_super", "entropy_sub", "entropy_super"]

# Helper to format dict results
def format_results(results_dict): #fucntion written by chat gpt and it made the program work
    return "\n".join(f"{k}: {v}" for k, v in results_dict.items())

# Solvers
def isentropic(choice, value, gamma_select):
    results = isentropic_solver(choice, value, gamma = gamma_select,to_dict=True)
    return format_results(results)

def normal(choice, value, gamma_select):
    results = normal_shockwave_solver(choice, value, gamma = gamma_select, to_dict=True)
    return format_results(results)

def fanno(choice, value, gamma_select):
    results = fanno_solver(choice, value, gamma = gamma_select, to_dict=True)
    return format_results(results)

def rayleigh(choice, value, gamma_select):
    results = rayleigh_solver(choice, value, gamma = gamma_select, to_dict=True)
    return format_results(results)

#Panel widgets
#logoz becauz it makes it look like a massive W
logos = pn.pane.Image('logo.png', width=400)

#gamma for all
gamma_input_raw = pn.widgets.TextInput(name="Gamma (applys for all functions)",value='1.4')

isentropic_input_raw = pn.widgets.TextInput(name="Isentropic Parameter Value")
isentropic_p1_select = pn.widgets.Select(name="Isentropic Parameter", options=iso_p1_choice)
isentropic_output = pn.pane.Markdown("Results will print here when a valid input is present.\nm:0.0\npr:0.0\ndr:0.0\ntr:0.0\nprs:0.0\ndrs:0.0\ntrs:0.0\nurs:0.0\nars:0.0\nma:0.0\npm:0.0\n")

normal_input_raw = pn.widgets.TextInput(name="Normal Shock Parameter Value.")
normal_p1_select = pn.widgets.Select(name="Normal Shock Parameter", options=normal_p1_choice)
normal_output = pn.pane.Markdown("Normal Shock Results:\nmu:0.0\nmd:0.0\npr:0.0\ndr:0.0\ntr:0.0\ntpr:0.0")

fanno_input_raw = pn.widgets.TextInput(name="Fanno Parameter Value")
fanno_p1_select = pn.widgets.Select(name="Fanno Parameter", options=fanno_p1_choice)
fanno_output = pn.pane.Markdown("Fanno Results:\nm:0.0\nprs:0.0\ndrs:0.0\ntrs:0.0\ntprs:0.0\nurs:0.0\nfps:0.0\neps:0.0")

rayleigh_input_raw = pn.widgets.TextInput(name="Rayleigh Parameter Value")
rayleigh_p1_select = pn.widgets.Select(name="Rayleigh Parameter", options=ray_p1_choice)
rayleigh_output = pn.pane.Markdown("Rayleigh Results:\nm:0.0\nprs:0.0\ndrs:0.0\ntrs:0.0\ntprs:0.0\nttrs:0.0\nurs:0.0\neps:0.0")
calc_button = pn.widgets.Button(name="Calculate", button_type='primary')

#for the lawyers lol
credits = pn.pane.Markdown("AeroCalculator by Liam Griesacker and Massimo Mansueto of the Embry-Riddle Aeronautical University CFAL 2025. Credit to Davide Sandona of PyGasFlow.")

    
# Update function which runs when calculate button is clicked
# for all the try and excepts first line the .value.strip() thing chat gpt did and it worked
def update_display(event=None):
    # ISENTROPIC
    try:
        ise_val = float(isentropic_input_raw.value.strip())
        gamma_val = float(gamma_input_raw.value.strip())
        ise_choice = isentropic_p1_select.value
        isentropic_output.object = f"Isentropic Results:\n{isentropic(ise_choice, ise_val,gamma_val)}"
    except Exception as e:
        isentropic_output.object = f"Results will print here when a valid input is present.\nm:\npr:\ndr:\ntr:\nprs:\ndrs:\ntrs:\nurs:\nars:\nma:\npm:\n"

    # NORMAL SHOCK
    try:
        nor_val = float(normal_input_raw.value.strip())
        nor_choice = normal_p1_select.value
        normal_output.object = f"Normal Shock Results:\n{normal(nor_choice, nor_val,gamma_val)}"
    except Exception as e:
        normal_output.object = f"Results will print here when a valid input is present:\nmu:0.0\nmd:0.0\npr:0.0\ndr:0.0\ntr:0.0\ntpr:0.0"

    # FANNO
    try:
        fan_val = float(fanno_input_raw.value.strip())
        fan_choice = fanno_p1_select.value
        fanno_output.object = f"Fanno Results:\n{fanno(fan_choice, fan_val,gamma_val)}"
    except Exception as e:
        fanno_output.object = f"Results will print here when a valid input is present.\nm:0.0\nprs:0.0\ndrs:0.0\ntrs:0.0\ntprs:0.0\nurs:0.0\nfps:0.0\neps:0.0"

    # RAYLEIGH
    try:
        ray_val = float(rayleigh_input_raw.value.strip())
        ray_choice = rayleigh_p1_select.value
        rayleigh_output.object = f"Rayleigh Results:\n{rayleigh(ray_choice, ray_val,gamma_val)}"
    except Exception as e:
        rayleigh_output.object = f"Results will print here when a valid input is present.\nm:0.0\nprs:0.0\ndrs:0.0\ntrs:0.0\ntprs:0.0\nttrs:0.0\nurs:0.0\neps:0.0"

calc_button.on_click(update_display)

# Layout
app = pn.Column(logos, gamma_input_raw,
    pn.Row(isentropic_input_raw, isentropic_p1_select, isentropic_output),
    pn.Row(normal_input_raw, normal_p1_select, normal_output),
    pn.Row(fanno_input_raw, fanno_p1_select, fanno_output),
    pn.Row(rayleigh_input_raw, rayleigh_p1_select, rayleigh_output),
    calc_button,
    credits
)

# Use this line when running via `panel serve`
pn.state.favicon = "static/erlogo.png"
app.servable(title="AeroCalculator")

# If running inside a Jupyter notebook, replace the last line with:
# app

