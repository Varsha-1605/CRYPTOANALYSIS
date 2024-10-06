# import yfinance as yf
# import plotly.graph_objects as go
# from datetime import datetime as dt
# from plotly.subplots import make_subplots

# def get_data(crypto_symbol, start_date, end_date):
#     data = yf.download(crypto_symbol, start=start_date, end=end_date)
#     return data

# def create_graph(crypto_data, crypto_name):
#     fig = go.Figure(data=[
#         go.Candlestick(
#             x=crypto_data.index,
#             open=crypto_data['Open'],
#             high=crypto_data['High'],
#             low=crypto_data['Low'],
#             close=crypto_data['Close'],
#             name='Candlesticks',
#             increasing_line_color='blue',
#             decreasing_line_color='grey'
#         ),
#         go.Scatter(
#             x=crypto_data.index,
#             y=crypto_data['Close'].rolling(window=30).mean(),
#             name='30 Day Moving Average',
#             mode='lines'
#         )
#     ])
#     fig.update_layout(title=f'Lakshya Crypto Price Graph Analysis - {crypto_name}', 
#                       yaxis_title='Price (USD)',
#                       height=600)
#     return fig

# def run():
#     # List of cryptocurrencies to analyze
#     crypto_list = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'ADA-USD']
    
#     start_date = '2024-01-01'
#     end_date = dt.now().strftime("%Y-%m-%d")

#     # Create a subplot for each cryptocurrency
#     fig = make_subplots(rows=len(crypto_list), cols=1, 
#                         subplot_titles=[f"{crypto} Analysis" for crypto in crypto_list],
#                         vertical_spacing=0.1)

#     for i, crypto in enumerate(crypto_list, start=1):
#         crypto_data = get_data(crypto, start_date, end_date)
#         crypto_fig = create_graph(crypto_data, crypto)
        
#         for trace in crypto_fig.data:
#             fig.add_trace(trace, row=i, col=1)

#     fig.update_layout(height=600*len(crypto_list), title_text="Cryptocurrency Analysis Dashboard")
#     fig.show()

# if __name__ == "__main__":
#     run()




















# import yfinance as yf
# import plotly.graph_objects as go
# from datetime import datetime as dt

# def get_data(crypto_symbol, start_date, end_date):
#     data = yf.download(crypto_symbol, start=start_date, end=end_date)
#     return data

# def create_graph(crypto_data, crypto_name):
#     fig = go.Figure(data=[
#         go.Candlestick(
#             x=crypto_data.index,
#             open=crypto_data['Open'],
#             high=crypto_data['High'],
#             low=crypto_data['Low'],
#             close=crypto_data['Close'],
#             name='Candlesticks',
#             increasing_line_color='blue',
#             decreasing_line_color='grey'
#         ),
#         go.Scatter(
#             x=crypto_data.index,
#             y=crypto_data['Close'].rolling(window=30).mean(),
#             name='30 Day Moving Average',
#             mode='lines'
#         )
#     ])
#     fig.update_layout(title=f'Lakshya Crypto Price Graph Analysis - {crypto_name}', 
#                       yaxis_title='Price (USD)',
#                       height=600)
#     return fig

# def display_menu(crypto_list):
#     print("\nSelect a cryptocurrency to analyze:")
#     for i, crypto in enumerate(crypto_list, 1):
#         print(f"{i}. {crypto}")
#     print("0. Exit")

# def get_user_choice(crypto_list):
#     while True:
#         try:
#             choice = int(input("Enter your choice (0-5): "))
#             if 0 <= choice <= len(crypto_list):
#                 return choice
#             else:
#                 print("Invalid choice. Please try again.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def run():
#     crypto_list = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'ADA-USD']
#     start_date = '2024-01-01'
#     end_date = dt.now().strftime("%Y-%m-%d")

#     while True:
#         display_menu(crypto_list)
#         choice = get_user_choice(crypto_list)

#         if choice == 0:
#             print("Exiting the program. Goodbye!")
#             break

#         selected_crypto = crypto_list[choice - 1]
#         print(f"\nAnalyzing {selected_crypto}...")
        
#         crypto_data = get_data(selected_crypto, start_date, end_date)
#         fig = create_graph(crypto_data, selected_crypto)
#         fig.show()

#         input("\nPress Enter to continue...")

# if __name__ == "__main__":
#     run()

















































from flask import Flask, render_template, request, jsonify
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime as dt
import json
import plotly

app = Flask(__name__)

def get_data(crypto_symbol, start_date, end_date):
    data = yf.download(crypto_symbol, start=start_date, end=end_date)
    return data

def create_graph(crypto_data, crypto_name):
    fig = go.Figure(data=[
        go.Candlestick(
            x=crypto_data.index,
            open=crypto_data['Open'],
            high=crypto_data['High'],
            low=crypto_data['Low'],
            close=crypto_data['Close'],
            name='Candlesticks',
            increasing_line_color='blue',
            decreasing_line_color='grey'
        ),
        go.Scatter(
            x=crypto_data.index,
            y=crypto_data['Close'].rolling(window=30).mean(),
            name='30 Day Moving Average',
            mode='lines'
        )
    ])
    fig.update_layout(title=f'Lakshya Crypto Price Graph Analysis - {crypto_name}', 
                      yaxis_title='Price (USD)',
                      height=600)
    return fig

@app.route('/')
def index():
    crypto_list = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'ADA-USD']
    return render_template('index.html', crypto_list=crypto_list)

@app.route('/get_graph', methods=['POST'])
def get_graph():
    crypto = request.form['crypto']
    start_date = '2024-01-01'
    end_date = dt.now().strftime("%Y-%m-%d")
    
    crypto_data = get_data(crypto, start_date, end_date)
    fig = create_graph(crypto_data, crypto)
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return jsonify(graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)
