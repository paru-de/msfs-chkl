AircraftName: Beechcraft Starship (Black Square)
AdaptedFrom: https://support.justflight.com/support/solutions/articles/17000146911-black-square-starship-msfs-manual https://flightsim.to/file/94821/beech-starship-procedures-and-checklist

- (Note) WORK IN PROGRESS: TYPOS, DIFFERENT APPROACHES

# Cockpit preparations

## Preflight

- (Tablet) Payload → Set Fuel/Payload
- Parking Brake: SET
- Control Locks: REMOVE
- Landing Gear: DOWN
- [Battery](../assets/img/blacksquare-starship/battery-master.png): ON
- Pitch/Roll/Rudder Trim: NEUTRAL
- [Fuel Qty](../assets/img/blacksquare-starship/fuel-qty.png): CHECK
- [Oxygen Pressure](../assets/img/blacksquare-starship/oxygen-pressure.png): CHECK
- [Annunciators; Door](../assets/img/blacksquare-starship/door.png): CHECK
- Battery: OFF
- Chocks: REMOVED
- Pitot/Static Covers: REMOVED
- Engine Covers: REMOVED
- Gear Locking Pins: REMOVED
- Emergency Exit: SECURE
- Door: LOCKED

## Before Starting Engine

- [Circuit Breakers (L/R/AUX)](../assets/img/blacksquare-starship/circuit-breakers.png): ALL IN
- [Outboard Reversionary Panels](../assets/img/blacksquare-starship/rev-panel.png): AS REQ
- Parking Brake: SET
- Audio Panels: AS REQ
- [Static Source](../assets/img/blacksquare-starship/static-source.png): NORM
- [Oxygen Supply](../assets/img/blacksquare-starship/oxygen-supply.png): PULL
- [Oxygen Masks](../assets/img/blacksquare-starship/oxygen-mask-test.png): TEST
- [Ice Protection](../assets/img/blacksquare-starship/ice-protections.png): ALL OFF
- Landing Gear: DOWN
- [Anti-Skid](../assets/img/blacksquare-starship/anti-skid.png): ANTI-SKID
- [Center Reversionary Panel](../assets/img/blacksquare-starship/center-rev-panel.png): AS REQ
- [Standby Instruments](../assets/img/blacksquare-starship/standby-ind.png): ON
- [STANDBY BATT PWR ON Annunciator](../assets/img/blacksquare-starship/standby-ind-ann.png): ILLUMINATED
- Power Levers: IDLE
- Propeller Levers: FULL FWD
- Condition Levers: FUEL CUTOFF
- [Bleed Air Valves](../assets/img/blacksquare-starship/bleed-air-valve.png): OFF
- [Temp Mode](../assets/img/blacksquare-starship/temp-mode.png): OFF

### Sys Tests

- Battery: ON
- [Triple-Fed BUS Volts](../assets/img/blacksquare-starship/trip-fed.png): 22V MIN
- [Center BUS Volts](../assets/img/blacksquare-starship/ctr-bus.png): 23V Min
- [EICAS](../assets/img/blacksquare-starship/eicas-switch.png): ON
- [Firewall Fuel Valves](../assets/img/blacksquare-starship/firewall-fuel-closed.png): PUSH CLOSED
- Extinguisher and F/W Valve: ILLUMINATED
- [Standby Pumps](../assets/img/blacksquare-starship/stby-pumps.png): ON
- Annunciator; Fuel Press LO: ILLUMINATED
- Firewall Fuel Valves: PUSH OPEN
- Extinguisher and F/W Valve: EXTINGUISHED
- Annunciators; Fuel Press LO : EXTINGUISHED
- Standby Pumps: OFF
- Annunciator; Fuel Press LO: ILLUMINATED
- [Transfer Flow](../assets/img/blacksquare-starship/transfer-flow.png): LEFT & RIGHT
- [EICAS; FUEL TRANSFER](../assets/img/blacksquare-starship/fuel-transfer-msg.png): ILLUMINATED
- Annunciators; Fuel Press LO: EXTINGUISHED
- Transfer Flow: OFF
- EICAS; AVIONIC AIR FAIL: ILLUMINATED
- [Avionics Alternate Blower](../assets/img/blacksquare-starship/avionics-alt-blow.png): ON
- EICAS; AV ALT BLWR ON: ILLUMINATED
- EICAS; AVIONIC AIR FAIL: EXTINGUISHED
- Avionics Alternate Blower: OFF
- [Fuel Qty (total and aft)](../assets/img/blacksquare-starship/fuel-qty-aft.png): CHECK
- Oxygen Pressure: CONFIRM
- [Interior Lights](../assets/img/blacksquare-starship/lights.png): AS REQ
- Exterior Lights: NAV

# Engine Start

## Engine Start (BAT)

- (Note) Right Engine first, then Left Engine
- Strobe: LOW
- [R/L Ignition and Engine Start](../assets/img/blacksquare-starship/eng-ign-start.png): ON
- R/L Condition Lever (12% N1 min): START
- EICAS; R/L N1 and ITT (1000C max): MONITOR
- EICAS; [R/L Oil Pressure](../assets/img/blacksquare-starship/oil-pres.png): CONFIRM RISING ELSE ABORT
- R/L Ignition and Engine Start: OFF
- R/L Condition Lever (65% N1 min): RUN
- [R/L Generator](../assets/img/blacksquare-starship/eng-gen.png): RESET; ON
- [R/L Volts](../assets/img/blacksquare-starship/r-gen.png): 27.5-29V
- [Charge Battery until](../assets/img/blacksquare-starship/loadmeter.png): LOADMETER < 50%
- (Note) Repeat for second Engine
- [Gen Ties](../assets/img/blacksquare-starship/gen-ties.png): OPEN
- EICAS; L/R GEN TIES OPEN: ILLUMINATED
- Triple-Fed BUS: 26.5-28V
- Gen Ties: NORM
- EICAS; L/R GEN TIES OPEN: EXTINGUISHED
- [Generator Load](../assets/img/blacksquare-starship/gen-load-paralleled.png): PARALLELED

## Engine Start (External Power)

- (Note) Right Engine first, then Left Engine
- Strobe: LOW
- [Battery Volts](../assets/img/blacksquare-starship/batt-volts.png): 20V MIN
- Propeller Levers: FEATHER
- EICAS Pilot and Copilot Avionics: OFF
- [R/L Generator](../assets/img/blacksquare-starship/eng-gen.png): OFF
- Battery: ON
- (Tablet) Payload → Connect External Power
- [EXT PWR Volts](../assets/img/blacksquare-starship/ext-pwr-volts.png): 28-28.4V
- [EXT PWR Switch](../assets/img/blacksquare-starship/ext-pwr-switch.png): ON
- EICAS: ON
- [R/L Ignition and Engine Start](../assets/img/blacksquare-starship/eng-ign-start.png): ON
- R/L Condition Lever (12% N1 min): START
- EICAS; R/L N1 and ITT (1000C max): MONITOR
- EICAS; [R/L Oil Pressure](../assets/img/blacksquare-starship/oil-pres.png): CONFIRM RISING ELSE ABORT
- R/L Ignition and Engine Start: OFF
- R/L Condition Lever (65% N1 min): RUN
- (Note) Repeat for second Engine
- EXT PWR: OFF
- (Tablet) Payload → Disconnect External Power
- R/L Generator: RESET; ON
- [R/L Volts](../assets/img/blacksquare-starship/r-gen.png): 27.5-29V
- [Gen Ties](../assets/img/blacksquare-starship/gen-ties.png): NORM
- EICAS; L/R GEN TIES OPEN: EXTINGUISHED
- [Generator Load](../assets/img/blacksquare-starship/gen-load-paralleled.png): PARALLELED
- Propeller Levers: FULL FWD

# Flight Plan / FMC Setup

### Introduction

- (Note) The Starship comes equipped with two means of navigation:
- The FMC does not support GPS or SID/STAR's. Use [SimBrief's Legacy Algorithm](../assets/img/blacksquare-starship/simbrief-vor.png) to find a compatible route.
- The [GNS 430](../assets/img/blacksquare-starship/gns430.png) supports GPS and SID/STAR's.
- The GNS can be controlled by PMS5's free [GTN750 widget](../assets/img/blacksquare-starship/gns430-panel.png). You can download it by visiting pms50.com/msfs

## Init

- Pilot and Copilot Avionics: ON
- (MCDU) CDU → INITIALIZE SYSTEM → ALL DATA OK
- (MCDU) MSG (btn) → UPDATE VLF → UPDATE VLF FROM FMS
- (MCDU) SYS CTRL (btn) → Verify AUTO LEG is active → Verify AP NAV SRC is FMS or GNS
- (MCDU) NAV SOURCE (btn) → Verify FMS 1 or FMS 2
- (ATC) Request clearance (IFR)

### NAV DATA Update

- (MCDU) [Insert floppy disk](../assets/img/blacksquare-starship/floppy.png)
- (MCDU) UPDATE DATA BASE → Select FLIGHT DATA → CONTINUE

## FMS-850

- (Note) When using SimBrief VOR route
- (Tablet) MSFS EFB → SimBrief Dispatch → VIEW → IMPORT ROUTE → FLT PLAN (btn)
- (MCDU) Click Departure airport → REPLACE WPT → Enter departure airport → DISPLAY RUNWAYS
- (MCDU) MFD Display → PLAN MAP → DISPLAY → Verify Route
- (Note) When not using SimBrief
- (MCDU) FLT PLAN → Click Screen to activate/deactivate hardware keyboard → Enter departure airport, waypoints, arrival airport → END FPL
- (MCDU) (optional) FPL → APPR → Set Approach
- (MCDU) MFD Display → PLAN MAP → DISPLAY → Verify Route
- (Note) To delete a flight plan, click on any WPT and select ERASE FLPT
- (MCDU) (optional) VNAV (btn) → Set altitudes (advisory only)

## GNS

- (Note) It is highly recommended to use the free GNT750 widget to set up the GNS
- (MCDU) Open GNT 750 Widget
- Flight Plan → MENU → Import → Import from SimBrief → Back
- PROC → Departure → Select SID/TRANS → Load Departure → Back
- (optional) PROC → Arrival → Select STAR/TRANS → Load Arrival → Back
- (optional) PROC → Approach → Select runway → Load Approach → Back
- Flight Plan → Verify RTE

# Taxi, Takeoff

## Before Taxi

- Standby Indicators: VERIFY ON
- Bleed Air Valves: BOTH
- [Blowers/Temperature](../assets/img/blacksquare-starship/blowers.png): SET
- Temperature Mode Selector: AUTO
- Exterior Lights: AS REQ
- Cabin Lights: AS REQ
- Seatbelts: ON
- Flight Controls: VERIFY FREE MOV
- Brakes: CHECKED
- EICAS; [AHRS ALIGNING](../assets/img/blacksquare-starship/ahrs-aligning.png): EXTINGUISHED
- EICAS: VERIFY / AFX OFF ONLY
- CDU Time and Date Position: VERIFY

### Avionics

- [Altimeter](../assets/img/blacksquare-starship/baro.png): SET LOCAL
- [Standby Altimeter](../assets/img/blacksquare-starship/baro_stby.png): SET LOCAL
- [Heading](../assets/img/blacksquare-starship/hdg_crs.png): SET RWY HDG
- [Altitude](../assets/img/blacksquare-starship/altitude.png): SET INITIAL CLEARANCE
- [Speed Bug](../assets/img/blacksquare-starship/speed-ref.png): 180 KIAS

### Continued

- [Squawk](../assets/img/blacksquare-starship/transponder.png): SET
- Transponder: STBY
- Nav Radios: AS REQ
- (MCDU) [RDR CONTROL (btn)](../assets/img/blacksquare-starship/rdr.png) STANDBY
- [Pitch/Roll/Rudder Trims](../assets/img/blacksquare-starship/trim.png): TO
- [Flap/FWD Wing](../assets/img/blacksquare-starship/flap.png): RETRACT
- [Engine Ice Protection](../assets/img/blacksquare-starship/inertial-sep.png): MAIN; AS REQ
- [AFX](../assets/img/blacksquare-starship/afx.png): ARMED

### Taxi

- (ATC) Request Taxi Clearance
- Taxi Lights: ON

## Before Takeoff (Abbreviated)

- Parking Brake: SET
- [Annunciators](../assets/img/blacksquare-starship/annun.png): PUSH TO TEST
- Pitch/Roll/Rudder Trims: CENTERED/GREEN
- Flap/FWD WING: TO; AS REQ

### Pressurization

- [Pressurization Altitude](../assets/img/blacksquare-starship/pressurization.png): 1000FT ABOVE CRZ
- [Rate Knob](../assets/img/blacksquare-starship/pressurization.png): 10 O'CLOCK
- [Manual Cabin Alt Control](../assets/img/blacksquare-starship/manual-cab.png): NORM (FULL CCW)
- Bleed Air Valves: VERIFY BOTH

### Avionics

- [AP](../assets/img/blacksquare-starship/ap-engage.png): ENGAGE
- [AP Yoke D/C](../assets/img/blacksquare-starship/yoke-dc.png): PRESS
- Altimeter: VERIFY LOCAL
- Standby Altimeter: VERIFY LOCAL

### Ice Protection

- [Stall Warning Heat](../assets/img/blacksquare-starship/stall_warn.png): ON
- [Pitot/Static Heat](../assets/img/blacksquare-starship/pitot_static.png): ON
- [Engine Ice Protection](../assets/img/blacksquare-starship/inertial-sep.png): AS REQ
- [Vent/Cable Heat](../assets/img/blacksquare-starship/ventcable.png): ON
- [Windshield Heat](../assets/img/blacksquare-starship/windshield.png): LOW

### Verify

- Transponder: ON
- (MCDU) [RDR CONTROL (btn)](../assets/img/blacksquare-starship/rdr.png) GND/WX (AS REQ)
- Engine Auto-Ignition: AS REQ
- Generator Loads: CHECK
- EICAS: VERIFY; CONSIDER
- (ATC) Request Departure Clearance

### Line-up

- Taxi Lights: OFF
- Landing Lights: ON
- Strobe: ANTI-COLL

# Takeoff, Climb, Cruise

## Takeoff

- Brakes: HOLD
- (Note) Takeoff Power: 100% TRQ, 850 ITT, 1700 RPM
- EICAS; AFX: ILLUMINATED
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
- [Yaw Damper](../assets/img/blacksquare-starship/yaw-damper.png): ON
- AP: ENGAGE
- [AP Controls](../assets/img/blacksquare-starship/ap-control.png): AS REQ
- (Note) Climb Power: 90% TRQ, 840 ITT, 1600 RPM
- [Propeller Sync](../assets/img/blacksquare-starship/prop-sync.png): ON
- (Note) Accelerate to desired climb speed

### Climb Speeds Reference

- (Note) AP IAS PROF can manage climb speeds automatically
- Max Rate: BLUE LINE + 10
- B FL100: 180 KIAS
- B FL200: 160 KIAS
- B FL300: 140 KIAS
- A FL300: 130 KIAS

### Climb (contd)

- Engine Display: MONITOR
- Cabin Pressurization: MONITOR
- (Altitude) TRANSITION ALTITUDE
- Altimeter; Standby Altimeter: SET STD
- (Altitude) FL100
- Seatbelts: OFF
- Landing Lights: OFF
- Ice Protection: AS REQ
- Engine Auto Ignition: AS REQ
- (MCDU) RDR Control → GND off, WX+TURB on

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

### 50nm before TOD

- Approach: CHECK; REFER TO CHARTS
- (MCDU) FMS - FLT PLAN → APPR → Set APPR
- (MCDU) GNS - PROC → Set ARRIVAL → Set APPROACH
- (MCDU) VNAV → Set faf altitude (ILS); Set MDA (RNAV)
- (MCDU) NAV (btn) → Set ILS Frequency
- [Minimums](../assets/img/blacksquare-starship/dh-minimum.png): SET
- Target Altitude (faf/MDA): SET

### ToD

- (ATC) Clearance received
- AP DESCEND or VS: ON
- Speed: MONITOR; ADJUST PWR
- Pressurization Altitude: 500FT ABOVE LANDING
- Rate Knob: AS REQ
- Ice Protection: AS REQ
- (Altitude) FL100
- Seatbelts: ON
- Landing Lights: ON
- Engine Auto Ignition: AS REQ
- AFX: ARMED
- (MCDU) NAV (btn) → Confirm ILS Frequency
- (MCDU) RDR CONTROL (btn) → GND MAP
- (Altitude) TRANSITION ALTITUDE
- Altimeter: SET LOCAL

# Approach

### Approach Speed Reference

- VREF: 107-121 KIAS
- VLE/VLO (max Gear): 200 KIAS
- VFE (max Flaps): 180 KIAS

## Landing

### Localizer Intercept

- Speed: 150-160 KIAS
- Heading: SYNC
- AP HDG: ON
- (MCDU) NAV SOURCE (btn) → VOR
- [CRS](../assets/img/blacksquare-starship/hdg_crs.png): SET RWY HDG
- AP NAV: ON
- PFD LOC: VERIFY CAPTURED

### Glide Slope Intercept

- AP APPR: ON
- PFD GS: VERIFY CAPTURED
- Flaps: DOWN
- Landing Gear: DOWN
- Speed: VREF + 10 KIAS
- AFX: VERIFY ARMED
- Propeller Lever: MAX RPM
- - Propeller Sync: OFF
- (Altitude) Before or at 200ft
- AP: OFF
- Yaw Damper: OFF
- (Altitude) 20-30FT
- Power Levers: IDLE
- (Altitude) 10FT
- Flare: 2-3 DEGREE
- (Altitude) TOUCHDOWN
- Power Levers: BETA RANGE; REV AS REQ

## Go Around

- Power Levers: 100% TQ
- [GO-AROUND Button](../assets/img/blacksquare-starship/go-around.png): PUSH
- VREF: ROTATE; MAINTAIN
- Flaps: UP
- Landing Gear: UP
- Yaw Damper: ON

# Shutdown

## Taxi

- (ATC) Report vacated
- Landing Lights: OFF
- Strobe: LOW; ANTI-COLL OFF
- Taxi Lights: ON
- Flaps: UP
- (MCDU) RDR CONTROL (btn) → STBY
- Transponder: STBY
- Engine Auto Ignition: OFF
- Stall Warning Heat: OFF
- Pitot/Static Heat: OFF
- Vent Cable Heat: OFF
- Windshield Heat: OFF
- Engine Anti-Ice: AS REQ

## Parking / Shutdown

- Parking Brake: SET
- Taxi Light: OFF
- AFX: OFF
- Oxygen Supply: PUSH IN
- Engine Anti-Ice: OFF
- Ice Protection: VERIFY ALL OFF
- Pilot and Copilot Avionics: OFF
- Standby Instruments: OFF
- Bleed Air Valves: OFF
- Temp Mode: OFF
- [Battery](../assets/img/blacksquare-starship/loadmeter.png): CHARGED

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
