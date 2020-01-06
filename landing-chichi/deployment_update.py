
def replace_in_file(filename, key, new_value):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for i, line in enumerate(lines):
        if line.split(':')[0].strip(' \n') == key:
            lines[i] = key + ' : ' + new_value + '\n'
    f = open(filename, "w")
    f.write("".join(lines))
    f.close()

with open("build-count.txt") as f:
    a = f.readline()
    print(a)
    line = str(a).split('=')
    latest_number =int(line[1])
    last_number = latest_number - 1
    last_image_str = f"includeamin/chichilanding:{last_number}"
    new_image_str = f"includeamin/chichilanding:{latest_number}"
    print("last",last_image_str)
    print("new",new_image_str)
    f.close()

# lines = open('deployment.yaml').read().splitlines()
# for item in lines:
#     if item.__contains__(f'        image: {last_image_str}'):
#         print(lines.index(item))
#         lines[lines.index(item)]=f'        image: {new_image_str}'
#
#         print("ya")
#
# open('deployment.yaml','w').write('\n'.join(lines))

import yaml

with open("deployment.yaml") as file:
    deployment = yaml.load(file)

print("build_number",f"includeamin/chichilanding:{latest_number}")
deployment["spec"]["template"]["spec"]["containers"][0]['image'] = f"includeamin/chichilanding:{latest_number}"

with open("deployment.yaml",'w') as file:
    yaml.dump(deployment,file)
