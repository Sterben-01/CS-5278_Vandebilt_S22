#!/usr/bin/env python3
# -*- coding: utf8 -*-
import sys
import os
import ast
import random
import astor
random.seed(2000)
assign_counter = 0
op_counter = 0
comp_counter = 0
random_number = 0
addcounter = 0
subcounter = 0
multcounter = 0
divcounter = 0
floordivcounter = 0
powcounter = 0
modcounter = 0
op_visit = False
comp_visit = False
del_visit = False
o = {
    "Add": 'ast.Sub()',
    "Sub": 'ast.Add()',
    "Mult": 'ast.Div()',
    "FloorDiv": 'ast.Mult()',
    "Div": 'ast.Mult()',
    "Pow": 'ast.Mod()',
    "Mod": 'ast.Pow()',
    "Eq": 'ast.NotEq()',
    "NotEq": 'ast.Eq()',
    "Lt": 'ast.GtE()',
    "Gt": 'ast.LtE()',
    "LtE": 'ast.Gt()',
    "GtE": 'ast.Lt()',
    "Is": 'ast.IsNot()',
    "IsNot": 'ast.Is()',
    "In": 'ast.NotIn()',
    "NotIn": 'ast.In()',
    "LShift":'ast.RShift()',
    "RShift":'ast.LShift()',
    "BitOr": 'ast.BitXor()',
    "BitXor": 'ast.BitOr()'
}

leftlist = ["Add","Sub","Mult","FloorDiv","Div","Pow","Mod"]
rightlist = ['ast.Sub()','ast.Add()','ast.Div()','ast.Mult()','ast.Mult()','ast.Mod()','ast.Pow()']
leftcomplist = ["Eq","NotEq","Lt","Gt","LtE","GtE","Is","IsNot","In","NotIn","LShift","RShift","BitOr","BitXor"]
rightcomplist = ['ast.NotEq()','ast.Eq()','ast.GtE()','ast.LtE()','ast.Gt()','ast.Lt()','ast.IsNot()','ast.Is()','ast.NotIn()','ast.In()','ast.RShift()','ast.LShift()','ast.BitXor()','ast.BitOr()']


class visit_ast(ast.NodeVisitor):
    def __init__(self):
        self.ascounter = 0
        #self.bincounter = 0
        self.compcounter = 0
        #self.addcounter = 0
    def visit_Assign(self, node):
        global assign_counter,random_number
        if isinstance(node, ast.Assign):
            self.ascounter = self.ascounter + 1
            assign_counter = self.ascounter
        return self.generic_visit(node)
        return self.generic_visit(node)
    def visit_BinOp(self, node):
        global assign_counter, random_number, addcounter, subcounter, multcounter, divcounter, floordivcounter, powcounter, modcounter
        if isinstance(node.op, ast.Add):
            addcounter = addcounter + 1
        if isinstance(node.op, ast.Sub):
            subcounter = subcounter + 1
        if isinstance(node.op, ast.Mult):
            multcounter = multcounter + 1
        if isinstance(node.op, ast.Div):
            divcounter = divcounter + 1
        if isinstance(node.op, ast.FloorDiv):
            floordivcounter = floordivcounter + 1
        if isinstance(node.op, ast.Pow):
            powcounter = powcounter + 1
        if isinstance(node.op, ast.Mod):
            modcounter = modcounter + 1
        return self.generic_visit(node)

    def visit_Compare(self, node):
        global comp_counter
        if isinstance(node, ast.Compare):
            self.compcounter = self.compcounter + 1
            comp_counter = self.compcounter
        return self.generic_visit(node)




class modify_ast(ast.NodeTransformer):
    def __init__(self):
        self.temp = 0
        self.bp = 0
        self.cm = 0
        self.addcounter = 0
        self.subcounter = 0
        self.multcounter = 0
        self.divcounter = 0
        self.floordivcounter = 0
        self.powcounter = 0
        self.modcounter = 0
    def visit_BinOp(self, node):
        global testpblicrandom, op_visit,op_counter
        global random_add_selection, random_sub_selection, random_mult_selection, random_div_selection
        global random_floordiv_selection, random_pow_selection, random_mod_selection
        self.bp = self.bp + 1
        if op_visit == False:
            return self.generic_visit(node)
        #random_dict_number = random.randint(0, test_number - 1)
        dicname = 'operationdic' + str(random_dict_number)
        if isinstance(node.op, ast.Add):
            self.addcounter = self.addcounter+1
            if self.addcounter == random_add_selection:
                node.op = eval(eval(dicname)[(str(type(node.op)).split("'")[1].split(".")[1])])
        if isinstance(node.op, ast.Sub):
            self.subcounter = self.subcounter+1
            if self.subcounter == random_sub_selection:
                node.op = eval(eval(dicname)[(str(type(node.op)).split("'")[1].split(".")[1])])
        if isinstance(node.op, ast.Mult):
            self.multcounter = self.multcounter+1
            if self.multcounter == random_mult_selection:
                node.op = eval(eval(dicname)[(str(type(node.op)).split("'")[1].split(".")[1])])
        if isinstance(node.op, ast.Div):
            self.divcounter = self.divcounter+1
            if self.divcounter == random_div_selection:
                node.op = eval(eval(dicname)[(str(type(node.op)).split("'")[1].split(".")[1])])
        if isinstance(node.op, ast.FloorDiv):
            self.floordivcounter = self.floordivcounter+1
            if self.floordivcounter == random_floordiv_selection:
                node.op = eval(eval(dicname)[(str(type(node.op)).split("'")[1].split(".")[1])])
        if isinstance(node.op, ast.Pow):
            self.powcounter = self.powcounter+1
            if self.powcounter == random_pow_selection:
                node.op = eval(eval(dicname)[(str(type(node.op)).split("'")[1].split(".")[1])])
        if isinstance(node.op, ast.Mod):
            self.modcounter = self.modcounter+1
            if self.modcounter == random_mod_selection:
                node.op = eval(eval(dicname)[(str(type(node.op)).split("'")[1].split(".")[1])])
        return self.generic_visit(node)


    def visit_Compare(self, node):
        global testpblicrandom, comp_visit,comp_counter
        self.cm = self.cm + 1
        if comp_visit == False:
            return self.generic_visit(node)
        #random_dict_number = random.randint(0, test_number - 1)
        dicname = 'operationdiccomp' + str(random_dict_number)
        if self.cm in random_comp_selection_list:
            for i in range(0, len(node.ops)):
                node.ops[i] = eval(eval(dicname)[(str(type(node.ops[i])).split("'")[1].split(".")[1])])
        return self.generic_visit(node)


    def visit_Assign(self,node):
        global del_visit
        self.temp = self.temp + 1

        if del_visit == False:
            return self.generic_visit(node)
        if self.temp == random_number or self.temp == random_number+1 or self.temp == random_number-1 :

            return ast.copy_location(ast.Expr(ast.Num(1)),node)

        ast.fix_missing_locations(node)

        return self.generic_visit(node)


def generate_ast(filename):
    global backtofile
    with open(filename,"r") as source:
        ast_tree = ast.parse(source.read()) # convert source code to AST
        modify_ast_handler = modify_ast()
        visit_count = visit_ast().visit(ast_tree)
        random_selection()
        new_tree = modify_ast_handler.visit(ast_tree) # modify AST tree
        backtofile = astor.to_source(new_tree) #convert back to source code
    return backtofile



def check_file_name(name):
    p = 0
    name = str(p) + ".py"
    while os.path.exists(name):
        p = p + 1
        name = str(p)+".py"
    print("file time", p)
    return name



def random_dict(a):
    templist = leftlist.copy()
    templist2 = rightlist.copy()
    tempcmplist = leftcomplist.copy()
    tempcmplist2 = rightcomplist.copy()
    names = globals()
    for i in range (0,a):
        random.shuffle(templist)
        random.shuffle(templist2)
        names['operationdic'+str(i)] = dict(zip(templist,templist2))
    for i in range (0,a):
        random.shuffle(tempcmplist)
        random.shuffle(tempcmplist2)
        names['operationdiccomp'+str(i)] = dict(zip(tempcmplist,tempcmplist2))
    return 0

def random_selection():
    global random_comp_selection_list, random_op_selection_list,random_number, random_dict_number,comp_counter,op_counter
    global addcounter,subcounter,multcounter,divcounter,floordivcounter,powcounter,modcounter
    global random_add_selection, random_sub_selection, random_mult_selection, random_div_selection
    global random_floordiv_selection, random_pow_selection, random_mod_selection

    if comp_counter == 0:
        comp_counter =1
    if op_counter == 0 :
        op_counter = 1
    random_comp_selection = random.randint(0,max(comp_counter-1,1))
    random_comp_selection_list = random.sample(range(0, comp_counter), random_comp_selection)
    random_add_selection = random.randint(0,max(addcounter-1,1))
    random_sub_selection = random.randint(0,max(subcounter-1,1))
    random_mult_selection = random.randint(0,max(multcounter-1,1))
    random_div_selection = random.randint(0,max(divcounter-1,1))
    random_floordiv_selection = random.randint(0,max(floordivcounter-1,1))
    random_pow_selection = random.randint(0,max(powcounter-1,1))
    random_mod_selection = random.randint(0,max(modcounter-1,1))
    # print("--------")
    # print("compcount:", comp_counter)
    # print("comp selec:", random_comp_selection)
    # print("comp list:", random_comp_selection_list)
    # print("----------")
    random_op_selection = random.randint(0, op_counter-1)
    random_op_selection_list = random.sample(range(0, op_counter), random_op_selection)
    print("+++++++")
    print("opcount:", op_counter)
    print("op selec:", random_op_selection)
    print("op list:", random_op_selection_list)
    print("+++++++")
    random_number = random.randint(0, assign_counter-1)  # 8
    random_dict_number = random.randint(0,test_number-1)





def main():
    global testpblicrandom, op_visit, del_visit,comp_visit, random_number,test_number
    if len(sys.argv) < 3:
        print("You must enter file name and the number of mutation")
        return 0
    test_number  = sys.argv[2]
    test_number = int(test_number)
    file_name = sys.argv[1]
    testpblicrandom = test_number
    random_number = random.randint(0, testpblicrandom - 1)
    print(test_number)
    print(file_name)
    # random_number()
    random_dict(test_number)
    for i in range(0,test_number): #write to file
        if (random.randint(0, 10) < 5):
            op_visit = True
        else:
            op_visit = True
        if (random.randint(0, 10) < 5):
            del_visit = True
        else:
            del_visit = False
        if (random.randint(0, 10) < 5):
            comp_visit = True
        else:
            comp_visit = False

        print("op_visit",op_visit)
        print("del_visit", del_visit)
        print("comp_visit", comp_visit)
        new_tree = generate_ast(file_name)  # generate AST tree
        new_file_name = check_file_name(file_name)
        file_out_put = open(new_file_name, "w")
        file_out_put.write(new_tree)
        file_out_put.close()
        print("test time", i)








if __name__ == '__main__':
    main()