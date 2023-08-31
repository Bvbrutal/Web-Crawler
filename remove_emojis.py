remove_file_path = 'static/README.md'
simple = 'static/previous_output.md'
try:
    with open(remove_file_path, 'r', encoding='utf-8') as f1:
        data1 = f1.read()

    with open(simple, 'r', encoding='utf-8') as f2:
        data2 = f2.read()
        data1 = data1.replace(data2, '')

    with open(remove_file_path, 'w', encoding='utf-8') as f3:
        f3.write(data1)

    print("succssfully delect :\n", data2)

except FileNotFoundError:
    print("Error: One or both files not found.")
except Exception as e:
    print(f"An error occurred: {e}")
