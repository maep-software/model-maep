''' MAEP Planning model 

e-mail: maep5600@gmail.com
Universidad de los Andes
Bogotá - Colombia

Licence MIT
'''

# packages
import timeit
from scripts import run_model

# import sys
# sys.stdout = open('output_console', 'w')

# simulation time
start = timeit.default_timer()

#==============================================================================

# Parameters simulation
file = '01_example_hydrothermal'       # input file name (DataSystem location)

class Param:
    
    max_iter = 4              # Maximun number of iterations
    bnd_stages = 4            # Boundary stages
    stages = 6 + bnd_stages  # planning horizon: (months + bundary months)
    seriesBack = 1            # scenarios for the backward phase
    seriesForw = 1            # scenarios the forward phase
    
    # Parameters analysis
    sensDem =  1.0      # Demand factor
    eps_area = 0.05       # Short-term - significance level area
    eps_all = 0.05        # Short-term - significance level for the whole system
    eps_risk = 0.15       # long-term risk
    commit = 0.0         # risk-measure comminment
    
    # Stages-horizon analysis (stages)
    horizon = "monthly"       # "monthly","weekly","daily" (weekly models are inconclusive)
    
    # read data options
    read_data = True         # read the input file
    param_calc = True         # parameters calculation
    
    # transmission network
    param_opf = False           # OPF model
    flow_gates = False          # Security constraints (inefficient calculation - inconclusive)
    
    # Short-term analysis
    short_term = False          # All short-term models are ignored
    
    # Short-term models
    # Dist-free: [P-efficient points, MVE method]
    dist_f = [False,False]        # Free distribution model (NO portfolio operation)
    dist_samples = 18             # sample for p-efficient points calculation
    # renewables additional models (ONLY for wind power integration)
    wind_aprox = False            # Distribution form assupmtions
    wind_model2 = False          # Second model of wind plants (inconcluse)
    
    # portfolio operation
    portfolio = [True,False]     # [storage-network, storage-wind]
                                 # [False,False] will be turn [True,False], [True,True] option is inconclusive
    # emissions
    emissions = False         # ObjectiveFunction - emissions costs
    emss_curve = False        # emissions curve calculation 
    thermal_co2 = [1, 1]      # Emission factor type selection [tech:Ton/Mwh, Fuel:MBTU/MWh]  
    ccs_tech = False          # Carbon capture and storage technology
    
    # operation model options
    policy = True            # algorithm: backward and forward 
    simulation = True        # algorithm: only forward (it needs cost-to-go function)
    parallel = False          # parallelization module (inconcluse)

    # PRINT ORDER:  
    results = True          # Print main variables 

    # reports
    curves = [True,          # 1. dispatch curves
              True,          # 2. marginal cost
              [False,3],     # 3. Hydro generation scenarios, Number of plant
              False,         # 4. Wind/Renewables generation scenarios
              [False,10],     # 5. Charge and discharge of storage systems, stage to graph
              False,         # 6. Transfer of energy (requieres areas setting)
              False]          # 7. Emissions

#==============================================================================
# run model
run_model.execution(Param, file)
              
#==============================================================================

# print execution time
end = timeit.default_timer()
print(end - start)
