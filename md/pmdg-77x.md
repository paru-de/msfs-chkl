AircraftName:PMDG Boeing 77X
AdaptedFrom: https://flightsim.to/file/76906/pmdg-boeing-777-checklist-procedures https://flightsim.to/file/77321/pmdg-777-300er-checklist

# Cockpit preparations

## Power Up

- Battery Switch: ON
- NAV Lights: ON
- Wipers: OFF
- Landing Gear: DOWN
- Parking Brake: SET
- Throttle: IDLE
- EXT PWR Primary/Secondary: ON
- ADIRU: ON
- IFE/CABIN Utility: ON
- APU: ON then START
- Emergency Lights: ARMED & GUARDED
- Window Heat: ON
- No Smoking: ON
- Seatbelts: AUTO

## Boarding & Refuel, Flight Plan

- (Note) Start Boarding & Refueling

### FMC Setup

- (Tablet) Import Simbrief route & weather
- (MCDU) FMC → Set Inertial Pos
- (MCDU) RTE → Route Request → Simbrief RTE → Set Payload → Set Fuel
- (MCDU) (contd) Select RTE → Load → Activate → EXEC
- (MCDU) (contd) Select PERF INIT → Accept → Verify CRZ ALT → Click ZFW twice
- (MCDU) LEGS → RTE Data → Load → EXEC
- (ATC) ATC: Request Departure Clearance (IFR)
- (MCDU) DEP/ARR → Set RWY → Set SID/TRANS → EXEC
- (MCDU) DEP/ARR → INDEX → ARR → Set RWY → Set STAR/TRANS → EXEC
- NAV display mode PLAN: VERIFY RTE
- (MCDU) LEG → STEP
- (MCDU) VNAV P3 → Forecast → Load
-

### Performance Calculation

- (Tablet) Performance Tool → Calculate Departure with desired config
- (MCDU) RTE → Takeoff → Set Flaps → Click CG twice
- (MCDU) THRUST LIMIT → Set SEL TEMP → Set TO Derate
- (MCDU) Takeoff → Set V1, VR, V2
- Stab Trim: SET TO

### Glareshield

- Altimeter: SET LOCAL
- Flight Director: ON x2
- Speed: V2+10
- LNAV: ARMED
- VNAV: ARMED
- HDG: RWY HDG
- Altitude: SET INITIAL CLEARANCE
- Autobrake: RTO
- EICAS: RECALL & VERIFY
- Thrust: IDLE
- Squawk: SET
- CHKL Pre-flight: COMPLETE

- (Note) Boarding & Refueling completed

# Push and Taxi

## Push

- (ATC) ATC: Request Push and Engine Start
- (Note) OnAir Company: Start tracking

### Preparation

- Ground Crew: ADVICE
- APU: VERIFY ON
- EXT POWER: OFF
- Hydraulic C1/C2: ON
- Hydraulic Switches: ALL AUTO
- Fuel Pumps: L/R ON, CENTER AS ADV
- Beacon: ON
- Transponder: XPNDR
- Doors: CLOSED & ARMED
- CHKL Before Start: COMPLETE

### Push and Engine Start

- Lower Center DIsplay: ENG PAGE
- Parking Brake: OFF
- ENG L/R: START
- Fuel Control 1/2: RUN
- Oil Pressure: VERIFY RISING ELSE ABORT
- Pushback Completed: VERIFY
- Parking Brake: SET

### Before Taxi

- APU: OFF
- ENG A/I: AUTO
- Flaps: TO
- Flight Controls: CHECK
- EICAS: RECALL & VERIFY
- (ATC) Request Taxi
- CHKL Before Taxi: COMPLETE
- Taxi Lights: ON
- Seatbelts: ON
-

# Line-up and Takeoff

## Before Takeoff

- Autobrake: VERIFY RTO
- Flaps: VERIFY TO
- Transponder / TCAS: TA/RA
- WX Radar: ON
- Terrain: AS REQ
- A/T: ARMED
- TO/GA: ARMED
- Cabin: ADVICE
- CHKL Before Takeoff: COMPLETE

## Line-up and Takeoff

- (ATC) Request Clearance
- Landing Lights: ON
- RWY TURNOFF Lights: ON
- Logo / Wing Lights: AS REQ
- Strobe: ON
- (Note) Line up and Hold Brake
- Throttle: 55% N1
- Brakes: RELEASE
- Airspeed alive: PITCH DOWN
- 80knts: RELEASE YOKE
- VR: ROTATE

# After Takeoff, Climb, Cruise

## Positive Rate of Climb

- Landing Gear: UP
- Flaps: UP AS ADV
- Taxi Lights: OFF
- RWY TURNOFF Lights: OFF
- AP: ENGAGE AS REQ
- Autobrake: VERIFY OFF
- CHKL After Takeoff: COMPLETE

## Climb

- (Altitude) TRANSITION ALTITUDE
- Altimeter: STD
- (Altitude) FL100
- Landing Lights: OFF
- Seatbelts: OFF
- WX: AS REQ
- Terrain: OFF

## Cruise

- HDG: SET
- Step Climbs: CHECK OFP / VNAV

# Descent

## Before Top Of Descent

### Landing Calculations

- (Tablet) Performance Arrival Enroute → Calculate with desired config
- (MCDU) Lower center display → COMM → Request METAR
- (MCDU) INIT REF → Select Landing Flaps and Vref

### Landing setup

- (MCDU) DEP/ARR → ARR RUNWAY → STAR → TRANS → Confirm or set
- (Tablet) NAV RAD → Confirm
- Autobrake: SET
- Altimeter: PRE-SELECT LOCAL
- Altitude (as instructed by ATC or restriction): PRE-SELECT
- CHKL Descent: COMPLETE

### Descent

- (ATC) Clearance received
- Altitude: VERIFY
- (Altitude) FL200
- Seatbelts: ON
- (Altitude) FL100
- Speed: VERIFY 250 KIAS
- Landing Lights: ON
- Terrain: ON
- (Altitude) TRANSITION ALTITUDE
- Altimeter: SWITCH LOCALE
- CHKL Approach: CALL

# Approach

## ILS

### Flaps Reference

- Flaps 1: AT/ABV UP
- Flaps 5: AT/ABV 1
- Flaps 15: AT/ABV 5
- Flaps 20: AT/ABV 15
- Flaps Landing: VREF + WIND (if unknown use +5knts

### 5-8nm PRIOR FAF

- LOC: ARMED
- APP: ARMED WHEN LOC CAPTURED
- Flaps: 15
- (ATC) Clearance received

### FAF

- Speed: VREF
- LOC and GS: CONFIRM ACTIVE
- Flaps: LANDING
- Speed Brake: ARMED
- Landing Gear: DOWN
- Altitude: SET MISSED
- CHKL Landing: COMPLETE
- (Altitude) 300ft
- AP (when not auto-landing): OFF
- (Altitude) 30ft
- Begin Flare: 2-3 DEGREES
- (Altitude) 20ft
- Thrust: IDLE
- Flare: HOLD
- (Altitude) TOUCHDOWN
- Thrust: REV AS REQ
- AP: OFF

## Go Around

- Thrust: TO/GA
- Pitch: ROTATE
- (ATC) Advice
- Flaps: 20
- Landing Gear: UP
- HDG: AS REQ
- AP: ENGAGE AS REQ
- Flaps: AS ADV
- Speed Brake: DISARM
- RWY TURN OFF Lights: OFF

# Shutdown

## Taxi

- (ATC) Report vacated
- Strobe: OFF
- Landing Lights: OFF
- RWY TURNOFF Lights: ON
- Taxi Lights: ON
- Flaps: UP
- Speed Brake: DISARM
- Autobrake: OFF
- Terrain: OFF
- WX: OFF
- APU: ON & START

## At Parking / Gate

- Taxi Lights: OFF
- Parking Brake: OFF
- APU: VERIFY ON
- Fuel Control 1/2: CUT-OFF
- Electric Hydraulic Pumps: OFF
- Fuel Pumps: OFF
- Seatbelts: OFF
- Beacon: OFF
- (Note) Request Deboarding

## Shutdown

- Flight Director: OFF x2
- Transponder: STBY
- CHKL Shutdown: CALL
- EXT PWR: ON IF AVAIL
- APU: OFF WITH EXT PWR
- Exterior Lights: ALL OFF
- No Smoking: OFF
- Emergency Lights: OFF
- APU: OFF
- BAT: OFF
- EXT PWR: OFF
