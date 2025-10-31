# Liam Griesacker copyright 2025
# most of this i wrote but it gave me some error because the solvers return dictonaries and kept retruning a weird error
# so i fed it into chad gpt and told it to fix it and it did and it also organized this prittey well so, imma take it. any
# code written by chad gpt is marked accordingly


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
iso_p1_choice = ["m", "pressure", "density", "temperature", "crit_area_sub", "crit_area_super", "mach_angle","prandtl_meyer"]
normal_p1_choice = ["pressure", "temperature", "density", "total_pressure", "mu", "md"]
fanno_p1_choice = ["m", "pressure", "density", "temperature", "total_pressure_sub", "total_pressure_super", "velocity","friction_sub", "friction_super", "entropy_sub", "entropy_super"]
ray_p1_choice = ["m", "pressure", "density", "velocity", "temperature_sub", "temperature_super", "total_pressure_sub","total_pressure_super", "total_temperature_sub", "total_temperature_super", "entropy_sub","entropy_super"]
con_p1_choice = ["mc", "theta_c", "beta"]
obl_p1_choice = ['pressure', 'temperature', 'density', 'total_pressure', 'mu', 'mnu', 'mnd', 'beta', 'theta']
obl_p2_choice = ['beta', 'theta', 'mnu']
flag_all = ['weak', 'strong']


# Helper to format dict results
def format_results(results_dict):  # fucntion written by chat gpt and it made the program work
    return "  \n".join(f"{k}: {v}" for k, v in results_dict.items())


# Solvers
def isentropic(p1, value, gamma_select):
    results = isentropic_solver(p1, value, gamma=gamma_select, to_dict=True)
    return format_results(results)


def normal(p1, value, gamma_select):
    results = normal_shockwave_solver(p1, value, gamma=gamma_select, to_dict=True)
    return format_results(results)


def fanno(p1, value, gamma_select):
    results = fanno_solver(p1, value, gamma=gamma_select, to_dict=True)
    return format_results(results)


def rayleigh(p1, value, gamma_select):
    results = rayleigh_solver(p1, value, gamma=gamma_select, to_dict=True)
    return format_results(results)


def conical(mu, p1, value, flag, gamma_select):
    results = conical_shockwave_solver(mu, p1, value, gamma=gamma_select, flag=flag, to_dict=True)
    return format_results(results)


def oblique(p1, p1_value, p2, p2_value, flag, gamma_select):
    results = oblique_shockwave_solver(p1, p1_value, p2, p2_value, gamma=gamma_select, flag=flag, to_dict=True)
    return format_results(results)


# Panel widgets
# logoz becauz it makes it look like a massive W
logos = pn.pane.Image('logo.png', width=400)

# gamma for all
gamma_input_raw = pn.widgets.TextInput(name="Gamma (applys for all functions)", value='1.4')

isentropic_input_raw = pn.widgets.TextInput(name="Isentropic Parameter Value")
isentropic_p1_select = pn.widgets.Select(name="Isentropic Parameter", options=iso_p1_choice)
isentropic_output = pn.pane.Markdown("Results will print here when a valid input is present.  \nMach Number:0.0  \nPressure Ratio P/P0:0.0  \nDensity Ratio rho/rho0:0.0  \nTemperature Ratio T/T0:0.0  \nCritical Pressure Ratio P/P*:0.0  \nCritical Density Ratio rho/rho*:0.0  \nCritical Temperature Ratio T/T*:0.0  \nCritical Velocity Ratio U/U*:0.0  \nCritical Area Ratio A/A*:0.0  \nMach Angle:0.0  \nPrandtl-Meyer Angle:0.0  \n")

normal_input_raw = pn.widgets.TextInput(name="Normal Shock Parameter Value.")
normal_p1_select = pn.widgets.Select(name="Normal Shock Parameter", options=normal_p1_choice)
normal_output = pn.pane.Markdown("Normal Shock Results:  \nUpstream Mach Number:0.0  \nMach Number Downstream:0.0  \nPressure Ratio:0.0  \nDensity Ratio:0.0  \nTemperature Ratio:0.0  \nTotal Pressure Ratio:0.0")

fanno_input_raw = pn.widgets.TextInput(name="Fanno Parameter Value")
fanno_p1_select = pn.widgets.Select(name="Fanno Parameter", options=fanno_p1_choice)
fanno_output = pn.pane.Markdown("Fanno Results:  \nMach Number:0.0  \nCritical Pressure Ratio P/P*:0.0  \nCritical Density Ratio rho/rho*:0.0  \nCritical Temperature Ratio T/T*:0.0  \nCritical Total Pressure Ratio P0/P0:0.0  \nCritical Velocity Ratio U/U*:0.0  \nCritical Friction Parameter 4fL*/D:0.0  \nCritical Entropy Ratio (s*-s)/R:0.0")

rayleigh_input_raw = pn.widgets.TextInput(name="Rayleigh Parameter Value")
rayleigh_p1_select = pn.widgets.Select(name="Rayleigh Parameter", options=ray_p1_choice)
rayleigh_output = pn.pane.Markdown("Rayleigh Results:  \Mach Number:0.0  \nCritical Pressure Ratio P/P*:0.0  \nCritical Density Ratio rho/rho*:0.0  \nCritical Temperature Ratio T/T*:0.0  \nCritical Total Pressure Ratio P0/P0:0.0  \nCritical Total Temperature Ratio T0/T0:0.0  \nCritical Velocity Ratio U/U*:0.0  \nCritical Entropy Ratio (s*-s)/R:0.0")
calc_button = pn.widgets.Button(name="Calculate", button_type='primary')

conical_input_raw = pn.widgets.TextInput(name="Conical Shockwave Parameter Value")
conical_p1_select = pn.widgets.Select(name="Conical Shockwave Parameter", options=con_p1_choice)
conical_mu_input_raw = pn.widgets.TextInput(name="Conical Shockwave Upstream Mach Number Value (Mu)")
conical_flag_select = pn.widgets.Select(name="Conical Flag", options=flag_all)
conical_output = pn.pane.Markdown("Conical Results:  \nUpstream Mach Number:0.0  \nMach Number at Cones' Surface:0.0  \nHalf Cone Angle:0.0  \nBeta (Shockwave Angle):0.0  \nDelta (Flow Deflection Angle):0.0  \nPressure Ratio Pd/Pu:0.0  \nDensity Ratio rhod/rhou:0.0  \nTemperature Ratio:0.0  \nTotal Pressure Ratio across Shockwave:0.0  \nPressure Ratio Between Cone Surface and Upstream Condition:0.0  \nDensity Ratio Between Cone Surface and Upstream Condition:0.0  \nTemperature Ratio Between Cone Surface and Upstream Condition:0.0")

oblique_p1_raw = pn.widgets.TextInput(name="Oblique Shockwave Parameter One Value")
oblique_p1_select = pn.widgets.Select(name="Oblique Shockwave Parameter One", options=obl_p1_choice)
oblique_p2_raw = pn.widgets.TextInput(name="Oblique Schockwave Parameter Two value")
oblique_p2_select = pn.widgets.Select(name="Oblique Shockwave Parameter Two", options=obl_p2_choice)
oblique_flag_select = pn.widgets.Select(name="Oblique Flag", options=flag_all)
oblique_output = pn.pane.Markdown("Oblique Results:  \nUpstream Mach Number:0.0  \nUpstream Normal Mach Number:0.0  \nMach Number Downstream:0.0  \nDownstream Normal Mach Number:0.0  \nBeta:0.0  \nTheta:0.0  \nPressure Ratio:0.0  \nDensity Ratio:0.0  \nTemperature Ratio:0.0  \nTotal Pressure Ratio:0.0")

# for the lawyers lol
credits = pn.pane.Markdown("AeroCalculator by Liam Griesacker and Massimo Mansueto of the Embry-Riddle Aeronautical University CFAL 2025. Credit to Davide Sandona of PyGasFlow.")

#tell the users the unfinished pages are works in progress
label_wip = pn.pane.Markdown("AeroCalculator by Liam Griesacker and Massimo Mansueto of the Embry-Riddle Aeronautical University CFAL 2025. Credit to Davide Sandona of PyGasFlow.")

# Update function which runs when calculate button is clicked
# for all the try and excepts first line the .value.strip() thing chat gpt did and it worked
def update_display(event=None): #TODO: add error printouts for the user
    #up top so its avalible for all fucntions
    gamma_val = float(gamma_input_raw.value.strip())

    #all functions have the if thing so evrything runs, otherwise weird stuff happens with panel if one of the fields isnt filled out
    # ISENTROPIC
    if isentropic_input_raw.value.strip():
        try:
            ise_val = float(isentropic_input_raw.value.strip())
            ise_choice = isentropic_p1_select.value
            isentropic_output.object = f"Isentropic Results:  \n{isentropic(ise_choice, ise_val, gamma_val)}"
        except Exception as e:
            isentropic_output.object = f"Results will print here when a valid input is present.  \nMach Number:0.0  \nPressure Ratio P/P0:0.0  \nDensity Ratio rho/rho0:0.0  \nTemperature Ratio T/T0:0.0  \nCritical Pressure Ratio P/P*:0.0  \nCritical Density Ratio rho/rho*:0.0  \nCritical Temperature Ratio T/T*:0.0  \nCritical Velocity Ratio U/U*:0.0  \nCritical Area Ratio A/A*:0.0  \nMach Angle:0.0  \nPrandtl-Meyer Angle:0.0  \n"

    # NORMAL SHOCK
    if normal_input_raw.value.strip():
        try:
            nor_val = float(normal_input_raw.value.strip())
            nor_choice = normal_p1_select.value
            normal_output.object = f"Normal Shock Results:  \n{normal(nor_choice, nor_val, gamma_val)}"
        except Exception as e:
            normal_output.object = f"Results will print here when a valid input is present:  \nUpstream Mach Number:0.0  \nMach Number Downstream:0.0  \nPressure Ratio:0.0  \nDensity Ratio:0.0  \nTemperature Ratio:0.0  \nTotal Pressure Ratio:0.0"

    # FANNO
    if fanno_input_raw.value.strip():
        try:
            fan_val = float(fanno_input_raw.value.strip())
            fan_choice = fanno_p1_select.value
            fanno_output.object = f"Fanno Results:  \n{fanno(fan_choice, fan_val, gamma_val)}"
        except Exception as e:
            fanno_output.object = f"Results will print here when a valid input is present.  \nMach Number:0.0  \nCritical Pressure Ratio P/P*:0.0  \nCritical Density Ratio rho/rho*:0.0  \nCritical Temperature Ratio T/T*:0.0  \nCritical Total Pressure Ratio P0/P0:0.0  \nCritical Velocity Ratio U/U*:0.0  \nCritical Friction Parameter 4fL*/D:0.0  \nCritical Entropy Ratio (s*-s)/R:0.0"

    # RAYLEIGH
    if rayleigh_input_raw.value.strip():
        try:
            ray_val = float(rayleigh_input_raw.value.strip())
            ray_choice = rayleigh_p1_select.value
            rayleigh_output.object = f"Rayleigh Results:  \n{rayleigh(ray_choice, ray_val, gamma_val)}"
        except Exception as e:
            rayleigh_output.object = f"Results will print here when a valid input is present.  \Mach Number:0.0  \nCritical Pressure Ratio P/P*:0.0  \nCritical Density Ratio rho/rho*:0.0  \nCritical Temperature Ratio T/T*:0.0  \nCritical Total Pressure Ratio P0/P0:0.0  \nCritical Total Temperature Ratio T0/T0:0.0  \nCritical Velocity Ratio U/U*:0.0  \nCritical Entropy Ratio (s*-s)/R:0.0"

    # CONICAL
    if conical_input_raw.value.strip() and conical_mu_input_raw.value.strip():
        try:
            con_val = float(conical_input_raw.value.strip())
            con_mu_val = float(conical_mu_input_raw.value.strip())
            con_choice = conical_p1_select.value
            con_flag = conical_flag_select.value
            conical_output.object = f"Conical Results:  \n{conical(con_mu_val, con_choice, con_val, con_flag, gamma_val)}"
        except Exception as e:
            conical_output.object = f"Results will print here when a valid input is present.  \nUpstream Mach Number:0.0  \nMach Number at Cones' Surface:0.0  \nHalf Cone Angle:0.0  \nBeta (Shockwave Angle):0.0  \nDelta (Flow Deflection Angle):0.0  \nPressure Ratio Pd/Pu:0.0  \nDensity Ratio rhod/rhou:0.0  \nTemperature Ratio:0.0  \nTotal Pressure Ratio across Shockwave:0.0  \nPressure Ratio Between Cone Surface and Upstream Condition:0.0  \nDensity Ratio Between Cone Surface and Upstream Condition:0.0  \nTemperature Ratio Between Cone Surface and Upstream Condition:0.0""

    # OBLIQUE
    if oblique_p1_raw.value.strip() and oblique_p2_raw.value.strip():
        try:
            obl_p1_val = float(oblique_p1_raw.value.strip())
            obl_p2_val = float(oblique_p2_raw.value.strip())
            obl_choice_p1 = oblique_p1_select.value
            obl_choice_p2 = oblique_p2_select.value
            obl_flag = oblique_flag_select.value
            oblique_output.object = f"Oblique Results:  \n{oblique(obl_choice_p1, obl_p1_val, obl_choice_p2, obl_p2_val, obl_flag, gamma_val)}"
        except Exception as e:
            oblique_output.object = f"Results will print here when a valid input is present.  \nUpstream Mach Number:0.0  \nUpstream Normal Mach Number:0.0  \nMach Number Downstream:0.0  \nDownstream Normal Mach Number:0.0  \nBeta:0.0  \nTheta:0.0  \nPressure Ratio:0.0  \nDensity Ratio:0.0  \nTemperature Ratio:0.0  \nTotal Pressure Ratio:0.0"


# you know, the button
calc_button.on_click(update_display)

# Layout
app = pn.Column(logos, pn.Tabs(
    ("Compressable Functions Calculator",
     pn.Column(
         gamma_input_raw,
         pn.Row(isentropic_input_raw, isentropic_p1_select, isentropic_output),
         pn.Row(normal_input_raw, normal_p1_select, normal_output),
         pn.Row(fanno_input_raw, fanno_p1_select, fanno_output),
         pn.Row(rayleigh_input_raw, rayleigh_p1_select, rayleigh_output),
         pn.Row(conical_mu_input_raw, conical_flag_select),
         pn.Row(conical_input_raw, conical_p1_select, conical_output),
         pn.Row(oblique_p1_raw, oblique_p1_select, oblique_flag_select),
         pn.Row(oblique_p2_raw, oblique_p2_select, oblique_output),
         calc_button,
         credits
     )),
    ("Compressable Functions Graphs",
     pn.Column(
         pn.Row(label_wip),
         pn.Row(credits)
     )),
    ("Incompressable Functions Calculator",
     pn.Column(
         pn.Row(label_wip),
         pn.Row(credits)
     )),
    ("Incompressable Functions Graphs",
     pn.Column(
         pn.Row(label_wip),
         pn.Row(credits)
     ))
))

# Use this line when running via `panel serve`
pn.state.favicon = "static/erlogo.png"
app.servable(title="AeroCalculator")
#commit test
