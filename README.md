# Fluid-Simulator

This is a fluid simulator created from scratch in Python. In order to build this simulator, I have had to solve different problems and different methods have been implemented to obtain a proper behaviour of the particles.

## Content

I have implemented the spatial integration method of <b>Smoothed Particles Hidrodynamics</b> (SPH). This method is based on the Lagrangian formulation, where the particles move with the fluid and each particle has its own dynamic information about itself.

### Methods

Each particle contains information about its position, velocity, acceleration, density and viscosity. To find each characteristic, <b>Kernel functions</b> are needed which must be symmetric, with a finite domain, with a centred inflection and must be normalised. We have: 

- <b>Kernel Function</b>: It is used to calculate the density of the particle.
- <b>Kernel Gradient</b>: It is used to calculate the pressure of the particle.
- <b>Kernel Laplacian</b>: It is used to calculate the viscosity of the particle.

### Implementation

There are different kinds to be able to create the particles and the environment, as well as the way in which the fluid is generated. The sources that can be generated are in the form of cubes, cylinders, spheres and cones, and the inclination can be adjusted and the fluid can be generated in layers. The objects that the fluid can encounter and interact with are cubes, spheres and cones.

Hash search has been used for neighbour calculation, as it has a lower computational cost compared to other methods and optimises memory. This method divides the space into cells and each particle is assigned to its corresponding cell. In this way, in order to know the neighbours of a particle, the contiguous cells are checked.

### Results

After performing the different calculations, the most important characteristics of all the particles were saved and by means of Realflow a mesh was created and texture was applied to the fluid. Different simulations have been carried out varying some characteristics of the fluid such as the number of particles, having between 1600 to 7000 total particles.

The following link shows the simulations obtained: https://youtu.be/13Xmbq8FV_s

## Screenshots

Spiral Render
![Cylinder Render](https://github.com/BorjaSBON/Fluid-Simulator/blob/main/Screenshots/Render%20Spiral.png?raw=true)

Cylinder Render
![Cylinder Render](https://github.com/BorjaSBON/Fluid-Simulator/blob/main/Screenshots/Render%20Cylinder.png?raw=true)

Doble Cylinder Render
![Cylinder Render](https://github.com/BorjaSBON/Fluid-Simulator/blob/main/Screenshots/Render%202%20Cylinder.png?raw=true)

Sphere Render
![Cylinder Render](https://github.com/BorjaSBON/Fluid-Simulator/blob/main/Screenshots/Render%20Sphere.png?raw=true)
