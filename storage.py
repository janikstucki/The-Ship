import requests

while True:
    structure_response = requests.get("http://10.255.255.254:2012/structure")
    structure_data = structure_response.json()
    print(structure_data["hold"][0])

    if None not in structure_data["hold"][0]:
        row_length = len(structure_data["hold"][0])
        column_height = len(structure_data["hold"])
        row_selected = column_height - 1

        for row in structure_data["hold"]:
            if None in structure_data["hold"][row_selected]:
                break
            else: 
                row_selected -= 1
        
        for col_index in range(row_length):
            for row_index in range(row_selected):
                while True:
                    swap_response = requests.post("http://10.255.255.254:2012/swap_adjacent", json={"a": {"x": col_index, "y": row_index}, "b": {"x": col_index, "y": row_index + 1}})
                    if swap_response.status_code == 200:
                        break