ROOT_DIR = "results"
import json
import os


def read_json_data(root_dir: str) -> float:
    acc = 0
    for db_name in os.listdir(root_dir):
        db_path = os.path.join(root_dir, db_name)
        if os.path.isdir(db_path):
            for cpu_count in os.listdir(db_path):
                cpu_path = os.path.join(db_path, cpu_count)
                if os.path.isdir(cpu_path):
                    for file_name in os.listdir(cpu_path):
                        if file_name.endswith(".json"):
                            file_path = os.path.join(cpu_path, file_name)
                            with open(file_path, "r") as file:
                                json_data = json.load(file)
                                time = json_data["time"]
                                acc += float(time)
    return acc


if __name__ == "__main__":
    acc = read_json_data(ROOT_DIR)
    print(acc)
