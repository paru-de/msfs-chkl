AircraftName:Fenix Airbus A32x
AdaptedFrom: https://flightsim.to/file/90077/fenix-a319-a320-a321-essential-checklist

# Cockpit Preparations

## Power Up & Overhead

- (Tablet) Fenix → My Flight → Import from Simbrief

### Verify

- WX Radar (SYS): OFF
- Predictive Wind Shear (PWS): OFF
- WX Mode knob: WX+T+HZD
- Gain knob: CAL
- Ground Clutter Suppression (GCS): AUTO
- ENG Master 1/2: OFF
- ENG Mode Selector: NORM
- Landing Gear: DOWN
- Wipers 1/2: OFF

### Power Up

- BAT 1/2: ON
- EXT PWR (if available): ON
- (Note) Wait for boot-up and self-checks to be completed (three clicks)
- APU Master: ON
- APU Start (3sec after Master): ON
- APU Bleed (AVAIL): ON
- EXT PWR: OFF
- ADIRS: NAV x3

## Boarding & Refuel, Flight Plan

### MCDU and EFB setup

- (MCDU) ATSU → AOC → FLT INIT → INIT DATA REQ
- (MCDU) INIT → INIT RQUEST → Enter ATC FLT NBR
- (Tablet) Fenix → MASS AND BALANCE → LOAD AIRCRAFT

### Overhead panel

- NAV & LOGO Lights: ON (1 or 2)
- Fuel Pumps: ALL ON
- Oxygen Crew: ON
- GND CTL: ON
- CVR TEST: PUSH
- Emergency Exit Lights: ARMED
- No Smoking: AUTO
- Seat Belts: ON

### Flight plan setup

- (ATC) Request Clearance (IFR)
- (MCDU) INIT → Enter CI → Enter CRZ FL → WIND → WIND Request
- (MCDU) F-PLN → Select DEP RW/SID/TRANS → TMPY INSERT
- (MCDU) SEC F-PLN → COPY ACTIVE
- (MCDU) F-PLN → Select ARR RWY/STAR/TRANS → TMPY INSERT
- CSTR: ON
- NAV display mode PLAN: VERIFY RTE
- Squawk: SET

### Performance calculations

- (MCDU) INIT P2 → Enter ZFW/ZFWCG → FUEL PLANNING → Confirm BLOCK
- (Note) Confirm Boarding and Refueling has finished
- (Tablet) Fenix → MASS AND BALANCE → SEND TO MCDU
- (MCDU) MENU → ATSU → AOC → RCVD MSFS → LOADSHEET (latest) → ACCEPT
- (MCDU) Departure Perf → SYNC LOADSHEET → SYNC LIVE WX → Set config → CALCULATE → SEND TO MCDU

### Seven Segment Display

- Altimeter: SET LOCALE
- Flight Director: ON x2
- HDG: DASHED
- Altitude: SET INITIAL CLEARANCE

# Push & Taxi, Line-up and Takeoff

## Push

### Prepare Push

- Transponder: AUTO
- Beacon: ON
- Thrust: IDLE
- APU Bleed: VERIFY on

### Push and Engine start

- (ATC) Request Push and Engine Start
- (ATC) OnAir Company: Start tracking
- Ground Crew: ADVICE
- Parking Brake: OFF
- ENG Mode: IGN/START
- ENG Master 1/2: ON
- ENG Status: VERIFY AVAIL
- ENG Mode: NORM
- Pushback Completed: VERIFY
- Parking Brake: SET

## Before Taxi

- APU Bleed: OFF
- APU Master: OFF
- ENG A/I: AS REQ
- Autobrake: ARMED MAX
- Ground Spoilers: ARMED
- RUD TRIM: PUSH RESET
- Flaps: TO
- Trim: TO
- (ATC) Request Taxi Clearance
- Nose Light: TAXI
- RWY TURN OFF Lights: AS REQ
- Transponder / TCAS: AUTO / ABV

## Line-up and Takeoff

- (ATC) Request Clearance
- PACKS 1/2: OFF
- ENG A/I: AS REQ
- Cabin: ADVICE
- Transponder: TA
- Strobe: ON
- ENG Mode: AS REQ
- Terrain: ON
- WX (SYS): ON
- Wind shear (PWS): ON
- TO Config Button: PUSH & CONFIRM
- Landing Lights: ON
- Nose Lights: TO

# After Takeoff, Climb, Cruise

## After Takeoff

### Positive Rate of Climb

- Landing Gear: UP
- Thrust Levers: CLB (when flashing)
- Flaps: UP 1 at S
- AP1: ENGAGE AS REQ
- Ground Spoilers: DISARM
- PACK 1/2: ON
- ENG A/I: AS REQ
- RWY TURN OFF Lights: OFF
- ENG Mode: NORM
- Transponder / TCAS: TA/RA; ABV

### Climb

- (Altitude) TRANSITION ALTITUDE
- Altimeter: STD
- PACKS 1/2 ON: VERIFY
- (Altitude) FL100
- Landing Lights: OFF & RETRACT
- Nose Light: OFF
- Seatbelts: OFF
- Terrain: OFF

### Cruise

- TCAS: ALL
- Step Climbs (LR/Neo): CHECK OFP

# Descent

## Before Top of Descent

### Landing calculations

- (MCDU) INIT → WIND → WIND REQUEST → WIND → UPLINK INSERT
- (Tablet) Arrival Perf → Refresh METAR
- (MCDU) FUEL PRED → DEST EFOB - FOB → Subtract difference from GW
- (Tablet) Arrival Perf → Set LANDING WT → Set Landing Config → Calculate and confirm landing distance

### Landing setup

- (MCDU) F-PLN → ARR RUNWAY → STAR → TRANS → TMPY INSERT
- (MCDU) PERF P3 → Enter QNH, TEMP, WINDS, TRANS FL, BARO/RADIO, LDG CONF
- Autobrake: SET
- Altimeter: PRE-SELECT LOCAL
- (Note) If LDG CONF 3: GPWS OVERHEAD PANEL → LDG FLAP 3 ON

### Descent

- (ATC) Clearance received
- Altitude: SET; MANAGED
- Speed: MANAGED
- ENG A/I: AS REQ
- TCAS: BLW
- (Altitude) FL150
- Seatbelts: ON
- (Altitude) FL100
- Landing Lights: ON
- Nose Lights: ON
- Terrain: ON
- ENG Mode: AS REQ
- LS (ILS): ON
- (Altitude) TRANSITION ALTITUDE
- Altimeter: SWITCH LOCAL

# Approach

## ILS

### Decel point

- (MCDU) PERF → APPR → Activate → Confirm
- Altitude: MANAGED
- LS: VERIFY ON

### 3-5nm PRIOR FAF

- Flaps: 1
- (Note) Wait for Speed S
- (ATC) Clearance received
- LOC and GS: CONFIRM ACTIVE
- APPR: ON
- AP2: ON

### LOC and GS captured

- Altitude: SET MISSED
- Flaps: 2
- Landing Gear: DOWN
- Flaps: LANDING
- Ground Spoilers: ARMED
- (Altitude) 300ft
- AP (when not autolanding): OFF
- (Altitude) 30ft
- Begin Flare: 2-3 DEGREES
- (Altitude) 20ft
- Thrust: RETARD: IDLE
- Flare: HOLD
- (Altitude) TOUCHDOWN
- Thrust: REV AS REQ
- AP: OFF

## Go Around

- Thrust: TO/GA
- Pitch: ROTATE
- (ATC) Advice
- Flaps: ONE UP
- Landing Gear: UP
- HDG, AP: AS REQ
- Thrust: CLB
- F Speed: FLAPS 1
- S Speed: FLAPS UP
- Ground Spoilers: DISARM
- RWY TURN OFF Lights: OFF

# Shutdown

## Taxi

- (ATC) Report vacated
- Strobe: OFF
- Landing Lights: OFF & RETRACTED
- Nose Light: OFF
- Flaps: UP
- Ground Spoilers: VERIFY DISARM
- Terrain: OFF
- WX (SYS): OFF
- Wind shear (PWS): OFF
- ENG A/I: AS REQ
- APU Master: ON
- APU Start (3sec after Master): ON

## At Parking / Gate

### Deboarding

- Parking Brake: SET
- RWY TURN OFF Lights: OFF
- ENG A/I: OFF
- APU Bleed (AVAIL): ON
- Seatbelts: OFF
- ENG Master 1/2: OFF
- Beacon: OFF
- Fuel Pumps: ALL OFF
- TransponderL STBY
- (Note) Request Deboarding

### Shutdown

- EXT PWR: ON if AVAIL
- APU Bleed: OFF with EXT PWR
- APU Master: OFF with EXT PWR
- Oxygen Crew: OFF
- ADIRS: OFF x3
- Exterior Lights: ALL OFF
- No Smoking: OFF
- Emergency Lights: OFF
- APU Bleed: OFF
- APU Master: OFF
- BAT 1/2: OFF
- EXT PWR: OFF
