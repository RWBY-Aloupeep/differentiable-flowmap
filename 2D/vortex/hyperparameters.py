dim = 2
res_x = 64
res_y = 64
dx = 1.0 /res_y
dpi_vor = 256
reinit_every = 25
CFL = 0.5

exp_name = f"optimize_passive_16_for_8_with_obstacles"
BFECC_clamp = False
RK_number = 2
use_short_BFECC = False

adaptive_short_reinit = True
short_reinit_tau = 0.5
short_reinit_stride = 4
short_reinit_min_interval = 3
short_reinit_max_per_long_window = 3

map_reg_enabled = True
map_reg_lambda = 1e-3
map_reg_fd_eps = 1e-4
map_reg_rollout_steps = 20
map_reg_eval_every = 5
map_reg_param_group = "strengths"

act_dt = 0.01
frame_per_step = 10
total_steps = 100
sub_steps = 20
sub_iters = 30

sub_optimize=False
output_image_frame = True
add_passive_scalar = False
poisson_output_log = False
backward_u = False
add_control_force = False
viscosity = 0.0

print_time = False
