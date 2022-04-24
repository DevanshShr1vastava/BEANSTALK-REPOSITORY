import sqlite3
from turtle import update
import pandas as pd
import functools
import plotly
import plotly.graph_objects as go
import plotly.express as px 
from flask import Flask, render_template
import json
app = Flask(__name__)
@app.route('/')
def try_stuff():

    conn = sqlite3.connect('analyse.db')
    cur = conn.cursor()
    cur.execute("""Select * from USER_ANALYSIS_TABLE WHERE U_ID = 101""")
    analyse_ds_df = pd.DataFrame(cur.fetchall())
    analyse_ds_df.columns = ['U_ID','Q_ID','Sub_ID','SK_LVL','Q_Time','N_Hint',"User_Answer"]
    T_hint = []
    T_Time = []
    T_Answer = []
    User_id = 101
    for i in range(len(analyse_ds_df)):
        T_hint.append(analyse_ds_df['N_Hint'][i])
        T_Time.append(analyse_ds_df['Q_Time'][i])
        T_Answer.append(analyse_ds_df['User_Answer'][i])
    print(T_hint)
    print(T_Time)
    print(T_Answer)

    def Hint_Obs_test():
        global mark_h
        T_hint_s = functools.reduce(lambda a, b: a+b,T_hint) 
        if T_hint_s >=0 and T_hint_s <=2:
            mark_h = 10
        elif T_hint_s >=3 and T_hint_s <=5:
            mark_h = 9
        elif T_hint_s >=6 and T_hint_s <=7:
            mark_h = 8
        elif T_hint_s >=8 and T_hint_s <=13:
            mark_h = 7
        elif T_hint_s >=14 and T_hint_s <=18:
            mark_h = 6
        elif T_hint_s >=19 and T_hint_s <=23:
            mark_h = 5
        elif T_hint_s >=24 and T_hint_s <=28:
            mark_h = 4
        elif T_hint_s >=29 and T_hint_s <=33:
            mark_h = 3
        elif T_hint_s >=24 and T_hint_s <=38:
            mark_h = 2
        elif T_hint_s >=39 and T_hint_s <=43:
            mark_h = 1
        else:
            mark_h = 0
    def Time_obs_test(): 
        global mark_t
        T_time_s = functools.reduce(lambda a, b: a+b,T_Time)
        if T_time_s >=150 and T_time_s <=200:
            mark_t = 10
        elif T_time_s >=201 and T_time_s <=290:
            mark_t = 9
        elif T_time_s >=291 and T_time_s <=370:
            mark_t = 8
        elif T_time_s >=371 and T_time_s <=450:
            mark_t = 7
        elif T_time_s >=451 and T_time_s <=530:
            mark_t = 6
        elif T_time_s >=531 and T_time_s <=620:
            mark_t = 5
        elif T_time_s >=621 and T_time_s <=710:
            mark_t = 4
        elif T_time_s >=711 and T_time_s <=800:
            mark_t = 3
        elif T_time_s >=801 and T_time_s <=900:
            mark_t = 2
        elif T_time_s >=901 and T_time_s <=1000:
            mark_t = 1
        else:
            mark_t = 0
    def Answer_obs_test():
        global mark_a
        T_Answer_s = functools.reduce(lambda a, b: a+b,T_Answer)
        T_answer_s_p = int((T_Answer_s/15)*100)
        if T_answer_s_p < 100 and T_answer_s_p > 90:
            mark_a = 10
        elif T_answer_s_p > 80 and T_answer_s_p < 89:
            mark_a = 9 
        elif T_answer_s_p > 70 and T_answer_s_p < 79:
            mark_a = 8
        elif T_answer_s_p > 60 and T_answer_s_p < 69:
            mark_a = 7
        elif T_answer_s_p > 50 and T_answer_s_p < 59:
            mark_a = 6
        elif T_answer_s_p > 40 and T_answer_s_p < 49:
            mark_a = 5
        elif T_answer_s_p > 30 and T_answer_s_p < 39:
            mark_a = 4
        elif T_answer_s_p > 20 and T_answer_s_p < 29:
            mark_a = 3
        elif T_answer_s_p > 10 and T_answer_s_p < 19:
            mark_a = 2
        else:
            mark_a = 1

    def update_obs_table():
        cur.execute("""INSERT INTO OBSERVED VALUES ( ?,?,?,?,?) """,(User_id,mark_h,mark_t,mark_a,total_m))
        conn.commit()

    Hint_Obs_test()
    Time_obs_test()
    Answer_obs_test()
    total_m = mark_a+mark_h+mark_t
    update_obs_table()
    conn.commit()
    conn.close()

    def graph_create():
        fig = go.Figure(go.Bar(x = [mark_h,mark_t,mark_a],y = ['Hint marks','Time marks','Answer Marks'],orientation = 'h'))
        
        graphJSON = json.dumps(fig,cls = plotly.utils.PlotlyJSONEncoder)
        return graphJSON
    bar = graph_create()
    return render_template("test.html",plot = bar)

if __name__ == "__main__":
    app.run(debug = True)