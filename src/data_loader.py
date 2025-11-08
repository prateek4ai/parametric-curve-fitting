import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Load (x, y) coordinates from CSV file.
    
    Args:
        filepath: Path to CSV file containing x, y columns
    
    Returns:
        x_data: numpy array of x coordinates
        y_data: numpy array of y coordinates
    """
    df = pd.read_csv(filepath)
    
    # Extract x and y columns
    x_dat
