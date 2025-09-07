AircraftName: Cessna Citation X (FlightFX)
AdaptedFrom: https://flightsim.to/file/95515/cessna-citation-x-c750-normal-checklist https://drive.google.com/drive/folders/1NWuKPU2KJW3FDMpQ7VqQ52-mh8H1-SVS

- (Note) Work in progress: Typos, Flow, Pictures

# Cockpit preparations

## Before Start

- (Tablet) Weights → Import from SimBrief
- (Tablet) (optional) Ground Services → Connect Ground Power
- [Standby Power](../assets/img/flightfx-citationx/stby-power.png): ON
- [Emergency Lights](../assets/img/flightfx-citationx/emerg-lt.png): ARMED
- [Battery 1/2](../assets/img/flightfx-citationx/batt-switch.png): ON
- [EICAS Power](../assets/img/flightfx-citationx/eicas-pwr.png): ON
- External Power: AS REQ
- [Nav Lights](../assets/img/flightfx-citationx/exterior-lights.png): ON

## APU Start

- [LH Fuel Boost](../assets/img/flightfx-citationx/lh-fuel-boost.png): NORM
- [APU Starter Disengage](../assets/img/flightfx-citationx/apu-starter-disengage.png): NORM
- [APU Master](../assets/img/flightfx-citationx/apu-master.png): ON
- [APU Test](../assets/img/flightfx-citationx/apu-test.png): PUSH
- [APU Generator](../assets/img/flightfx-citationx/apu-gen-switch.png): ON
- APU DC Volts: 22V MIN
- [APU Start](../assets/img/flightfx-citationx/apu-start-switch.png): ON
- APU RELAY ENGAGED Light: ON; OFF; READY TO LOAD
- [Load Shed](../assets/img/flightfx-citationx/load-shed-switch.png): NORM
- (Tablet) Ground Services → Disonnect Ground Power
- [APU Ammeter](../assets/img/flightfx-citationx/apu-ammeter.png): 400A MAX
- [APU Bleed Air](../assets/img/flightfx-citationx/apu-bleed.png): ON; AS REQ

## Before Start (contd)

- [Avionics](../assets/img/flightfx-citationx/avionics-pwr.png): ON
- [IRS](../assets/img/flightfx-citationx/irs-align.png): ALIGN; NAV
- Parking Brake: VERIFY SET
- (Tablet) Ground Services → Remove Chocks → Close Main/Luggage Door → Remove Covers
- EICAS: NO WARN
- EICAS: Fuel: CHECK QTY
- [CTR Wing Xfer](../assets/img/flightfx-citationx/ctr-wing-xfer.png): NORM; AS REQ

## FMC / Flight Plan

### Flight Plan

- (MCDU) POS INIT → GPS 1 POS → LOAD
- (MCDU) NAV → SIMBRIEF → FPLN RECALL
- (Note) As of 09/2025 SimBrief imports will sometimes fail and get stuck on REQ PENDING when Navigraph data is installed. No workaround exists.
- (ATC) Request clearance (IFR)
- (MCDU) (manual entry) FPL → Enter ORIGIN, DEST, Enroute WPT, Finalize Flight Plan
- (Note) Enter airways in format aw.wpt (f.e. UL612.HON)
- (MCDU) NAV → DEPARTURE → Enter RWY, SID/TRANS → ACTIVATE
- (MCDU) (optional) NAV → ARRIVAL → Enter RWY, STAR/TRANS
- (MCDU) [MFD Map → SKP/RCL](../assets/img/flightfx-citationx/mdf-map.png)
- (MCDU) (contd) FPL → NEXT/PREV → Confirm RTE
- (Note) To delete an entry: FPL → DEL → Line Select

### Performance

- (MCDU) PERF → PERF INIT P3 → Set/Check → PERF INIT P4 → SYNC EFB → CONFIRM INIT
- (MCDU) PERF → TAKEOFF P1 → Set Temperature, Pressure, Wind → TAKEOFF P2 → Set/Check
- (MCDU) (contd) TAKEOFF P3 → Set Flaps → Check TO Weight → CONFIRM INIT
- (MCDU) (contd) TAKEOFF DATA P2 → Check V-Speeds

### Before Start (contd)

- (MCDU) MFD → MFD SETUP → TRAFFIC/TERRAIN, VERT PROF (as desired)
- [Altimeter](../assets/img/flightfx-citationx/baro.png): SET LOCAL
- [Altitude](../assets/img/flightfx-citationx/alt_hdg.png): SET INITIAL CLEARANCE
- [Heading](../assets/img/flightfx-citationx/alt_hdg.png): SET RWY HDG
- (Tablet) (optional) Config → Systems → Enable AT Module
- [ATS](../assets/img/flightfx-citationx/ats.png): ON/ARMED
- [AP NAV/VNAV](../assets/img/flightfx-citationx/ap.png): ARMED; AS REQ
- [Standby Gyro](../assets/img/flightfx-citationx/gyro.png): UNCAGED
- Seatbelts: ON

### Engine Start

- (ATC) Request Engine Start
- Ground Rec/Anti-Coll Lights: GND REC
- [Thrust](../assets/img/flightfx-citationx/fuel-cutoff.png): FUEL CUTOFF
- APU Bleed: VERIFY ON
- [PAC Isol Valve](../assets/img/flightfx-citationx/pac-isol.png): CLSD (vertical)
- EICAS: ENG PAGE
- [Engine Start RH/LH](../assets/img/flightfx-citationx/engine-start.png): PUSH -[N2 10%](../assets/img/flightfx-citationx/engine-monitor.png): THRUST IDLE
- Oil Pressure: CONFIRM RISING; ELSE ABORT
- APU Bleed: OFF; AS DES

# Taxi, Lineup, Takeoff

## Before Taxi / Taxi

- Flight Controls: VERIFY FREE MOV
- Flaps: TO
- [Trim](../assets/img/flightfx-citationx/trim.png): TO; CENTERED GREEN
- Speed Brake: VERIFY STOWED
- AHRS: VERIFY ALIGNED
- EICAS: VERIFY; CONSIDER
- Engine [Anti-Ice](../assets/img/flightfx-citationx/anti-ice.png): AS REQ
- [Pressurization Alt Sel](../assets/img/flightfx-citationx/prs-alt.png): NORM
- (ATC) Request Taxi clearance
- [Taxi Lights](../assets/img/flightfx-citationx/taxi-ldg.png): ON

## Before Takeoff

- PFD; MFD: SET AS REQ
- Altimeter: VERIFY LOCAL
- [AP YD](../assets/img/flightfx-citationx/ap.png): VERIFY ON
- AP MD TRIM: VERIFY ON
- [Pitot & Static Heaters](../assets/img/flightfx-citationx/pitot.png): BOTH ON
- [Windshield Heaters](../assets/img/flightfx-citationx/windshield.png): BOTH ON
- [Squawk](../assets/img/flightfx-citationx/atc-tca.png): SET
- [TA/RA](../assets/img/flightfx-citationx/atc-tca.png): SET
- [WX Radar](../assets/img/flightfx-citationx/wx-on.png): ON
- (MCDU) MFD → MFD SETUP → Verify TRAFFIC/TERRAIN
- (ATC) Request clearance
- [Landing Lights](../assets/img/flightfx-citationx/taxi-ldg.png)
- Ground Rec/Anti-Coll Lights: ANTI-COLL

## Takeoff

- Brakes: HOLD
- EICAS: VERIFY
- Thrust: 40% N1
- Brakes: RELEASE
- (optional) ATS & [TO/GA](../assets/img/flightfx-citationx/atis-toga.png): PRESS
- VR: ROTATE UP TO 13 DEGREES

# Climb, Cruise, Descent

### Reference Speeds

- VFE Flaps 5: 250 KIAS
- VFE Flaps 15: 210 KIAS
- VLE Gear: 210 KIAS

### Positive Rate of climb

- Landing Gear: UP

## Climb

- (Altitude) 1000FT

- Flaps UP: 170 KIAS
- Thrust: CLB DETENT
- Accelerate to CLB Speed: 250 KIAS
- AP: ENGAGE
- Taxi Lights: OFF
- APU Bleed: OFF
- APU Start: STOP
- APU Master: OFF
- (Altitude) TRANSITION ALTITUDE
- Altimeter: STD
- (Altitude) 10000FT
- Landing Lights: OFF
- Seatbelts: OFF

## Cruise

- Thrust: CRU
- Engine Anti-Ice: OFF; AS REQ
- Fuel Qty: MONITOR

## Descent

- (MCDU) → PROG P2 → Check TOD

### 50nm before TOD

- Approach: CHECK; REFER TO CHARTS
- (MCDU) NAV → ARRIVAL → Confirm
- (MCDU) PERF → LANDING → Set Temperature, Baro, Wind
- (MCDU) NAV → Set/Confirm (ILS)
- [Minimums](../assets/img/flightfx-citationx/minimums.png): SET
- Altitude: SET TARGET
- AP VNAV: VERIFY SET

## ToD

- (ATC) Clearance received
- Speed: MONITOR; ADJUST PWR
- Anti-Ice: AS REQ
- (Altitude) FL100
- Seatbelts: ON
- Landing Lights: ON
- (Altitude) TRANSITION ALTITUDE
- Altimeter: SET LOCAL
- [Pressurization](../assets/img/flightfx-citationx/press.png): CHECK; SET LANDING ALT

# Approach

### Reference Speeds

- VFE Flaps 5: 250 KIAS
- VFE Flaps 15: 210 KIAS
- VLE Gear: 210 KIAS
- VREF: 108-132 DEP ON WEIGHT

## Landing

### Localizer Intercept

- Speed: 150-160 KIAS
- Flaps: 15
- AP APP: ON
- (Note) Verify LOC and GS (ILS) / GP (RNAV) are armed on PFD

### Glide Slope / Path Intercept

- Landing Gear: DOWN
- Flaps: FULL
- Speed: VREF + 5 KIAS
- (Altitude) Before or at 200ft
- AP: OFF
- (Altitude) 20-30FT
- Thrust: IDLE
- (Altitude) 10FT
- Flare: 2-3 DEGREE
- (Altitude) TOUCHDOWN
- Speed Brake: FULL
- TThrust: REV; AS REQ

## Go Around

- TO/GA: PRESS
- Thrust: TO/MC DETENT
- Rotate: 10 DEGREES
- Flaps: RETRACT
- Landing Gear: RETRACT

# Shutdown

## Taxi

- (ATC) Report vacated
- Landing Lights: OFF
- Ground Rec/Anti-Coll Lights: GND REC
- Taxi Lights: ON
- Flaps: UP
- Speed Brakes: RETRACT
- WX Radar: OFF
- ATC / TCAS: STBY
- Pitot & Static Heaters: BOTH OFF
- Windshield Heaters: BOTH OFF
- Engine Anti-Ice: AS REQ
- APU: AS REQ

## Shutdown

- Parking Brake: SET
- Taxi Lights: OFF
- Engine Anti-Ice: OFF
- APU: AS REQ
- APU Bleed: AS REQ
- Thrust: FUEL OFF
- Ground Rec/Anti-Coll Lights: OFF
- Nav Lights: OFF
- Seatbelts: OFF
- (Tablet) Ground Services → Set Chocks and Covers
- IRS: OFF
- Standby Gyro: CAGED
- Standby Power: OFF
- Avionics: OFF
- EICAS: OFF
- Emergency Lights: OFF
- APU Bleed: OFF
- APU Start: STOP
- APU Master: OFF
- Battery 1/2: OFF
