# 没有使用函数
unprinted_designs = ['iphone case', 'robot pedant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

# 使用函数分块执行


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pedant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
len(unprinted_designs)
