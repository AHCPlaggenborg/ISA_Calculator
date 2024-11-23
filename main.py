import math

# SL Values
g_0 = 9.80665 # [m/s^2]
R = 287.0 # [J/kg*K]
h_0 = 0 # [m]
T_0 = 288.15 # [K]
p_0 = 101325. # [Pa]
p_SL = p_0 # [Pa]
rho_0 = p_0 / (R * T_0) # [kg/m^3]
rho_SL = rho_0 # [kg/m^3]

# Lists for h and a
h_lst = [11000, 20000, 32000, 47000, 51000, 71000, 86000] # [m]
a_lst = [-0.0065, 0., 0.001, 0.0028, 0., -0.0028, -0.002] # [K/m]

print("***** ISA Calculator Troposphere *****")

# States possible choices for height
print("\n1. Calculate ISA for altitude in meters.")
print("2. Calculate ISA for altitude in feet.")
print("3. Calculate ISA for altitude in FL.")
pick = int(input("\nEnter your choice: "))

h = 0 # [m]
if pick == 1:
    h = float(input("\nEnter altitude [m]: "))
elif pick == 2:
    h = float(input("\nEnter altitude [ft]: ")) * 0.3048 # [m]
elif pick == 3:
    h = float(input("\nEnter altitude [FL]: ")) * 100 * 0.3048 # [m]
else:
    print("\nPlease opt for choice 1, 2 or 3.")

# If there were no problems with picking a choice
if h != 0:
    if h < 0 or h > 86000:
        print("\nPlease choose a height between 0 and 86,000 m.")
    else:
        for i in range(len(h_lst)):
            h_1 = min(h, h_lst[i])
            # First calculate T_1
            T_1 = T_0 + a_lst[i] * (h_1 - h_0)
            
            # Next, calculate p_1
            if a_lst[i] == 0:
                p_1 = p_0 * math.exp(-g_0 / (R * T_1) * (h_1 - h_0))
            else:
                p_1 = p_0 * (T_1 / T_0) ** (-g_0 / (a_lst[i] * R))
                
            # Next, calculate rho
            rho_1 = p_1 / (R * T_1)

            # If we haven't reached h yet
            if h > h_1:
                # Change h_1 here to h_0 for the folllowing layer, etc.
                h_0 = h_1
                T_0 = T_1
                p_0 = p_1
            else:
                # We reached h, now print the answers
                break

        # Print output
        print("\nTemperature: ", round(T_1, 2), "K (" + str(round(T_1 - 273.15, 1)), "'C)")
        print("Pressure: ", round(p_1), "Pa (" + str(round(p_1 / p_SL * 100)), "% SL)")
        print("Density: ", round(rho_1, 4), "kg/m^3 (" + str(round(rho_1 / rho_SL * 100)), "% SL)")

dummy = input("\nPress enter to end the ISA Calculator.")
