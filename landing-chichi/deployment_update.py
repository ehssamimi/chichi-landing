import yaml

registry_url: str = "registry.api.chichiapp.ir:4443/chichi/"
image_name: str = "chichilanding"
final_image: str = f"{registry_url}{image_name}"

with open("build-count.txt") as f:
    a = f.readline()
    print(a)
    line = str(a).split('=')
    latest_number = int(line[1])
    last_number = latest_number - 1
    last_image_str = f"{final_image}:{last_number}"
    new_image_str = f"{final_image}:{latest_number}"
    print("last", last_image_str)
    print("new", new_image_str)
    f.close()

with open("deployment.yaml") as file:
    deployment = yaml.load(file)

print("build_number", f"{final_image}:{latest_number}")
deployment["spec"]["template"]["spec"]["containers"][0][
    'image'] = f"{final_image}:{latest_number}"

with open("deployment.yaml", 'w') as file:
    yaml.dump(deployment, file)
