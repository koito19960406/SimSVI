# simsvi

simulate SVI analysis in a simple way

## Installation

```bash
$ pip install simsvi
```

## Usage

The `simsvi` package allows you to simulate the seasonal variation of greenery in urban environments and calculate the Green View Index (GVI). Follow these steps to use `simsvi` in your project:

### Basic Simulation

1. **Import the SVISimulation class** from the `simsvi` package:

    ```python
    from simsvi import SVISimulation
    ```

2. **Create an instance of SVISimulation** with desired parameters:

    ```python
    simulation = SVISimulation(
        size=31,  # Size of the street
        green_max=1,  # Maximum greenery intensity
        green_min=0,  # Minimum greenery intensity
        road_width=0.5,  # Road width ratio
        tree_ratio=0.1,  # Ratio of trees
        camera_position_range=1,  # Camera position range
        hot_month=7,  # Month with maximum greenery
        cold_month=1,  # Month with minimum greenery
        tree_change=[0.1, -0.1],  # Yearly change in number of trees
        dir_plot="plots",  # Directory to save plots (set to False to disable plotting)
        seed=42  # Random seed for reproducibility
    )
    ```

3. **Run the simulation** using the `run_simulation` method:

    ```python
    simulation.run_simulation()
    ```

### Advanced Usage: Running Multiple Simulations

To run multiple simulations with different parameters concurrently, you can use the `run_multiple_simulations` function:

1. **Prepare a list of parameter dictionaries** for each simulation:

    ```python
    parameters_list = [
        {'size': 31, 'green_max': 1, 'tree_change': [0.1, -0.1], 'dir_plot': "plots", 'seed': 42},
        {'size': 31, 'green_max': 1.5, 'tree_change': [0.05, -0.05], 'dir_plot': "plots", 'seed': 43},
        # Add more parameter sets as needed
    ]
    ```

2. **Call the `run_multiple_simulations` function** with your parameters list:

    ```python
    from simsvi import run_multiple_simulations

    results = run_multiple_simulations(parameters_list)
    ```

This function will execute each set of parameters in parallel (adjust `max_workers` based on your system's capabilities) and collect the Green View Index results from each simulation.

### Visualizing Results

If `dir_plot` is set to a valid directory path, `simsvi` will save plots of the simulated environment and the Green View Index over time. These plots provide a visual representation of how greenery changes throughout the year and across different simulation parameters.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`simsvi` was created by Koichi Ito. It is licensed under the terms of the MIT license.

## Credits

`simsvi` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
