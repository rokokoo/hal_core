# icim_msgs

All of these terminals, contain a set of labels that are identical. The labels are:

| Name                    | Type | Label        |
|-------------------------|------|--------------|
| Online                  | bool | online       |
| Operational             | bool | oper         |
| Terminal initialization | bool | state_init   |
| Pre-operational         | bool | state_preop  |
| Safe-operational        | bool | state_safeop |
| Operational             | bool | state_op     |

## EL1008, 8-channel digital input terminal 24 V DC, 3 ms

This MSG type has 8 boolean values, from din_0 to din_7


```bash
rosmsg show icim_msgs/EL1008 
bool din_0
bool din_1
bool din_2
bool din_3
bool din_4
bool din_5
bool din_6
bool din_7

bool online
bool oper
bool state_init
bool state_op
bool state_preop
bool state_safeop
```

## EL2008, 8-channel digital output terminal 24 V DC, 0.5 A

Similar to EL1008, but you can change the value of the outputs.

```bash
rosmsg show icim_msgs/EL2008 
bool dout_0
bool dout_1
bool dout_2
bool dout_3
bool dout_4
bool dout_5
bool dout_6
bool dout_7

bool online
bool oper
bool state_init
bool state_op
bool state_preop
bool state_safeop
```

## EL7342, 2-channel DC motor terminal, 48 V DC, 3.5 A

There are several values in this message. This might change to multiple messages, with specific purpose.

Arrays that are labeled as `enc_*` and `srv_*` will be for [channel_1, channel_2]

```bash
rosmsg show icim_msgs/EL7342 
int32[] 	enc_count
bool[] 		enc_count_overflow
bool[] 		enc_count_underflow
bool[] 		enc_expol_stall
bool[] 		enc_in_a
bool[] 		enc_in_b
bool[] 		enc_index_ext_neg_enable
bool[] 		enc_index_ext_pos_enable
bool[] 		enc_inext
bool[] 		enc_latch_ext_valid
float64[] 	enc_pos
float64[] 	enc_pos_scale
int32[] 	enc_raw_count
int32[] 	enc_raw_latch
bool[] 		enc_reset
bool[] 		enc_set_raw_count
int32[] 	enc_set_raw_count_val
bool[] 		enc_sync_error
bool[] 		enc_tx_toggle

bool[] 		srv_absmode
float64[] 	srv_cmd
float64[] 	srv_curr_dc
float64[] 	srv_current_fb
bool[] 		srv_din1
bool[] 		srv_din2
bool[] 		srv_enable
bool[] 		srv_error
float64[] 	srv_max_dc
float64[] 	serv_min_dc
bool[] 		srv_move_neg
bool[] 		srv_move_pos
float64[] 	srv_offset
int32[] 	srv_raw_cmd
int32[] 	srv_raw_info1
int32[] 	srv_raw_info2
bool[] 		srv_ready
bool[] 		srv_ready_to_enable
bool[] 		srv_reduce_torque
bool[] 		srv_reset
float64[] 	srv_scale
uint32[] 	srv_sel_info1
uint32[] 	srv_sel_info2
bool[] 		srv_sync_error
bool[] 		srv_torque_reduced
bool[] 		srv_tx_toggle
bool[] 		srv_warning

bool online
bool oper
bool state_init
bool state_op
bool state_preop
bool state_safeop
```

## EK9576, Brake chopper terminal

```bash
rosmsg show icim_msgs/EL9576 
bool overload
bool power_ok

bool online
bool oper
bool state_init
bool state_op
bool state_preop
bool state_safeop
```