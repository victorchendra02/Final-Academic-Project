import os
import pickle
import seaborn as sns
import matplotlib.pyplot as plt


def create_folder(path):
    try:
        os.makedirs(path)
        print(f"Folder --> '{path}' created")
    except FileExistsError:
        print(f"Already exist --> '{path}'")


def save_pkl(obj: any, name: str):
    """Saves an object to a pickle file, ensuring proper file extension and security.

    Args:
        obj: The object to serialize and save.
        name (str): The desired filename or path.
            - If it doesn't end with ".pkl", `.pkl` will be appended.
            - Supports relative and absolute paths.
        protocol (int, optional): The pickle protocol version to use. Defaults to the
            highest compatible with the current Python version.

    Raises:
        ValueError: If `name` is an empty string or if file operations fail.
        PickleError: If pickling encounters an error.
    """

    
    if len(name) == 0:
        raise ValueError("Filename cannot be empty")

    if not name.endswith(".pkl"):
        name += ".pkl"

    try:
        with open(name, 'wb') as file:
            pickle.dump(obj, file)
    except (OSError, IOError) as e:
        raise ValueError(f"Failed to save pickle file: {e}") from e
    except pickle.PickleError as e:
        raise pickle.PickleError(f"Pickling error: {e}") from e

    print(f"Saved: \"{name}\"")


def load_pkl(name: str):
    if len(name) == 0:
        raise ValueError("Filename cannot be empty")

    with open(name, 'rb') as file:
        return pickle.load(file)


def plot_bar_chart(labels, values, title='', x_label='', y_label='', y_range=None, bar_colors=None):
    """
    Plot a bar chart on a specified axis with given labels and values, and annotate bars with values.

    Parameters:
        labels (list of str): Labels for each bar.
        values (list of numeric): Values corresponding to each label.
        title (str): Title of the bar chart.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        y_range (tuple of int, optional): Tuple (min, max) specifying the range of the y-axis.
        bar_colors (list of str, optional): List of colors for each bar. If None, uses default colors.
    """
    if bar_colors is None:
        bar_colors = plt.get_cmap('viridis')(range(len(labels)))

    bars = plt.bar(labels, values, color=bar_colors)
    plt.title(title, fontsize=10)
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    
    # Annotate bars
    for label, value in zip(labels, values):
        plt.text(label, value + 0.5, str(value),
                 ha='center', va='bottom', fontsize=11, color='black', weight='bold')

    if y_range:
        plt.ylim(y_range[0], y_range[1])
    
    # Add a horizontal line for the highest value
    max_value = max(values)
    plt.axhline(y=max_value, color='red', linestyle='--', linewidth=1.5, label=f'Highest Value: {max_value}')

    plt.plot()
    

def plot_density_plot(data, title='', xlabel='', ylabel='Density', xlim=(-1, 11)):
    """
    Plot a density distribution (KDE) on top of a histogram on a specified axis.

    Parameters:
        data (list or array-like): Input data for the histogram and KDE.
        bins (int or sequence, optional): Specification of histogram bins. Default is 10 bins.
        title (str, optional): Title of the plot.
        xlabel (str, optional): Label for the x-axis.
        ylabel (str, optional): Label for the y-axis (default: 'Density').
    """
    
    sns.kdeplot(data, color='red', linewidth=2, shade=True)
    
    plt.xlim(xlim)
    plt.title(title, fontsize=10)
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    
    plt.plot()
    
    
def plot_histogram(ax, data, bins=10, title='', xlabel='', ylabel='Frequency'):
    """
    Plot a histogram with annotations inside each bar on a specified axis.

    Parameters:
        ax (matplotlib.axes.Axes): Axis object to draw the histogram on.
        data (list or array-like): Input data for the histogram.
        bins (int or sequence, optional): Specification of histogram bins. Default is 10 bins.
        title (str, optional): Title of the histogram plot.
        xlabel (str, optional): Label for the x-axis.
        ylabel (str, optional): Label for the y-axis (default: 'Frequency').
    """
    ax.hist(data, bins=bins, edgecolor='black')
    
    ax.set_title(title, fontsize=10)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    
    # Plot histogram and get bar properties
    counts, bin_edges, patches = ax.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    
    # Annotate bars with frequencies inside the bars
    for patch, count in zip(patches, counts):
        ax.text(patch.get_x() + patch.get_width() / 2, patch.get_height() - 0.5, str(int(count)),
                ha='center', va='top', fontsize=10, color='white', weight='bold')
