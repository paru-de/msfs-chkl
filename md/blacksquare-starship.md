AircraftName: Beechcraft Starship (Blacksquare)
AdaptedFrom: https://downloads.justflight.com/products/JFF003744/BKSQ_StarshipManual.pdf https://flightsim.to/file/94821/beech-starship-procedures-and-checklist

- (Note) WORK IN PROGRESS: TYPOS, PICTURES, FMC FLOW

# Cockpit preparations

## Preflight

- (Tablet) Payload → Set Fuel/Payload
- (Tablet) MSFS EFB → Load flightplan
- Parking Brake: SET
- Control Locks: REMOVE
- Landing Gear: DOWN
- Battery: ON
- Pitch/Roll/Rudder Trim: NEUTRAL
- Fuel Qty: CHECK
- Oxygen Pressure: CHECK
- Airstair Door Annunciator: CHECK
- Battery: OFF
- Chocks: REMOVED
- Pitot/Static Covers: REMOVED
- Engine Covers: REMOVED
- Gear Locking Pins: REMOVED
- Emergency Exit: SECURE
- Airstair door: LOCKED

## Before Starting Engine

- Circuit Breakers (L/R/AUX): ALL IN
- Outboard Reversionary Panels: AS REQ
- Parking Brake: SET
- Audio Panels: AS REQ
- Static Source: NORM
- Oxygen Supply: PULL
- Oxygen Masks: TEST
- Ice Protection: OFF
- Landing Gear: DOWN
- Anti-Skid Switch: ANTI-SKID
- Center Reversionary Panel: AS REQ
- Standby Instruments: ON
- STANDBY BATT PWR ON Annunciator: ILLUMINATED
- Power Levers: IDLE
- Propeller Levers: FULL FWD
- Condition Levers: FUEL CUTOFF
- Bleed Air Valves: OFF
- Temp Mode: OFF

### Sys Tests

- Battery: ON
- Triple-Fed BUS Volts: 22V MIN
- Center BUS Volts: 23V Min
- EICAS: ON
- Firewall Fuel Valves: PUSH CLOSED
- Extinguisher and F/W Valve: ILLUMINATED
- Standby Pumps: ON
- Fuel Press LO Annunciators: ILLUMINATED
- Firewall Fuel Valves: PUSH OPEN
- Extinguisher and F/W Valve: EXTINGUISHED
- Fuel Press LO Annunciators: EXTINGUISHED
- Standby Pumps: OFF
- Fuel Press LO Annunciators: ILLUMINATED
- Transfer Flow: LEFT & RIGHT
- FUEL TRANSFER Msg: ILLUMINATED
- Fuel Press LO Annunciator: EXTINGUISHED
- Transfer Flow: OFF
- AvIONIC AIR FAIL Msg: ILLUMINATED
- Avionics Alternate Blower: ON
- AV ALT BLWR ON Msg: ILLUMINATED
- AVIONIC AIR FAIL Msg: EXTINGUISHED
- Avionics Alternate Blower: OFF
- Fuel Qty: CHECK
- Oxygen Pressure: CONFIRM
- Lights: AS REQ

# Engine Start

## Engine Start (BAT)

- (Note) Right Engine first, then Left Engine
- Strobes: LOW
- R/L Ignition and Engine Start: ON
- R/L Condition Lever (12% N1 min): START
- R/L N1 and ITT (1000C max): MONITOR
- R/L Oil Pressure: CONFIRM RISING ELSE ABORT
- R/L Ignition and Engine Start: OFF
- R/L Condition Lever (65% N1 min): RUN
- R/L Generator: RESET; ON
- R/L Volts: 27.5-29V
- Charge Battery until: LOADMETER < 50%
- (Note) Repeat for second Engine
- Gen Ties: OPEN
- L/R GEN TIES OPEN Msg: ILLUMINATED
- Triple-Fed BUS Volts: 26.5-28V
- Gen Ties: NORM
- L/R GEN TIES OPEN Msg: EXTINGUISHED
- Generator Load: PARALLELED

## Engine Start (External Power)

- (Note) Right Engine first, then Left Engine
- Strobes: LOW
- Battery Volts: 20V MIN
- Propeller Levers: FEATHER
- EICAS Pilot and Copilot Avionics: OFF
- L/R GEN: OFF
- Battery: ON
- External Power Source: CONNECT
- EXT PWR Volts: 28-28.4V
- EXT PWR Switch: ON
- EICAS: ON
- R/L Ignition and Engine Start: ON
- R/L Condition Lever (12% N1 min): START
- R/L N1 and ITT (1000C max): MONITOR
- R/L Oil Pressure: CONFIRM RISING ELSE ABORT
- R/L Ignition and Engine Start: OFF
- R/L Condition Lever (65% N1 min): RUN
- (Note) Repeat for second Engine
- EXT PWR: OFF
- External Power Source: DISCONNECT
- R/L Generator: RESET; ON
- R/L Volts: 27.5-29V
- Gen Ties: NORM
- L/R GEN TIES OPEN Msg: EXTINGUISHED
- Generator Load: PARALLELED
- Propeller Levers: FULL FWD

# Taxi, Takeoff

- (ATC) Request Clearance (IFR)

## Before Taxi

- Pilot and Copilot Avionics: ON
- Standby Indicators: ON
- Bleed Air Valves: BOTH
- Blowers/Temperatur: SET
- Temp Mode Selector: AUTO
- Lights: AS REQ
- Cabin Lights: AS REQ
- NO SMOKE/SEATBELTS: ON
- Flight Controls: VERIFY FREE MOV
- Flap/FWD Wing: RETRACT
- AHRS ALIGNING Msg: EXTINGUISHED
- CDU Time and Date Position: VERIFY
- Radar: STANDBY
- Brakes: CHECKED
- CAS: VERIFY / AFX OFF ONLY
- Altimeter: SET LOCAL
- Heading: SET RWY HDG
- CDU: INIT
- MSG: CHECK
- Squawk: SET
- Transponder: STBY
- Nav Radios: AS REQ
- Altitude: SET INITIAL CLEARANCE
- Pitch/Roll/Rudder Trims: TO
- Inertial Separators: MAIN; AS REQ

### Flight Plan

- (Tablet) MSFS EFB → Send to Avionics
- (MCDU) FLP → VERIFY RTE
- (MCDU) VNAV → SET AS REQ
- (MCDU) SYS CTRL → VERIFY NAV SOURCE

### Taxi

- (ATC) Request Taxi Clearance
- Taxi Lights: ON
- Parking Brake: OFF

## Before Takeoff (Abbreviated)

- Parking Brake: SET
- Annunciators: PUSH TO TEST
- Surface Deice / Ice Protection: AS REQ
- Pressurization Altitude: 1000FT ABOVE CRZ
- Rate Knob: 10 O'CLOCK
- Manual Cabin Alt Control: NORM (FULL CCW)
- Avionics: CHECK AND SET
- AP: ENGAGE
- AP: YOKE D/C
- Pitch/Roll/Rudder Trims: VERIFY TO
- Flap/FWD WING: TO; AS REQ
- Autofeather: ARMED
- Altimeter: SET
- Standby Altimeter: SET
- Flight and Engine Displays: CHECK
- Stall Warning Heat: ON
- Pitot/Static Heat: ON
- Engine Ice Protection: AS REQ
- Vent/Cable Heat: ON
- Windshield Heat: LOW
- Bleed Air Valves: VERIFY BOTH
- Transponder: ON
- CAS: VERIFY; CONSIDER
- Engine Auto-Ignition: AS REQ
- Generator Loads: CHECK
- Pitch/Roll/Rudder Trims: CENTERED/GREEN
- (ATC) Request Departure Clearance
- Strobe: ANTI-COLL

# Takeoff, Climb, Cruise

## Takeoff

- Brakes: HOLD
- (Note) Takeoff Power: 100% TRQ, 850 ITT, 1700 RPM
- AFX Msg: ILLUMINATED ON EICAS
- Brakes: Release
- VR No Flaps: 106 - 108 KIAS
- VR Flaps: 91-101 KIAS
- VR Speed: ROTATE TO 8 DEGREES

### Takeoff Speeds Reference

- VFE (max Flaps): 180 KIAS
- VLE/VLO (max Gear): 200 KIAS
- VXSE (single engine best angle): 115 KIAS
- VYSE (single engine best rate): SL 130 KIAS; -0.55/1000ft
- VX (two engine best angle): 115 KIAS
- VY (two engine best rate): SL 140 KIAS; -0.55/1000ft

### Positive Rate of Climb

- Landing Gear: UP

## Climb

- (Altitude) 400FT
- Flap/FWD Wing: RETRACT
- Yaw Damper: ON
- (Note) Climb Power: 90% TRQ, 840 ITT, 1600 RPM
- Propeller Sync: ON
- (Note) Accelerate to desired climb speed

### Climb Speeds Reference

- Max Rate: BLUE LINE + 10
- B FL100: 180 KIAS
- B FL200: 160 KIAS
- B FL300: 140 KIAS
- A FL300: 130 KIAS

### Climb (contd)

- Engine Display: MONITOR
- Cabin Pressurization: MONITOR
- (Altitude) TRANSITION ALTITUDE
- Altimeter: SET STD
- (Altitude) FL100
- Seatbelts: OFF
- Lights: OFF
- Inertial Separators: AS REQ
- Anti-Ice: AS REQ
- Engine Auto Ignition: AS REQ

## Cruise

- (Note) Cruise Climb Power: 97% TRQ, 840 ITT, 1600 RPM
- (Note) Cruise Power: Keep ITT below 840!
- AFX: OFF
- Engine Display: MONITOR
- Fuel QTY: MONITOR

# Descent, Approach

## Descent

- (Note) Normal Descent profile: 4 Degrees!
- (Note) 4 Degree Formula (nm): (CRZ Alt - Target Alt) / 1000 x 2.5 + 10-15
- (Note) → Remove 0's from delta, times 2 + half of that + buffer

### 50nm before TOD

- Approach: CHECK; REFER TO CHARTS
- (MCDU) VNAV → Set faf altitude (ILS); Set MDA (RNAV)
- ILS Frequency: VERIFY & SET
- Minimums: SET
- Target Altitude (faf/MDA): SET
- Target VS (AP VS): SET

### ToD

- (ATC) Clearance received
- AP DESCEND or VS: ON
- Speed: MONITOR; ADJUST PWR
- Pressurization Altitude: 500FT ABOVE LANDING
- Rate Knob: AS REQ
- (Altitude) FL100
- Seatbelts: ON
- Lights: ON
- Inertial Separators: MAIN; AS REQ
- Anti-Ice: AS REQ
- Engine Auto Ignition: AS REQ
- AFX: ARMED
- ILS Frequency: CONFIRM
- Terrain: ON; AS REQ
- (Altitude) TRANSITION ALTITUDE
- Altimeter: SET LOCAL

## Approach

### Approach Speed Reference

- VREF: 107-121 KIAS
- VLE/VLO (max Gear): 200 KIAS
- VFE (max Flaps): 180 KIAS

## Landing

### Localizer Intercept

- Speed: 150-160 KIAS
- Heading: SYNC
- AP HDG: ON
- (MCDU) Nav Source: VOR
- CRS: SET RWY HDG
- AP APPR: ON
- FMA LOC; GS: VERIFY ARMED

### Glide Slope Intercept

- Flaps: DOWN
- Landing Gear: DOWN
- Propeller Sync: OFF
- AFX: VERIFY ARMED
- Speed: VREF + 10 KIAS
- Propeller Lever: MAX RPM
- (Altitude) Before or at 200ft
- AP: OFF
- Yaw Damper: OFF
- (Altitude) 50FT
- Power Levers: IDLE
- (Altitude) 10FT
- Flare: 3-5 DEGREE
- (Altitude) TOUCHDOWN
- Power Levers: BETA RANGE; REV AS REQ

## Go Around

- Power Levers: 100% TQ
- GO-AROUND Button: PUSH
- VREF: ROTATE; MAINTAIN
- Flaps: UP
- Landing Gear: UP
- Yaw Damper: ON

# Shutdown

## Taxi

- (ATC) Report vacated
- Lights: OFF
- Strobe: LOW; ANTI-COLL OFF
- Taxi Lights: ON
- Flaps: UP
- Radar: OFF
- Transponder: STBY
- AFX: OFF
- Engine Auto Ignition: OFF
- Stall Warning Heat: OFF
- Pitot/Static Heat: OFF
- Inertial Separators: AS REQ
- Vent Cable Heat: OFF
- Windshield Heat: OFF

## Parking / Shutdown

- Parking Brake: SET
- Taxi Light: OFF
- Oxygen Supply: PUSH IN
- Inertial Separators: OFF
- Anti-Ice: ALL OFF
- Pilot and Copilot Avionics: OFF
- Standby Instruments: OFF
- Bleed Air Valves: OFF
- Temp Mode: OFF
- Battery: CHARGED

### ITT at minimum for at least one minute

- Condition levers: FUEL CUT-OFF
- Propeller Levers: FEATHERED
- Cabin Lights: ALL OFF
- EICAS: OFF
- Battery: OFF
- Generators: OFF
- Control Lock: INSTALL
- Chocks: INSTALL
- Covers: INSTALL
