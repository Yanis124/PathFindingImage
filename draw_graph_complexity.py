import matplotlib.pyplot as plt

def read_execution_times(file_path):
    execution_times = []
    
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line != "\n":
                execution_times.append(float(line.strip()))
    execution_times.sort()
    return execution_times

def display_graph_data(list_data,name_algo,nombre_tries):

    list_tries=[i for i in range(1,nombre_tries+1)]
        
    plt.plot(list_tries, list_data, marker='o',label=name_algo)
    
    plt.ylabel('nombre de sommets explorés')
    title="Comparaison entre Dijkstra naïf et Dijkstra optimisé"
    plt.title(title)
    plt.grid(True)
    plt.legend()
    
    plt.ylim(0, max(list_data) + 1)
    
    plt.savefig('complexité Djikstra ')  # sauvgarder le diagramme
    
def main():

    # Replace these file paths with your actual file paths
    file_path_algo1 = "execution_time_dijkstra.txt"
    file_path_algo2 = "execution_time_dijkstra_optimisation.txt"

    # Read execution times from files
    execution_times_algo2 = read_execution_times(file_path_algo2)
    execution_times_algo1 = read_execution_times(file_path_algo1)

    display_graph_data(execution_times_algo2,"Dijkstra optimisé",len(execution_times_algo2))
    display_graph_data(execution_times_algo1,"Dijkstra",len(execution_times_algo1))
    
main()



