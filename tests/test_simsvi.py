import pytest
from simsvi import SVISimulation  # Assuming your class is saved in svi_simulation.py
import numpy as np
import os

def test_initialization():
    sim = SVISimulation(seed=123)
    assert sim.size == 31
    assert sim.seed == 123
    # Add more assertions for other default values or overridden values

def test_create_scenario():
    sim = SVISimulation(tree_min=10, tree_max=10, seed=123)  # Fixed number of trees for predictability
    sim.create_scenario()
    assert len(sim.tree_position) == 10  # Ensure the correct number of trees were created
    # Further tests could check tree positions are within bounds, but randomness makes this complex

def test_get_greenery():
    # This test would require setting up a known scenario where the greenery calculation is predictable
    pass

def test_update_scenario():
    sim = SVISimulation(seed=123)
    sim.month = 6  # Set to a month known to influence greenery values
    sim.update_scenario()
    # Verify that greenery values are updated as expected
    pass

def test_update_tree_position():
    sim = SVISimulation(tree_change=[0.1], seed=123)
    initial_positions = sim.tree_position.copy()
    sim.update_tree_position()
    # Check if tree positions have changed as expected
    pass

def test_run_simulation():
    sim = SVISimulation(seed=123)
    sim.run_simulation()
    assert len(sim.greenery_dict_list) > 0  # Ensure the simulation results are populated

def test_plot_scenario(tmp_path):
    sim = SVISimulation(dir_plot=str(tmp_path), seed=123)
    sim.plot_scenario()
    assert len(os.listdir(tmp_path)) > 0  # Check if a plot file was created in the temp directory
