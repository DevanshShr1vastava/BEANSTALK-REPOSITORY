from flask import Blueprint,render_template,request,redirect,url_for
import re
from flask_login import current_user
import sqlite3
import pandas as pd
import functools
import plotly
import plotly.graph_objects as go
import plotly.express as px 
import json
mcq = Blueprint ('mcq',__name__)
@mcq.route('/mcq',methods = ["GET","POST"])

def test():
    import sqlite3
    import random
    import pandas as pd

    def q_time_test(Q_TIME):
        global T_obs
        if Q_TIME < 35:
            T_obs = 'mo'
        elif Q_TIME >= 35 and Q_TIME <= 60:
            T_obs = 'rst'
        else:
            T_obs = 'rsq' 
    def q_hint_test(N_HINT):
        global H_obs
        if N_HINT == 1:
            H_obs = 'rst'
        elif N_HINT == 2 or N_HINT == 3:
            H_obs = 'rsq'
        else:
            H_obs = 'mo'
    def answer_test(USER_ANSWER):
        global A_obs
        if USER_ANSWER == 0:
            A_obs = 'rsq'
        else:
            A_obs = 'mo'

    conn = sqlite3.connect('analyse.db')
    cur = conn.cursor()

    cur.execute("""Select * from QB_TABLE""")
    questions_df = pd.DataFrame(cur.fetchall())
    questions_df.columns = ['Q_ID','Sub_ID','SK_LVL','Question','Op1','Op2','Op3','Op4','Answer','Hint1','Hint2']
    cur.execute("""Select * from USER_ANALYSIS_TABLE""")
    analyse_ds_df = pd.DataFrame(cur.fetchall())
    analyse_ds_df.columns = ['U_ID','Q_ID','SK_LVL','Q_Time','N_Hint',"User_Answer"]


    def update_processed_data():
        cur.execute("""DELETE FROM PROCESSED_DATA""")
        for i in range(len(analyse_ds_df)):
            user_id = analyse_ds_df['U_ID'][i]
            
            question_id = analyse_ds_df['Q_ID'][i]
            q_hint_test(analyse_ds_df['N_Hint'][i])
            q_time_test(analyse_ds_df['Q_Time'][i])
            answer_test(analyse_ds_df['User_Answer'][i])
            Sk_lvl = analyse_ds_df['SK_LVL'][i]
            cur.execute("""INSERT INTO PROCESSED_DATA VALUES(?,?,?,?,?,?)""",(int(user_id),question_id,H_obs,T_obs,A_obs,int(Sk_lvl)))
        conn.commit()
    update_processed_data()
    cur.execute("""SELECT * FROM PROCESSED_DATA""")
    Processed_Data = pd.DataFrame(cur.fetchall())
    Processed_Data.columns = ['U_ID','Q_ID','H_Obs','T_Obs','A_Obs','SK_LVL']


    def add_into_qp():
        global q_add_list
        q_add_list = []
        for i in range(len(Processed_Data)):
            verdict = ''
            grouping_list = []
            grouping_list.append(Processed_Data['H_Obs'][i])
            grouping_list.append(Processed_Data['A_Obs'][i])
            grouping_list.append(Processed_Data['T_Obs'][i])
            if grouping_list[0] == 'rst':
                verdict = 'rst'
            elif grouping_list[0] == 'rsq':
                verdict = 'rsq'
            else:
                if grouping_list[1] == 'rsq':
                    verdict = 'rsq'
                else:
                    if grouping_list[2] == 'mo':
                        verdict = 'mo'
                    elif grouping_list[2] == 'rsq':
                        verdict = 'rsq'
                    else:
                        verdict = 'rst'
            if verdict == 'mo':
                temp_list = []
                for j in range(len(questions_df)):
                    temp_list.append(questions_df['Q_ID'][j])
                temp_list.remove(Processed_Data['Q_ID'][i])
                if Processed_Data['Q_ID'][i] not in q_add_list:
                    rc = random.choice(temp_list)
                    if rc != Processed_Data['Q_ID'][i]:
                        q_add_list.append(rc)
                    else:
                        continue
                else:
                    continue

            elif verdict == 'rst':
                for j in range(len(questions_df)):
                    if (questions_df['SK_LVL'][j] == Processed_Data['SK_LVL'][i]):
                        temp_list = []
                        if questions_df['Q_ID'][j] not in temp_list:
                            temp_list.append(questions_df['Q_ID'][j])
                        else:
                            continue
                    else:
                        continue
                rc = random.choice(temp_list)
                if rc not in q_add_list:
                    q_add_list.append(rc)
            else:
                if Processed_Data['Q_ID'][i] not in q_add_list:
                    q_add_list.append(Processed_Data['Q_ID'][i])
    def create_qp():
        global qp 
        qp = []
        patt1 = r"""[(][']|[(]["]"""
        patt2 = r"""['][,][)]|["][,][)]"""
        
        for i in q_add_list:
            cur.execute("""SELECT Question FROM QB_TABLE where Q_ID = ?""",(i,))
            question = re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone())))
            cur.execute("""SELECT op1 FROM QB_TABLE where Q_ID = ?""",(i,))
            op1 = re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone())))
            cur.execute("""SELECT op2 FROM QB_TABLE where Q_ID = ?""",(i,))
            op2 = re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone())))
            cur.execute("""SELECT op3 FROM QB_TABLE where Q_ID = ?""",(i,))
            op3 = re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone())))
            cur.execute("""SELECT op4 FROM QB_TABLE where Q_ID = ?""",(i,))
            op4 = re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone())))
            cur.execute("""SELECT answer from QB_TABLE where Q_ID = ?""",(i,))
            answer = re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone())))
            cur.execute("""SELECT Hint1 from QB_TABLE where Q_ID = ?""",(i,))
            hint1 = re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone())))
            cur.execute("""SELECT Hint2 from QB_TABLE where Q_ID = ?""",(i,))
            hint2 = re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone())))
            cur.execute("""SELECT Q_ID FROM QB_TABLE WHERE Q_ID = ?""",(i,))
            qid = re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone())))
            qp.append([question,op1,op2,op3,op4,answer,hint1,hint2,qid])

    update_processed_data()
    add_into_qp() 
    create_qp()
    print(q_add_list)
    print(Processed_Data)
    print(analyse_ds_df)   
    def submit():
        if request.method == "POST":
            if request.form['BTN'] == "submit":
                cur.execute("""DELETE FROM USER_ANALYSIS_TABLE""")
                print("Submit Pressed!")
                ans2 = request.form.get('radio2')
                ans3 = request.form.get('radio3')
                ans4 = request.form.get('radio4')
                ans1 = request.form.get('radio1')
                if (qp[0][5] == ans1):
                    ansre1 = 1
                else:
                    ansre1 = 0
                if (qp[1][5] == ans2):
                    ansre2 = 1
                else:
                    ansre2 = 0
                if (qp[2][5] == ans3):
                    ansre3 = 1
                else:
                    ansre3 = 0
                if (qp[3][5] == ans4):
                    ansre4 = 1
                else:
                    ansre4 = 0    
                anslist = [ansre1,ansre2,ansre3,ansre4]
                print(ansre1," ",ansre2," ",ansre3," ",ansre4)
                timelist = [request.form.get('t1'), request.form.get('t2'), request.form.get('t3'),request.form.get('t4')]
                print(timelist[0]," ", timelist[1]," ", timelist[2]," " ,timelist[3]," ")
                hintclist = [request.form.get('hc1'),request.form.get('hc2'),request.form.get('hc3'),request.form.get('hc2')]
                print(hintclist[0]," ",hintclist[1]," ",hintclist[2]," ",hintclist[3])
                total_time_elapsed = request.form.get('tte')
                print(total_time_elapsed)
                patt1 = r"""[[(][']|[(]["]"""
                patt2 = r"""['][,][)]|["][,][)]"""
                for i in range(4):
                    q_id = qp[i][8]
                    cur.execute("""select SK_LVL FROM QB_TABLE where Q_ID = (?)""",(qp[i][8],))
                    sk_lvl = int(re.sub(r"[(]","",re.sub(r"[,][)]","",re.sub(patt1,"",re.sub(patt2,"",repr(cur.fetchone()))))))
                    hintc = hintclist[i]
                    timec = timelist[i]
                    ansc = anslist[i]
                    cur.execute("""INSERT INTO USER_ANALYSIS_TABLE VALUES (?,?,?,?,?,?)""",(101,q_id,sk_lvl,hintc,timec,ansc))
            conn.commit()
            conn.close()
    submit()
    conn.close()

    return render_template("mcq.html",data = qp,user = current_user) 
    #with user = current_users
    #we will be able to reference the user in our current template to check whether the user is authenticated or not
