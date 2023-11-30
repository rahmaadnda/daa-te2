import time
import tracemalloc

def dp_partition(arr):
    """
    Implementasi dari Set Partition Problem menggunakan Dynamic Programming

    Returns:
    bool: True jika suatu set dapat dibagi menjadi dua subset dengan jumlah nilai semua elemen yang sama,
    False jika tidak.

    Referensi (dengan modifikasi):
    https://www.geeksforgeeks.org/partition-problem-dp-18/
    """

    # menghitung total nilai semua elemen
    total = sum(arr)
        
    # base case, jika totalnya bernilai ganjil
    if (total % 2 != 0):
        return False

    # inisialisasi array partisi dengan 0    
    part = [0] * ((total // 2) + 1)
    
    # mengisi array partisi secara bottom-up
    for i in range(len(arr)):
        for j in range(total // 2, arr[i] - 1, -1):
            if (part[j - arr[i]] == 1 or j == arr[i]):
                part[j] = 1
                
    # mengembalikan elemen pada index yang sesuai
    return bool(part[total // 2])

def partition_values(values):
    """
    Implementasi main function dari Set Partition Problem menggunakan Branch and Bound
    
    Returns:
    bool: True jika suatu set dapat dibagi menjadi dua subset dengan jumlah nilai semua elemen yang sama,
    False jika tidak.
    
    Referensi (dengan modifikasi):
    http://www.csharphelper.com/howtos/howto_partition_exhaustive.html
    """
    
    # menghitung total nilai semua elemen
    total_value = sum(values)
    
    # base case, jika totalnya bernilai ganjil
    if (total_value % 2 != 0):
        return False
    
    # inisialisasi
    best_assignment = [None] * len(values)
    test_assignment = [None] * len(values)
    best_err = [total_value]

    # pemanggilan helper function
    partition_values_from_index(values, 0, total_value, total_value, 
                             test_assignment, 0, best_assignment, best_err);
    
    # mengecek selisih kedua partisi
    if best_err[0] == 0:
        return True

    return False


def partition_values_from_index(values, start_index, total_value, unassigned_value, 
                             test_assignment, test_value, best_assignment, best_err):
    """
    Implementasi helper function dari Set Partition Problem menggunakan Branch and Bound

    Referensi (dengan modifikasi):
    http://www.csharphelper.com/howtos/howto_partition_branch_and_bound.html#google_vignette
    """

    # base case, jika semua elemen sudah ditelusuri
    if start_index >= len(values):
        test_err = abs(2*test_value - total_value)
        # update jika hasilnya lebih baik
        if test_err < best_err[0]:
            best_err[0] = test_err
            best_assignment[:] = test_assignment[:]

    else:
        # rekursi untuk mencari partisi terbaik
        test_err = abs(2*test_value - total_value)
        if test_err - unassigned_value < best_err[0]:
            if best_err[0] > 1:
                unassigned_value -= values[start_index]

                test_assignment[start_index] = True
                partition_values_from_index(values, start_index + 1, total_value, unassigned_value,
                                        test_assignment, test_value+values[start_index], best_assignment, best_err)
                
                test_assignment[start_index] = False
                partition_values_from_index(values, start_index + 1, total_value, unassigned_value,
                                        test_assignment, test_value, best_assignment, best_err)


def analyze_algorithm(dataset, algorithm):
    """
    Pengujian untuk setiap algoritma dengan setiap variasi dataset.
    Untuk setiap pengujian, dilakukan perhitungan waktu eksekusi dan penggunaan memori
    
    Referensi:
    https://docs.python.org/3/library/time.html 
    https://docs.python.org/3/library/tracemalloc.html 
    """

    tracemalloc.start()
    start_time = time.time()

    result = algorithm(dataset)
    
    end_time = time.time()
    memory_used = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    execution_time = (end_time - start_time) * 1000

    return result, execution_time, memory_used

# main program yang akan membaca dataset dan memanggil setiap fungsi
dataset_sizes = {'kecil': 10, 'sedang': 40, 'besar': 80}

for size in dataset_sizes:
    with open(f"dataset/{size}.txt", "r") as f:
        dataset = f.read().split("\n")
        dataset = [int(data) for data in dataset if data.isnumeric()]
        print(f"Ukuran dataset: {size} ({dataset_sizes[size]} elemen)\n")
        print("Dynamic Programming:")
        dp_result, dp_time, dp_memory = analyze_algorithm(dataset, dp_partition)
        print(f"Partition solution: {dp_result}")
        print(f"Memory used: {dp_memory:.2f} B")
        print(f"Execution time: {dp_time:.2f} ms\n")

        print("Branch and Bound:")
        bnb_result, bnb_time, bnb_memory = analyze_algorithm(dataset, partition_values)
        print(f"Partition solution: {bnb_result}")
        print(f"Memory used: {bnb_memory:.2f} B")
        print(f"Execution time: {bnb_time:.2f} ms\n")
        print("="*50)

