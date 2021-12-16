# Import needed modules from PuLP
import numpy as np
import pandas as pd
from pulp import *
from pulp import GLPK





#List of Students
students=['st1', 'st2', 'st3', 'st4', 'st5', 'st6', 'st7', 'st8', 'st9', 'st10', 'st11', 'st12', 'st13', 'st14', 'st15', 'st16', 'st17', 'st18', 'st19', 'st20', 'st21', 'st22', 'st23', 'st24', 'st25', 'st26', 'st27', 'st28', 'st29', 'st30', 'st31', 'st32', 'st33', 'st34', 'st35', 'st36', 'st37', 'st38', 'st39', 'st40', 'st41', 'st42', 'st43', 'st44', 'st45', 'st46', 'st47', 'st48', 'st49', 'st50', 'st51', 'st52', 'st53', 'st54', 'st55', 'st56', 'st57', 'st58', 'st59', 'st60','st61', 'st62', 'st63', 'st64', 'st65', 'st66', 'st67', 'st68', 'st69', 'st70','st71', 'st72', 'st73', 'st74', 'st75', 'st76', 'st77', 'st78', 'st79', 'st80', 'st81', 'st82', 'st83', 'st84', 'st85', 'st86', 'st87', 'st88', 'st89', 'st90', 'st91', 'st92', 'st93', 'st94', 'st95', 'st96', 'st97', 'st98', 'st99', 'st100', 'st101', 'st102', 'st103', 'st104', 'st105', 'st106', 'st107', 'st108', 'st109', 'st110', 'st111', 'st112', 'st113', 'st114', 'st115', 'st116', 'st117', 'st118', 'st119', 'st120', 'st121', 'st122', 'st123', 'st124', 'st125', 'st126', 'st127', 'st128', 'st129', 'st130', 'st131', 'st132', 'st133', 'st134', 'st135', 'st136', 'st137', 'st138', 'st139', 'st140','st141', 'st142', 'st143', 'st144', 'st145', 'st146', 'st147', 'st148', 'st149', 'st150','st151', 'st152', 'st153', 'st154', 'st155', 'st156', 'st157', 'st158', 'st159', 'st160']

#List of Lecturers
lecturers = ['lec1', 'lec2','lec3','lec4','lec5','lec6','lec7','lec8','lec9','lec10','lec11', 'lec12','lec13','lec14','lec15','lec16','lec17','lec18']

#Workload Vector

workload_Vec = {'lec1':12,'lec2':6,'lec3':9,'lec4':12,'lec5':10,
                'lec6':10,'lec7':9,'lec8':8,'lec9':9,'lec10':18,
                'lec11':4,'lec12':8,'lec13':9,'lec14':9,'lec15':4,'lec16':6,
                'lec17':8,'lec18':9}

students_Lec = [range(1)]
#Cost Matrix
MyCost = pd.read_csv(r'C:\Users\PROF. STEPHEN\Desktop\New folder (3)\Untitled form.csv\MyDATA.csv')
print(MyCost)
x = np.array(MyCost)


y =np.array([x[0,2:162],x[1,2:162],x[2,2:162],x[3,2:162],x[4,2:162],x[5,2:162],x[6,2:162],x[7,2:162],x[8,2:162],x[9,2:162],x[10,2:162],x[11,2:162],x[12,2:162],x[13,2:162],x[14,2:162],x[15,2:162],x[16,2:162],x[17,2:162]])

cost_Mat = y
print(cost_Mat)

print()
model1 = LpProblem(name='SSA-Problem', sense=LpMinimize)

stud= {st:1 for st in students}

cost_Mat= makeDict([lecturers, students], cost_Mat, 0)
#cost_Mat
#makeDict
#Assignments 
assignments = [(l,s) for l in lecturers for s in students]


variables = LpVariable.dicts("ASSIGN", (lecturers, students), 0, None, LpBinary)
#variables

#Objective function
model1 += lpSum( [variables[l][s] * cost_Mat[l][s] for (l,s) in assignments])


#workload Constriants
for l in lecturers:
    model1 += lpSum([variables[l][s] for s in students]) <= workload_Vec[l]


#one lecturer to only one students constaints
for s in students:
    model1 += lpSum([variables[l][s] for l in lecturers]) == stud[s] 


#status = model1.solve(solver=XPRESS)
status = model1.solve()
print(status)


# Status
print(f"status: {model1.status}, {LpStatus[model1.status]}")
#Value of Obj_Fxn
print(f"objective: {model1.objective.value()}")

for var in model1.variables():
    Sec = var.value()
    if Sec ==1:
        print(f"{var.name}: {Sec}") 
    #else:
        #print("Sorry")
    
        
#for name, constraint in model1.constraints.items():
  #  print(f"{name}: {constraint.value()}")
    
