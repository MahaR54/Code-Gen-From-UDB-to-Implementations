import yaml

with open("mock.yaml", "r") as f:
    data = yaml.safe_load(f)

name = data.get("name", "")
encoding = data.get("encoding", {})
match = encoding.get("match", "")
variables = encoding.get("variables", [])

with open("inst_data.h", "w") as f:
    f.write("// Auto-generated from mock.yaml\n\n")
    f.write("#ifndef INST_DATA_H\n#define INST_DATA_H\n\n")
    f.write(f'#define INST_NAME "{name}"\n')
    f.write(f'#define MATCH_PATTERN "{match}"\n\n')

    for var in variables:
        var_name = var.get("name")
        location = var.get("location")
        f.write(f'#define {var_name.upper()}_LOCATION "{location}"\n')

    f.write("\n#endif // INST_DATA_H\n")

print("inst_data.h generated from mock.yaml")
