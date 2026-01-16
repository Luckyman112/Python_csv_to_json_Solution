import json


def read_csv(path: str) -> list[dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    if not lines:
        return []
    headers = lines[0].split(",")
    result: list[dict[str, str]] = []
    for line in lines[1:]:
        values = line.split(",")
        row = dict(zip(headers, values))
        result.append(row)
    return result

def write_json(path: str, data: list[dict[str, str]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main() -> None:
    data = read_csv("aaa.csv")
    write_json("aaa.json", data)
    print("Успех")

if __name__ == "__main__":
    main()
