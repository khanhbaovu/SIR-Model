# SIR-Model
SIR Model for Spread of Disease

I use the SIR Model to simulate the spread of disease. We can simulate the spread of Covid 19 with its data.


𝑁  is the total population.

𝑆=𝑆(𝑡) is the number of susceptible individuals, 𝑠(𝑡)=𝑆(𝑡)/𝑁, the susceptible fraction of the population,

𝐼=𝐼(𝑡) is the number of infected individuals, 𝑖(𝑡)=𝐼(𝑡)/𝑁, the infected fraction of the population, &

𝑅=𝑅(𝑡) is the number of recovered individuals, 𝑟(𝑡)=𝑅(𝑡)/𝑁, the recovered fraction of the population.

With the constraint: 𝑠(𝑡)+𝑖(𝑡)+𝑟(𝑡)=1

The susceptible equation:
 𝑑𝑠/𝑑𝑡=−𝑏⋅𝑠(𝑡)⋅𝑖(𝑡)(1)
 
The recovered equation:
 𝑑𝑟𝑑𝑡=𝑘⋅𝑖(𝑡)
 
 The infected equations is:
  𝑑𝑖𝑑𝑡=𝑏⋅𝑠(𝑡)⋅𝑖(𝑡)−𝑘⋅𝑖(𝑡)
  
 Use the parameters  𝑏=1/2 𝑎𝑛𝑑 𝑘=1/3 , with the ICs: s(0) = 1, i(0) = 1.27 x 10-6, and r(0) = 0 and set up the to integrate the ODE model to run for 150 days, Initially take a timestep  Δ𝑡=10 days
  
