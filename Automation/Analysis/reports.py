import time
import psutil
import matplotlib.pyplot as plt

# Initialize empty lists to store data
time_points = []
memory_usage = []
cpu_usage = []

# Function to update the data
def update_data():
    for i in range(30):
        # Fetch memory information
        vm = psutil.virtual_memory()
        memory_percent = vm.percent
        # Fetch top 10 processes with highest CPU usage
        processes = sorted(psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']) if hasattr(psutil, 'process_iter') else [],
                           key=lambda p: p.info['cpu_percent'], reverse=True)[:10]
        # Calculate total CPU usage
        total_cpu_usage = sum([p.info['cpu_percent'] for p in processes])

        # Append data to lists
        time_points.append(i)
        memory_usage.append(memory_percent)
        cpu_usage.append(total_cpu_usage)

        # Wait for 1 second before collecting next data point
        time.sleep(1)

    # Clear previous plot
    plt.clf()
    
    # Plot memory usage
    plt.subplot(2, 1, 1)
    plt.plot(time_points, memory_usage, label='Memory (%)')
    plt.xticks(range(0, max(time_points)+1, 1))
    plt.xlabel('Time (s)')
    plt.ylabel('Memory Usage (%)')
    plt.title('Memory Usage over Time')
    plt.legend()

    # Plot CPU usage
    plt.subplot(2, 1, 2)
    plt.plot(time_points, cpu_usage, label='CPU (%)')
    plt.xticks(range(0, max(time_points)+1, 1))
    plt.xlabel('Time (s)')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage over Time')

    # Adjust layout so there is a space between the memory and cpu plots
    plt.subplots_adjust(hspace=0.5)
    plt.tight_layout()
    # Show the plot
    plt.show()

# Call the function
update_data()