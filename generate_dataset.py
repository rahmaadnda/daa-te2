import random

def generate_dataset(size):
    """
    Pembuatan dataset sesuai dengan kriteria variasi yang diminta.
    Data akan berada pada range 1 sampai 100.
    Hasilnya akan disimpan ke dalam suatu file .txt
    """
    dataset = set()
    sizes = {'kecil': 10, 'sedang': 40, 'besar': 80}
    count = sizes[size]
    while len(dataset) < count:
        dataset.add(random.randint(1, 100))
    dataset = list(dataset)
    save_dataset(f"dataset/{size}.txt", dataset)
    return dataset

def save_dataset(filename, dataset):
    with open(filename, "w") as f:
        for data in dataset:
            f.write(str(data) + "\n")

dataset_sizes = ['kecil', 'sedang', 'besar']

# main program
for size in dataset_sizes:
    dataset = generate_dataset(size)  