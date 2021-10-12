# 2-channel DC motor terminal, 48 V DC, 3.5 A

## Encoder [0,1]
int32[] enc_count
bool[] enc_count_overflow
bool[] enc_count_underflow
bool[] enc_expol_stall
bool[] enc_in_a
bool[] enc_in_b
bool[] enc_index_ext_neg_enable
bool[] enc_index_ext_pos_enable
bool[] enc_inext
bool[] enc_latch_ext_valid

float64[] enc_pos
float64[] enc_pos_scale

int32[] enc_raw_count
int32[] enc_raw_latch
bool[] enc_reset
bool[] enc_set_raw_count
int32[] enc_set_raw_count_val

bool[] enc_sync_error
bool[] enc_tx_toggle

# Server/Service? [0,1]
bool[] srv_absmode
float64[] srv_cmd
float64[] srv_curr_dc
float64[] srv_current_fb
bool[] srv_din1
bool[] srv_din2
bool[] srv_enable
bool[] srv_error
float64[] srv_max_dc
float64[] serv_min_dc
bool[] srv_move_neg
bool[] srv_move_pos
float64[] srv_offset
int32[] srv_raw_cmd
int32[] srv_raw_info1
int32[] srv_raw_info2
bool[] srv_ready
bool[] srv_ready_to_enable
bool[] srv_reduce_torque
bool[] srv_reset
float64[] srv_scale
uint32[] srv_sel_info1
uint32[] srv_sel_info2
bool[] srv_sync_error
bool[] srv_torque_reduced
bool[] srv_tx_toggle
bool[] srv_warning

# General information
bool online
bool oper
bool state_init
bool state_op
bool state_preop
bool state_safeop