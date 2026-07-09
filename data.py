import yfinance as yf
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
SRC_DIR = Path(__file__).resolve().parent


def get_data(ticker="SPY", start="2000-01-01", end="2025-12-31"):
    csv_path = DATA_DIR / "spy_data.csv"
    
    if csv_path.exists():
        data = pd.read_csv(csv_path, index_col=0, parse_dates=True)
        return data
    

    else:

        data = yf.download(ticker, start, end)

        data.columns = data.columns.droplevel(1) # type: ignore


        
   
        data['returns']= data['Close'].pct_change() # type: ignore
        data['returns_shift(next_day_returns)']= data['returns'].shift() # type: ignore
        # data['returns(*100)']= data['Close'].pct_change()*100 # type: ignore
        data.dropna(inplace=True) # type: ignore
        
        data.index.name= 'date'  # type: ignore


    
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    data.to_csv(csv_path) # type: ignore
    return data





