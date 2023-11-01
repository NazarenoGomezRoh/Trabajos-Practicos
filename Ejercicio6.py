from arbol_binario import BinaryTree, get_value_from_file

file_jedi = open("jedis.txt", "r")
read_lines = file_jedi.readlines()
file_jedi.close()

#a.
name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()

read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    name_tree.insert_node(jedi[0], index+2)
    specie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)

print("---------------------------------")
print("b. Barrido por nombre y ranking")
name_tree.inorden_file('jedis.txt')
print()
ranking_tree.inorden_file('jedis.txt')

print("---------------------------------")
print("c. Barrido por ranking y especie")
ranking_tree.by_level()
print()
specie_tree.by_level()
print("---------------------------------")


print("d.")
print("YODA.INFO:")
pos = name_tree.search('yoda')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')
print("")
print("SKYWALKER.INFO")
pos = name_tree.search('luke skywalker')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')

print("---------------------------------")

print("e. JEDIS MASTERS")

#ranking_tree.search_by_ranking('jedi master')

print("---------------------------------")

print("f.JEDIS CON SABLE COLOR VERDE")
name_tree.inorden_file_lightsaber('jedis.txt', 'green')
print("---------------------------------")

print('g. ')
#name_tree.inorden_maestros('jedis.txt')
print("---------------------------------")

#print("h. Togruta o Cerean")

print("i.JEDIS QUE EMPIEZAN CON 'A' y '-' ")
name_tree.inorden_start_with_jedi('A, "-"')
print("")