from fetcher import fetch_crypto_prices, search_crypto
from csv_saver import save_to_csv
from visualizer import bar_chart, pie_chart, line_chart

result = None  # Initialize globally to store search results

def user_interface():
    """
    Main user interface for the Cryptocurrency Tracker.
    Provides options to view top cryptocurrencies, search for a specific cryptocurrency,
    save data to CSV, visualize data, and exit the application.
    """

    print('\nWelcome to the Cryptocurrency Tracker!')

    while True: #Infinite loop to keep the program running    
        print('\nChoose an option: ')
        print('1. View top cryptocurrencies')
        print('2. Search for a cryptocurrency')
        print('3. Save Data to CSV')
        print('4. Visualize Data')
        print('5. Exit')

        try:
            option = int(input('\nChoose an Option: '))

            if option == 1:  # Option 1: View Top Cryptocurrencies
                print('\nViewing top cryptocurrencies...')
                top_cryptos = fetch_crypto_prices()  # Fetch the data
                if top_cryptos:  # Check if data was fetched successfully
                    print("\nTop Cryptocurrencies by Market Cap:\n") #Displaying header
                    for coin in top_cryptos: #Looping through each cryptocurrency
                        print(f"{coin['name']} ({coin['symbol']}): ${coin['price']:.2f} ({coin['change_24h']:+.2f}%)")
                else:
                    print("Failed to fetch top cryptocurrencies. Please try again.")

            elif option == 2:  # Option 2: Search for a Cryptocurrency
                coin_name = input("Enter the name or symbol of the cryptocurrency: ").strip().lower()
                print('Searching...')
                global result  # Access the global variable to store the search result
                result = search_crypto(coin_name)  # Perform the search
                if result:
                    print(f"\nSearch Result:\n")
                    print(f"Name: {result['name']}")
                    print(f"Symbol: {result['symbol']}")
                    print(f"Price: ${result['price']:.2f}")
                    print(f"Market Cap: ${result['market_cap']:,}")
                    print(f"24-Hour Change: {result['change_24h']:+.2f}%")
                else:
                    print(f"No results found for '{coin_name}'. Please try again.")

            elif option == 3:  # Option 3: Save Data to CSV
                print('\nSaving data to a CSV...')
                print('\nWhich data do you want to save?')
                print('1. Top Cryptocurrencies')
                print('2. Searched Cryptocurrency')
                try:
                    save_option = int(input('Enter your choice: '))
                    if save_option == 1:
                        print('Alright, lets save the top cryptocurrencies!')
                        file_name = input('Enter the file name you would like to save it to: ')
                        top_cryptos = fetch_crypto_prices()  # Fetch the data again for saving
                        if top_cryptos:
                            save_to_csv(top_cryptos, file_name)
                            print(f"Data successfully saved to {file_name}.")
                        else:
                            print("Failed to fetch top cryptocurrencies. Please try again.")
                    elif save_option == 2:
                        if result:  # Ensure a search result exists
                            file_name = input('Enter the file name you would like to save it to: ')
                            save_to_csv(result, file_name)
                            print(f"Data successfully saved to {file_name}.")
                        else:
                            print("No searched cryptocurrency data available. Please search first.")
                    else:
                        print('Invalid choice. Please enter 1 or 2.')
                except ValueError:
                    print('Invalid input, please enter a number.')

            elif option == 4:  # Option 4: Visualize Data
                print('\nChoose a visualization type: ')
                print('1. Bar chart (prices)')
                print('2. Pie chart (Market Cap)')
                print('3. Line chart (24 - Hour change)')

                try:
                    chart_option = int(input('Enter the choice you would like (1-3): '))
                    top_cryptos = fetch_crypto_prices()
                    if top_cryptos:
                        if chart_option == 1:
                            bar_chart(top_cryptos)
                        elif chart_option == 2:
                            pie_chart(top_cryptos)
                        elif chart_option == 3:
                            line_chart(top_cryptos)
                        else:
                            print('Invalid choice, try again: ')
                except ValueError:
                    print('Invalid input, try again: ')

            elif option == 5:  # Option 5: Exit
                print('\nThanks for using the crypto tracker! Bye!')
                break
            
            else:
                print('\nInvalid choice. Please enter a number between 1 and 5.')

        except ValueError:
            print('\nInvalid input. Please try again.')

        print('\nReturning to the main menu...')


if __name__ == '__main__':
    user_interface()



