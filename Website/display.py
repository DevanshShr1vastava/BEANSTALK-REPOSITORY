import sqlite3
def sk_lvl_test(sk_lvl):
    global S_SK_LVL
    if sk_lvl == 1:
        S_SK_LVL = 'beginner'
    elif sk_lvl == 2:
        S_SK_LVL = 'intermediate'
    elif sk_lvl == 3:
        S_SK_LVL = 'Advanced'
    else:
        pass
def q_time_test(Q_TIME):
    global T_obs
    if Q_TIME < 20:
        T_obs = 'mo'
    elif Q_TIME >= 20 and Q_TIME <= 60:
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
        A_obs = 'rst'
    else:
        A_obs = 'mo'

conn = sqlite3.connect('analyse.db')
c = conn.cursor()
c.execute("Select U_ID,SUB_ID from USER_ANALYSIS_TABLE")
user_data = c.fetchone()
user_id = user_data[0]
subject_id = user_data[1]

c.execute("SELECT Q_ID,SK_LVL, Q_TIME, N_HINT, USER_ANSWER From USER_ANALYSIS_TABLE")
user_analysis_data = c.fetchall()
for i in user_analysis_data:
    sk_lvl_test(i[1])
    q_time_test(i[2])
    q_hint_test(i[3])
    answer_test(i[4])
    c.execute("""INSERT INTO USER_PREFERENCE_TABLE VALUES(?,?,?,?,?,?,?)""",(user_id,subject_id,S_SK_LVL,H_obs,T_obs,i[0],A_obs))
c.execute("""SELECT * FROM USER_PREFERENCE_TABLE""")
table1 = list(c.fetchall())
print(table1)
conn.commit()
conn.close()
