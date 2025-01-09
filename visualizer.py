import matplotlib.pyplot as plt

def bar_chart(data):
    # Extract names and prices from the data
    names = [coin['name'] for coin in data]
    prices = [coin['price'] for coin in data]

    # Bar chart
    plt.figure(figsize=(10, 6))  # Set the size of the figure
    plt.bar(names, prices, color='skyblue')  # Create a bar chart with skyblue bars
    plt.title('Top Cryptocurrencies by Price (USD)', fontsize=16)  # Add a title
    plt.xlabel('Cryptocurrency', fontsize=12)  # Label for the x-axis
    plt.ylabel('Price (USD)', fontsize=12)  # Label for the y-axis
    plt.xticks(rotation=45, fontsize=10)  # Rotate x-axis labels for readability
    plt.tight_layout()  # Automatically adjust layout to fit all elements
    plt.show()  # Display the plot

def pie_chart(data):
    
    # Extract the names and market caps of the cryptocurrencies
    names = [coin['name'] for coin in data]
    market_caps = [coin['market_cap'] for coin in data]

    # Create a new figure for the pie chart
    plt.figure(figsize=(8, 8))
    
    # Plot the pie chart
    plt.pie(
        market_caps,  # Data to plot
        labels=names,  # Labels for each slice
        autopct='%1.1f%%',  # Format for displaying percentages
        startangle=140,  # Starting angle for the pie chart
        colors=plt.cm.Paired.colors  # Colors for the slices
    )
    
    # Set the title of the pie chart
    plt.title('Market Cap Distribution of Top Cryptocurrencies', fontsize=16)
    
    # Automatically adjust layout to fit all elements
    plt.tight_layout()
    
    # Display the pie chart
    plt.show()

def line_chart(data):
    
    # Extract the names and 24-hour percentage changes of the cryptocurrencies
    names = [coin['name'] for coin in data]
    changes = [coin['change_24h'] for coin in data]

    # Create a new figure for the line chart
    plt.figure(figsize=(10, 6))
    
    # Plot the line chart
    plt.plot(
        names,  # X-axis data
        changes,  # Y-axis data
        marker='o',  # Marker style
        color='green',  # Line color
        linestyle='-'  # Line style
    )
    
    # Set the title of the line chart
    plt.title('24-Hour Percentage Price Change', fontsize=16)
    
    # Set the label for the x-axis
    plt.xlabel('Cryptocurrency', fontsize=12)
    
    # Set the label for the y-axis
    plt.ylabel('Percentage Change (%)', fontsize=12)
    
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, fontsize=10)
    
    # Add a horizontal line at y=0 for reference
    plt.axhline(0, color='red', linestyle='--')
    
    # Automatically adjust layout to fit all elements
    plt.tight_layout()
    
    # Display the line chart
    plt.show()
