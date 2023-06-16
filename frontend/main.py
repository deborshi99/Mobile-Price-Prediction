# Mobile specifications: 
#     "ram", "int_memory", "clock_speed",
#     "battery_power"
# ]

# Mobile outer_spec: [
#     fc, m_dep, mobile_wt, pc ,
#     px_height,
#     px_weight,
#     sc_h, sc_w
# ]

# Mobile_properties : [
#     'blue',
#   'dual_sim',
#   'four_g',
#   'n_cores',
#   'three_g',
#   'touch_screen',
#   'wifi',
#   'price_range'
# ]

tag = "talk-time"
label = "Longest time that a single battery charge will last"
type= "number"
f = f"""
    <p class='field required half'>
      <label class='label' for='{tag}'>{label}</label>
      <input class='text-input' id='{tag}' name='{tag}' required type='{type}'>
    </p>
"""
print(f)