# Adaptive Flow-Map Stabilization for Differentiable Vortex-Based Fluid Simulation

**Adaptive Flow-Map Stabilization** extends differentiable vortex-based fluid simulation with stabilization mechanisms that preserve flow-map invertibility and improve long-horizon optimization reliability.

## Background
Flow-map-based differentiable fluid simulation represents advection through mappings between reference and current particle or grid coordinates, enabling efficient gradient propagation through long simulation windows. In vortex-dominated regimes, however, repeated composition of flow maps can introduce geometric distortion, Jacobian collapse, and numerical stiffness in adjoint backpropagation. These effects degrade optimization quality, especially in long-horizon control and inverse design tasks where stable gradients are essential.

## Contributions
1. **Adaptive Reinitialization**  
   We monitor distortion-sensitive diagnostics (e.g., local map deformation and Jacobian quality) during rollout. When instability increases, the simulator **reinitializes the flow-map horizon** by restarting composition from a fresh short-term reference state. This limits accumulation of numerical deformation while preserving end-to-end differentiability through segmented trajectories.

2. **Round-Trip Flow-Map Regularization**  
   We optimize simulation and control variables with an additional **round-trip consistency loss** that enforces agreement between a forward map and its inverse/return map. This regularizer discourages singular map behavior, improves local invertibility, and yields better-conditioned gradients for long-horizon optimization.

Together, these mechanisms stabilize map geometry and adjoint signals without requiring fundamental changes to the vortex-based solver architecture.

## Results
We expect the proposed stabilization strategy to provide:

- **Higher simulation stability** under strong vortical deformation and extended rollout lengths.
- **More reliable long-horizon optimization**, with fewer gradient pathologies caused by map degeneration.
- **Improved vortex control performance** in inverse and trajectory-matching tasks through better-conditioned differentiable dynamics.

## Quick Start
### 1) Environment Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install taichi torch numpy scipy matplotlib imageio
```

### 2) Run a Baseline Optimization
```bash
cd 2D/vortex
python optimize_vortex.py
```

## Acknowledgement
This project builds upon the differentiable flow-map framework proposed in:

Li et al., *An Adjoint Method for Differentiable Fluid Simulation on Flow Maps*, 
ACM SIGGRAPH Asia 2025.

## Reference

```bibtex
@inproceedings{li2025adjoint,
  year = {2025},
  title = {An Adjoint Method for Differentiable Fluid Simulation on Flow Maps},
  booktitle = {ACM SIGGRAPH Asia 2025 (Conference Track)},
  author = {Li, Zhiqi and He, Jinjin and Börcsök, Barnabás and Zhang, Taiyuan and Chen, Duowen and Du, Tao and Lin, Ming C. and Turk, Greg and Zhu, Bo}
}
