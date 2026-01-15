"""Constants for service document generation - machine types, problems, solutions, and parts."""

# Machine models by category (kept separate for flexibility)
MACHINE_CATEGORIES = {
	"Ovens": {
		"models": [
			"ConvectionPro 5000",
			"RapidBake 3000",
			"TurboHeat X-200",
			"CombiSteam Elite",
			"DeckMaster 480",
		],
	},
	"Fryers": {
		"models": [
			"DeepFry Pro 450",
			"TurboCrisp 2000",
			"OilGuard Elite",
			"FryMaster XL-4000",
			"CrispKing 300",
		],
	},
	"Mixers": {
		"models": [
			"PlanetaryMix 60",
			"DoughMaster 80Q",
			"SpiralPro 120",
			"VersaMix 40",
			"HeavyDuty 100",
		],
	},
	"Refrigeration": {
		"models": [
			"ChillMaster 2000",
			"WalkIn Pro Series",
			"ReachIn Elite 3-Door",
			"UndercounterCool 48",
			"DisplayCase Premium",
		],
	},
	"Dishwashers": {
		"models": [
			"SaniSpray 3000",
			"RackMaster Conveyor",
			"UndercounterClean Pro",
			"DoorType HT-60",
			"FlightType Industrial",
		],
	},
	"Griddles": {
		"models": [
			"FlatTop Pro 48",
			"ElectricGrill 36",
			"GasGriddle HeavyDuty",
			"ChromeTop Elite",
			"ThermoStatic 60",
		],
	},
}

# Linked service issues: each problem has a consistent solution and valid parts
# Generated using generate_service_data.py - replace this with AI-generated data
SERVICE_ISSUES = {
	"Ovens": [
		{
			"problem": "Convection oven temperature fluctuating wildly between 250\u00b0F and 450\u00b0F despite thermostat set to 350\u00b0F. Kitchen staff reports uneven baking and burnt food on one side.",
			"solution": "Replaced faulty thermocouple that was providing erratic temperature readings to the control board. Calibrated temperature controller and verified proper sensor placement.",
			"parts": ["Thermocouple Type K 18-inch with 1/4-inch NPT fitting", "Temperature Controller Digital PID 240V", "High-temperature ceramic wire nuts"],
		},
		{
			"problem": "Gas deck oven pilot light keeps going out every 2-3 hours, causing complete loss of heat. Flame sensor appears dirty and corroded.",
			"solution": "Cleaned flame sensor with fine steel wool and replaced faulty thermocouple assembly. Adjusted gas pressure regulator to manufacturer specifications.",
			"parts": ["Flame Sensor Rod 6-inch stainless steel", "Thermocouple Assembly 24-inch universal gas", "Gas Pressure Regulator 1/2-inch NPT 11-inch WC"],
		},
		{
			"problem": "Combi-steam oven producing insufficient steam with visible calcium buildup around steam injection nozzles. Steam generator cycling but minimal steam output observed.",
			"solution": "Descaled steam generator using manufacturer-approved descaling solution and replaced clogged steam injection nozzles. Flushed entire steam system and tested output pressure.",
			"parts": ["Steam Injection Nozzle Assembly brass 1/8-inch", "Steam Generator Heating Element 4500W 240V", "Solenoid Valve 240V 1/4-inch NPT steam-rated"],
		},
		{
			"problem": "Convection fan motor making loud grinding noise and running slower than normal, causing poor air circulation and uneven cooking results.",
			"solution": "Replaced worn convection fan motor bearings and installed new motor assembly. Cleaned fan blade and housing of grease buildup that was causing additional drag.",
			"parts": ["Convection Fan Motor 1/3 HP 240V 1725 RPM", "Fan Blade 12-inch diameter aluminum", "Motor Mount Bracket heavy-duty steel"],
		},
		{
			"problem": "Oven door not sealing properly with visible gaps at corners, causing heat loss and longer cooking times. Door gasket appears cracked and hardened.",
			"solution": "Removed old door gasket and installed new high-temperature silicone seal. Adjusted door hinges and latch mechanism for proper alignment and compression.",
			"parts": ["Door Gasket high-temp silicone 8-foot length", "Door Hinge Pin stainless steel 3/8-inch", "Door Latch Assembly spring-loaded commercial grade"],
		},
		{
			"problem": "Electric heating elements in bottom of deck oven not heating evenly, with cold spots visible on stone surface. Elements appear to have burn marks.",
			"solution": "Replaced two damaged heating elements that had developed hot spots and were drawing inconsistent amperage. Rewired connections with high-temperature wire and new terminals.",
			"parts": ["Heating Element 5000W 240V tubular", "High-temperature Wire 12 AWG 500\u00b0F rated", "Terminal Block ceramic 240V 30A"],
		},
		{
			"problem": "Digital control display shows error code and oven will not start heating cycle. Control board appears to have moisture damage from steam exposure.",
			"solution": "Replaced water-damaged control board and installed protective cover shield. Reprogrammed controller with original parameters and tested all safety interlocks.",
			"parts": ["Control Board PCB assembly with display", "Protective Cover polycarbonate steam-resistant", "Ribbon Cable 20-pin flat conductor"],
		},
		{
			"problem": "High-limit safety switch tripping every 20 minutes during normal operation, shutting down oven completely. Oven cavity temperature reads normal on main thermostat.",
			"solution": "Replaced faulty high-limit switch that was tripping at 450\u00b0F instead of rated 550\u00b0F. Cleaned temperature probe and verified proper mounting location away from direct heat sources.",
			"parts": ["High-Limit Switch 550\u00b0F manual reset", "RTD Temperature Probe 100-ohm platinum", "Probe Mounting Bracket stainless steel adjustable"],
		},
		{
			"problem": "Rapid-bake oven conveyor belt tracking to one side and scraping against side walls, causing belt damage and uneven product heating.",
			"solution": "Adjusted belt tracking mechanism and replaced worn conveyor drive roller with proper crown. Realigned belt guides and tensioned to manufacturer specifications.",
			"parts": ["Conveyor Drive Roller 4-inch diameter crowned", "Belt Tracking Guide adjustable stainless", "Drive Belt polyester mesh 24-inch width"],
		},
		{
			"problem": "Oven timer stuck at 15 minutes and will not advance, causing products to overcook. Digital display flickering intermittently during operation.",
			"solution": "Replaced defective timer motor assembly and updated control software. Cleaned timer contact points and verified proper voltage supply to timing circuit.",
			"parts": ["Timer Motor Assembly 120V synchronous", "Timer Contact Switch DPDT 15A", "Control Software EPROM chip latest version"],
		},
		{
			"problem": "Stone deck developing cracks and uneven heating patterns, with hot spots creating burnt areas on pizza crusts. Stone appears to have absorbed grease over time.",
			"solution": "Removed and replaced damaged stone deck with new refractory material. Sealed stone surface and adjusted heating element positioning for even heat distribution.",
			"parts": ["Refractory Stone Deck 2-inch thick cordierite", "Stone Sealer food-safe high-temperature", "Support Rails stainless steel adjustable"],
		},
		{
			"problem": "Gas ignition system failing to light burners reliably, requiring multiple attempts and causing delayed start-up. Igniter glowing but insufficient spark observed.",
			"solution": "Replaced worn hot surface igniter with higher amperage model and cleaned gas orifices of debris. Adjusted gas valve timing sequence for reliable ignition.",
			"parts": ["Hot Surface Igniter silicon carbide 120V", "Gas Valve Solenoid dual-stage 24V", "Ignition Control Module solid-state with safety timer"],
		},
		{
			"problem": "Oven cavity lighting flickering and two bulbs completely burned out, making it difficult for staff to monitor food during cooking cycles.",
			"solution": "Replaced all interior light bulbs with high-temperature LED versions and repaired loose wiring connections in light fixture junction box.",
			"parts": ["LED Light Bulb 25W 500\u00b0F rated", "Light Fixture high-temp glass lens", "Junction Box stainless steel vapor-proof"],
		},
		{
			"problem": "Excessive grease buildup in ventilation system causing poor exhaust and smoke backing into kitchen. Exhaust fan motor running but insufficient airflow measured.",
			"solution": "Disassembled and deep cleaned entire exhaust system removing hardened grease deposits. Replaced exhaust fan motor that had seized bearings from grease contamination.",
			"parts": ["Exhaust Fan Motor 1/2 HP 240V high-temp rated", "Fan Housing stainless steel grease-resistant", "Ductwork Cleaning Kit industrial scrapers and brushes"],
		},
		{
			"problem": "Combi-oven water level sensor giving false readings causing unit to shut down with 'low water' error despite full reservoir. Sensor probe covered with mineral deposits.",
			"solution": "Replaced corroded water level sensor and installed new water filtration system to prevent mineral buildup. Flushed water lines and calibrated sensor readings.",
			"parts": ["Water Level Sensor stainless steel probe type", "Water Filter cartridge sediment and scale", "Water Solenoid Valve 120V 3/8-inch NPT"],
		},
		{
			"problem": "Electric convection oven heating elements cycling on and off rapidly every 30 seconds, preventing oven from reaching set temperature of 425\u00b0F. Temperature controller display shows erratic readings jumping between temperatures.",
			"solution": "Replaced faulty RTD temperature sensor that was providing incorrect feedback to the controller, causing rapid cycling. Recalibrated temperature controller and verified proper sensor placement in oven cavity.",
			"parts": ["RTD Temperature Sensor PT100 3-wire 6-inch probe", "Temperature Controller PID Digital 240V", "Sensor mounting bracket stainless steel"],
		},
		{
			"problem": "Gas convection oven burner flames burning yellow and sooty instead of blue, creating excessive carbon buildup on oven walls. Gas pressure appears normal but combustion is incomplete.",
			"solution": "Cleaned and adjusted primary air shutters on main burners to achieve proper air-to-gas ratio. Replaced clogged orifices that were restricting gas flow and causing poor combustion.",
			"parts": ["Gas burner orifices #54 drill size brass", "Primary air shutter assembly", "Flame sensor rod 8-inch length"],
		},
		{
			"problem": "Combi-oven drain system backing up with standing water in bottom of unit, causing error messages and automatic shutdown. Water overflowing from drain pan during rinse cycles.",
			"solution": "Cleared blocked drain line filled with food debris and scale buildup using enzymatic cleaner and mechanical snake. Replaced damaged drain valve that was not seating properly.",
			"parts": ["Drain valve assembly 1-inch NPT solenoid", "Drain line flexible hose 1-inch diameter", "Water level sensor probe 12-inch"],
		},
		{
			"problem": "Deck oven door hinges binding and requiring excessive force to open, causing safety concerns for kitchen staff. Door alignment appears off and gasket compressed unevenly.",
			"solution": "Replaced worn door hinge pins and bushings that had developed excessive play from repeated use. Adjusted door alignment and replaced compressed door gasket for proper sealing.",
			"parts": ["Door hinge pin set stainless steel 5/8-inch", "Hinge bushing bronze sleeve bearing", "Door gasket high-temp silicone 1-inch width"],
		},
		{
			"problem": "Electric oven main contactor chattering and arcing when heating elements engage, creating sparks and burning smell. Electrical connections appear loose and overheated.",
			"solution": "Replaced main heating contactor with burned contacts and loose coil. Tightened all electrical connections and applied dielectric grease to prevent future corrosion and arcing.",
			"parts": ["Contactor 3-pole 50-amp 240V coil", "Wire nuts high-temp ceramic rated", "Electrical contact cleaner spray"],
		},
		{
			"problem": "Rapid-bake oven variable speed drive displaying fault codes and conveyor running at incorrect speeds. Drive overheating and fan cycling constantly to cool electronics.",
			"solution": "Replaced damaged variable frequency drive that had internal component failure from heat exposure. Installed additional ventilation fan to prevent future overheating of drive electronics.",
			"parts": ["Variable Frequency Drive 2HP 480V", "Cooling fan 120V 4-inch axial", "Drive mounting bracket with heat sink"],
		},
		{
			"problem": "Gas oven flame rollout switch tripping during normal operation, shutting down main burners immediately after ignition. Switch appears to be sensing flames outside combustion chamber.",
			"solution": "Cleaned blocked heat exchanger passages that were causing flame impingement and rollout. Replaced heat-damaged rollout switch that had become overly sensitive from repeated exposure.",
			"parts": ["Flame rollout switch manual reset 250\u00b0F", "Heat exchanger gasket high-temp fiber", "Burner tube cleaning brush kit"],
		},
		{
			"problem": "Convection oven door latch mechanism not engaging properly, allowing door to open during cooking cycles and triggering safety shutdowns. Latch spring appears weakened and worn.",
			"solution": "Replaced door latch assembly including worn spring mechanism and striker plate. Adjusted door alignment to ensure proper engagement and tested safety interlocks for proper operation.",
			"parts": ["Door latch assembly spring-loaded", "Striker plate stainless steel adjustable", "Safety microswitch SPDT 15-amp"],
		},
		{
			"problem": "Electric deck oven bottom heating elements drawing excessive current and tripping 50-amp breaker repeatedly. Elements glowing cherry red and overheating stone deck surface.",
			"solution": "Replaced shorted heating elements that had internal insulation breakdown causing current leakage. Tested element resistance and verified proper electrical isolation before reassembly.",
			"parts": ["Heating element 240V 5000W tubular", "Element mounting bracket ceramic", "High-limit switch 500\u00b0F manual reset"],
		},
		{
			"problem": "Combi-oven steam generator not producing steam despite water supply being adequate and heating elements functioning. Steam chamber pressure gauge reading zero during steam mode.",
			"solution": "Descaled steam generator chamber that was completely blocked with mineral deposits preventing steam formation. Replaced damaged steam solenoid valve that was not opening properly.",
			"parts": ["Steam solenoid valve 3/4-inch 24V", "Descaling solution commercial grade", "Steam chamber gasket EPDM rubber"],
		},
		{
			"problem": "Oven exhaust blower motor seized and not rotating, causing excessive heat buildup in oven cavity and triggering high-limit shutdowns. Motor windings appear burned from overheating.",
			"solution": "Replaced burned-out exhaust blower motor and cleaned grease-clogged impeller that had caused motor overload. Balanced impeller and verified proper belt tension after installation.",
			"parts": ["Exhaust blower motor 1/2HP 208V", "Blower wheel 10-inch diameter", "Motor drive belt B-section 62-inch"],
		},
		{
			"problem": "Gas oven electronic ignition module clicking continuously but failing to light main burners. Igniter electrode gap appears correct but spark is weak and intermittent.",
			"solution": "Replaced failed ignition module with degraded transformer output causing insufficient spark energy. Cleaned igniter electrodes and verified proper grounding of ignition system.",
			"parts": ["Electronic ignition module 120V input", "Igniter electrode ceramic insulated", "Ignition wire high-voltage rated 18-inch"],
		},
		{
			"problem": "Programmable oven controller losing memory settings and reverting to default programs after power cycles. Clock time resetting and stored recipes being deleted randomly.",
			"solution": "Replaced internal backup battery in controller that was no longer holding charge for memory retention. Updated controller firmware and restored all customer recipe programs from backup.",
			"parts": ["Lithium backup battery 3V coin cell", "Controller firmware chip EPROM", "Memory expansion module 64KB"],
		},
		{
			"problem": "Deck oven stone surface developing hot and cold zones with temperature variations exceeding 100\u00b0F across baking area. Infrared temperature readings showing uneven heat distribution patterns.",
			"solution": "Replaced damaged radiant heat deflector plates beneath stone that had warped from thermal cycling. Recalibrated zone heating controls and verified even temperature distribution across deck.",
			"parts": ["Heat deflector plate stainless steel", "Zone temperature sensor thermocouple", "Thermal insulation blanket ceramic fiber"],
		},
		{
			"problem": "Convection oven control panel buttons becoming unresponsive and display showing garbled characters intermittently. Membrane switch overlay appears cracked and moisture damaged.",
			"solution": "Replaced damaged membrane switch overlay and control panel display module that had moisture intrusion from steam exposure. Sealed all panel connections with waterproof gaskets.",
			"parts": ["Membrane switch overlay tactile", "LCD display module 4x20 character", "Panel gasket kit silicone rubber"],
		},
		{
			"problem": "Combi-steam oven steam generator producing excessive noise and vibration during steam cycles, with visible mineral scale buildup on internal components. Water pump motor running continuously even when steam demand is low.",
			"solution": "Descaled steam generator system using manufacturer-approved descaling solution and replaced worn water pump motor assembly. Calibrated water flow sensors and adjusted pump cycling parameters.",
			"parts": ["Water pump motor assembly 1/8 HP 120V with mounting bracket", "Descaling solution concentrate 1-gallon commercial grade", "Water flow sensor 1/4-inch NPT thread"],
		},
		{
			"problem": "Electric deck oven bottom heating elements glowing bright red but producing insufficient heat, with resistance readings showing 50% higher than specification. Baking times increased significantly for pizza and bread products.",
			"solution": "Replaced degraded heating elements that had developed internal breaks and hot spots. Verified proper voltage supply and tightened all electrical connections to prevent future element failure.",
			"parts": ["Electric heating element 5000W 240V 24-inch serpentine", "High-temperature ceramic wire nuts rated 480V", "Element mounting brackets stainless steel set of 4"],
		},
		{
			"problem": "Convection oven exhaust blower motor running but producing minimal airflow, causing excessive moisture and grease accumulation in oven cavity. Motor amperage reading normal but fan blade damaged.",
			"solution": "Replaced bent and cracked exhaust fan impeller assembly and rebalanced motor shaft. Cleaned accumulated grease from housing and verified proper belt tension on motor drive.",
			"parts": ["Exhaust fan impeller 12-inch diameter stainless steel", "Motor drive belt 3L320 industrial grade", "Motor shaft bearing assembly sealed 6203-2RS"],
		},
		{
			"problem": "Gas convection oven electronic ignition module sparking continuously but failing to establish stable flame, causing burner lockout after 30 seconds. Igniter electrode gap appears correct but weak spark visible.",
			"solution": "Replaced faulty electronic ignition control module and cleaned corroded electrode connections. Adjusted electrode gap to manufacturer specification and tested ignition sequence timing.",
			"parts": ["Electronic ignition control module 24VAC with flame sensing", "Igniter electrode assembly with 3/16-inch gap setting", "High-voltage ignition cable 18-inch length"],
		},
		{
			"problem": "Rapid-bake oven temperature probe reading 100\u00b0F below actual cavity temperature, causing extended baking cycles and inconsistent product quality. Probe appears physically intact but temperature differential increasing.",
			"solution": "Replaced drift-calibrated RTD temperature sensor and recalibrated temperature controller to factory specifications. Verified probe placement and thermal coupling to oven cavity.",
			"parts": ["RTD temperature sensor Pt100 Class A 6-inch probe", "Temperature controller 1/16 DIN PID digital display", "Probe mounting thermowell 1/2-inch NPT stainless"],
		},
		{
			"problem": "Combi-oven humidity sensor providing erratic readings causing automatic cooking programs to fail mid-cycle. Sensor readings fluctuating between 20% and 95% humidity regardless of actual conditions.",
			"solution": "Replaced contaminated humidity sensor element and cleaned sensor housing of grease and food residue. Performed sensor calibration using certified humidity reference standards.",
			"parts": ["Humidity sensor element capacitive type 0-100% RH", "Sensor housing assembly IP65 rated stainless steel", "Calibration kit with 75% RH salt solution"],
		},
		{
			"problem": "Electric convection oven main power contactor coil overheating and dropping out intermittently, causing complete loss of heating during busy service periods. Contactor contacts showing pitting and burning.",
			"solution": "Replaced overheated main power contactor with proper amperage rating and installed suppression circuit to reduce coil stress. Tightened all power connections and verified proper wire sizing.",
			"parts": ["Power contactor 3-pole 50A 240VAC coil with auxiliary contacts", "RC suppression circuit 120VAC rated", "Power terminal lugs 6 AWG crimp type set of 6"],
		},
		{
			"problem": "Deck oven steam injection system producing inconsistent steam bursts with visible air bubbles in water supply lines. Steam quality poor with excessive water droplets rather than dry steam.",
			"solution": "Replaced malfunctioning steam solenoid valve and installed water line air purge system. Adjusted steam pressure regulator and cleaned mineral deposits from injection nozzles.",
			"parts": ["Steam solenoid valve 1/2-inch NPT 24VAC normally closed", "Pressure regulator 0-15 PSI adjustable with gauge", "Steam injection nozzles stainless steel set of 4"],
		},
		{
			"problem": "Gas deck oven flame safety sensor failing to detect pilot flame consistently, causing nuisance shutdowns every 45 minutes during normal operation. Sensor appears clean but flame detection unreliable.",
			"solution": "Replaced aging flame safety sensor with UV-sensitive photoelectric type and adjusted sensor positioning for optimal flame detection. Cleaned and aligned pilot burner orifice.",
			"parts": ["UV flame sensor photoelectric type with 2-second response", "Sensor mounting bracket adjustable stainless steel", "Pilot burner orifice #54 drill natural gas"],
		},
		{
			"problem": "Convection oven door latch mechanism sticking and requiring excessive force to engage, creating safety hazard for kitchen staff. Latch springs appear compressed and striker plate worn.",
			"solution": "Replaced worn door latch assembly and striker plate, then adjusted door alignment to ensure smooth operation. Lubricated all pivot points with high-temperature food-safe grease.",
			"parts": ["Door latch assembly heavy-duty with spring return", "Striker plate stainless steel with wear insert", "High-temperature grease NSF certified 4-oz tube"],
		},
		{
			"problem": "Electric combi-oven heating elements in steam generator compartment showing signs of corrosion and reduced heating capacity. Scale buildup visible on element surfaces affecting heat transfer efficiency.",
			"solution": "Replaced corroded steam generator heating elements and performed complete system descaling procedure. Installed water filtration system to prevent future mineral buildup and corrosion.",
			"parts": ["Steam generator heating element 3000W 240V Incoloy sheath", "Water filter cartridge 5-micron sediment type", "Heating element gasket set high-temperature silicone"],
		},
		{
			"problem": "Rapid-bake oven conveyor motor overheating and tripping thermal overload protection during peak usage periods. Motor housing hot to touch and belt showing signs of slippage.",
			"solution": "Replaced overloaded conveyor drive motor with higher capacity unit and adjusted belt tension to manufacturer specifications. Cleaned accumulated flour and debris from motor ventilation.",
			"parts": ["Conveyor motor 1/2 HP 120V totally enclosed fan cooled", "Drive belt V-type 4L380 oil and heat resistant", "Motor thermal overload relay 5.8-8.5A adjustable"],
		},
		{
			"problem": "Gas convection oven pressure regulator diaphragm ruptured causing erratic gas pressure and unstable flame patterns. Burner flames varying in height and producing incomplete combustion.",
			"solution": "Replaced damaged gas pressure regulator assembly and tested system for proper outlet pressure regulation. Performed complete combustion analysis and adjusted air-to-gas mixture ratios.",
			"parts": ["Gas pressure regulator 1/2-inch NPT 4-12 inch WC adjustable", "Regulator diaphragm kit with springs and hardware", "Gas pressure gauge 0-15 inch WC liquid filled"],
		},
		{
			"problem": "Electric deck oven stone surface developing hot spots and uneven temperature distribution, with pyrometer readings showing 75\u00b0F variance across baking surface. Stone appears to have hairline cracks developing.",
			"solution": "Replaced cracked baking stone with segmented design for better thermal expansion control and rebalanced heating element power distribution. Calibrated surface temperature sensors.",
			"parts": ["Segmented baking stone set 1-inch thick cordierite", "Surface temperature sensor RTD flat mounting type", "Stone support rails stainless steel adjustable"],
		},
		{
			"problem": "Combi-oven water level switch providing false high-level readings causing unit to overflow during fill cycles. Switch float mechanism appears to be sticking in up position.",
			"solution": "Replaced malfunctioning water level switch assembly and cleaned mineral deposits from float chamber. Adjusted switch activation point and tested complete fill and drain cycle operation.",
			"parts": ["Water level switch assembly with adjustable float", "Float chamber cleaning brush kit", "Switch mounting gasket food-grade EPDM rubber"],
		},
		{
			"problem": "Rapid-bake oven heating elements on one side completely dead with no power reaching the elements, causing half of products to remain raw while other half cooks normally. Electrical meter shows no continuity through affected heating circuit.",
			"solution": "Replaced failed power relay that controls heating elements and installed new circuit breaker that was internally damaged from previous electrical surge. Tested all heating zones for proper voltage and current draw after repairs.",
			"parts": ["Power Relay 40A 240V DPDT", "Circuit Breaker 30A 2-pole 240V", "Wire Nuts 12AWG rated (6-pack)"],
		},
		{
			"problem": "Combi-oven steam generator producing rusty water and metallic-tasting steam, with visible corrosion inside steam chamber. Water quality test shows high iron content and pH imbalance affecting food quality.",
			"solution": "Replaced corroded steam generator tank assembly and installed new water filtration system with deionizer cartridge. Flushed entire water system with descaling solution and recalibrated water quality sensors.",
			"parts": ["Steam Generator Tank 6-gallon stainless steel", "Water Filter Cartridge deionizer type", "Water Quality Sensor pH/conductivity probe"],
		},
		{
			"problem": "Gas deck oven experiencing delayed ignition with loud 'whooshing' sounds during startup, creating dangerous gas accumulation before lighting. Ignition sequence taking 15-20 seconds instead of normal 3-5 seconds.",
			"solution": "Replaced worn gas valve actuator motor and cleaned clogged gas orifices that were restricting proper gas flow. Adjusted ignition timing sequence in control module to ensure safer startup cycle.",
			"parts": ["Gas Valve Actuator Motor 120V synchronous", "Gas Orifice Set #54 drill size brass", "Ignition Control Module programmable sequence"],
		},
		{
			"problem": "Electric convection oven fan motor overheating and shutting down on thermal protection after 45 minutes of operation, causing loss of air circulation during peak cooking periods. Motor housing extremely hot to touch.",
			"solution": "Replaced seized motor bearings and installed new thermal protection switch with higher temperature rating. Cleaned accumulated grease from motor housing and improved ventilation around motor compartment.",
			"parts": ["Motor Bearing Set 6203-2RS sealed type", "Thermal Overload Switch 160\u00b0C reset", "Motor Mount Gasket high-temperature silicone"],
		},
		{
			"problem": "Combi-oven humidity sensor providing incorrect readings causing unit to add excessive steam during baking modes, resulting in soggy bread products. Sensor reading 90% humidity in dry heat mode.",
			"solution": "Replaced failed capacitive humidity sensor that had moisture infiltration in sensor housing and recalibrated humidity control system. Updated sensor mounting position away from direct steam exposure area.",
			"parts": ["Humidity Sensor capacitive 0-100% RH", "Sensor Housing stainless steel IP65", "Calibration Kit 33% and 75% RH standards"],
		},
	],
	"Fryers": [
		{
			"problem": "Gas fryer fails to ignite and displays error code E3, with pilot light not lighting despite gas flow being present.",
			"solution": "Replaced faulty thermocouple that was not generating sufficient millivoltage to keep gas valve open, and cleaned pilot orifice of carbon buildup.",
			"parts": ["Thermocouple Type K 24-inch 750\u00b0F rated", "Pilot orifice #56 drill size", "Gas valve solenoid coil 24V"],
		},
		{
			"problem": "Electric fryer heating elements cycle on and off rapidly, causing oil temperature to fluctuate between 280\u00b0F and 380\u00b0F instead of maintaining set temperature.",
			"solution": "Replaced malfunctioning solid-state temperature controller that had internal relay failure, and calibrated new controller to proper temperature differential.",
			"parts": ["Digital temperature controller 240V with K-type input", "Temperature probe RTD 1/8-inch NPT", "Contactor 40-amp 240V 3-pole"],
		},
		{
			"problem": "Fryer high-limit safety switch keeps tripping at 375\u00b0F, shutting down unit even though thermostat is set to 350\u00b0F.",
			"solution": "Replaced defective high-limit switch with incorrect temperature rating and relocated temperature bulb away from direct heating element contact.",
			"parts": ["High-limit safety switch 400\u00b0F manual reset", "Capillary tube 6-feet stainless steel", "Temperature bulb 1/4-inch diameter"],
		},
		{
			"problem": "Oil filtration system pump runs continuously but no oil circulates through filter, with pump making grinding noise.",
			"solution": "Replaced seized pump motor and damaged impeller assembly, then primed system and adjusted flow control valve.",
			"parts": ["Pump motor 1/3 HP 115V single-phase", "Impeller assembly 3-inch diameter bronze", "Mechanical seal kit for pump housing"],
		},
		{
			"problem": "Basket lift mechanism moves up slowly and stops halfway, requiring manual assistance to reach full height.",
			"solution": "Rebuilt pneumatic cylinder with new seals and adjusted air pressure regulator to proper 80 PSI operating pressure.",
			"parts": ["Pneumatic cylinder rebuild kit with O-rings", "Air pressure regulator 0-120 PSI", "Solenoid valve 120V 1/4-inch NPT"],
		},
		{
			"problem": "Gas fryer loses flame during cooking cycles and safety system shuts off gas flow, occurring randomly throughout the day.",
			"solution": "Replaced corroded flame sensor rod that was giving intermittent signal and cleaned burner ports to ensure proper flame pattern.",
			"parts": ["Flame sensor rod 8-inch stainless steel", "Gas valve safety module 24V", "Burner orifice set natural gas BTU rated"],
		},
		{
			"problem": "Control panel timer display is blank and touch buttons are unresponsive, though fryer heating elements still function manually.",
			"solution": "Replaced failed control board with blown capacitors and updated firmware to latest version for improved reliability.",
			"parts": ["Control board assembly with LCD display", "Membrane switch overlay keypad", "Power supply board 12V/5V output"],
		},
		{
			"problem": "Oil drains extremely slowly from fryer tank taking over 30 minutes to empty, with visible debris backing up in drain line.",
			"solution": "Replaced clogged drain valve with full-port ball valve and cleared grease blockage from drain piping with mechanical snake.",
			"parts": ["Ball valve 2-inch full-port stainless steel", "Drain coupling 2-inch NPT threaded", "Flexible drain hose 2-inch ID food-grade"],
		},
		{
			"problem": "Electric fryer heating elements glow red-hot continuously and oil temperature exceeds 450\u00b0F despite thermostat setting of 325\u00b0F.",
			"solution": "Replaced welded-closed contactor contacts that could not open circuit and installed new temperature sensor with proper calibration.",
			"parts": ["Contactor 50-amp 240V NEMA rated", "Temperature sensor RTD Pt100 6-inch probe", "Control relay 24V coil DPDT contacts"],
		},
		{
			"problem": "Fryer oil level sensor gives false readings showing empty tank when oil level is adequate, triggering unnecessary low-oil alarms.",
			"solution": "Cleaned oil buildup from capacitive level sensor probe and replaced sensor electronics module with recalibrated unit.",
			"parts": ["Capacitive oil level sensor 12-inch probe", "Sensor electronics module 24V DC", "Mounting bracket stainless steel adjustable"],
		},
		{
			"problem": "Gas fryer burner flames are yellow and sooty instead of blue, with black residue accumulating on fryer tank bottom.",
			"solution": "Adjusted primary air shutter for proper air-gas mixture and replaced worn burner venturi tube that was restricting airflow.",
			"parts": ["Burner venturi tube assembly", "Primary air shutter adjustment plate", "Gas orifice spud natural gas #43 drill"],
		},
		{
			"problem": "Fryer tank develops pinhole leak near heating element mounting area, causing oil to drip onto floor during operation.",
			"solution": "Welded and reinforced tank wall with food-grade stainless steel patch, then pressure tested system before returning to service.",
			"parts": ["Stainless steel patch plate 6x6 inch 16-gauge", "Food-grade welding rod 308L stainless", "Tank drain gasket high-temperature rated"],
		},
		{
			"problem": "Filter pump cycles on randomly every few minutes even when filtration is not requested, causing oil level fluctuations.",
			"solution": "Replaced faulty filter pump relay that had internal contact welding and reprogrammed control logic to prevent unwanted pump activation.",
			"parts": ["Control relay 120V coil 30-amp contacts", "Relay socket 11-pin octal base", "Control board EPROM chip programmed"],
		},
		{
			"problem": "Fryer thermostat reads 50\u00b0F lower than actual oil temperature measured with calibrated thermometer, causing overcooking of products.",
			"solution": "Replaced temperature probe with correct resistance curve and recalibrated control system using precision temperature calibrator.",
			"parts": ["RTD temperature probe Pt1000 8-inch stem", "Thermostat controller analog 0-500\u00b0F range", "Calibration resistor set precision 0.1%"],
		},
		{
			"problem": "Gas safety valve clicks repeatedly but will not open to allow gas flow to main burner, despite successful pilot light operation.",
			"solution": "Replaced gas safety valve with corroded internal components and adjusted pilot gas pressure to proper millivolt output for valve operation.",
			"parts": ["Gas safety valve 3/4-inch NPT 24V", "Pressure regulator 11-inch WC natural gas", "Thermopile generator 750mV output rating"],
		},
		{
			"problem": "Electric fryer displays error code E7 and shuts down after 10 minutes of operation, with contactors chattering and cycling rapidly during heating cycles.",
			"solution": "Replaced worn contactors and cleaned oxidized electrical connections in control box. Adjusted voltage settings and verified proper amperage draw on all heating circuits.",
			"parts": ["Contactor 40A 240V 3-pole NEMA rated", "Terminal block connector strips 12AWG", "Control relay 24V SPDT 10A"],
		},
		{
			"problem": "Gas fryer produces weak flames that cannot maintain oil temperature above 250\u00b0F, with gas pressure reading only 2 inches water column at manifold.",
			"solution": "Cleaned gas orifices and replaced clogged gas regulator assembly. Adjusted gas pressure to manufacturer specification of 4 inches water column and tested flame characteristics.",
			"parts": ["Gas pressure regulator 1/2-inch NPT natural gas", "Gas orifice set #54 drill size", "Gas manifold gasket kit"],
		},
		{
			"problem": "Fryer drain valve leaks oil continuously from handle area and will not close completely, creating safety hazard and oil loss.",
			"solution": "Disassembled drain valve assembly and replaced worn valve seat and handle packing. Applied high-temperature thread sealant and adjusted valve stem tension.",
			"parts": ["Drain valve seat stainless steel 1-inch", "Valve stem packing PTFE high-temp", "Ball valve handle assembly 1-inch"],
		},
		{
			"problem": "Oil filtration system creates excessive foam in fryer vat during filtering cycle, with oil overflowing and filter pump drawing air intermittently.",
			"solution": "Replaced damaged return line diffuser and cleaned filter pump suction strainer. Adjusted pump flow rate and verified proper oil return positioning to minimize turbulence.",
			"parts": ["Oil return diffuser perforated stainless", "Filter pump strainer 40-mesh stainless", "Oil pump impeller assembly 1/3 HP"],
		},
		{
			"problem": "Fryer temperature probe reads erratically jumping between 150\u00b0F and 400\u00b0F randomly, causing inconsistent heating and product quality issues.",
			"solution": "Diagnosed faulty RTD temperature probe with multimeter testing and replaced entire probe assembly. Calibrated new sensor and verified accurate temperature readings throughout range.",
			"parts": ["RTD temperature probe 1000-ohm platinum", "Probe well stainless steel 6-inch", "Temperature sensor cable 4-wire shielded"],
		},
		{
			"problem": "Electric fryer makes loud humming noise from heating elements and draws excessive amperage, tripping 50-amp breaker after 15 minutes of operation.",
			"solution": "Found heating elements with internal short circuits and replaced complete element assembly. Tested electrical load and verified proper amperage draw within specifications.",
			"parts": ["Heating element 15kW 240V immersion type", "Element gasket high-temperature silicone", "Element terminal box weatherproof NEMA 4"],
		},
		{
			"problem": "Basket lift mechanism jerks violently during raise cycle and motor stalls with burning smell, requiring multiple attempts to lift baskets fully.",
			"solution": "Replaced seized lift motor bearings and cleaned accumulated grease from gear reduction box. Lubricated lift chains and adjusted motor timing controls.",
			"parts": ["Lift motor 1/2 HP 115V reversible", "Motor bearing set sealed ball type", "Gear reduction oil SAE 90 weight"],
		},
		{
			"problem": "Fryer control panel displays correct temperature but heating system does not respond to thermostat calls, remaining cold during cooking cycles.",
			"solution": "Diagnosed failed control relay in temperature controller and replaced solid-state relay module. Cleaned control board connections and updated temperature control parameters.",
			"parts": ["Solid state relay 25A 240V zero-cross", "Control board fuse 3A slow-blow", "Thermostat control module digital"],
		},
		{
			"problem": "Gas fryer produces loud popping and rumbling noises during ignition sequence, with delayed ignition causing flame rollout from burner area.",
			"solution": "Cleaned burner orifices and replaced damaged ignition electrode assembly. Adjusted gas-air mixture and synchronized ignition timing with gas valve opening sequence.",
			"parts": ["Ignition electrode ceramic insulated", "Spark ignition module 120V intermittent", "Burner orifice spud brass #45"],
		},
		{
			"problem": "Fryer oil level drops significantly during filtration cycles and takes excessive time to return, with visible air bubbles in return oil stream.",
			"solution": "Replaced cracked oil return line and tightened loose fittings in filtration plumbing. Cleaned filter tank and adjusted return oil flow rate to eliminate cavitation.",
			"parts": ["Oil return line 1-inch stainless flex", "Compression fitting set 1-inch NPT", "Filter tank drain valve 3/4-inch ball"],
		},
		{
			"problem": "Electric fryer heating elements cycle properly but oil temperature never exceeds 275\u00b0F, with elements appearing to have reduced heating capacity.",
			"solution": "Tested heating elements and found 30% voltage drop due to corroded electrical connections. Replaced contactors and cleaned all electrical connections in junction box.",
			"parts": ["Electrical contactor 30A 240V 3-pole", "Wire nuts high-temperature ceramic", "Junction box gasket neoprene seal"],
		},
		{
			"problem": "Gas fryer safety system locks out after pilot proves but main burner fails to light, displaying fault code F4 on control panel.",
			"solution": "Replaced faulty flame sensor with poor microamp signal and cleaned main burner crossover tubes. Adjusted pilot flame position to improve main burner ignition reliability.",
			"parts": ["Flame sensor rod stainless steel", "Burner crossover tube stainless", "Ignition control module Honeywell S8610"],
		},
		{
			"problem": "Fryer timer functions work but cook cycle automatically extends beyond set time, with timer display showing incorrect remaining time during operation.",
			"solution": "Diagnosed faulty timer relay in control circuit and replaced digital timer module. Recalibrated timing parameters and verified accurate cycle timing across all preset programs.",
			"parts": ["Digital timer module 24V programmable", "Timer relay DPDT 10A contacts", "Control circuit fuse 5A fast-blow"],
		},
		{
			"problem": "Oil filtration pump motor overheats and trips thermal overload protection after 5 minutes of operation, with motor housing becoming extremely hot.",
			"solution": "Found blocked pump impeller and cleaned debris from pump housing. Replaced worn motor bearings and verified proper motor ventilation and cooling air flow.",
			"parts": ["Pump motor 1/3 HP 115V capacitor start", "Motor thermal overload switch", "Pump impeller bronze with stainless shaft"],
		},
		{
			"problem": "Fryer vat develops hairline crack near drain fitting causing slow oil seepage, with crack visible when oil temperature exceeds 350\u00b0F.",
			"solution": "Drained and cleaned fryer vat completely, then applied high-temperature food-grade epoxy repair compound. Reinforced repair area with stainless steel patch plate and retested under pressure.",
			"parts": ["High-temp epoxy repair compound food-grade", "Stainless steel patch plate 16-gauge", "Drain fitting gasket PTFE reinforced"],
		},
		{
			"problem": "Electric fryer contactor coil burns out causing loud humming sound and no heating, with visible burn marks on contactor housing and acrid smell.",
			"solution": "Replaced failed contactor assembly and inspected electrical connections for proper wire gauge and tightness to prevent future coil burnout.",
			"parts": ["Contactor 3-pole 40A 240V", "Wire nuts 12-14 AWG", "Electrical cleaner spray"],
		},
		{
			"problem": "Gas fryer combustion air blower motor seized causing incomplete combustion and carbon monoxide production, with motor shaft locked and windings overheated.",
			"solution": "Installed new combustion air blower motor and cleaned burner assembly of carbon buildup to restore proper air-fuel mixture.",
			"parts": ["Blower motor 1/6 HP 115V 1750 RPM", "Motor capacitor 5 MFD 370V", "Burner cleaning brush set"],
		},
		{
			"problem": "Fryer vat shows warping and oil pooling in corners due to overheating damage, with visible metal discoloration and uneven oil distribution during cooking.",
			"solution": "Replaced damaged fryer vat assembly and recalibrated temperature controls to prevent future overheating and thermal damage.",
			"parts": ["Fryer vat assembly stainless steel 40-lb capacity", "Vat gasket kit", "Temperature calibration thermometer"],
		},
		{
			"problem": "Electric fryer heating element terminal block shows signs of arcing with blackened connections and intermittent power loss during peak heating demand.",
			"solution": "Replaced heating element terminal block and installed new high-temperature wire connections rated for continuous duty operation.",
			"parts": ["Terminal block ceramic 3-pole 50A", "High-temp wire 10 AWG THWN", "Terminal lugs copper 10 AWG"],
		},
		{
			"problem": "Gas fryer regulator diaphragm ruptures causing erratic gas pressure and flame instability, with audible gas leakage from regulator vent.",
			"solution": "Installed new gas pressure regulator assembly and performed leak test with soap solution to ensure all connections are gas-tight.",
			"parts": ["Gas pressure regulator 1/2 inch NPT", "Pipe dope gas-rated", "Gas leak detection solution"],
		},
		{
			"problem": "Fryer oil return line from filter system becomes clogged with carbonized debris causing slow oil return and extended filter cycles.",
			"solution": "Disassembled and cleaned oil return line system and installed new filter screen to prevent future debris accumulation.",
			"parts": ["Oil return tube stainless steel 1 inch diameter", "Filter screen 20-mesh stainless", "Pipe cleaning rod flexible"],
		},
		{
			"problem": "Electric fryer heating element develops hairline crack causing oil contamination with metallic particles and electrical shorts to ground.",
			"solution": "Replaced cracked heating element with new heavy-duty model and tested electrical isolation to ensure safe operation.",
			"parts": ["Heating element 240V 18kW tubular", "Element gasket high-temperature", "Megohmmeter for testing"],
		},
		{
			"problem": "Gas fryer ignition transformer fails providing weak spark that cannot reliably light pilot, with transformer case showing heat damage and cracking.",
			"solution": "Installed new ignition transformer rated for continuous duty and verified proper electrode gap and positioning for reliable ignition.",
			"parts": ["Ignition transformer 120V primary 10kV secondary", "Ignition electrode assembly", "Electrode wire high-voltage"],
		},
		{
			"problem": "Fryer control board experiences power supply failure causing erratic operation and random shutdowns, with visible capacitor bulging and component overheating.",
			"solution": "Replaced control board power supply section and updated firmware to latest version to improve system stability and performance.",
			"parts": ["Control board power supply module", "Cooling fan 12V DC axial", "Thermal interface compound"],
		},
		{
			"problem": "Electric fryer ground fault circuit interrupter trips repeatedly during normal operation due to moisture infiltration in electrical connections.",
			"solution": "Sealed all electrical connections with weatherproof connectors and installed new GFCI breaker rated for commercial kitchen environments.",
			"parts": ["GFCI breaker 2-pole 30A", "Weatherproof connector kit", "Electrical sealant compound"],
		},
		{
			"problem": "Gas fryer manifold develops stress crack near burner connection causing gas leak and uneven flame distribution across burner tubes.",
			"solution": "Welded manifold crack and pressure tested system, then adjusted individual burner orifices for uniform flame pattern across all tubes.",
			"parts": ["Gas manifold assembly cast iron", "Burner orifice set", "Manifold pressure gauge"],
		},
		{
			"problem": "Fryer basket lift chain stretches and skips on drive sprocket causing jerky motion and incomplete basket travel to programmed positions.",
			"solution": "Replaced worn lift chain and adjusted sprocket alignment to ensure smooth basket movement and accurate positioning control.",
			"parts": ["Lift chain stainless steel 1/4 inch pitch", "Drive sprocket 12-tooth", "Chain tensioner assembly"],
		},
		{
			"problem": "Electric fryer develops short circuit in control wiring harness causing random function activation and potential fire hazard from overheating wires.",
			"solution": "Completely rewired control system with new harness and installed protective conduit to prevent future wire damage and shorts.",
			"parts": ["Wiring harness pre-assembled", "Flexible conduit 3/4 inch", "Wire protection sleeve split-loom"],
		},
		{
			"problem": "Gas fryer burner tubes become clogged with grease and carbon deposits reducing heat output and causing incomplete combustion with sooty exhaust.",
			"solution": "Disassembled burner assembly and chemically cleaned all tubes, then adjusted air shutters for proper combustion air mixture.",
			"parts": ["Burner tube cleaning kit", "Combustion analyzer", "Air shutter adjustment tool"],
		},
		{
			"problem": "Fryer oil level sight glass cracks allowing oil seepage and creating inaccurate level readings, with visible stress fractures around mounting points.",
			"solution": "Replaced sight glass assembly with tempered glass model and installed new gasket seals to prevent oil leakage and ensure accurate readings.",
			"parts": ["Sight glass tempered 4-inch diameter", "Gasket set Viton high-temperature", "Glass mounting hardware stainless"],
		},
		{
			"problem": "Gas fryer produces loud banging noise during ignition sequence and flames appear to roll out of burner ports intermittently. Burner assembly shows signs of corrosion and several burner orifices appear partially blocked.",
			"solution": "Replaced corroded burner assembly and cleaned all gas orifices with proper drill bits. Adjusted gas-to-air mixture ratio and tested ignition sequence for proper flame characteristics.",
			"parts": ["Burner Assembly Model FB-8500 Natural Gas", "Gas Orifice Kit #45 Drill Size 0.0820 inch", "Burner Gasket Set High-Temperature Silicone"],
		},
		{
			"problem": "Electric fryer contactor remains energized after unit is switched off, causing heating elements to stay powered and creating potential safety hazard. Control relay shows signs of welded contacts and burning smell is present.",
			"solution": "Replaced faulty contactor with welded contacts and installed new control relay. Verified proper voltage isolation and tested all safety interlocks for correct operation.",
			"parts": ["Contactor 3-Pole 50 Amp 240V AC Coil", "Control Relay DPDT 24V DC Coil", "Wire Nuts 12 AWG High-Temperature Rated"],
		},
		{
			"problem": "Fryer vat shows significant warping along bottom panel causing uneven heating patterns and hot spots that burn product. Temperature differential across cooking surface measures 75\u00b0F between center and edges.",
			"solution": "Removed heating elements and replaced warped fryer vat with new heavy-duty stainless steel tank. Reinstalled heating elements with proper thermal expansion gaskets and verified even heat distribution.",
			"parts": ["Fryer Vat 40-Pound Capacity 316 Stainless Steel", "Heating Element Gasket Kit Ceramic Fiber", "Tank Drain Fitting 1.5 inch NPT Stainless"],
		},
		{
			"problem": "Oil level sensor float mechanism is stuck in down position due to accumulated grease buildup, preventing automatic oil replenishment system from functioning. Low oil alarms do not activate even when tank is nearly empty.",
			"solution": "Disassembled float chamber and thoroughly cleaned all components with degreasing solvent. Replaced worn float mechanism and recalibrated oil level detection system for accurate readings.",
			"parts": ["Float Switch Assembly Stainless Steel SPDT", "Float Chamber Gasket Viton High-Temperature", "Sensor Wiring Harness 12-Pin Weatherproof Connector"],
		},
		{
			"problem": "Fryer produces excessive smoke and oil vapor emissions even with fresh oil, and exhaust fan cannot keep up with vapor production. Internal inspection reveals clogged heat exchanger fins and blocked ventilation passages.",
			"solution": "Performed complete heat exchanger cleaning using specialized degreasing chemicals and high-pressure steam cleaning. Replaced damaged exhaust ducting and verified proper ventilation airflow rates.",
			"parts": ["Heat Exchanger Cleaning Kit Industrial Grade", "Exhaust Duct Flexible 8-inch Diameter Aluminum", "Ventilation Damper Motorized 8-inch Round 120V"],
		},
	],
	"Mixers": [
		{
			"problem": "60-quart planetary mixer motor runs but bowl fails to rotate, with grinding noise coming from the planetary gear assembly during operation.",
			"solution": "Disassembled planetary gear assembly and found stripped main drive gear teeth. Replaced the damaged planetary drive gear and rebuilt the entire assembly with fresh lubrication.",
			"parts": ["Planetary Drive Gear Assembly P/N PG-60-2", "Gear Housing Gasket Set GS-PL60", "Food Grade Gear Oil SAE 90 (1 quart)"],
		},
		{
			"problem": "Spiral mixer speed controller display shows error code E04 and motor fails to start when mixing switch is engaged.",
			"solution": "Diagnosed faulty VFD output module causing the error code. Replaced the variable frequency drive unit and reprogrammed speed parameters to factory specifications.",
			"parts": ["VFD Controller 5HP 480V 3-Phase Model VF-5480", "VFD Programming Cable PC-VF5", "Control Fuse 5A 250V Fast-Acting"],
		},
		{
			"problem": "20-quart planetary mixer bowl lift mechanism operates sluggishly and fails to reach full height position, making loud clicking sounds during operation.",
			"solution": "Found worn bowl lift cam and damaged limit switch assembly. Replaced the lift cam mechanism and adjusted limit switch positioning for proper bowl height detection.",
			"parts": ["Bowl Lift Cam Assembly BL-20-CAM", "Bowl Height Limit Switch LS-BH20 SPDT", "Lift Chain 3/8 inch 24-link stainless steel"],
		},
		{
			"problem": "80-quart spiral mixer main motor bearing produces excessive heat and metal shavings are visible around the motor housing during extended mixing cycles.",
			"solution": "Removed motor from mixer frame and replaced failed main shaft bearings. Cleaned bearing races thoroughly and reassembled with proper bearing preload specifications.",
			"parts": ["Motor Shaft Bearing 6208-2RS Deep Groove Ball", "Motor Housing Bearing 6307-ZZ Shielded", "High Temperature Bearing Grease 400\u00b0F rated (4 oz tube)"],
		},
		{
			"problem": "Planetary mixer safety interlock prevents operation when bowl guard is properly closed and locked in position.",
			"solution": "Tested safety interlock switches and found misaligned bowl guard switch causing false open signal. Adjusted switch mounting bracket and replaced worn actuator pin.",
			"parts": ["Safety Interlock Switch SPST-NC 15A 250V", "Switch Actuator Pin 1/4 inch stainless steel", "Interlock Switch Mounting Bracket SG-20"],
		},
		{
			"problem": "Mixer attachment hub wobbles excessively during operation and fails to hold beater attachment securely, causing intermittent slipping.",
			"solution": "Disassembled attachment hub and found worn hub bushing and damaged retention spring. Replaced hub bushing and spring mechanism, then realigned hub concentricity.",
			"parts": ["Attachment Hub Bushing Bronze 1.5 inch ID", "Hub Retention Spring Assembly RS-ATT20", "Hub Alignment Shim Set 0.005-0.020 inch"],
		},
		{
			"problem": "40-quart mixer motor runs continuously regardless of timer setting and speed control position, indicating control circuit malfunction.",
			"solution": "Located stuck motor contactor causing continuous operation. Replaced the primary motor contactor and cleaned oxidized contact surfaces on control relay.",
			"parts": ["Motor Contactor 30A 3-pole 240V coil Model MC-30-240", "Control Relay 8-pin DPDT 24VDC", "Contact Cleaner Spray 12 oz aerosol"],
		},
		{
			"problem": "Spiral mixer gearbox temperature runs excessively hot at 180\u00b0F during normal operation and oil level appears adequate.",
			"solution": "Found contaminated gear oil with metal particles indicating internal wear. Drained gearbox completely, replaced oil seals, and refilled with fresh food-grade gear oil.",
			"parts": ["Gearbox Output Seal 2.5 inch Viton", "Input Shaft Seal 1.75 inch NBR", "Food Grade Gear Oil ISO 220 (2 gallons)"],
		},
		{
			"problem": "Planetary mixer operates normally at low speeds but motor trips circuit breaker when switched to high speed settings above speed 6.",
			"solution": "Measured motor current draw and found excessive amperage due to failed start capacitor. Replaced motor start capacitor and verified proper motor current on all speed settings.",
			"parts": ["Motor Start Capacitor 250\u00b5F 330VAC", "Run Capacitor 40\u00b5F 370VAC", "Capacitor Mounting Bracket CAP-MNT-20"],
		},
		{
			"problem": "60-quart mixer planetary shaft seized completely and cannot be rotated manually, with visible scoring marks on the shaft surface.",
			"solution": "Removed planetary assembly and found seized planetary shaft bearings due to lubrication failure. Replaced both upper and lower planetary shaft bearings and relubricated assembly.",
			"parts": ["Upper Planetary Bearing 6004-2RS Sealed", "Lower Planetary Bearing 6006-ZZ Shielded", "Planetary Shaft Seal Kit PSK-60"],
		},
		{
			"problem": "Mixer bowl lock mechanism engages but bowl rotates freely instead of remaining stationary during planetary mixing operation.",
			"solution": "Inspected bowl lock assembly and found worn lock pin and damaged cam surface. Replaced bowl lock pin assembly and resurfaced the bowl lock cam.",
			"parts": ["Bowl Lock Pin Assembly BLP-40-SS", "Lock Cam Surface Insert Hardened Steel", "Bowl Lock Spring Heavy Duty BLS-40"],
		},
		{
			"problem": "Speed controller responds to input commands but mixer operates only at maximum speed regardless of speed selector position.",
			"solution": "Diagnosed failed speed control potentiometer providing constant maximum signal to motor controller. Replaced speed control potentiometer and calibrated speed response curve.",
			"parts": ["Speed Control Potentiometer 10k\u03a9 Linear Taper", "Control Knob Assembly with Set Screw", "Potentiometer Dust Cover PC-10K"],
		},
		{
			"problem": "Spiral mixer automatic lubrication system fails to distribute oil to gearbox components, with lubrication pump motor running but no oil flow visible.",
			"solution": "Found clogged oil filter and failed oil pump causing lubrication system malfunction. Replaced oil pump assembly and installed new oil filtration system.",
			"parts": ["Automatic Oil Pump 24VDC 0.5 GPM", "Oil Filter Element 10 micron washable", "Oil Distribution Line 1/4 inch nylon tubing (10 feet)"],
		},
		{
			"problem": "Planetary mixer produces loud grinding noise during bowl rotation with visible metal debris collecting under the mixer base.",
			"solution": "Located failed bowl drive gear at bottom of mixer causing grinding noise and debris. Replaced bowl drive gear assembly and cleaned all contaminated oil from gear housing.",
			"parts": ["Bowl Drive Gear 48-tooth hardened steel", "Bowl Drive Bearing 6205-2RS", "Gear Housing Drain Plug with O-ring"],
		},
		{
			"problem": "Mixer motor starts normally but loses power progressively during operation until it stops completely after 10-15 minutes of runtime.",
			"solution": "Measured motor temperature and found overheating due to failed cooling fan and clogged motor ventilation. Replaced cooling fan motor and cleaned all ventilation passages.",
			"parts": ["Motor Cooling Fan 115VAC 4-inch diameter", "Fan Motor Mounting Bracket FM-20", "Motor Air Filter Washable Foam Type"],
		},
		{
			"problem": "80-quart planetary mixer motor capacitor bulged and leaked electrolyte, causing motor to struggle starting and run with reduced torque under load.",
			"solution": "Replaced failed run capacitor and cleaned electrolyte residue from motor housing, tested motor current draw and operation.",
			"parts": ["Motor Run Capacitor 45\u00b5F 370VAC", "Motor Start Capacitor 189-227\u00b5F 115VAC", "Capacitor Mounting Bracket"],
		},
		{
			"problem": "Spiral mixer VFD drive displays overheating alarm and shuts down after 5 minutes of operation, with cooling fan running but inadequate airflow.",
			"solution": "Cleaned blocked heat sink fins and replaced failed cooling fan, updated VFD thermal protection parameters.",
			"parts": ["Axial Cooling Fan 120VAC 172mm x 51mm", "VFD Heat Sink Compound", "Air Filter Element 6x12 inches"],
		},
		{
			"problem": "20-quart mixer agitator shaft bearing produces metallic grinding noise and exhibits 0.125-inch radial play during rotation.",
			"solution": "Pressed out worn bearing assembly and installed new sealed ball bearing with proper preload torque specification.",
			"parts": ["Deep Groove Ball Bearing 6309-2RS", "Bearing Retaining Ring 45mm", "Food Grade Bearing Grease NLGI-2"],
		},
		{
			"problem": "Planetary mixer electrical contactor chatters continuously when energized and fails to hold contacts closed, causing intermittent motor operation.",
			"solution": "Replaced worn contactor assembly and adjusted control voltage to proper 24VAC level, cleaned all electrical connections.",
			"parts": ["Motor Contactor 3-Pole 40A 120VAC Coil", "Auxiliary Contact Block NO/NC", "Terminal Block 10-Position"],
		},
		{
			"problem": "60-quart mixer bowl lift hydraulic cylinder leaks fluid internally causing bowl to drift downward under load during operation.",
			"solution": "Rebuilt hydraulic cylinder with new seals and O-rings, replaced contaminated hydraulic fluid with food-grade oil.",
			"parts": ["Hydraulic Cylinder Seal Kit", "Food Grade Hydraulic Oil ISO 32", "Hydraulic Filter Element 10-Micron"],
		},
		{
			"problem": "Spiral mixer transmission output shaft keyway sheared completely, preventing power transfer from motor to mixing paddle assembly.",
			"solution": "Machined new keyway in output shaft and replaced sheared Woodruff key, aligned coupling and torqued to specification.",
			"parts": ["Woodruff Key 1/4 x 1-1/4 inch", "Output Shaft Coupling", "Thread Locking Compound"],
		},
		{
			"problem": "Planetary mixer timer mechanism sticks at 15-minute position and fails to advance, leaving mixer running beyond set time limits.",
			"solution": "Disassembled timer assembly and cleaned internal contacts, replaced worn timer motor and calibrated timing sequence.",
			"parts": ["Timer Motor 120VAC 1RPM", "Timer Contact Assembly", "Timer Dial Face"],
		},
		{
			"problem": "40-quart mixer bowl clamp assembly loosens during operation allowing bowl to shift position and contact mixing attachment.",
			"solution": "Replaced worn bowl clamp springs and adjusted clamp tension mechanism, resurfaced contact surfaces.",
			"parts": ["Bowl Clamp Spring Set", "Clamp Adjustment Screw M12x1.5", "Bowl Positioning Pin"],
		},
		{
			"problem": "Mixer main motor overheating protection relay trips repeatedly during normal operation despite motor running at proper amperage.",
			"solution": "Replaced defective thermal overload relay and recalibrated trip setting to motor nameplate current rating.",
			"parts": ["Thermal Overload Relay 15-22A Range", "Relay Contact Block", "Motor Temperature Sensor"],
		},
		{
			"problem": "Spiral mixer dough hook attachment loosens during heavy mixing cycles due to worn attachment hub threads and retention mechanism.",
			"solution": "Re-threaded attachment hub with thread repair insert and replaced worn retaining collar with new locking design.",
			"parts": ["Thread Repair Insert M24x2.0", "Attachment Retaining Collar", "Hub Locking Pin"],
		},
		{
			"problem": "Planetary mixer speed selector switch contacts are burned and pitted, causing erratic speed changes and motor hesitation.",
			"solution": "Replaced entire speed selector switch assembly and cleaned carbon deposits from switch housing and terminals.",
			"parts": ["Multi-Position Rotary Switch 12-Position", "Switch Contact Cleaner Spray", "Switch Terminal Block"],
		},
		{
			"problem": "60-quart mixer transmission input bearing races show pitting and scoring, creating vibration that increases with operating speed.",
			"solution": "Disassembled transmission and replaced both input shaft bearings, realigned input coupling to eliminate side loading.",
			"parts": ["Tapered Roller Bearing 32008", "Bearing Lock Nut M40x1.5", "Input Shaft Seal 40x62x8mm"],
		},
		{
			"problem": "Mixer control transformer primary winding shorted to ground causing 120VAC control circuit to lose power intermittently.",
			"solution": "Replaced damaged control transformer and upgraded to higher VA rating, installed new fuse holder with indicator.",
			"parts": ["Control Transformer 480/120VAC 250VA", "Fuse Holder with LED Indicator", "Control Circuit Fuse 2A Fast-Acting"],
		},
		{
			"problem": "Spiral mixer bowl rotation bearing seized due to water contamination and corrosion, preventing bowl from turning during mixing.",
			"solution": "Removed corroded bearing assembly and installed stainless steel replacement bearing with improved sealing system.",
			"parts": ["Stainless Steel Ball Bearing 6218-SS", "Nitrile Bowl Seal 90x110x12mm", "Bearing Housing Gasket"],
		},
		{
			"problem": "Planetary mixer agitator height adjustment mechanism binding prevents proper clearance setting between beater and bowl bottom.",
			"solution": "Disassembled height adjustment assembly and replaced worn lead screw and bronze nut, lubricated all moving parts.",
			"parts": ["Adjustment Lead Screw M16x2.0", "Bronze Lead Screw Nut", "Food Grade Assembly Grease"],
		},
		{
			"problem": "40-quart planetary mixer emergency stop button remains stuck in pressed position and cannot be reset, preventing any mixer operation despite all other controls functioning normally.",
			"solution": "Replaced faulty emergency stop switch assembly and cleaned accumulated flour debris from the switch housing mechanism that was preventing proper reset operation.",
			"parts": ["Emergency Stop Switch Assembly NCR 22mm Red Mushroom Head", "Switch Contact Block NO/NC 10A 600V", "Switch Mounting Collar Chrome Plated"],
		},
		{
			"problem": "Spiral mixer transmission input shaft coupling exhibits severe wear with 0.25-inch end play, causing excessive vibration and misalignment between motor and gearbox.",
			"solution": "Installed new flexible jaw coupling and realigned motor-to-transmission assembly using precision dial indicators to achieve 0.003-inch maximum total indicator runout.",
			"parts": ["Flexible Jaw Coupling L095 1.5-inch Bore", "Coupling Spider Insert Polyurethane 95A Durometer", "Motor Mounting Bolts Grade 8 M12x1.75x60mm"],
		},
		{
			"problem": "20-quart mixer bowl tilt mechanism hydraulic pump motor runs continuously but fails to build pressure, with oil reservoir level dropping rapidly during operation.",
			"solution": "Replaced worn hydraulic pump assembly and rebuilt hydraulic cylinder with new seals, then refilled system with ISO 32 hydraulic fluid and bled all air.",
			"parts": ["Hydraulic Gear Pump 0.5 GPM 1800 RPM", "Hydraulic Cylinder Seal Kit 2-inch Bore", "Hydraulic Fluid ISO 32 Anti-Wear 5 Gallon"],
		},
		{
			"problem": "Planetary mixer dough hook attachment falls off during operation due to worn attachment hub threads that no longer maintain secure connection.",
			"solution": "Machined hub threads to oversize specification and installed threaded insert sleeve, then applied thread-locking compound to ensure secure attachment retention.",
			"parts": ["Threaded Insert Sleeve Stainless Steel 1.25-inch", "Thread-Locking Compound Loctite 243 Medium Strength", "Hub Retaining Washer Hardened Steel"],
		},
		{
			"problem": "80-quart spiral mixer VFD parameter settings corrupted causing motor to run in reverse direction and operate at incorrect frequency despite proper input commands.",
			"solution": "Performed VFD factory reset and reprogrammed all operational parameters including motor nameplate data, acceleration/deceleration times, and direction control settings.",
			"parts": ["VFD Programming Cable USB to RS485", "VFD Parameter Manual and Software CD", "VFD Display Module Replacement LCD"],
		},
		{
			"problem": "Planetary mixer bowl guard proximity sensor fails to detect closed position causing safety interlock to prevent mixer startup even with guard properly installed.",
			"solution": "Replaced defective inductive proximity sensor and adjusted sensor mounting bracket to achieve 2mm sensing gap with proper LED indication during guard closure.",
			"parts": ["Inductive Proximity Sensor M18 PNP 10-30VDC", "Sensor Mounting Bracket Adjustable Stainless Steel", "Sensor Cable 3-Wire Shielded 10 Meter"],
		},
		{
			"problem": "60-quart mixer planetary gear assembly oil seal leaks continuously creating oil puddle under mixer and contaminating food preparation area with lubricant.",
			"solution": "Disassembled planetary housing and replaced worn oil seal with proper installation tools, then refilled gearbox with synthetic gear oil to specification level.",
			"parts": ["Oil Seal Double Lip Viton 2.5-inch Shaft", "Synthetic Gear Oil ISO VG 220 1 Quart", "Seal Installation Tool Set Metric"],
		},
		{
			"problem": "Spiral mixer main motor thermal overload relay trips repeatedly after 3-5 minutes of operation under normal load conditions indicating overheating protection activation.",
			"solution": "Cleaned motor cooling fan and air passages, then replaced thermal overload relay with correct amperage rating and verified motor current draw within specifications.",
			"parts": ["Thermal Overload Relay 15-22 Amp Range", "Motor Cooling Fan Blade 6-inch Diameter", "Fan Motor Bearings Sealed Ball Bearing Set"],
		},
		{
			"problem": "20-quart planetary mixer speed selector switch intermittently fails to make contact at speed positions 4 and 6, causing mixer to skip these speeds during operation.",
			"solution": "Disassembled rotary switch assembly and cleaned oxidized contacts with electrical contact cleaner, then replaced worn contact springs and applied dielectric grease.",
			"parts": ["Rotary Switch Contact Kit 8-Position", "Electrical Contact Cleaner Spray 12oz", "Dielectric Grease High Temperature 4oz Tube"],
		},
		{
			"problem": "Mixer motor control circuit exhibits intermittent power interruption with lights dimming and motor stuttering during startup indicating loose electrical connections.",
			"solution": "Tightened all electrical connections in control panel and motor junction box, then applied anti-oxidant compound to prevent corrosion and ensure reliable contact.",
			"parts": ["Anti-Oxidant Electrical Compound 4oz Tube", "Wire Nuts Assorted Pack 10-14 AWG", "Terminal Block Screws Stainless Steel M4x12mm"],
		},
		{
			"problem": "Planetary mixer agitator shaft develops 0.050-inch axial play allowing vertical movement that affects mixing consistency and causes bowl contact during operation.",
			"solution": "Replaced worn thrust bearing assembly and adjusted preload to eliminate axial play while maintaining smooth rotation without binding or excessive drag.",
			"parts": ["Thrust Bearing Assembly 1.5-inch Bore", "Bearing Lock Nut KM Series M30x1.5", "Bearing Preload Spring Disc Washer Set"],
		},
		{
			"problem": "80-quart mixer gearbox drain plug stripped threads preventing proper oil changes and causing minor oil seepage during operation.",
			"solution": "Drilled out damaged drain plug and installed threaded insert with sealant, then performed complete oil change with synthetic gear lubricant and new drain plug.",
			"parts": ["Threaded Insert M14x1.5 Stainless Steel", "Thread Sealant Pipe Dope High Temperature", "Magnetic Drain Plug M14x1.5 with Gasket"],
		},
		{
			"problem": "Spiral mixer limit switch for bowl position fails to activate when bowl reaches upper limit causing bowl lift to over-travel and jam against mechanical stops.",
			"solution": "Replaced defective limit switch and adjusted actuator arm positioning to ensure reliable switching at proper bowl height with adequate overtravel protection.",
			"parts": ["Heavy Duty Limit Switch DPDT 15A 250V", "Adjustable Actuator Arm Roller Bearing Type", "Limit Switch Mounting Bracket Zinc Plated"],
		},
		{
			"problem": "Planetary mixer timer mechanism fails to advance properly causing mixing cycle to run continuously without automatic shut-off after preset time interval.",
			"solution": "Replaced mechanical timer motor and gear assembly, then calibrated timing mechanism to ensure accurate cycle control within \u00b15% of set time periods.",
			"parts": ["Timer Motor Assembly 60Hz Synchronous", "Timer Gear Reduction Unit 60:1 Ratio", "Timer Dial Calibration Decal Set"],
		},
		{
			"problem": "60-quart mixer planetary drive pinion gear exhibits chipped teeth and excessive backlash causing rough operation and metallic clicking sounds during mixing cycles.",
			"solution": "Replaced damaged pinion gear and mating ring gear assembly, then adjusted gear mesh pattern and backlash to manufacturer specifications using dial indicator.",
			"parts": ["Planetary Drive Pinion Gear 24-Tooth Hardened Steel", "Planetary Ring Gear Assembly Heat Treated", "Gear Mesh Compound Blue Prussian 2oz Tube"],
		},
		{
			"problem": "30-quart planetary mixer transmission oil seal failed, causing lubricant to leak onto the floor and contaminate food preparation area. Gearbox oil level dropped below minimum line and internal components show signs of inadequate lubrication.",
			"solution": "Replaced transmission input shaft oil seal and replenished gearbox with proper grade lubricant. Cleaned contaminated areas and verified seal integrity through extended operational test.",
			"parts": ["Transmission input shaft oil seal 45mm x 65mm x 10mm Viton", "Gearbox lubricant ISO VG 220 synthetic gear oil 2-liter bottle", "Gasket sealant high-temperature food-grade silicone"],
		},
		{
			"problem": "Spiral mixer dough hook attachment slips during heavy bread dough mixing, with visible wear on the drive hub splines. Attachment cannot maintain proper engagement under normal operating loads.",
			"solution": "Machined and rebuilt attachment hub with oversize hardened steel splines, then fitted matching oversize splined dough hook. Torque specifications verified to manufacturer standards.",
			"parts": ["Attachment hub assembly hardened steel 1.5-inch bore with keyway", "Spiral dough hook 80-quart capacity with reinforced spline connection", "Drive hub retaining bolt Grade 8 M16 x 2.0 x 50mm"],
		},
		{
			"problem": "40-quart planetary mixer bowl lift motor thermal protector trips repeatedly during normal operation, preventing bowl positioning. Motor housing temperature reaches 160\u00b0F within 5 minutes of operation.",
			"solution": "Replaced bowl lift motor with identical specification unit and cleaned debris from motor cooling vents. Verified proper amperage draw and thermal protector reset functionality.",
			"parts": ["Bowl lift motor 1/3 HP 115V 1725 RPM single-phase with thermal protection", "Motor mounting bracket galvanized steel with vibration dampeners", "Thermal protector switch automatic reset 130\u00b0F trip point"],
		},
		{
			"problem": "20-quart mixer planetary beater shaft bushing shows excessive wear causing 0.200-inch radial movement and uneven mixing patterns. Bronze bushing material is visibly scored and worn beyond service limits.",
			"solution": "Pressed out worn bronze bushing and installed new oversized bushing, then machined shaft journal to restore proper clearances. Applied food-grade bearing grease per service manual specifications.",
			"parts": ["Planetary shaft bronze bushing 1.250-inch ID x 1.500-inch OD x 1.000-inch length", "Shaft journal repair sleeve hardened steel 1.250-inch diameter", "Food-grade bearing grease NLGI Grade 2 lithium complex 14-ounce cartridge"],
		},
		{
			"problem": "Spiral mixer VFD parameter settings corrupted causing erratic speed control and motor stalling at low frequencies. Drive displays fault code F008 indicating parameter configuration error.",
			"solution": "Performed factory reset of VFD parameters and reprogrammed all motor control settings according to equipment specifications. Conducted full speed range calibration and load testing.",
			"parts": ["Variable frequency drive 5 HP 480V three-phase with integrated keypad", "VFD input line reactor 5% impedance 480V 10-amp rating", "Parameter backup module EEPROM with factory default settings"],
		},
	],
	"Refrigeration": [
		{
			"problem": "Walk-in cooler compressor short cycling every 2-3 minutes with high head pressure readings of 350 PSI on R-404A system. Unit unable to maintain temperature below 45\u00b0F.",
			"solution": "Replaced failed condenser fan motor and cleaned heavily fouled condenser coils with coil cleaner and pressure washing. Adjusted TXV superheat to 8\u00b0F.",
			"parts": ["Condenser Fan Motor 1/3 HP 208-230V 1075 RPM", "TXV Valve R-404A 3 Ton Sporlan TFVE-3", "Nu-Calgon Evap Foam No Rinse Coil Cleaner"],
		},
		{
			"problem": "Three-door reach-in freezer experiencing ice buildup on evaporator coils with defrost cycle not completing. Temperature rising to 15\u00b0F during peak hours.",
			"solution": "Replaced faulty defrost heater and defrost termination thermostat, then reprogrammed defrost timer for 4 cycles per 24 hours with 30-minute duration.",
			"parts": ["Defrost Heater 240V 800W 18-inch", "Defrost Termination Thermostat 45\u00b0F", "Paragon 8145-00 Defrost Timer"],
		},
		{
			"problem": "Display case compressor running continuously with evaporator fan motor making grinding noise and reduced airflow. Case temperature at 42\u00b0F instead of target 35\u00b0F.",
			"solution": "Replaced seized evaporator fan motor and cleaned debris from fan blade assembly. Checked and topped off refrigerant charge to proper subcooling of 12\u00b0F.",
			"parts": ["Evaporator Fan Motor 1/25 HP 115V Shaded Pole", "Fan Blade 8-inch CW Rotation", "R-134a Refrigerant 30 lb Cylinder"],
		},
		{
			"problem": "Walk-in freezer door not sealing properly with visible gaps at corners causing frost buildup around door frame. Internal temperature fluctuating between -5\u00b0F and 5\u00b0F.",
			"solution": "Replaced worn magnetic door gasket and adjusted door hinges for proper alignment. Applied food-grade silicone sealant to corner gaps.",
			"parts": ["Magnetic Door Gasket 84-inch x 30-inch Gray", "Stainless Steel Hinge Heavy Duty 6-inch", "Food Grade Silicone Sealant Clear"],
		},
		{
			"problem": "Prep table refrigerator thermostat stuck at maximum cooling setting causing overcooling to 28\u00b0F and freezing stored vegetables. Compressor cycling normally but temperature cannot be adjusted.",
			"solution": "Replaced faulty mechanical thermostat with digital temperature controller and recalibrated temperature range to 35-38\u00b0F operating band.",
			"parts": ["Digital Temperature Controller Dixell XR10CX", "Temperature Sensor NTC 10K Ohm", "Control Box Enclosure 6x4x2 inch NEMA 4"],
		},
		{
			"problem": "Ice machine/storage bin combination unit producing ice normally but melting rapidly in storage bin. Drain pan overflowing and water pooling on floor underneath unit.",
			"solution": "Replaced cracked drain pan and installed new drain heater assembly. Cleared blocked drain line and improved insulation around storage bin walls.",
			"parts": ["Drain Pan Assembly 24-inch Stainless Steel", "Drain Heater 120V 100W", "Rigid Foam Insulation 2-inch R-13"],
		},
		{
			"problem": "Two-door reach-in cooler compressor not starting with start relay clicking repeatedly. Digital display showing error code and internal temperature rising above 50\u00b0F.",
			"solution": "Diagnosed failed compressor start capacitor and potential relay. Replaced both components and tested amp draw during startup sequence.",
			"parts": ["Start Capacitor 88-108 MFD 330V", "Potential Relay 220V Pickup 170V Dropout", "Hard Start Kit 3-in-1 Universal"],
		},
		{
			"problem": "Deli display case with curved glass front showing heavy condensation on interior glass surface obscuring product visibility. Case maintaining proper temperature but high humidity levels.",
			"solution": "Replaced malfunctioning anti-sweat heater elements in glass frame and adjusted humidity control settings. Sealed air gaps around glass mounting hardware.",
			"parts": ["Anti-Sweat Heater Element 120V 200W", "Humidity Control Switch 24V", "Structural Glazing Tape 1/4-inch"],
		},
		{
			"problem": "Walk-in cooler evaporator coil completely iced over with no defrost occurring. Defrost timer motor not advancing and unit running in continuous cooling mode.",
			"solution": "Replaced seized defrost timer motor and recalibrated timer wheel position. Manually initiated defrost cycle and monitored complete ice removal.",
			"parts": ["Defrost Timer Motor 120V 60Hz Paragon", "Timer Dial Assembly 24-hour", "Defrost Bi-Metal Switch 35\u00b0F Open"],
		},
		{
			"problem": "Beverage cooler with glass doors experiencing refrigerant leak at TXV connection with hissing sound audible. System low on charge and struggling to cool below 50\u00b0F.",
			"solution": "Located and repaired refrigerant leak at TXV flare fitting, evacuated system to 500 microns, and recharged with proper R-134a quantity per nameplate specifications.",
			"parts": ["TXV Valve R-134a 1.5 Ton Danfoss TEN-2", "Flare Fitting 1/2-inch Brass", "R-134a Refrigerant 15 lb Cylinder"],
		},
		{
			"problem": "Sandwich prep unit compressor overheating and shutting off on thermal protection with internal overload tripping every 10 minutes. Compressor housing too hot to touch.",
			"solution": "Cleaned blocked condenser coils and replaced failed condenser fan capacitor causing reduced airflow. Verified proper compressor amp draw and cooling operation.",
			"parts": ["Run Capacitor 40 MFD 370V Oval", "Condenser Fan Blade 12-inch CCW", "Compressor Overload Protector"],
		},
		{
			"problem": "Four-door freezer section losing temperature overnight with one evaporator fan not operating. Ice crystals forming on non-working fan motor housing.",
			"solution": "Replaced burned-out evaporator fan motor and damaged wire harness connector. Tested electrical continuity and verified proper voltage supply to motor terminals.",
			"parts": ["Evaporator Fan Motor 1/40 HP 115V", "Wire Harness Connector 4-pin Weatherproof", "Motor Mounting Bracket Adjustable"],
		},
		{
			"problem": "Salad bar refrigeration system drain line backing up causing water damage to floor and electrical components. Drain heater not warming drain pan adequately.",
			"solution": "Cleared blocked drain line with CO2 pressure and replaced low-wattage drain heater with higher capacity unit. Installed drain pan overflow alarm.",
			"parts": ["Drain Line Heater 120V 200W", "Drain Pan Alarm Float Switch", "PVC Drain Fittings 3/4-inch Kit"],
		},
		{
			"problem": "Pizza prep table refrigerator experiencing electrical issues with lights flickering and temperature control display intermittently going blank. Unit cooling inconsistently.",
			"solution": "Diagnosed loose electrical connections in main control panel and replaced corroded wire terminals. Updated control board firmware and tested all electrical circuits.",
			"parts": ["Control Board Assembly Universal PCB", "Wire Terminal Kit Insulated Spade", "LED Light Strip 120V 36-inch"],
		},
		{
			"problem": "Wine display cooler maintaining temperature but producing excessive noise from compressor area with vibrations felt throughout cabinet structure. Customer complaints about noise levels.",
			"solution": "Replaced worn compressor mounting grommets and realigned compressor position. Installed additional vibration dampening pads and sound insulation material.",
			"parts": ["Compressor Mounting Grommets Set of 4", "Vibration Dampening Pads 6x6 inch", "Acoustic Foam Insulation 1-inch Thick"],
		},
		{
			"problem": "Walk-in freezer condenser fan motor seized with bearing failure, causing high head pressure alarms and compressor thermal shutdown. System cycling on high pressure cutout every 5 minutes.",
			"solution": "Replaced failed condenser fan motor and cleaned condenser coils of grease buildup. Reset high pressure cutout switch and verified proper refrigerant pressures.",
			"parts": ["Condenser Fan Motor 1/2 HP 208-230V 1075 RPM", "High Pressure Cutout Switch R-404A 400/320 PSI", "Motor Mounting Bracket 12-inch Galvanized Steel"],
		},
		{
			"problem": "Reach-in cooler expansion valve hunting with temperature swings between 32\u00b0F and 45\u00b0F every 15 minutes. Superheat readings fluctuating between 5\u00b0F and 25\u00b0F at evaporator outlet.",
			"solution": "Replaced thermostatic expansion valve with correct tonnage rating and adjusted superheat setting to 8-10\u00b0F. Cleaned moisture from refrigerant lines and replaced filter drier.",
			"parts": ["Thermostatic Expansion Valve R-134A 3-Ton Sporlan TFVE-3", "Liquid Line Filter Drier 3/8 inch SAE Flare", "Sensing Bulb Clamp 7/8 inch Copper Tube"],
		},
		{
			"problem": "Bakery display case defrost heater elements burned out causing incomplete defrost cycles and ice accumulation blocking airflow. Case struggling to maintain 38\u00b0F during defrost recovery.",
			"solution": "Replaced all three defrost heater elements and defrost termination thermostat. Reprogrammed defrost timer for 45-minute cycles every 8 hours with 35\u00b0F termination temperature.",
			"parts": ["Electric Defrost Heater 240V 500W 24-inch Stainless Steel", "Defrost Termination Thermostat 35\u00b0F Cut-in/55\u00b0F Cut-out", "Defrost Timer 8-Hour Cycle 240V SPDT Contacts"],
		},
		{
			"problem": "Meat display case refrigeration system losing oil with oil separator malfunctioning and compressor running hot. Low oil pressure alarm triggering after 30 minutes of operation.",
			"solution": "Replaced faulty oil separator and oil return solenoid valve. Added 32 ounces of POE oil to system and verified oil return operation through sight glass.",
			"parts": ["Oil Separator 1-5/8 inch ODF R-404A Rated", "Oil Return Solenoid Valve 1/4 inch 24V AC", "Polyol Ester Oil POE 32 ISO VG 1-Gallon Container"],
		},
		{
			"problem": "Walk-in cooler door closer mechanism broken with door not self-closing properly, causing warm air infiltration. Internal temperature climbing to 50\u00b0F during busy periods.",
			"solution": "Replaced hydraulic door closer assembly and adjusted closing speed and latching force. Aligned door frame and replaced worn door strike plate for proper seal engagement.",
			"parts": ["Hydraulic Door Closer Heavy Duty Commercial Grade", "Door Strike Plate Stainless Steel Adjustable", "Door Closer Mounting Hardware Kit Grade 8 Bolts"],
		},
		{
			"problem": "Ice cream dipping cabinet compressor short cycling on low pressure cutout with refrigerant leak at evaporator coil connection. System charge critically low at 45 PSI suction pressure.",
			"solution": "Located and repaired pinhole leak in evaporator coil using silver solder. Evacuated system to 500 microns and recharged with proper R-404A refrigerant amount per nameplate.",
			"parts": ["Silver Solder Rod 15% Silver 1/8 inch Diameter", "Low Pressure Cutout Switch R-404A 5/25 PSI", "Service Valve Core 1/4 inch SAE Standard"],
		},
		{
			"problem": "Beverage cooler electronic temperature controller displaying 'Sensor Error' code with erratic temperature readings. Actual temperature at 55\u00b0F while display shows -20\u00b0F intermittently.",
			"solution": "Replaced defective temperature sensor probe and controller display module. Recalibrated temperature settings and verified sensor resistance values at various temperatures.",
			"parts": ["Temperature Sensor Probe 10K Ohm Thermistor 6-foot Cable", "Electronic Temperature Controller Digital Display 120V", "Sensor Mounting Well 1/4 inch NPT Brass"],
		},
		{
			"problem": "Deli meat slicer refrigerated base losing cooling capacity with evaporator coil frosted over and drain pan heater not functioning. Condensate backing up into cabinet interior.",
			"solution": "Replaced failed drain pan heater and cleaned blocked drain line with hot water flush. Installed new drain pan with improved slope for proper drainage.",
			"parts": ["Drain Pan Heater 120V 80W Silicone Pad Type", "Drain Pan Stainless Steel 18 x 12 x 2 inch", "Drain Line 5/8 inch ID Clear Vinyl Tubing"],
		},
		{
			"problem": "Produce cooler dual temperature system with one zone maintaining 34\u00b0F while other zone running at 50\u00b0F. Zone damper actuator motor not responding to temperature controller signals.",
			"solution": "Replaced defective zone damper actuator motor and recalibrated damper position sensors. Adjusted airflow balance between zones and verified independent temperature control operation.",
			"parts": ["Zone Damper Actuator Motor 24V AC 90 Second Rotation", "Temperature Control Sensor RTD Platinum 100 Ohm", "Damper Blade Assembly 8 x 6 inch Aluminum Frame"],
		},
		{
			"problem": "Frozen yogurt machine refrigeration condenser coil heavily blocked with lint and debris causing high ambient cutout trips. Unit shutting down every hour during peak service.",
			"solution": "Thoroughly cleaned condenser coil using coil cleaning chemicals and high-pressure water rinse. Replaced clogged air filter and adjusted condenser fan speed for improved airflow.",
			"parts": ["Condenser Coil Cleaner Heavy Duty Alkaline 1-Gallon", "Air Filter Washable Aluminum Mesh 16 x 20 x 1 inch", "Fan Speed Controller Variable 115V 5-Amp Rating"],
		},
		{
			"problem": "Walk-in freezer floor heating system not operating with floor ice buildup creating safety hazard. Floor heating cables showing no continuity and moisture intrusion evident.",
			"solution": "Removed damaged floor heating cables and installed new self-regulating heating cable system. Applied waterproof membrane and sealed all cable entry points to prevent moisture infiltration.",
			"parts": ["Self-Regulating Floor Heating Cable 240V 8 Watts/Foot", "Floor Heating Thermostat 35\u00b0F On/45\u00b0F Off NEMA 4X", "Cable Junction Box Waterproof NEMA 4X Rating"],
		},
		{
			"problem": "Cheese display case refrigeration system experiencing liquid floodback with compressor making knocking sounds during startup. Suction line warm to touch near compressor inlet.",
			"solution": "Installed suction line accumulator to prevent liquid refrigerant from entering compressor. Adjusted TXV superheat setting higher and insulated suction line to prevent condensation.",
			"parts": ["Suction Line Accumulator 1-3/8 inch ODF R-134A Rated", "Suction Line Insulation 7/8 inch ID Closed Cell Foam", "TXV Superheat Spring Kit 8-12\u00b0F Range Adjustment"],
		},
		{
			"problem": "Prep table refrigerator experiencing electrical power fluctuations with compressor contactor chattering and lights dimming during compressor startup. Voltage dropping to 195V during start.",
			"solution": "Installed hard start kit with potential relay and start capacitor to reduce inrush current. Upgraded electrical supply wiring to handle compressor starting load and verified proper grounding.",
			"parts": ["Hard Start Kit Potential Relay 330V Pick-up 250V Drop-out", "Start Capacitor 88-108 MFD 330V AC Electrolytic", "Electrical Wire 12 AWG THHN Stranded Copper 25-foot"],
		},
		{
			"problem": "Salad bar sneeze guard refrigeration coils sweating excessively with condensate dripping onto food products. Humidity levels high and air circulation inadequate around coil area.",
			"solution": "Installed condensate management system with collection trough and improved drainage. Added circulation fan to reduce humidity levels and prevent condensation on cooling coils.",
			"parts": ["Condensate Collection Trough Stainless Steel 48-inch Length", "Circulation Fan 115V 50 CFM Axial Flow", "Humidity Control Damper 6-inch Motorized 24V AC"],
		},
		{
			"problem": "Blast chiller refrigeration system experiencing oil foaming in sight glass with compressor running erratically and cooling capacity reduced by 40%. System recently serviced with refrigerant added.",
			"solution": "Evacuated system and found moisture contamination causing oil breakdown. Replaced compressor oil, filter drier, and performed triple evacuation to 250 microns before recharging with dry refrigerant.",
			"parts": ["Compressor Oil POE 46 ISO VG 1-Quart Moisture-Free", "Bi-Flow Filter Drier 1/2 inch ODF 100% Activated Alumina", "Vacuum Pump Oil 1-Quart High Vacuum Grade"],
		},
		{
			"problem": "Commercial freezer condenser coil severely blocked with grease and debris causing high discharge temperatures of 180\u00b0F and compressor overheating. System shutting down on thermal protection every 20 minutes.",
			"solution": "Performed thorough condenser coil cleaning with coil cleaner and pressure washing, then installed condenser coil guard to prevent future contamination. Verified proper airflow and normal discharge temperatures.",
			"parts": ["Condenser Coil Guard 24x36 inch aluminum mesh", "Coil cleaner concentrate Nu-Calgon Cal-Foam", "High temperature cutout switch 180\u00b0F manual reset"],
		},
		{
			"problem": "Reach-in refrigerator experiencing erratic temperature control with digital thermostat displaying incorrect readings 10\u00b0F higher than actual. Compressor cycling inappropriately based on false readings.",
			"solution": "Replaced faulty temperature sensor and recalibrated digital controller to factory specifications. Verified accurate temperature readings and proper compressor cycling.",
			"parts": ["Temperature sensor probe 10K ohm thermistor 6-foot cable", "Digital temperature controller Dixell XR20CX 120V", "Sensor mounting bracket stainless steel"],
		},
		{
			"problem": "Walk-in cooler experiencing liquid refrigerant flooding back to compressor with loud knocking sounds and oil foaming in sight glass. Compressor at risk of mechanical damage from liquid slugging.",
			"solution": "Installed liquid line solenoid valve and adjusted TXV superheat setting to 12\u00b0F to prevent liquid flood-back. Added suction line accumulator for additional protection.",
			"parts": ["Liquid line solenoid valve Alco 240RA8T4 3/8 inch 120V", "Suction accumulator Parker HAD-164-S 1-5/8 inch", "TXV Sporlan ORIT-6 R-404A 3/8 x 1/2 inch"],
		},
		{
			"problem": "Ice maker water curtain freezer showing premature compressor bearing failure with metallic grinding noise and excessive vibration. Compressor amperage drawing 15% above nameplate rating.",
			"solution": "Replaced failed hermetic compressor and installed vibration dampeners to reduce cabinet stress. Added hard start kit to reduce starting torque on new compressor.",
			"parts": ["Hermetic compressor Tecumseh AEA4440EXA 1/2 HP R-404A", "Hard start kit Supco 3-in-1 RCO410", "Vibration dampener mounts rubber 1/4-20 thread"],
		},
		{
			"problem": "Salad bar refrigeration unit drain pan heater not functioning causing ice blockage in drain line and water backing up into cabinet. Standing water creating sanitation concerns.",
			"solution": "Replaced burned out drain pan heater element and installed new drain pan thermostat with proper temperature differential. Cleared ice blockage and sanitized affected areas.",
			"parts": ["Drain pan heater element 120V 50W silicone", "Drain pan thermostat Ranco A30-3210 SPST 35\u00b0F", "Drain line insulation foam tube 1/2 inch ID"],
		},
		{
			"problem": "Beverage merchandiser compressor start capacitor swollen and leaking with compressor failing to start consistently. Unit attempting to start but motor not engaging properly.",
			"solution": "Replaced failed start capacitor and tested start relay functionality. Verified proper compressor starting sequence and measured correct running amperage.",
			"parts": ["Start capacitor 88-108 MFD 330V round", "Start relay Supco 3ARR3-TC73 120V", "Overload protector Tecumseh 9532-007"],
		},
		{
			"problem": "Deli case evaporator drain system frozen solid with ice dam preventing defrost water drainage. Water overflowing onto product shelves during defrost cycles.",
			"solution": "Installed higher wattage drain line heater and improved insulation around drain pan. Modified drain slope for better gravity flow and added drain line thermostat.",
			"parts": ["Drain line heater cable 120V 7W per foot", "Drain pan insulation kit reflective bubble wrap", "Drain slope adjustment brackets stainless steel"],
		},
		{
			"problem": "Walk-in freezer insulation panels showing deterioration with visible ice formation between wall panels and significant energy loss. Interior frost patterns indicating thermal bridging.",
			"solution": "Replaced damaged insulation panels and sealed all joints with appropriate sealant. Installed vapor barrier and verified proper panel alignment to eliminate thermal bridges.",
			"parts": ["Insulation panel polyurethane 4-inch thick 4x8 foot", "Panel sealant Dow Corning 732 RTV clear", "Vapor barrier tape aluminum foil 3-inch width"],
		},
		{
			"problem": "Reach-in cooler condenser fan motor shaft bearing seized causing fan blade wobble and reduced airflow across condenser coils. Head pressure climbing above normal operating range.",
			"solution": "Replaced condenser fan motor and balanced fan blade assembly. Verified proper motor mounting and measured correct CFM airflow across condenser coil.",
			"parts": ["Condenser fan motor 1/6 HP 208-230V 1075 RPM", "Fan blade 10-inch diameter 3-blade aluminum", "Motor mounting bracket galvanized steel adjustable"],
		},
		{
			"problem": "Pizza prep cooler refrigerant circuit showing signs of moisture contamination with acid formation and copper plating on compressor internals. System performance declining rapidly.",
			"solution": "Performed complete system evacuation and installed oversized filter drier. Added sight glass with moisture indicator and recharged system with fresh refrigerant after triple evacuation.",
			"parts": ["Filter drier Sporlan C-164-S 1/2 inch liquid line", "Sight glass Alco AMI-200S with moisture indicator", "Refrigerant R-134a 30 lb cylinder"],
		},
		{
			"problem": "Commercial chest freezer lid gasket torn and compressed allowing warm air infiltration and excessive frost buildup around lid perimeter. Compressor runtime increased 40%.",
			"solution": "Replaced entire lid gasket and adjusted lid alignment for proper sealing. Cleaned gasket channel and applied food-grade lubricant to maintain seal flexibility.",
			"parts": ["Lid gasket magnetic strip 72-inch length gray", "Gasket adhesive 3M weather strip adhesive", "Food grade silicone lubricant NSF approved"],
		},
		{
			"problem": "Reach-in freezer defrost timer mechanical contacts pitted and burned causing irregular defrost initiation. Some defrost cycles skipping entirely leading to coil icing.",
			"solution": "Upgraded mechanical defrost timer to solid-state electronic controller with programmable defrost intervals. Set appropriate defrost frequency for high-traffic application.",
			"parts": ["Electronic defrost timer Paragon 8145-20 120V 4-wire", "Timer mounting bracket plastic NEMA 1", "Wiring harness adapter 4-pin to terminal strip"],
		},
		{
			"problem": "Salad bar sneeze guard refrigeration system experiencing short cycling due to oversized TXV causing rapid temperature swings. Evaporator alternating between flooding and starving.",
			"solution": "Replaced oversized TXV with properly rated valve and adjusted superheat to 8\u00b0F. Installed electronic expansion valve for more precise refrigerant control.",
			"parts": ["Electronic expansion valve Danfoss ETS250 R-134A", "EEV controller Danfoss AK-CC55 with display", "Superheat sensor Danfoss AKS41 strap-on type"],
		},
		{
			"problem": "Walk-in cooler evaporator fan blade cracked and unbalanced causing excessive noise and vibration transmission through cabinet structure. Fan motor overworking due to imbalanced load.",
			"solution": "Replaced damaged fan blade with dynamically balanced replacement and installed vibration isolation mounts on fan motor. Verified smooth operation and reduced noise levels.",
			"parts": ["Evaporator fan blade 12-inch 4-blade plastic balanced", "Vibration isolation mounts rubber 10-32 thread", "Fan guard wire 12-inch diameter powder coated"],
		},
		{
			"problem": "Beverage cooler high pressure cutout switch contacts welded closed from electrical arcing preventing system shutdown during high pressure events. Safety system compromised with potential compressor damage risk.",
			"solution": "Replaced faulty high pressure switch and installed pressure transducer with electronic monitoring system. Added redundant high pressure protection with manual reset capability.",
			"parts": ["High pressure switch Ranco O17-204 automatic reset 400 PSI", "Pressure transducer Sporlan 0-500 PSI 4-20mA output", "Electronic pressure monitor with display and alarm"],
		},
		{
			"problem": "Commercial blast chiller condenser coil completely blocked with grease and debris causing system to trip on high pressure cutout at 425 PSI. Unit shutting down every 8 minutes and unable to pull temperatures below 60\u00b0F.",
			"solution": "Thoroughly cleaned condenser coil using alkaline coil cleaner and high-pressure wash, then replaced damaged high pressure switch that was chattering. Verified proper airflow and system operation with head pressure stabilized at 280 PSI.",
			"parts": ["High Pressure Switch 425 PSI Cut-Out R-404A 1/4-inch NPT", "Alkaline Coil Cleaner Concentrate 1-Gallon", "Condenser Fan Motor Capacitor 35 MFD 370V"],
		},
		{
			"problem": "Six-door upright freezer experiencing refrigerant migration during off cycles with liquid slugging compressor on startup. Compressor making loud knocking sounds and tripping on current overload after 3-4 minutes of operation.",
			"solution": "Installed crankcase heater on compressor to prevent refrigerant migration and replaced damaged reed valves in compressor head. Added suction line accumulator to prevent future liquid slugging issues.",
			"parts": ["Crankcase Heater 150W 240V Wrap-Around Style", "Suction Line Accumulator 1-5/8-inch ODF R-404A", "Compressor Reed Valve Set Copeland Discus Series"],
		},
		{
			"problem": "Undercounter refrigerator electronic expansion valve control board failing with erratic superheat control and system short cycling. EEV opening and closing randomly causing temperature swings between 30\u00b0F and 48\u00b0F.",
			"solution": "Replaced faulty electronic expansion valve controller and recalibrated system parameters for proper superheat control. Updated firmware and performed complete system commissioning with stable 8-10\u00b0F superheat.",
			"parts": ["Electronic Expansion Valve Controller 24VAC Danfoss AK-CC550", "EEV Stepper Motor ODFR-067G00 1/4-inch ODF", "Superheat Sensor RTD PT1000 6-foot Lead"],
		},
		{
			"problem": "Walk-in cooler using obsolete R-22 refrigerant with major leak at evaporator coil inlet requiring complete refrigerant circuit replacement. System completely out of charge and compressor oil contaminated with moisture.",
			"solution": "Performed complete refrigerant retrofit to R-407C including new evaporator coil, filter drier, and POE oil change. Installed new TXV sized for R-407C and leak-tested entire system before charging.",
			"parts": ["Evaporator Coil R-407C 18,000 BTU 3-Row Fin Spacing", "Thermostatic Expansion Valve R-407C 3-Ton External Equalizer", "POE Refrigeration Oil 1-Gallon Copeland Ultra 32-3MAF"],
		},
		{
			"problem": "Chest freezer interior light staying on continuously due to faulty door switch causing excessive heat load and internal temperature rising to 12\u00b0F. Light bulb burning out every few days from constant operation.",
			"solution": "Replaced defective magnetic door switch with heavy-duty commercial grade switch and adjusted mounting bracket for proper alignment. Installed LED bulb to reduce heat generation and verified proper switch operation.",
			"parts": ["Magnetic Door Switch Heavy-Duty 10A 250VAC SPST", "LED Interior Light Bulb 7W 120V Appliance Base", "Door Switch Mounting Bracket Stainless Steel Adjustable"],
		},
	],
	"Dishwashers": [
		{
			"problem": "Door-type dishwasher wash pump motor overheating and tripping thermal overload breaker every 15 minutes during operation. Motor draws excessive amperage and makes grinding noise.",
			"solution": "Replaced failed wash pump motor and damaged impeller housing that was causing motor bind. Cleaned debris from pump chamber and tested electrical connections.",
			"parts": ["Wash Pump Motor 2 HP 208V 3-phase", "Pump Impeller Housing Assembly", "Thermal Overload Relay 15-amp"],
		},
		{
			"problem": "Conveyor dishwasher not reaching proper sanitizing temperature of 180\u00b0F, staying at 160\u00b0F. Booster heater element shows no continuity on multimeter test.",
			"solution": "Replaced burned-out booster heater element and faulty high-limit thermostat that was preventing proper heating cycle. Recalibrated temperature controller settings.",
			"parts": ["Booster Heater Element 18kW 208V", "High-Limit Thermostat 200\u00b0F", "Temperature Controller Digital Display"],
		},
		{
			"problem": "Upper spray arm in undercounter dishwasher not rotating and has poor water pressure. Visible food debris blocking multiple nozzles.",
			"solution": "Disassembled and thoroughly cleaned spray arm assembly, replacing worn bearing and spring mechanism. Cleared all nozzle blockages with wire brush.",
			"parts": ["Spray Arm Bearing Assembly", "Spray Arm Spring Mechanism", "Nozzle Cleaning Wire Set"],
		},
		{
			"problem": "Chemical dispenser system not injecting detergent into wash cycle. Peristaltic pump motor runs but no chemical flow observed.",
			"solution": "Replaced cracked chemical feed tubing and worn peristaltic pump rollers that had lost compression. Primed system and adjusted flow rate settings.",
			"parts": ["Chemical Feed Tubing 1/4-inch ID", "Peristaltic Pump Roller Set", "Check Valve 1/4-inch NPT"],
		},
		{
			"problem": "Drain pump not evacuating water from wash tank, causing overflow condition. Pump motor hums but impeller not turning.",
			"solution": "Removed and replaced seized drain pump with new unit after finding damaged impeller shaft. Cleaned drain lines and tested backflow prevention valve.",
			"parts": ["Drain Pump 1/2 HP 115V", "Pump Impeller Shaft Assembly", "Backflow Prevention Valve 2-inch"],
		},
		{
			"problem": "Door safety interlock system malfunctioning, allowing operation with door open. Door microswitch shows intermittent continuity.",
			"solution": "Replaced faulty door microswitch and adjusted door alignment mechanism for proper engagement. Tested all safety interlock circuits for proper operation.",
			"parts": ["Door Microswitch SPDT 15-amp", "Door Hinge Pin Set", "Safety Interlock Relay 24VDC"],
		},
		{
			"problem": "Cycle timer stuck on wash phase, not advancing to rinse cycle. Timer motor shows 24V input but gear mechanism not advancing.",
			"solution": "Replaced defective timer motor assembly with stripped internal gears. Calibrated new timer for proper cycle sequencing and tested all phases.",
			"parts": ["Timer Motor Assembly 24V", "Timer Cam Switch Set", "Timer Drive Gear Assembly"],
		},
		{
			"problem": "Water fill valve not opening, causing low water level alarm and cycle interruption. Solenoid coil measures infinite resistance.",
			"solution": "Installed new water fill valve with solenoid coil and cleaned mineral deposits from valve seat. Adjusted water level sensor calibration.",
			"parts": ["Water Fill Valve 3/4-inch NPT", "Solenoid Coil 120V AC", "Water Level Sensor Probe"],
		},
		{
			"problem": "Exhaust fan motor making excessive noise and vibration, reducing ventilation effectiveness. Fan blade assembly visibly wobbling during operation.",
			"solution": "Replaced worn exhaust fan motor bearings and rebalanced fan blade assembly. Tightened all mounting hardware and lubricated motor bearings.",
			"parts": ["Exhaust Fan Motor 1/3 HP 115V", "Fan Blade Assembly 12-inch", "Motor Bearing Set Sealed"],
		},
		{
			"problem": "Tank heater not maintaining wash water temperature, dropping to 140\u00b0F during heavy use. Thermostat contacts pitted and not making reliable connection.",
			"solution": "Replaced faulty tank thermostat and cleaned corroded electrical terminals. Tested heater element continuity and insulation resistance.",
			"parts": ["Tank Thermostat 160\u00b0F Bulb Type", "Heater Element 12kW 208V", "Terminal Block 3-position"],
		},
		{
			"problem": "Rinse aid dispenser not functioning, leaving spots on glassware. Dispenser pump diaphragm cracked and leaking internally.",
			"solution": "Rebuilt rinse aid dispenser pump with new diaphragm and check valves. Adjusted dispenser timing and flow rate for optimal coverage.",
			"parts": ["Dispenser Pump Diaphragm Kit", "Check Valve Set 1/8-inch", "Flow Control Orifice 0.5mm"],
		},
		{
			"problem": "Door lift mechanism sticking and requiring excessive force to open. Pneumatic cylinder not extending smoothly and making hissing sound.",
			"solution": "Replaced worn pneumatic cylinder seals and adjusted air pressure regulator. Lubricated all pivot points and tested door balance.",
			"parts": ["Pneumatic Cylinder Seal Kit", "Air Pressure Regulator 0-100 PSI", "Door Hinge Lubricant Food-Grade"],
		},
		{
			"problem": "Wash water temperature sensor reading incorrectly, showing 200\u00b0F when actual temperature is 150\u00b0F. Sensor probe corroded and giving false readings.",
			"solution": "Replaced corroded temperature sensor probe and recalibrated temperature controller. Cleaned sensor well and applied thermal compound.",
			"parts": ["RTD Temperature Sensor PT100", "Sensor Well Thermowell 1/2-inch", "Thermal Compound Food-Safe"],
		},
		{
			"problem": "Final rinse water pressure insufficient for proper sanitizing coverage. Pressure regulator valve stuck in partially closed position.",
			"solution": "Disassembled and cleaned pressure regulator valve, replacing worn internal springs and seals. Adjusted outlet pressure to specification.",
			"parts": ["Pressure Regulator Valve 3/4-inch", "Regulator Spring Set", "Valve Seal Kit Viton"],
		},
		{
			"problem": "Control panel displaying error codes intermittently and cycle buttons not responding consistently. Circuit board showing signs of moisture damage and corrosion.",
			"solution": "Replaced water-damaged main control board and installed improved ventilation shield. Sealed all electrical connections with marine-grade sealant.",
			"parts": ["Main Control Board PCB Assembly", "Control Panel Membrane Switch", "Electrical Connection Sealant"],
		},
		{
			"problem": "Conveyor dishwasher belt motor running continuously but conveyor not moving dishes through machine. Drive chain broken and hanging loose from motor sprocket.",
			"solution": "Replaced broken drive chain and adjusted chain tension to manufacturer specifications. Lubricated chain guides and verified proper belt tracking alignment.",
			"parts": ["Drive Chain #50 Roller 10-foot length", "Chain Master Link #50", "Chain Tensioner Assembly Model CT-240"],
		},
		{
			"problem": "Door-type dishwasher producing excessive foam during wash cycle, causing suds overflow from tank. Detergent concentration too high due to faulty metering system.",
			"solution": "Calibrated chemical feed pump flow rate and replaced clogged flow restrictor orifice. Adjusted detergent dilution ratio to 1:240 per manufacturer specs.",
			"parts": ["Flow Restrictor Orifice 0.8mm diameter", "Peristaltic Pump Tubing 6mm ID", "Chemical Feed Pump Calibration Kit"],
		},
		{
			"problem": "Undercounter dishwasher door seal leaking water onto floor during operation. Rubber door gasket cracked and hardened from heat exposure.",
			"solution": "Removed old door gasket and installed new heat-resistant silicone seal. Adjusted door alignment and pressure for proper sealing contact.",
			"parts": ["Door Gasket Silicone 72-inch perimeter", "Gasket Adhesive High-Temp", "Door Hinge Pin Stainless Steel 3/8-inch"],
		},
		{
			"problem": "Booster heater cycling on and off rapidly without reaching setpoint temperature. High limit switch tripping due to scale buildup on heating elements.",
			"solution": "Descaled heating elements with commercial deliming solution and replaced faulty high limit switch. Adjusted temperature differential to prevent short cycling.",
			"parts": ["High Limit Switch 200\u00b0F Manual Reset", "Heating Element 6kW 240V", "Temperature Control Relay SPDT 240V"],
		},
		{
			"problem": "Wash arms not receiving adequate water flow, resulting in poor cleaning performance. Internal wash pump impeller damaged and causing cavitation noise.",
			"solution": "Disassembled wash pump and replaced damaged impeller and worn mechanical seal. Checked pump alignment and motor coupling integrity.",
			"parts": ["Pump Impeller 6-inch diameter Bronze", "Mechanical Seal Carbon/Ceramic 1.5-inch", "Pump Coupling Spider Insert Polyurethane"],
		},
		{
			"problem": "Final rinse water not hot enough for sanitization, measuring only 165\u00b0F instead of required 180\u00b0F. Mixing valve not blending hot and cold water properly.",
			"solution": "Rebuilt thermostatic mixing valve with new internal components and calibrated temperature setting. Verified hot water supply temperature at 200\u00b0F minimum.",
			"parts": ["Thermostatic Mixing Valve Cartridge", "Mixing Valve Seat Assembly", "Temperature Adjustment Screw M6x20mm"],
		},
		{
			"problem": "Control system randomly stopping mid-cycle with no error code displayed. Loose wire connections at main control board causing intermittent power loss.",
			"solution": "Tightened all wire terminal connections and applied dielectric grease to prevent corrosion. Replaced main control board with updated firmware version.",
			"parts": ["Main Control Board PCB Assembly", "Wire Terminal Connectors 14-16 AWG", "Dielectric Grease 4oz tube"],
		},
		{
			"problem": "Drain valve not opening at end of wash cycle, requiring manual operation to empty tank. Pneumatic actuator diaphragm ruptured and losing air pressure.",
			"solution": "Replaced pneumatic actuator diaphragm and O-ring seals. Adjusted air pressure regulator to 25 PSI and tested valve operation timing.",
			"parts": ["Pneumatic Actuator Diaphragm 4-inch", "O-Ring Kit Viton High-Temp", "Air Pressure Regulator 0-60 PSI"],
		},
		{
			"problem": "Water level sensor giving false high readings, causing overfill conditions and water waste. Sensor probe covered in grease and food particles affecting conductivity.",
			"solution": "Cleaned sensor probe with degreasing solvent and replaced corroded sensor head assembly. Recalibrated water level control settings to manufacturer specifications.",
			"parts": ["Water Level Sensor Probe Assembly", "Sensor Head Stainless Steel", "Sensor Cable 10-foot shielded"],
		},
		{
			"problem": "Prewash spray manifold clogged with grease causing poor pre-rinse performance. Multiple spray nozzles completely blocked with solidified fat deposits.",
			"solution": "Removed spray manifold and soaked in hot alkaline cleaning solution overnight. Replaced severely clogged nozzles and reinstalled with proper alignment.",
			"parts": ["Spray Nozzle 15\u00b0 Pattern 1/8 NPT", "Manifold Cleaning Brush Set", "Spray Manifold Gasket Kit"],
		},
		{
			"problem": "Door counterweight cable snapped causing door to slam shut dangerously. Cable frayed due to improper routing over sharp edges on door frame.",
			"solution": "Installed new stainless steel cable with proper routing guides to prevent chafing. Adjusted counterweight tension for smooth door operation and safety.",
			"parts": ["Stainless Steel Cable 3/32-inch 10-foot", "Cable End Fittings Swage Type", "Door Weight Assembly 25-pound"],
		},
		{
			"problem": "Scrap accumulator system not removing food debris effectively, causing drain blockages. Scrapper blade worn down and not making contact with conveyor surface.",
			"solution": "Replaced worn scrapper blade and adjusted height for proper contact pressure. Cleaned debris chute and verified proper waste removal operation.",
			"parts": ["Scrapper Blade Polyurethane 24-inch", "Blade Mounting Hardware Kit", "Debris Chute Gasket Rubber"],
		},
		{
			"problem": "Chemical rinse aid not dispensing consistently, resulting in water spots on dishes. Venturi injector system clogged with mineral deposits from hard water.",
			"solution": "Disassembled venturi injector and cleaned mineral deposits with acid-based descaler. Replaced worn venturi nozzle and recalibrated injection rate.",
			"parts": ["Venturi Injector Nozzle 0.6mm orifice", "Venturi Body Assembly Brass", "Chemical Injection Tubing 4mm ID"],
		},
		{
			"problem": "Tank overflow alarm activating falsely during normal operation. Float switch mechanism sticking in up position due to grease accumulation on pivot point.",
			"solution": "Cleaned float switch assembly and pivot mechanism with degreasing agent. Replaced float switch with sealed magnetic reed switch type for reliability.",
			"parts": ["Magnetic Float Switch 250V 10A", "Float Assembly Stainless Steel", "Switch Mounting Bracket Adjustable"],
		},
		{
			"problem": "Heated air drying system not functioning, leaving dishes wet at cycle completion. Blower motor seized due to bearing failure and overheating protection activated.",
			"solution": "Replaced blower motor assembly and cleaned air intake filters. Verified heating element operation and adjusted drying cycle timer for optimal performance.",
			"parts": ["Blower Motor 1/3 HP 115V 1725 RPM", "Motor Mounting Bracket Steel", "Air Filter Washable Aluminum 16x20"],
		},
		{
			"problem": "Conveyor dishwasher making loud grinding noise from drive motor compartment and belt speed fluctuating erratically. Motor coupling shows visible wear and misalignment.",
			"solution": "Replaced worn flexible coupling between motor and gearbox, realigned motor mount, and adjusted belt tension to manufacturer specifications.",
			"parts": ["Flexible coupling assembly 1.5-inch bore", "Motor mount bracket kit stainless steel", "V-belt 5L section 48-inch length"],
		},
		{
			"problem": "Door-type dishwasher final rinse temperature only reaching 160\u00b0F instead of required 180\u00b0F for sanitization. Booster heater thermostat clicking but elements not energizing.",
			"solution": "Replaced faulty contactor that was not closing properly to energize heating elements, and calibrated thermostat to correct temperature setpoint.",
			"parts": ["Contactor 3-pole 30A 240V coil", "Thermostat bulb and capillary 180\u00b0F setpoint", "Heating element 6kW 240V stainless steel"],
		},
		{
			"problem": "Undercounter dishwasher overflow sensor triggering false alarms and stopping cycles prematurely. Sensor probe covered in grease buildup and not detecting actual water level.",
			"solution": "Cleaned sensor probe thoroughly with degreasing solution, adjusted sensor mounting height, and recalibrated control board sensitivity settings.",
			"parts": ["Water level sensor probe 6-inch stainless steel", "Sensor mounting bracket adjustable", "Control board calibration module"],
		},
		{
			"problem": "Conveyor dishwasher wash tank losing temperature rapidly during peak operation hours. Tank insulation damaged and heat exchanger coils showing scale buildup.",
			"solution": "Replaced deteriorated foam insulation panels around tank walls and descaled heat exchanger coils using commercial descaling solution.",
			"parts": ["Foam insulation panels 2-inch thick fiberglass", "Heat exchanger coil cleaning kit", "Tank insulation adhesive high-temperature"],
		},
		{
			"problem": "Door-type dishwasher upper wash arm assembly vibrating excessively and spraying water outside tank area. Bearing assembly worn and arm mounting loose.",
			"solution": "Replaced worn wash arm bearing assembly, tightened mounting hardware to proper torque specifications, and balanced spray arm rotation.",
			"parts": ["Wash arm bearing assembly stainless steel", "Mounting hardware kit grade 8 bolts", "Wash arm balance weight set"],
		},
		{
			"problem": "Undercounter dishwasher detergent pump running continuously but no soap dispensing into wash water. Pump check valve stuck open causing backflow.",
			"solution": "Replaced faulty check valve in detergent line and cleaned pump chamber of crystallized detergent deposits that were preventing proper sealing.",
			"parts": ["Check valve 1/4-inch NPT brass", "Detergent pump diaphragm kit", "Pump chamber gasket set"],
		},
		{
			"problem": "Conveyor dishwasher exhaust damper not opening automatically during wash cycles, causing excessive humidity buildup. Damper actuator solenoid not receiving power signal.",
			"solution": "Repaired broken wire connection to damper solenoid and replaced corroded terminal connections, tested damper operation through full cycle.",
			"parts": ["Damper actuator solenoid 24V DC", "Terminal connector kit weatherproof", "Control wire 14 AWG 25-foot length"],
		},
		{
			"problem": "Door-type dishwasher drain valve not sealing properly during wash cycle, causing continuous water loss and poor cleaning results. Valve seat pitted from chemical corrosion.",
			"solution": "Disassembled drain valve assembly, machined valve seat smooth, and replaced valve disc and spring mechanism for proper sealing.",
			"parts": ["Drain valve disc assembly 3-inch diameter", "Valve seat repair kit", "Valve spring stainless steel heavy-duty"],
		},
		{
			"problem": "Undercounter dishwasher wash pump priming slowly and losing prime between cycles. Air leak in suction line causing cavitation and reduced flow.",
			"solution": "Located and sealed air leak at pump housing gasket, replaced cracked suction line fitting, and adjusted pump priming sequence timing.",
			"parts": ["Pump housing gasket silicone", "Suction line fitting 1.5-inch NPT", "Pump priming valve assembly"],
		},
		{
			"problem": "Conveyor dishwasher pre-rinse section not activating when dishes enter detection zone. Photoelectric sensor lens clouded with grease and not detecting product.",
			"solution": "Cleaned sensor lens with appropriate solvent, adjusted sensor alignment and sensitivity, and replaced sensor housing seal to prevent future contamination.",
			"parts": ["Photoelectric sensor lens assembly", "Sensor mounting bracket adjustable", "Housing seal kit O-ring set"],
		},
		{
			"problem": "Door-type dishwasher producing inconsistent wash results with some racks poorly cleaned. Wash pump impeller partially broken and creating uneven flow patterns.",
			"solution": "Removed wash pump assembly, replaced damaged impeller with new balanced unit, and checked pump housing for wear or damage.",
			"parts": ["Wash pump impeller 6-inch diameter bronze", "Impeller key stock 1/4-inch", "Pump housing wear ring"],
		},
		{
			"problem": "Undercounter dishwasher door gasket hardening and cracking at high-temperature areas near steam vents. Door not sealing properly during operation.",
			"solution": "Replaced entire door gasket with high-temperature silicone version, adjusted door alignment, and applied food-grade gasket lubricant.",
			"parts": ["Door gasket high-temp silicone 10-foot length", "Gasket adhesive food-grade", "Door adjustment hardware kit"],
		},
		{
			"problem": "Conveyor dishwasher chemical feed lines becoming clogged with crystallized chemicals and causing erratic dispensing. Automatic dilution system not maintaining proper ratios.",
			"solution": "Flushed all chemical lines with hot water solution, replaced clogged metering orifices, and recalibrated dilution system flow rates.",
			"parts": ["Metering orifice set various sizes", "Chemical feed line tubing 1/4-inch", "Dilution system calibration kit"],
		},
		{
			"problem": "Door-type dishwasher tank heater elements showing signs of scale buildup and reduced heating efficiency. Water temperature taking excessive time to reach setpoint.",
			"solution": "Descaled heating elements using commercial descaling solution, replaced sacrificial anode rod, and adjusted water treatment system parameters.",
			"parts": ["Sacrificial anode rod magnesium 12-inch", "Descaling solution commercial grade", "Element mounting gaskets high-temp"],
		},
		{
			"problem": "Undercounter dishwasher control board randomly resetting during operation and losing programmed cycle parameters. Power supply voltage fluctuating outside acceptable range.",
			"solution": "Installed voltage stabilizer for control circuit, replaced control board with updated firmware version, and improved electrical connections.",
			"parts": ["Voltage stabilizer 120V 5A", "Control board assembly latest revision", "Electrical terminal upgrade kit"],
		},
		{
			"problem": "Door-type dishwasher final rinse temperature inconsistent, fluctuating between 160\u00b0F and 185\u00b0F during cycle. Steam production varies dramatically and dishes not properly sanitized.",
			"solution": "Replaced faulty mixing valve that was allowing cold water bypass during rinse phase. Calibrated new valve to maintain consistent 180\u00b0F final rinse temperature.",
			"parts": ["Thermostatic Mixing Valve 3/4-inch NPT 180\u00b0F Set Point", "Temperature Sensor RTD Pt100 6-inch Probe", "Valve Actuator 24VAC Spring Return"],
		},
		{
			"problem": "Conveyor dishwasher wash tank water level dropping continuously during operation, requiring constant refill. No visible external leaks but water consumption excessive.",
			"solution": "Located internal tank crack along weld seam near heating element mount. Drained tank, cleaned area, and applied high-temperature epoxy repair followed by stainless steel reinforcement plate.",
			"parts": ["High-Temp Epoxy Repair Kit Food Grade 500\u00b0F Rating", "Stainless Steel Reinforcement Plate 6x8-inch 16 Gauge", "Tank Drain Valve 2-inch NPT Ball Valve"],
		},
		{
			"problem": "Undercounter dishwasher producing loud banging noise during wash cycle, particularly when spray arms change direction. Customers complaining about noise level in dining area.",
			"solution": "Diagnosed water hammer caused by worn wash pump check valve allowing backflow. Replaced check valve and installed water hammer arrestor to eliminate pressure spikes.",
			"parts": ["Swing Check Valve 1.5-inch NPT Bronze Disc", "Water Hammer Arrestor Size AA 1/2-inch NPT", "Pump Mounting Isolators Rubber 1/4-20 Thread"],
		},
		{
			"problem": "Door-type dishwasher control system randomly shutting down mid-cycle with no error codes displayed. Power cycling unit allows restart but problem recurs unpredictably.",
			"solution": "Found loose connection in main power contactor causing intermittent voltage drop to control board. Tightened all electrical connections and replaced worn contactor with matching amperage rating.",
			"parts": ["Power Contactor 40A 240VAC 3-Pole NEMA Size 1", "Control Transformer 240V Primary 24V Secondary 100VA", "Terminal Block 12-Position 600V 25A Rating"],
		},
		{
			"problem": "Conveyor dishwasher chemical sanitizer concentration reading zero on test strips despite dispenser pump running. Health inspector threatening closure due to inadequate sanitization.",
			"solution": "Discovered sanitizer supply line had developed pinhole leak allowing air infiltration and pump cavitation. Replaced entire supply line and primed system to restore proper chemical injection.",
			"parts": ["Chemical Supply Tubing 3/8-inch ID Sanitary Grade 10-foot", "Tube Fitting Barb 3/8-inch to 1/4-inch NPT Polypropylene", "Chemical Injection Check Valve 1/4-inch Spring Loaded"],
		},
	],
	"Griddles": [
		{
			"problem": "Gas griddle fails to ignite with pilot light system producing weak yellow flame instead of strong blue flame. Customer reports uneven heating and difficulty maintaining temperature.",
			"solution": "Cleaned pilot light orifice of grease buildup and replaced clogged pilot light assembly with proper gas pressure adjustment. Verified pilot flame characteristics and tested ignition sequence.",
			"parts": ["Pilot Light Assembly NAT-500 Natural Gas", "Pilot Orifice #56 Brass", "Pilot Tubing 1/4-inch Copper 18-inch"],
		},
		{
			"problem": "Electric griddle heating elements cycling on and off rapidly with temperature swings of 50\u00b0F above and below setpoint. Thermostat knob clicks repeatedly during operation.",
			"solution": "Replaced faulty capillary tube thermostat that had developed internal leak causing erratic temperature sensing. Calibrated new thermostat and verified even heat distribution across cooking surface.",
			"parts": ["Capillary Thermostat 200-450\u00b0F 48-inch", "Thermostat Mounting Bracket Stainless Steel", "Temperature Control Knob with Dial"],
		},
		{
			"problem": "Chrome griddle surface showing severe pitting and black discoloration in high-use areas with food sticking during cooking. Surface temperature varies by 75\u00b0F across the plate.",
			"solution": "Removed old chrome-plated griddle plate and installed new surface with proper seasoning procedure. Adjusted burner orifices for even heat distribution and performed surface leveling.",
			"parts": ["Chrome Griddle Plate 36-inch x 24-inch 1/2-inch Thick", "Burner Orifice Set Natural Gas #54", "Griddle Plate Gasket High-Temperature Silicone"],
		},
		{
			"problem": "Electronic ignition system sparks continuously without stopping after successful gas ignition. Control module LED shows constant fault code and gas valve cycles erratically.",
			"solution": "Replaced defective flame sensor that failed to detect proper flame signal and installed new electronic ignition control module. Verified proper grounding and flame detection timing.",
			"parts": ["Electronic Ignition Control Module 24V", "Flame Sensor Rod Stainless Steel 6-inch", "Ignition Transformer 120V Primary 6000V Secondary"],
		},
		{
			"problem": "Grease trap overflowing during busy periods with grease backing up onto cooking surface. Drain system appears blocked and grease collection drawer won't slide properly.",
			"solution": "Disassembled and deep-cleaned entire grease management system, replaced cracked grease trough, and installed new drawer slides. Verified proper drainage angle and flow capacity.",
			"parts": ["Grease Trough Stainless Steel 36-inch", "Drawer Slide Assembly Heavy-Duty 100-lb Capacity", "Grease Collection Drawer 4-quart Capacity"],
		},
		{
			"problem": "Gas control valve knob turns freely without resistance and griddle temperature cannot be adjusted. Gas flow appears constant regardless of control position.",
			"solution": "Replaced worn gas control valve with stripped internal threads and installed new control knob assembly. Performed gas pressure test and leak check on all connections.",
			"parts": ["Gas Control Valve 3/4-inch NPT Natural Gas", "Control Knob Assembly with Spring Return", "Valve Stem Packing Kit NBR O-Rings"],
		},
		{
			"problem": "Thermocouple safety system shutting down gas flow randomly during operation with pilot light remaining lit. System requires manual reset multiple times per day.",
			"solution": "Replaced deteriorated thermocouple with millivolt output below specification and cleaned connections showing corrosion. Adjusted thermocouple position for optimal flame contact.",
			"parts": ["Thermocouple Type K 24-inch Lead 900\u00b0F Rating", "Thermocouple Connection Nut 1/4-inch", "Safety Gas Valve 24 Millivolt Natural Gas"],
		},
		{
			"problem": "Burner manifold leaking gas at multiple connection points with visible corrosion and whistling sounds during operation. Gas pressure appears inconsistent across burners.",
			"solution": "Replaced corroded gas manifold assembly and all connection fittings with new brass components. Performed complete pressure test and adjusted individual burner orifices for uniform output.",
			"parts": ["Gas Manifold Assembly 1-inch NPT 4-Outlet Brass", "Pipe Nipples 1/2-inch NPT Black Iron Set of 4", "Thread Sealant High-Temperature Gas-Rated"],
		},
		{
			"problem": "Griddle surface tilted with 1/4-inch slope causing grease and food to pool on one side. Legs appear to have shifted and mounting hardware is loose.",
			"solution": "Disassembled griddle mounting system and replaced bent adjustable legs with heavy-duty versions. Re-leveled entire unit using precision instruments and secured with grade-8 hardware.",
			"parts": ["Adjustable Leg Assembly 6-inch Stainless Steel Set of 4", "Mounting Hardware Kit Grade-8 Bolts", "Leveling Foot Pads Non-Slip Rubber 4-inch"],
		},
		{
			"problem": "Backsplash grease shield rattling loudly during operation with visible cracks along mounting seams. Grease splatter reaching wall behind equipment.",
			"solution": "Removed damaged backsplash assembly and installed reinforced replacement with proper mounting brackets. Applied high-temperature sealant to all joints and verified structural integrity.",
			"parts": ["Backsplash Assembly 36-inch Stainless Steel 16-gauge", "Mounting Bracket Set Heavy-Duty L-Brackets", "High-Temperature Sealant FDA-Approved"],
		},
		{
			"problem": "Electric griddle heating elements showing visible red-hot spots with power consumption 40% higher than normal. Temperature zones reading incorrectly on digital display.",
			"solution": "Replaced burned-out heating elements with proper wattage rating and installed new temperature sensors. Verified electrical connections and performed amperage draw test on each zone.",
			"parts": ["Heating Element 3000W 240V Tubular", "Temperature Sensor RTD Probe 6-inch", "Element Terminal Block 30-Amp Rating"],
		},
		{
			"problem": "Pilot light won't stay lit after manual lighting with gas odor present around control area. Safety lockout engaging immediately after release of pilot button.",
			"solution": "Replaced faulty thermopile generator that wasn't producing sufficient millivoltage to hold safety valve open. Cleaned pilot light assembly and adjusted gas-air mixture for proper combustion.",
			"parts": ["Thermopile Generator 750 Millivolt Output", "Pilot Light Burner Assembly Natural Gas", "Gas-Air Mixer Adjustment Screw Assembly"],
		},
		{
			"problem": "Griddle surface temperature reading 100\u00b0F lower than thermostat setting with slow recovery time after food placement. Burner flames appear smaller than normal.",
			"solution": "Cleaned clogged burner orifices restricting gas flow and replaced worn pressure regulator maintaining incorrect manifold pressure. Calibrated thermostat sensing bulb placement for accurate readings.",
			"parts": ["Pressure Regulator 11-inch WC Natural Gas", "Burner Orifice Drill Set #54-#60", "Thermostat Sensing Bulb 1/4-inch Diameter"],
		},
		{
			"problem": "Grease channels cracked and leaking onto floor with visible structural damage around drain connections. Stainless steel showing stress corrosion at weld points.",
			"solution": "Fabricated and installed new grease channel system with improved drainage design and reinforced mounting points. Applied food-grade welding techniques for all joints and performed leak test.",
			"parts": ["Grease Channel Assembly 36-inch 16-gauge Stainless", "Drain Connection Elbow 1-inch NPT Stainless", "Channel Support Brackets Reinforced Set of 6"],
		},
		{
			"problem": "Electronic temperature controller display showing error codes with erratic zone control and inability to program cooking temperatures. Touch screen not responding to inputs.",
			"solution": "Replaced failed electronic control board with updated firmware version and installed new touch screen interface. Programmed default cooking profiles and calibrated temperature sensors.",
			"parts": ["Electronic Control Board 240V Multi-Zone", "Touch Screen Display 7-inch Color LCD", "Control Board Wiring Harness 20-Pin Connector"],
		},
		{
			"problem": "Gas griddle burner orifices clogged with carbon buildup causing uneven flame patterns and cold spots across cooking surface. Several burner ports completely blocked with no visible flame.",
			"solution": "Removed and cleaned all burner orifices using specialized drill bits and compressed air. Replaced heavily damaged orifices and recalibrated gas flow rates.",
			"parts": ["Burner Orifice Set #54 Natural Gas 0.0465-inch", "Orifice Cleaning Kit with Drill Bits", "Burner Tube Assembly 24-inch Stainless Steel"],
		},
		{
			"problem": "Electric griddle power distribution failing with only half the heating zones operational. Main power indicator shows normal but individual zone indicators remain dark.",
			"solution": "Diagnosed failed main contactor and damaged power distribution block. Replaced electrical components and tested all heating circuits for proper amperage draw.",
			"parts": ["Contactor 3-Pole 40A 240V AC Coil", "Power Distribution Block 6-Circuit 50A", "Heating Element 3000W 240V Flat Ribbon"],
		},
		{
			"problem": "Chrome griddle top showing extensive rust formation under chrome plating with surface becoming rough and difficult to clean. Chrome flaking off in multiple areas.",
			"solution": "Removed damaged chrome griddle plate and installed new factory replacement. Sealed mounting surface and adjusted leveling to prevent moisture infiltration.",
			"parts": ["Chrome Griddle Plate 36x24-inch 1/2-inch Thick", "Plate Mounting Gasket Set Food Grade", "Leveling Foot Assembly Adjustable 4-inch"],
		},
		{
			"problem": "Gas safety valve failing to open despite proper thermocouple signal with griddle remaining cold even when controls set to maximum temperature. Manual gas shut-off valve functions normally.",
			"solution": "Replaced defective combination gas valve and recalibrated opening pressure. Tested safety lockout system and verified proper thermocouple millivolt output.",
			"parts": ["Combination Gas Valve 3/4-inch NPT 24V", "Gas Valve Actuator Motor 24V AC", "Thermocouple Lead Wire 36-inch High-Temp"],
		},
		{
			"problem": "Griddle ignition transformer producing weak spark with delayed ignition and occasional failure to light. Spark gap appears correct but arc intensity insufficient.",
			"solution": "Replaced failed ignition transformer and cleaned spark electrode assemblies. Adjusted spark gap to specification and tested ignition timing sequence.",
			"parts": ["Ignition Transformer 15000V 35mA", "Spark Electrode Assembly Ceramic Insulated", "High-Voltage Ignition Wire 18-inch"],
		},
		{
			"problem": "Temperature probe reading 75\u00b0F higher than actual griddle surface temperature causing food to undercook. Digital controller shows steady temperature but infrared gun readings differ significantly.",
			"solution": "Calibrated temperature controller and replaced defective RTD temperature probe. Repositioned probe for better thermal contact with griddle plate.",
			"parts": ["RTD Temperature Probe 1000-Ohm Platinum", "Temperature Controller Digital Display 240V", "Thermal Compound Food-Grade High-Temp"],
		},
		{
			"problem": "Grease drawer guide rails bent and binding causing drawer to stick halfway during removal. Excessive force required to operate with visible track deformation.",
			"solution": "Straightened damaged guide rails using hydraulic press and replaced worn drawer slides. Lubricated mechanism with high-temperature food-grade grease.",
			"parts": ["Heavy-Duty Drawer Slides 20-inch 100lb Capacity", "Stainless Steel Guide Rails Set", "Food-Grade High-Temp Bearing Grease"],
		},
		{
			"problem": "Gas burner air shutters vibrating loose during operation causing improper air-fuel mixture and sooting. Flames appear yellow-orange instead of blue.",
			"solution": "Tightened all air shutter assemblies and replaced damaged adjustment screws. Rebalanced air-fuel mixture for optimal combustion across all burners.",
			"parts": ["Air Shutter Assembly Complete with Hardware", "Adjustment Screw Set Stainless Steel", "Burner Venturi Tube 8-inch Natural Gas"],
		},
		{
			"problem": "Griddle surface warping with visible bow in center causing oil to pool and uneven cooking results. Warpage measured at 3/16-inch deviation from flat.",
			"solution": "Removed and replaced warped griddle plate with heavy-duty reinforced version. Upgraded support structure and adjusted mounting points for even load distribution.",
			"parts": ["Heavy-Duty Griddle Plate 1/2-inch Extra Thick", "Reinforcement Support Brackets Set of 4", "Plate Support Channel 36-inch Stainless"],
		},
		{
			"problem": "Electric heating element connections overheating with visible discoloration and burning smell from junction box. Power consumption fluctuating during operation.",
			"solution": "Replaced burned electrical connections and upgraded to higher-rated terminal blocks. Retorqued all connections to proper specification and tested under full load.",
			"parts": ["High-Current Terminal Block 60A Ceramic", "Electrical Junction Box NEMA 4X Stainless", "Heat-Resistant Wire Nuts 600V Rated"],
		},
		{
			"problem": "Splash guard mounting bolts shearing under thermal expansion stress with guard becoming loose and rattling. Multiple bolt failures observed at different locations.",
			"solution": "Replaced failed mounting hardware with thermal expansion-rated bolts and added spring washers. Reinforced mounting points with backing plates.",
			"parts": ["Thermal Expansion Bolts 1/4-20 x 2-inch", "Spring Washer Set Stainless Steel", "Reinforcement Backing Plates 2x2-inch"],
		},
		{
			"problem": "Gas pressure regulator delivering inconsistent pressure with gauge readings varying between 8-15 inches water column. Burner flames fluctuating in size correspondingly.",
			"solution": "Rebuilt gas pressure regulator with new diaphragm and spring assembly. Calibrated output pressure to 11 inches water column and tested under varying load conditions.",
			"parts": ["Regulator Diaphragm Kit Natural Gas", "Pressure Spring Assembly Adjustable", "Gas Pressure Gauge 0-20 inch WC"],
		},
		{
			"problem": "Thermostat capillary tube kinked and damaged causing erratic temperature control with sudden temperature spikes. Visual inspection shows tube crushed near connection point.",
			"solution": "Replaced entire thermostat assembly including capillary sensing bulb and calibrated temperature response. Rerouted capillary tube to prevent future damage.",
			"parts": ["Hydraulic Thermostat 200-400\u00b0F Range", "Capillary Tube Assembly 48-inch", "Sensing Bulb Stainless Steel 1/4-inch"],
		},
		{
			"problem": "Grease collection system backing up with drain line completely blocked by solidified grease and food particles. System overflowing onto kitchen floor during peak hours.",
			"solution": "Hydro-jetted drain lines to remove blockage and installed grease separator system. Upgraded drain capacity with larger diameter piping and improved slope.",
			"parts": ["Automatic Grease Separator Unit", "PVC Drain Pipe 2-inch Schedule 40", "Floor Drain Grate Heavy-Duty Stainless"],
		},
		{
			"problem": "Control knob shaft stripped and spinning freely without engaging valve stem. Temperature adjustment impossible with knob rotating continuously without resistance.",
			"solution": "Replaced damaged valve stem and control knob assembly. Repaired stripped threads in valve body and ensured proper engagement between components.",
			"parts": ["Gas Valve Stem Assembly 1/4-turn", "Control Knob with Set Screw Stainless", "Thread Repair Insert Kit M8x1.25"],
		},
		{
			"problem": "Gas griddle pressure regulator malfunctioning with BTU output dropping 30% during peak cooking times. Flames turn orange and griddle fails to maintain temperature under heavy load.",
			"solution": "Replaced faulty gas pressure regulator and recalibrated gas line pressure to manufacturer specifications. Cleaned and adjusted primary air shutters on all burners.",
			"parts": ["Gas Pressure Regulator 3/4-inch NPT 11-inch WC", "Primary Air Shutter Assembly Set (6 pieces)", "Gas Line Pressure Gauge 0-14 WC"],
		},
		{
			"problem": "Electric griddle contactor chattering and arcing with visible burn marks on electrical contacts. Unit experiences intermittent power loss and tripping of circuit breakers.",
			"solution": "Installed new contactor assembly and replaced damaged wire terminals with heat-resistant connectors. Tightened all electrical connections and verified proper voltage supply.",
			"parts": ["Definite Purpose Contactor 40A 240V 3-Pole", "High-Temp Wire Terminals 10AWG (12 pack)", "Electrical Contact Cleaner Spray"],
		},
		{
			"problem": "Griddle drain system backing up with grease solidifying in drain lines and causing slow water evacuation. Kitchen staff reports standing water in grease trough after cleaning.",
			"solution": "Cleared blocked drain lines using commercial degreaser and installed new drain trap with larger capacity. Repositioned drain pipe slope for improved flow.",
			"parts": ["Commercial Grease Trap 20-Gallon Capacity", "Drain Line Snake 1/2-inch x 25-foot", "High-Temperature Drain Pipe 2-inch Schedule 40"],
		},
		{
			"problem": "Gas griddle flame sensors dirty and corroded causing erratic safety shutdowns during normal operation. System fails flame detection test and requires constant manual restarting.",
			"solution": "Cleaned flame sensor probes with fine abrasive cloth and replaced corroded sensor leads. Adjusted sensor positioning for optimal flame detection coverage.",
			"parts": ["Flame Sensor Probe Assembly 8-inch Length", "High-Temperature Sensor Wire 18AWG", "Flame Sensor Mounting Bracket Stainless Steel"],
		},
		{
			"problem": "Electric griddle zone control board displaying random temperature readings with cooking zones heating inconsistently. Digital readout flickering between different temperature values.",
			"solution": "Replaced defective control board and updated firmware to latest version. Recalibrated all temperature sensors and verified proper zone isolation.",
			"parts": ["Multi-Zone Control Board 240V 6-Zone", "Temperature Sensor RTD Probe 1/4-inch NPT", "Control Board Mounting Hardware Kit"],
		},
		{
			"problem": "Gas griddle burner tubes warped from overheating with visible deformation causing uneven gas distribution. Hot spots and cold zones apparent across cooking surface.",
			"solution": "Installed new burner tube assembly and realigned gas manifold connections. Adjusted gas orifice sizes to ensure uniform BTU distribution across all burners.",
			"parts": ["Stainless Steel Burner Tube 36-inch Length", "Gas Orifice Drill Set #53-#60", "Burner Tube Support Brackets (4 pieces)"],
		},
		{
			"problem": "Chrome griddle surface developing hairline cracks with grease penetrating into base metal causing discoloration. Cooking performance degraded with increased food sticking.",
			"solution": "Resurfaced griddle plate using diamond grinding wheel and applied new chrome plating treatment. Seasoned surface with high-temperature cooking oil per manufacturer protocol.",
			"parts": ["Chrome Plating Restoration Kit Industrial Grade", "Diamond Grinding Wheel 7-inch 120-Grit", "High-Temperature Griddle Seasoning Oil 1-Quart"],
		},
		{
			"problem": "Electric griddle heating element terminals overheating with visible discoloration and loose connections. Power draw fluctuating and causing voltage drops in kitchen panel.",
			"solution": "Replaced all heating element terminals with high-amperage connectors and upgraded wiring to proper gauge. Applied dielectric grease to prevent future corrosion.",
			"parts": ["High-Amp Terminal Block 50A 600V", "THHN Wire 8AWG Stranded 25-foot", "Dielectric Terminal Compound 4-ounce Tube"],
		},
		{
			"problem": "Gas griddle automatic shut-off valve sticking in closed position preventing startup after cleaning cycles. Manual override requires excessive force to operate.",
			"solution": "Disassembled and cleaned shut-off valve mechanism removing food debris and grease buildup. Replaced worn valve seats and lubricated moving components.",
			"parts": ["Gas Shut-Off Valve 3/4-inch NPT Automatic", "Valve Seat Repair Kit with O-Rings", "High-Temperature Valve Lubricant Food-Safe"],
		},
		{
			"problem": "Griddle splash guard mounting bolts loosening from thermal expansion cycles causing rattling and grease leakage. Guard shifting position during operation.",
			"solution": "Installed spring-loaded mounting hardware designed for thermal expansion and applied thread-locking compound. Realigned splash guard to proper clearances.",
			"parts": ["Spring-Loaded Mounting Bolts 1/4-20 x 2-inch (8 pack)", "High-Temperature Thread Locker Red", "Thermal Expansion Washers Stainless Steel"],
		},
		{
			"problem": "Electric griddle ground fault protection circuit tripping intermittently with no visible moisture present. Kitchen losing cooking capacity during busy periods.",
			"solution": "Identified degraded heating element insulation and replaced affected elements. Installed new GFCI breaker with higher sensitivity rating for commercial applications.",
			"parts": ["Griddle Heating Element 240V 3000W", "Commercial GFCI Breaker 30A 240V", "Element Insulation Tester Megohm Meter"],
		},
		{
			"problem": "Gas griddle venturi tubes blocked with grease and debris causing poor air-gas mixture and sooting. Burner flames burning yellow with carbon deposits on cooking surface.",
			"solution": "Removed and thoroughly cleaned all venturi tubes using compressed air and degreasing solvent. Adjusted primary air intake for optimal blue flame combustion.",
			"parts": ["Venturi Tube Assembly Complete Set", "Compressed Air Blow Gun with Extensions", "Commercial Degreasing Solvent 1-Gallon"],
		},
		{
			"problem": "Griddle surface thermometer reading incorrectly with 50\u00b0F variance from actual surface temperature. Cooking times inconsistent and food quality suffering.",
			"solution": "Calibrated surface thermometer using precision reference standards and replaced damaged thermal sensing bulb. Adjusted mounting depth for accurate readings.",
			"parts": ["Bi-Metal Surface Thermometer 2-inch Dial", "Thermometer Calibration Kit with Standards", "Thermal Sensing Bulb 6-inch Probe"],
		},
		{
			"problem": "Electric griddle power relay contacts welded shut causing zones to remain energized continuously. Temperature control non-functional and overheating risk present.",
			"solution": "Replaced power relay assembly with higher-rated contacts and installed surge protection device. Added thermal overload protection for each heating zone.",
			"parts": ["Power Relay 240V 40A DPDT", "Surge Protection Device 240V Commercial", "Thermal Overload Switch 180\u00b0F Auto-Reset"],
		},
		{
			"problem": "Gas griddle flexible connector showing stress cracks near fitting connections with slight gas odor detected during leak test. Safety inspection required immediate attention.",
			"solution": "Replaced entire flexible gas connector with new approved commercial-grade line and upgraded to larger diameter for improved flow. Pressure tested all connections.",
			"parts": ["Flexible Gas Connector 3/4-inch x 48-inch CSA Approved", "Gas Line Thread Sealant High-Pressure", "Digital Gas Leak Detector Instrument"],
		},
		{
			"problem": "Electric griddle shorting to ground with circuit breaker tripping repeatedly during startup. Kitchen staff reports electrical shock sensations when touching griddle frame and burning smell from control panel area.",
			"solution": "Replaced damaged wiring harness with water intrusion damage and installed new GFCI protection circuit. Rewired control panel connections with proper grounding and sealed all electrical junction boxes.",
			"parts": ["Control panel wiring harness 240V 16-gauge THWN", "GFCI breaker 50-amp 240V double-pole", "Electrical junction box NEMA 4X stainless steel"],
		},
		{
			"problem": "Gas griddle producing sooty yellow flames with excessive carbon monoxide readings during health inspection. Burner flames unstable and wavering with poor combustion efficiency noted.",
			"solution": "Cleaned and adjusted primary air shutters on all burners for proper air-to-gas mixture ratio. Replaced worn gas pressure regulator and calibrated manifold pressure to manufacturer specifications.",
			"parts": ["Gas pressure regulator 1/2-inch NPT 11-inch WC", "Primary air shutter assembly set of 6", "Manifold pressure gauge 0-15 WC digital"],
		},
		{
			"problem": "Stainless steel griddle plate warped with 3/8-inch bow causing oil to pool in center and uneven cooking results. Plate shows stress cracks near mounting bolts from thermal expansion.",
			"solution": "Removed and replaced entire griddle plate with heavy-duty reinforced version. Installed flexible mounting system with thermal expansion joints to prevent future warping.",
			"parts": ["Griddle plate 36-inch x 24-inch 1/2-inch thick reinforced steel", "Thermal expansion joint kit stainless steel", "Mounting bolt set M12 x 1.75 grade 8 heat-treated"],
		},
		{
			"problem": "Gas control knob stems seized and cannot be turned with internal valve mechanisms corroded from steam exposure. Multiple control valves stuck in partially open positions affecting temperature control.",
			"solution": "Disassembled and rebuilt all gas control valves with new stems and seals rated for high-temperature operation. Applied food-grade anti-seize compound to all threaded connections.",
			"parts": ["Gas valve stem assembly 1/2-inch with packing gland", "High-temperature valve seal kit Viton O-rings", "Food-grade anti-seize compound 4-oz tube"],
		},
		{
			"problem": "Temperature probe sensor reading 200\u00b0F high causing griddle to underheat and automatic shutdowns during peak cooking periods. Digital controller shows sensor fault intermittently with erratic temperature displays.",
			"solution": "Replaced failed RTD temperature sensor with calibrated unit and updated controller firmware to match new sensor specifications. Recalibrated temperature zones using certified reference thermometer.",
			"parts": ["RTD temperature sensor Pt100 1/8-inch diameter 6-inch probe", "Digital temperature controller firmware update chip", "Sensor mounting well 1/4-inch NPT stainless steel"],
		},
	],
}

TECHNICIANS = [
	{"name": "Mike Johnson", "id": "TECH-001", "cert": "EPA Universal Certified"},
	{"name": "Sarah Williams", "id": "TECH-015", "cert": "CFESA Certified Master"},
	{"name": "Carlos Rodriguez", "id": "TECH-008", "cert": "Master Technician Level 3"},
	{"name": "Jennifer Kim", "id": "TECH-023", "cert": "CFESA Level II Certified"},
	{"name": "David Chen", "id": "TECH-012", "cert": "EPA Type I/II Certified"},
	{"name": "Amanda Foster", "id": "TECH-019", "cert": "Factory Certified Specialist"},
	{"name": "Robert Taylor", "id": "TECH-005", "cert": "Senior Field Technician"},
	{"name": "Lisa Martinez", "id": "TECH-031", "cert": "CFESA Certified Specialist"},
]

COMPANIES = [
	"Restaurant Equipment Services LLC",
	"Commercial Kitchen Solutions Inc",
	"FoodService Tech Pros",
	"National Restaurant Repair",
	"Metro Kitchen Equipment Service",
	"Professional Food Equipment Co",
]
SERVICE_ISSUES = {
	"Ovens": [
		{
			"problem": "Our convection oven is making this awful grinding noise whenever we turn it on, and it's getting louder every day. The fan seems to be struggling and the air circulation isn't working right - my cookies are coming out unevenly baked. My staff is getting frustrated because they can't predict cooking times anymore.",
			"solution": "Replaced the worn convection fan motor and damaged fan blade assembly that was causing excessive noise and poor air circulation.",
			"parts": ["SKU-MT-004721 - Convection Fan Motor 1/3 HP 115V 1725 RPM", "SKU-FB-002845 - Fan Blade Assembly 12-inch diameter stainless steel"],
		},
		{
			"problem": "The door on our deck oven won't stay closed anymore - it keeps popping open during baking and all the heat escapes. We're losing money on ruined bread and pizza because the temperature drops too much. I have to have someone hold the door shut while we bake, which is ridiculous.",
			"solution": "Replaced the damaged door latch mechanism and adjusted the door alignment to ensure proper sealing and secure closure.",
			"parts": ["SKU-DL-009334 - Heavy Duty Door Latch Assembly with spring-loaded mechanism"],
		},
		{
			"problem": "This combi oven isn't steaming properly anymore - when I hit the steam button, barely any steam comes out. My bread isn't getting the crust I need and my vegetables are coming out dry instead of perfectly steamed. It worked fine last month but now it's basically useless for half of what I need it for.",
			"solution": "Cleaned the clogged steam injection nozzles and replaced the faulty steam solenoid valve that was restricting water flow to the steam generator.",
			"parts": ["SKU-SV-007612 - Steam Solenoid Valve 24V AC with 1/2-inch NPT connections", "SKU-SN-003298 - Steam Injection Nozzle Set stainless steel (set of 4)"],
		},
		{
			"problem": "Our gas oven won't light at all today - I can smell gas when I try to start it but there's no flame. My whole kitchen is backed up because this is our main oven for roasting. I'm worried about the gas smell and had to shut it off completely.",
			"solution": "Replaced the defective electronic ignition module and cleaned the gas burner orifices that were blocked with debris.",
			"parts": ["SKU-IG-008847 - Electronic Ignition Module 120V with spark generator"],
		},
		{
			"problem": "The temperature control on this convection oven is completely messed up - I set it to 375 but my thermometer shows it's running at 450 degrees. Everything is burning and I've already ruined two batches of dinner rolls. The digital display seems fine but the actual temperature is way off.",
			"solution": "Replaced the failed thermocouple sensor and recalibrated the temperature controller to restore accurate temperature readings and control.",
			"parts": ["SKU-TC-005529 - Type K Thermocouple 24-inch probe length with ceramic protection tube", "SKU-CC-004183 - Digital Temperature Controller with PID control and display"],
		},
		{
			"problem": "The timer on our rapid-bake oven stopped working yesterday and now everything is overcooking because we have to guess when things are done. My staff keeps burning pizzas because they're busy with other orders and can't watch the oven constantly. This is costing us money and making customers unhappy.",
			"solution": "Replaced the malfunctioning digital timer module and updated the control board firmware to restore automated timing functions.",
			"parts": ["SKU-TM-006471 - Digital Timer Module programmable 99-minute countdown with audible alarm"],
		},
		{
			"problem": "The stone deck in our pizza oven has a huge crack right down the middle and pieces are starting to chip off onto our food. It's not heating evenly anymore and I'm worried about food safety with stone fragments. We can't serve pizza with rocks in it, so I had to shut down our pizza station.",
			"solution": "Replaced the cracked stone deck with a new refractory stone surface and sealed all joints to prevent future cracking and contamination.",
			"parts": ["SKU-SD-009186 - Refractory Stone Deck 30x24 inches cordierite material", "SKU-SS-002750 - High-temperature Stone Sealant 32 oz container"],
		},
		{
			"problem": "The control panel on our combi oven is going crazy - buttons don't respond half the time and the display keeps flickering. Sometimes it starts cooking on its own settings instead of what I programmed. My cooks are afraid to use it because it's so unpredictable.",
			"solution": "Replaced the damaged control board and touchscreen interface module, then reprogrammed all cooking presets to factory specifications.",
			"parts": ["SKU-CB-007923 - Main Control Board PCB with microprocessor and relay outputs", "SKU-TS-004651 - Touchscreen Interface Module 7-inch color display with membrane overlay"],
		},
		{
			"problem": "Our convection oven suddenly stopped heating completely this morning - the fan runs and the lights come on, but there's no heat at all. I've got a full lunch rush coming and this is my main baking oven for everything from cookies to roasted vegetables. My pastry chef is panicking because she can't finish today's desserts without it.",
			"solution": "Replaced failed heating element that had burned out completely, also installed new element contactor that was causing intermittent power issues.",
			"parts": ["SKU-HE-002847 - Electric Heating Element 4800W 240V with mounting brackets", "SKU-CT-001592 - Element Contactor 40A 240V coil"],
		},
		{
			"problem": "The ignition system on our gas deck oven is acting up - sometimes it lights right away, other times I have to try five or six times before it catches. When it doesn't light, I can hear the gas flowing but no spark. It's making me nervous about safety and my bakers are wasting time trying to get it started every morning.",
			"solution": "Cleaned and adjusted the spark igniter electrode positioning and replaced the faulty ignition module that was providing inconsistent spark timing.",
			"parts": ["SKU-IG-003471 - Electronic Ignition Module 24V with spark transformer"],
		},
		{
			"problem": "The high-limit safety switch keeps shutting down our combi oven right in the middle of cooking cycles, usually when we're running it at full capacity during dinner service. The oven just goes dead and I have to wait for it to cool down and reset before I can use it again. It's happened three times this week and my kitchen crew is getting frustrated with the delays.",
			"solution": "Replaced malfunctioning high-limit temperature switch that was tripping at incorrect temperature and cleaned blocked ventilation causing overheating conditions.",
			"parts": ["SKU-HL-004829 - High-Limit Safety Switch 500\u00b0F manual reset with 1/2-inch probe", "SKU-VT-002156 - Exhaust Ventilation Fan Motor 1/4 HP 120V", "SKU-FS-001743 - Temperature Sensor RTD Pt100 with 6-inch probe"],
		},
		{
			"problem": "My rapid-bake oven is heating unevenly - the back corner gets super hot while the front stays cool, so my pizzas come out with burnt crusts in back and doughy fronts. I've tried rotating pans but it's not working well enough for our quality standards. Customers are starting to complain about inconsistent food.",
			"solution": "Repaired damaged convection motor that was causing poor air circulation and replaced warped air deflector plate that was directing heat improperly.",
			"parts": ["SKU-MT-005683 - Convection Fan Motor 1/2 HP 208V with mounting assembly", "SKU-DF-002841 - Air Deflector Plate stainless steel with gasket kit"],
		},
		{
			"problem": "The door seal on our convection oven is completely shot - I can feel heat pouring out around the edges when it's running. My energy bills are going through the roof and the oven takes forever to reach temperature now. Plus the kitchen gets uncomfortably hot when we're using it during busy periods.",
			"solution": "Installed new door gasket seal and adjusted door alignment to ensure proper sealing contact around entire perimeter.",
			"parts": ["SKU-GS-003927 - Door Gasket Seal 48-inch high-temperature silicone with adhesive backing"],
		},
		{
			"problem": "The steam injection nozzles in our combi oven are clogged up with mineral buildup and only a few spots are getting any steam at all. My bread isn't developing proper crust and steamed vegetables are coming out dry and overcooked in some areas. The water in our area is really hard so this keeps happening every few months.",
			"solution": "Descaled and cleaned all steam nozzles, replaced three completely blocked nozzles, and installed new water filtration system to prevent future mineral buildup.",
			"parts": ["SKU-SN-004572 - Steam Injection Nozzle set of 6 with mounting hardware", "SKU-WF-001829 - Water Filter Cartridge for hard water applications", "SKU-DK-002365 - Descaling Kit with pump and cleaning solution"],
		},
		{
			"problem": "Our deck oven's bottom heating elements aren't working properly - the tops of our pizzas and bread are cooking fine but the bottoms stay pale and soft. I end up having to cook everything much longer which dries out the tops. My pizza maker says the stone isn't getting hot enough underneath.",
			"solution": "Replaced two failed bottom heating elements and repaired damaged wiring connections that were causing insufficient power delivery to lower heating zone.",
			"parts": ["SKU-HE-006194 - Bottom Deck Heating Element 3200W 240V U-shaped", "SKU-WH-003851 - High-temperature Wire Harness with ceramic connectors"],
		},
		{
			"problem": "The thermocouple in our gas oven must be going bad because the safety system keeps shutting off the gas flow even when there's a good flame. I'll get it lit and cooking, then twenty minutes later the flame goes out and I have to relight everything. It's driving my cooks crazy because they never know if their roasts will finish cooking.",
			"solution": "Replaced faulty thermocouple sensor that was giving incorrect temperature readings to the gas valve safety system.",
			"parts": ["SKU-TC-005238 - Thermocouple Type K 24-inch with pilot assembly connection", "SKU-GV-002947 - Gas Safety Valve with thermocouple input 3/4-inch NPT"],
		},
		{
			"problem": "The convection fan motor in our main oven started making this horrible screeching sound yesterday and now it's completely seized up - won't turn at all. Without the fan running, everything bakes unevenly and takes twice as long. My prep cook had to move all the sheet pans to our smaller oven and we're way behind on our dinner prep.",
			"solution": "Replaced the failed convection fan motor and cleaned out accumulated grease and debris from the motor housing.",
			"parts": ["SKU-MT-004721 - Convection Fan Motor 1/2 HP 115V with mounting bracket", "SKU-BL-002156 - Motor Bearing Kit with seals and gaskets"],
		},
		{
			"problem": "Our gas combi oven's pilot light keeps going out randomly, sometimes multiple times during service. When it happens, the whole oven shuts down and I lose whatever was cooking inside. My kitchen manager is frustrated because we can't rely on it for our dinner specials anymore and customers are waiting too long for their food.",
			"solution": "Cleaned and adjusted the pilot light assembly and replaced the faulty thermocouple that was causing intermittent shutdowns.",
			"parts": ["SKU-TC-003892 - Pilot Thermocouple 24-inch with safety valve connection"],
		},
		{
			"problem": "The programmable controller on our deck oven has gone completely blank - no display at all, just a black screen. I can't set any temperatures or times, so we're stuck trying to use it manually with guesswork. My bakers are having a really hard time getting consistent results without being able to program their usual settings.",
			"solution": "Diagnosed failed control board due to power surge damage and installed new programmable temperature controller with updated firmware.",
			"parts": ["SKU-CB-007834 - Digital Temperature Controller with LCD display and timer functions", "SKU-WH-001245 - Control Board Wiring Harness 6-pin connector", "SKU-FU-000892 - Control Circuit Fuse Kit 5A fast-blow"],
		},
		{
			"problem": "The door hinges on our convection oven are completely worn out and the door sags so badly that it won't close properly anymore. Heat keeps escaping and my utility bills are getting ridiculous. Plus my staff has to physically lift the door to get it to latch, which is getting dangerous when they're carrying hot pans.",
			"solution": "Replaced worn door hinges and realigned the door frame to ensure proper sealing and safe operation.",
			"parts": ["SKU-HG-005671 - Heavy Duty Door Hinge Set stainless steel with bushings", "SKU-LT-002934 - Door Latch Assembly with striker plate and spring mechanism"],
		},
		{
			"problem": "Our rapid-bake oven's heating elements are burning out constantly - this is the third one this month that's just stopped working in the middle of a shift. When they fail, half the oven goes cold and my pizzas come out with raw dough on one side. I'm losing money on wasted food and my pizza guy is ready to quit from the stress.",
			"solution": "Identified voltage fluctuation issue causing premature element failure and installed voltage stabilizer along with new heating elements.",
			"parts": ["SKU-HE-008923 - Electric Heating Element 240V 5000W with ceramic insulators", "SKU-VS-001567 - Voltage Stabilizer 30A single-phase with surge protection"],
		},
		{
			"problem": "The flame sensor in our gas deck oven must be dirty or broken because it keeps thinking there's no flame even when I can see it burning perfectly fine. The safety system shuts everything down every few minutes and my bread keeps getting interrupted mid-bake. My head baker is pulling her hair out trying to finish orders with all these shutdowns.",
			"solution": "Cleaned corrosion from flame sensor and replaced faulty sensor rod that was providing inconsistent flame detection signals.",
			"parts": ["SKU-FS-004512 - Flame Sensor Rod with ceramic insulator and mounting hardware"],
		},
		{
			"problem": "The water line to our combi oven's steam system is completely clogged with mineral deposits and barely any water is getting through anymore. The steam function is basically useless and my vegetables are coming out dry and overcooked. We're in a hard water area and this keeps happening, but it's gotten really bad this time.",
			"solution": "Replaced clogged water supply lines and installed water filtration system to prevent future mineral buildup in steam injection system.",
			"parts": ["SKU-WL-007821 - Stainless Water Supply Line 1/2-inch with fittings", "SKU-WF-003456 - Water Filter System with mineral reduction cartridge", "SKU-SI-002187 - Steam Injection Nozzle Assembly with check valve"],
		},
		{
			"problem": "Our convection oven's temperature probe is giving crazy readings - the display shows 350 degrees but when I check with my own thermometer it's actually running at 275. Everything is taking way longer to cook and my customers are complaining about wait times. I've had to adjust all our cooking times but it's still not consistent.",
			"solution": "Calibrated and replaced faulty RTD temperature sensor that was providing inaccurate temperature readings to the control system.",
			"parts": ["SKU-RT-005823 - RTD Temperature Sensor 100-ohm platinum with stainless probe", "SKU-CA-001934 - Sensor Calibration Kit with test leads"],
		},
		{
			"problem": "The electric heating elements in our convection oven are only working on one side - the left side gets blazing hot while the right side barely warms up. My cookies and sheet pan dinners are coming out completely lopsided, with one side burnt and the other side raw. I've been rotating pans halfway through but it's a pain and my kitchen staff is complaining about the extra work.",
			"solution": "Replaced the failed heating element assembly on the right side and tested both elements for proper amperage draw.",
			"parts": ["SKU-HE-293847 - Electric heating element 3500W 240V with mounting brackets", "SKU-WH-105629 - Wiring harness connector for heating element circuit"],
		},
		{
			"problem": "Our gas deck oven's flame sensor must be dirty or broken because it keeps thinking the flame went out when it's actually burning fine. The safety system shuts off the gas every few minutes and I have to keep relighting it. My pizza guys are going nuts because they can't finish orders without constant interruptions.",
			"solution": "Cleaned the flame sensor rod and replaced the corroded sensor assembly that was giving false readings to the control system.",
			"parts": ["SKU-FS-847362 - Flame sensor rod assembly with 24-inch lead wire"],
		},
		{
			"problem": "The electronic ignition system in our rapid-bake oven is completely dead - no spark at all when I try to light it. I can hear the gas valve opening but there's no ignition happening. We've been using a lighter to start it manually but that can't be safe, and my insurance guy would have a heart attack if he saw us doing that.",
			"solution": "Replaced the failed ignition control module and installed a new spark electrode with proper gap adjustment.",
			"parts": ["SKU-IG-654128 - Electronic ignition control module 24V AC", "SKU-SE-398275 - Spark electrode assembly with ceramic insulator"],
		},
		{
			"problem": "My combi oven's water level sensor is acting crazy - it keeps saying there's no water even when the tank is full, so the steam functions won't work at all. I've tried draining and refilling it multiple times but the error message won't go away. My steamed fish specials are off the menu until this gets fixed.",
			"solution": "Replaced the malfunctioning water level sensor and recalibrated the steam system water management controls.",
			"parts": ["SKU-WS-752940 - Water level sensor probe with mounting gasket"],
		},
		{
			"problem": "The interior light bulbs in our deck oven keep burning out every few days, and now the last one just died so we can't see anything inside when we're baking. My bread bakers are having to use flashlights to check their loaves, which is ridiculous and probably dangerous. The bulbs seem to be getting way too hot in there.",
			"solution": "Installed high-temperature rated oven light fixtures with proper heat shields to prevent premature bulb failure.",
			"parts": ["SKU-LF-483619 - High-temp oven light fixture with heat shield", "SKU-LB-290156 - Halogen oven bulb 50W heat-resistant"],
		},
		{
			"problem": "Our convection oven's door latch mechanism broke and now the door won't stay securely closed during cooking. It pops open slightly which lets heat escape and makes the cooking times completely unpredictable. My cooks are having to hold it shut with a towel, which seems dangerous and definitely isn't professional.",
			"solution": "Replaced the worn door latch assembly and adjusted the strike plate alignment for proper door sealing.",
			"parts": ["SKU-DL-618735 - Door latch assembly with spring-loaded mechanism", "SKU-SP-427193 - Strike plate with adjustment screws"],
		},
		{
			"problem": "The gas valve on our combi oven is stuck partially open and won't shut off completely when we turn off the oven. I can still hear gas flowing and smell it faintly even when the controls are off. This is making everyone nervous about safety and I had to shut off the main gas line until we get it fixed.",
			"solution": "Replaced the faulty gas control valve assembly and tested all gas connections for proper sealing and operation.",
			"parts": ["SKU-GV-956281 - Gas control valve assembly 3/4-inch NPT with safety shutoff"],
		},
		{
			"problem": "The baking stone in our pizza deck oven has developed several deep cracks and now pieces are breaking off and falling onto the pizzas below. The heat distribution is terrible with chunks missing and I'm worried about customers getting stone fragments in their food. We've had to stop using the bottom deck completely.",
			"solution": "Removed the damaged stone deck and installed a new food-grade refractory stone surface with proper thermal expansion joints.",
			"parts": ["SKU-DS-374852 - Refractory baking stone 24x36 inch food-grade ceramic", "SKU-SJ-168493 - Thermal expansion joint sealant high-temperature"],
		},
		{
			"problem": "The exhaust fan above our combi oven stopped working completely and now steam is pouring out into the dining room every time we use the steam function. My servers are complaining that customers can't see their food through all the fog and it's making the whole restaurant humid and uncomfortable. We had to stop using steam mode completely which means our vegetables and fish aren't coming out right.",
			"solution": "Replaced the burned out exhaust fan motor and cleaned the accumulated grease from the fan blades and housing to restore proper ventilation.",
			"parts": ["SKU-MF-445821 - Exhaust Fan Motor 1/3 HP 115V with mounting bracket"],
		},
		{
			"problem": "Our rapid-bake oven's internal lights all went dark yesterday and now my cooks can't see what they're cooking without opening the door constantly. Every time they open it to check on pizzas, we lose heat and everything takes longer to cook. It's especially bad during dinner rush when they need to monitor multiple orders at once.",
			"solution": "Replaced all interior halogen bulbs and repaired loose wiring connections in the light fixture assemblies to restore proper illumination.",
			"parts": ["SKU-LB-233947 - Halogen Oven Light Bulb 50W high-temp rated", "SKU-WH-892341 - High Temperature Wire Harness 12-inch with ceramic connectors"],
		},
		{
			"problem": "The gas burners in our deck oven won't adjust properly anymore - they're either full blast or barely lit, no in-between settings. My pizza chef can't control the heat like he needs to and we're either burning crusts or they're taking forever to cook. The flame adjustment knobs turn but don't seem to actually change anything.",
			"solution": "Rebuilt the gas valve assemblies and replaced worn modulation components to restore proper flame control across the full range of settings.",
			"parts": ["SKU-GV-667123 - Gas Control Valve Assembly with modulating actuator", "SKU-OR-445892 - O-Ring Kit for gas valve seals", "SKU-SP-129847 - Spring Set for valve modulation mechanism"],
		},
		{
			"problem": "Our convection oven's digital display is showing error codes I don't understand and it won't let me start any cooking cycles. The screen keeps flashing 'E04' and 'E12' and when I try to override it, nothing happens. My breakfast prep is completely stalled because I can't bake anything and my pastry chef is freaking out about her morning bread orders.",
			"solution": "Diagnosed and replaced the faulty main control board which had corrupted firmware causing multiple sensor error codes to display incorrectly.",
			"parts": ["SKU-CB-778934 - Main Control Board with preprogrammed firmware", "SKU-HR-334567 - Wire Harness for control board connections"],
		},
		{
			"problem": "The door latch mechanism on our combi oven broke and now the door won't lock shut during steam cycles. The safety system won't let it run with steam unless the door is properly sealed, so we're stuck only being able to use it as a regular convection oven. This is killing our steamed vegetable and bread production.",
			"solution": "Replaced the broken door latch assembly and adjusted the strike plate alignment to ensure proper sealing and safety system engagement.",
			"parts": ["SKU-DL-556789 - Door Latch Assembly with safety microswitch", "SKU-SP-223445 - Strike Plate with adjustment hardware"],
		},
		{
			"problem": "Our deck oven's stone surface is cracking and crumbling in several spots, and now we're getting stone dust on our bread and pizza. The heat distribution is all wrong too - some areas are way hotter than others. My head baker noticed the problem first when flour started sticking to the rough patches instead of dusting off normally.",
			"solution": "Removed the damaged stone deck and installed a new food-grade ceramic stone surface with proper support rails and thermal expansion joints.",
			"parts": ["SKU-DS-889123 - Ceramic Deck Stone 24x36 inch food-grade surface", "SKU-SR-445672 - Stone Support Rail Kit with thermal brackets"],
		},
		{
			"problem": "The water level sensor in our combi oven must be broken because it keeps saying the water tank is empty even when I just filled it completely. Without steam injection working, my bread isn't getting the proper crust and my steamed dishes are coming out dry. I've tried refilling it multiple times but the error message won't go away.",
			"solution": "Cleaned mineral deposits from the water level sensor probe and replaced the sensor assembly which had corroded contacts from hard water exposure.",
			"parts": ["SKU-WS-334891 - Water Level Sensor with stainless probe and mounting hardware"],
		},
		{
			"problem": "The flame sensor on our gas convection oven keeps shutting down the burners randomly, even when there's a perfectly good flame burning. It'll run fine for twenty minutes then suddenly cut out, and I have to wait for it to cool down before I can relight it. My roast chicken orders are taking forever because I can't count on consistent heat.",
			"solution": "Replaced the corroded flame sensor rod and cleaned carbon buildup from the sensor mounting assembly to restore reliable flame detection.",
			"parts": ["SKU-FS-667234 - Flame Sensor Rod 4-inch with ceramic insulator and mounting bracket"],
		},
		{
			"problem": "The flame sensor in our gas oven keeps cutting out the gas supply even though I can see a perfect blue flame burning. It'll run fine for maybe ten minutes, then suddenly shut down and I have to restart the whole ignition sequence. My line cooks are getting behind on orders because they never know when the oven will quit working in the middle of cooking steaks.",
			"solution": "Replaced the faulty flame sensor that was giving intermittent signals to the safety control module due to carbon buildup on the sensor tip.",
			"parts": ["SKU-FS-002847 - Flame Sensor Rod 8-inch length with ceramic insulator"],
		},
		{
			"problem": "Our combi oven's water pump for the steam system makes this awful whining noise and barely any water is getting through to create steam. I can hear it struggling to work but my vegetables are coming out dry as a bone. The whole reason we bought this expensive oven was for the steam feature and now it's basically broken.",
			"solution": "Replaced the worn water circulation pump and cleaned out mineral deposits from the water lines that were restricting flow.",
			"parts": ["SKU-WP-001923 - Water Circulation Pump 120V 0.5HP with mounting bracket", "SKU-WL-000457 - Water Line Filter Assembly with bypass valve"],
		},
		{
			"problem": "The RTD temperature probe in our convection oven must be giving bad readings because the display says 350 degrees but my instant-read thermometer shows it's actually 280. My cookies are taking forever to bake and my dinner rolls are coming out pale and doughy. I've wasted three batches of pastries today trying to figure out what's wrong.",
			"solution": "Replaced the defective RTD temperature sensor that had drifted out of calibration and recalibrated the temperature controller.",
			"parts": ["SKU-RT-003412 - RTD Temperature Sensor Pt100 12-inch probe with connection head"],
		},
		{
			"problem": "The electric heating elements in our deck oven aren't heating up at all on the bottom - I can see the top ones glowing red but the bottom stays cold. My pizza crusts are staying soggy and pale no matter how long I leave them in. It's like trying to cook with only half an oven and customers are complaining about undercooked food.",
			"solution": "Replaced the burned-out bottom heating elements and the faulty contactor that was preventing power from reaching them.",
			"parts": ["SKU-HE-004729 - Electric Heating Element 5000W 240V bottom mount", "SKU-CT-001856 - Electrical Contactor 30A 240V with auxiliary contacts"],
		},
		{
			"problem": "The door latch mechanism on our rapid-bake oven is completely broken and won't engage properly anymore. The door looks closed but it's not actually sealed, so heat keeps leaking out and cooking times are all messed up. My pizza guy has to lean against the door to keep it shut, which is ridiculous and probably dangerous.",
			"solution": "Replaced the worn door latch assembly and adjusted the door alignment to ensure proper sealing when closed.",
			"parts": ["SKU-DL-002638 - Door Latch Assembly with spring-loaded mechanism", "SKU-DS-001174 - Door Strike Plate with adjustment screws", "SKU-DG-000892 - Door Gasket High-temperature silicone 6-foot length"],
		},
		{
			"problem": "Our combi oven's control board keeps resetting itself randomly during cooking cycles, losing all the programmed settings and shutting down whatever we're cooking. It happened twice during yesterday's dinner rush and ruined a whole tray of salmon. My sous chef is afraid to use any of the preset programs because we can't trust it to finish the job.",
			"solution": "Replaced the main control board that had failing capacitors and updated the firmware to the latest version.",
			"parts": ["SKU-CB-005841 - Main Control Board Assembly with LCD display interface"],
		},
		{
			"problem": "The electronic ignition system in our gas convection oven takes forever to light and sometimes doesn't work at all - I hear the clicking for thirty seconds before it finally catches, if it catches at all. My morning prep is getting delayed because I can't count on getting the oven started when I need it. Sometimes I have to try three or four times before it lights.",
			"solution": "Replaced the weak ignition module and cleaned the spark electrodes that were fouled with grease and carbon deposits.",
			"parts": ["SKU-IG-003275 - Electronic Ignition Module 120V with spark generator", "SKU-SE-001429 - Spark Electrode Assembly with ceramic insulator and ground strap"],
		},
		{
			"problem": "The baking stone in our deck oven has developed several deep cracks and now heats really unevenly - some spots are blazing hot while others barely get warm. My artisan breads are coming out with burnt bottoms in some places and pale spots in others. The stone pieces are also starting to flake off, which is getting into the food.",
			"solution": "Replaced the cracked stone deck with a new refractory stone and reset the support brackets to ensure even heat distribution.",
			"parts": ["SKU-ST-004692 - Refractory Baking Stone 30x20 inches with thermal mass properties", "SKU-SB-002158 - Stone Support Bracket Set stainless steel adjustable height"],
		},
		{
			"problem": "The flame sensor in our gas deck oven must be dirty or something because it keeps thinking there's no flame when there clearly is one. The oven will light up fine, burn for maybe ten minutes, then suddenly shut off all the gas even though I can see the flame is still going strong. My bread baker is going nuts because loaves keep getting half-baked when this happens during the middle of a baking cycle.",
			"solution": "Cleaned the flame sensor thoroughly to remove carbon buildup and soot deposits that were preventing proper flame detection, then calibrated the sensor sensitivity.",
			"parts": ["SKU-FS-002941 - Flame Sensor Assembly with ceramic insulator and mounting bracket"],
		},
		{
			"problem": "Our combi oven's water pump for the steam system died completely - when I try to use any steam functions, I can hear it trying to work but no water is moving at all. The pump makes this grinding noise for a few seconds then gives up. Without steam, I can't do proper bread baking or vegetable steaming, which cuts out about half of my menu options.",
			"solution": "Replaced the failed steam system water pump and checked all water lines for proper flow and pressure.",
			"parts": ["SKU-WP-008527 - Steam System Water Pump 120V with inlet/outlet fittings", "SKU-GL-004813 - Water Line Gasket Set for steam connections"],
		},
		{
			"problem": "The electronic ignition module in our rapid-bake oven completely gave out yesterday - there's no spark at all when I try to light it. I can turn the gas on and everything looks normal on the control panel, but there's just no ignition happening. We're dead in the water for our lunch pizza rush without this thing working.",
			"solution": "Replaced the faulty electronic ignition module and verified proper voltage supply to the ignition system.",
			"parts": ["SKU-IG-007253 - Electronic Ignition Module with mounting hardware and wiring harness"],
		},
		{
			"problem": "The RTD temperature sensor in our convection oven is giving completely wrong readings - the display shows 300 degrees but my handheld thermometer reads 425 degrees inside. My cookies are burning because I'm setting lower temperatures thinking the oven is running cool. This has been getting worse over the past two weeks and now I can't trust any of the temperature settings.",
			"solution": "Replaced the failed RTD temperature sensor and recalibrated the temperature control system to ensure accurate readings.",
			"parts": ["SKU-RT-005674 - RTD Temperature Sensor Pt100 with 6-inch probe and 1/2-inch NPT fitting", "SKU-WH-009182 - High-temperature sensor wire harness 10-foot length"],
		},
		{
			"problem": "The ductwork connection to our convection oven came loose somehow and now hot air is blowing out the back instead of circulating inside the oven. My kitchen is getting way too hot and the food isn't cooking evenly because the air flow is all messed up. I can actually see the loose duct flapping around when the fan runs.",
			"solution": "Reconnected and secured the loose convection ductwork with new clamps and verified proper airflow direction throughout the system.",
			"parts": ["SKU-DC-003156 - Ductwork Clamp Set with gaskets for 8-inch diameter ducts", "SKU-DG-007429 - High-temperature duct gasket material 36-inch roll"],
		},
		{
			"problem": "Our deck oven's baking stone cracked in half during the dinner rush last night and now there's a huge gap running right through the middle of the deck. The heat isn't distributing evenly anymore and my pizza crusts are coming out with weird patterns where the crack is. I'm worried about the stone pieces breaking off into the food too.",
			"solution": "Removed the damaged baking stone and installed a new cordierite stone deck with proper thermal expansion gaps.",
			"parts": ["SKU-BS-001895 - Cordierite Baking Stone 30x40 inch with thermal shock resistance"],
		},
		{
			"problem": "The latch mechanism on our combi oven door broke and now the door won't stay securely closed during cooking cycles. It pops open randomly, especially when there's steam pressure building up inside. All my steam escapes and the cooking times are completely unpredictable because I never know when the door will swing open.",
			"solution": "Replaced the worn door latch assembly and adjusted the door alignment to ensure proper sealing pressure.",
			"parts": ["SKU-DL-008741 - Heavy-duty Door Latch Assembly with spring-loaded mechanism", "SKU-SP-002358 - Door Latch Spring Set with mounting hardware"],
		},
		{
			"problem": "The heating elements in our electric convection oven are only working on one side - the left elements glow red hot but the right side stays completely cold. Everything I bake comes out lopsided with one side perfectly done and the other side barely cooked. My pastry chef is having to rotate everything halfway through baking but it's still not working well.",
			"solution": "Replaced the failed heating element bank on the right side of the oven and checked electrical connections for proper voltage distribution.",
			"parts": ["SKU-HE-006492 - Electric Heating Element 240V 5000W with mounting brackets", "SKU-CB-004671 - Circuit Breaker 30-amp for heating element protection"],
		},
	],
	"Fryers": [
		{
			"problem": "Our main fryer just won't heat up anymore - I turn it on and wait forever but the oil stays cold. We had to shut down the whole fried chicken station during lunch rush yesterday. My kitchen staff is getting frustrated because we can't make any of our signature items and customers are complaining about wait times.",
			"solution": "Replaced the faulty gas control valve and ignition module that were preventing proper gas flow to the burner assembly.",
			"parts": ["SKU-GV-245891 - Gas Control Valve 3/4-inch NPT with pilot safety", "SKU-IG-078234 - Electronic Ignition Module 120V with flame sensor"],
		},
		{
			"problem": "The fryer keeps shutting itself off randomly throughout the day, sometimes right in the middle of cooking a batch of fries. The oil will be hot one minute, then boom - everything just stops working. It's driving my cooks crazy because they never know when it's going to happen.",
			"solution": "Replaced the malfunctioning high-limit safety switch that was triggering false shutdowns due to internal sensor drift.",
			"parts": ["SKU-HL-156742 - High-Limit Safety Switch 400\u00b0F manual reset with mounting bracket"],
		},
		{
			"problem": "I can't get the oil temperature right anymore - I set it for 350 degrees but sometimes it barely gets warm, other times it gets so hot it starts smoking and ruins the food. Yesterday we had to throw out three batches of chicken because the oil was way too hot. This thing is costing me money every day.",
			"solution": "Replaced the defective thermostat and recalibrated the temperature control system to maintain accurate oil temperature within specified range.",
			"parts": ["SKU-TS-389156 - Digital Thermostat Controller 200-400\u00b0F range", "SKU-TP-067823 - Temperature Probe RTD sensor 12-inch stainless steel"],
		},
		{
			"problem": "The oil filtration system stopped working completely - the pump won't turn on no matter what we do. Now we have to manually change the oil way more often because we can't filter out the particles. It's taking forever and costing us a fortune in oil costs.",
			"solution": "Replaced the burned-out filtration pump motor and installed new pump relay in the control panel.",
			"parts": ["SKU-PM-234567 - Oil Filtration Pump Motor 1/3 HP 115V single phase", "SKU-RL-445789 - Pump Control Relay 30A 120V coil with mounting socket"],
		},
		{
			"problem": "The basket won't go up and down anymore - it's stuck halfway and we can't lift it out of the oil. My guys are having to use tongs to fish everything out which is dangerous and slow. We're worried someone's going to get burned trying to work around this thing.",
			"solution": "Repaired the pneumatic basket lift cylinder and replaced the damaged air valve that controls basket movement.",
			"parts": ["SKU-CY-678912 - Pneumatic Lift Cylinder 4-inch bore double acting", "SKU-AV-123456 - Air Control Valve 1/4-inch NPT 3-way solenoid operated"],
		},
		{
			"problem": "There's oil leaking all over the floor from underneath the fryer. We're constantly mopping it up but it just keeps coming back. It's making the kitchen floor slippery and dangerous, plus we're losing expensive oil. Health inspector is coming next week and I'm freaking out.",
			"solution": "Replaced the corroded drain valve and associated gaskets that were causing the oil leak at the tank bottom.",
			"parts": ["SKU-DV-789123 - Drain Valve Assembly 2-inch ball valve with lever handle", "SKU-GS-456789 - Drain Valve Gasket Kit high-temperature silicone", "SKU-PT-234891 - Drain Pipe Elbow 2-inch stainless steel 90-degree"],
		},
		{
			"problem": "The control panel is going haywire - half the buttons don't work and the timer keeps resetting itself randomly. We can't set cooking times properly so everything is either overcooked or undercooked. The digital display is flickering and sometimes just goes blank completely.",
			"solution": "Replaced the faulty control board and updated the display module with new programming.",
			"parts": ["SKU-CB-567234 - Main Control Board PCB assembly with temperature controls", "SKU-DS-890456 - Digital Display Module LED 4-digit with timer functions"],
		},
		{
			"problem": "The heating element isn't working right - the oil takes forever to heat up in the morning and never gets hot enough during busy periods. We used to be able to recover temperature quickly between batches but now everything takes twice as long. Customers are complaining about slow service.",
			"solution": "Replaced the damaged electric heating element that had developed internal breaks reducing its heating capacity.",
			"parts": ["SKU-HE-345678 - Electric Heating Element 208V 15kW immersion type tubular"],
		},
		{
			"problem": "The gas fryer keeps making this weird clicking sound but won't light up at all. I can smell a little gas when I try to turn it on, which is making everyone nervous. We've been without our main fryer for two days now and had to move everything to the backup unit, but that's way too small for our volume.",
			"solution": "Replaced faulty gas valve solenoid that was failing to open properly and cleaned gas orifices that were partially blocked.",
			"parts": ["SKU-GV-002847 - Gas valve solenoid 24V AC with 1/2-inch NPT connection", "SKU-GO-001293 - Gas orifice set for natural gas BTU rating 90,000"],
		},
		{
			"problem": "The temperature probe must be broken because the fryer thinks the oil is at 400 degrees when I can tell it's barely warm enough to cook anything. My fries are coming out soggy and pale, and chicken takes forever. The digital readout shows the right temperature but something's definitely not right with the actual heat.",
			"solution": "Installed new temperature probe sensor and recalibrated the digital temperature controller for accurate readings.",
			"parts": ["SKU-TP-003621 - Temperature probe RTD sensor 12-inch with stainless steel sheath"],
		},
		{
			"problem": "Every time we try to drain the oil for cleaning, it just trickles out super slowly instead of flowing normally. What used to take 10 minutes now takes over an hour, and we can never get all the old oil out. It's backing up our whole cleaning schedule and the oil that stays in there goes bad faster.",
			"solution": "Replaced clogged drain valve assembly and cleared blockage in the drain line plumbing system.",
			"parts": ["SKU-DV-004782 - Drain valve assembly 2-inch ball valve with lever handle", "SKU-PF-001956 - Drain line fitting 2-inch NPT elbow connector", "SKU-GS-002341 - Drain valve gasket set high-temperature silicone"],
		},
		{
			"problem": "The safety switch keeps kicking in and shutting everything down even when the oil temperature looks normal. It happened three times during dinner service last night and we lost so many orders. The fryer will run for maybe 20 minutes then just cuts out completely until we reset it.",
			"solution": "Replaced malfunctioning high-limit safety switch that was triggering at incorrect temperature threshold.",
			"parts": ["SKU-HL-005194 - High-limit safety switch 450\u00b0F automatic reset with mounting bracket"],
		},
		{
			"problem": "The oil filter pump is making this horrible grinding noise and barely moving any oil through the system. When it does work, it's so slow that we can't keep up with filtering during busy periods. The oil gets dirty way faster now and everything tastes off because of all the burnt particles floating around.",
			"solution": "Rebuilt the oil filtration pump with new impeller and motor bearings, and replaced worn pump housing gaskets.",
			"parts": ["SKU-FP-003847 - Oil filter pump impeller assembly with stainless steel blades", "SKU-MT-002619 - Pump motor bearing set sealed ball bearings 1/2-inch shaft"],
		},
		{
			"problem": "The fryer vat has these dark stains and pitting that won't come clean no matter how hard we scrub. The oil looks dirty right after we change it, and I'm worried it's affecting the taste of our food. Some spots look like they might even be starting to rust or corrode.",
			"solution": "Replaced deteriorated fryer vat with new stainless steel tank and installed fresh heating element mounting hardware.",
			"parts": ["SKU-FV-006283 - Fryer vat stainless steel 40-pound capacity with drain fitting", "SKU-MH-001742 - Heating element mounting hardware kit with gaskets", "SKU-IF-003456 - Insulation foam kit high-temperature rated for fryer tank"],
		},
		{
			"problem": "The timer function stopped working completely - we set it for 4 minutes but it never beeps or shuts off automatically. Now my cooks have to watch everything like hawks and use their phones to time batches. We've already overcooked several orders because people forgot to check.",
			"solution": "Replaced defective control board timer module and updated the display panel programming.",
			"parts": ["SKU-CB-004921 - Control board timer module with digital display interface"],
		},
		{
			"problem": "The electric heating elements aren't heating evenly anymore - one side of the fryer gets really hot while the other side stays cooler. Food cooks unevenly and we're constantly having to move baskets around to different spots. It's slowing down our whole operation during rush periods.",
			"solution": "Replaced one burned-out heating element and rebalanced the electrical connections to ensure even heat distribution.",
			"parts": ["SKU-HE-005673 - Electric heating element 5000W 240V tubular with terminal connections", "SKU-TC-002847 - Terminal connector set high-temperature rated for heating elements"],
		},
		{
			"problem": "The fryer won't turn on at all - no lights, no heat, nothing happens when I flip the switch. We checked the breaker and it's fine, but this thing is completely dead. It was working fine yesterday afternoon but came in this morning and it's like someone unplugged the whole unit from the inside.",
			"solution": "Replaced faulty main power contactor that had burned contacts preventing electrical connection to the fryer's systems.",
			"parts": ["SKU-CT-098234 - Main Power Contactor 40A 220V with auxiliary contacts"],
		},
		{
			"problem": "The gas valve is stuck open and we can't shut off the gas flow to the burners. Even when I turn the control knob to off position, I can still hear gas flowing and smell it around the unit. This is really dangerous and we had to shut down the whole fryer station until someone can fix it.",
			"solution": "Replaced defective gas solenoid valve that was stuck in the open position and calibrated the gas pressure regulator.",
			"parts": ["SKU-GV-145672 - Gas Solenoid Valve 3/4-inch NPT with 120V coil", "SKU-GR-289453 - Gas Pressure Regulator 1-15 PSI with gauge"],
		},
		{
			"problem": "The oil keeps overflowing from the vat even though we're not overfilling it. It seems like the oil level keeps rising on its own during cooking, and we've had hot oil spill onto the floor twice this week. My staff is scared to use the fryer because they don't know when it might overflow again.",
			"solution": "Replaced cracked oil return line and malfunctioning oil level sensor that was causing filtration system backflow into the main vat.",
			"parts": ["SKU-OL-567891 - Oil Return Line Assembly 1-inch diameter 36-inch length", "SKU-SN-334578 - Oil Level Sensor with float switch and 10-foot cable"],
		},
		{
			"problem": "The fryer makes this loud banging noise every few minutes like something is hitting the inside of the unit. It's so loud that customers in the dining room are asking about it, and my kitchen crew jumps every time it happens. The noise started about a week ago and keeps getting worse.",
			"solution": "Replaced worn filtration pump motor mounts and balanced the impeller assembly that was causing vibration and mechanical noise.",
			"parts": ["SKU-PM-778912 - Filtration Pump Motor Mount Kit with rubber isolators", "SKU-IM-445667 - Pump Impeller Assembly 5-inch diameter stainless steel"],
		},
		{
			"problem": "The digital display shows error codes that keep changing, and none of us know what they mean. Sometimes it shows E03, other times E07, and occasionally just flashes random numbers. The fryer still works but we can't tell what temperature it's actually running at or set any timers properly.",
			"solution": "Replaced faulty control board with corrupted firmware and updated all system programming to manufacturer specifications.",
			"parts": ["SKU-CB-223456 - Main Control Board with LCD display and memory backup"],
		},
		{
			"problem": "The basket lift mechanism moves up and down but it's really jerky and sometimes gets stuck halfway. When it does move, it makes this grinding sound like metal scraping against metal. Yesterday it got stuck with a full basket of fish and we had to manually crank it up, which was really difficult and dangerous with hot oil splashing around.",
			"solution": "Rebuilt basket lift assembly with new drive chain, sprockets, and lubricated all pivot points and guide rails.",
			"parts": ["SKU-BC-667889 - Drive Chain Assembly 48-link stainless steel", "SKU-SP-112233 - Lift Mechanism Sprocket Set with bearings", "SKU-LU-998877 - High-temperature food-grade lubricant 16oz tube"],
		},
		{
			"problem": "There's this weird smell coming from the fryer that's not the usual cooking smells - it's like something electrical is burning. The smell gets stronger when we turn the heat up high, and I'm worried something dangerous is happening inside the unit. A couple of my cooks have complained about headaches after working near it all day.",
			"solution": "Replaced overheating transformer and damaged wiring harness that was causing electrical insulation to burn and emit toxic fumes.",
			"parts": ["SKU-TR-445566 - Step-down Transformer 480V to 24V 100VA", "SKU-WH-778844 - Main Wiring Harness 12-circuit with heat-resistant coating"],
		},
		{
			"problem": "The fryer takes forever to heat up in the morning - what used to take 15 minutes now takes almost an hour. Even when it finally gets warm, it can't keep up with demand during lunch rush and the temperature drops way down every time we add food. We're falling behind on orders and customers are getting impatient.",
			"solution": "Replaced deteriorated thermal insulation around the vat and installed new high-efficiency heating elements with improved heat transfer design.",
			"parts": ["SKU-IN-556677 - Thermal Insulation Kit ceramic fiber 2-inch thickness", "SKU-HE-889900 - High-efficiency Heating Element 15KW 240V with titanium coating"],
		},
		{
			"problem": "The fryer is taking way too long to heat up in the mornings - it used to be ready in 15 minutes but now it takes over an hour to get to temperature. By the time we're ready to cook, we're already behind schedule and the breakfast rush is starting. My crew is getting stressed because we can't prep properly and customers are waiting forever for their hash browns.",
			"solution": "Replaced the faulty gas burner assembly and cleaned out blocked gas orifices that were restricting proper flame distribution.",
			"parts": ["SKU-GB-284751 - Gas Burner Assembly with pilot light and flame spreader", "SKU-OR-156293 - Gas Orifice Set 0.035-inch diameter for natural gas"],
		},
		{
			"problem": "The thermostat seems completely off - I set it to 325 for donuts but the oil gets so hot it's smoking, then other times it won't even bubble when I drop food in. The temperature display shows one thing but the oil feels completely different. We've ruined so many batches trying to figure out what temperature we're actually cooking at.",
			"solution": "Calibrated and replaced the main thermostat control unit and installed a new temperature bulb sensor.",
			"parts": ["SKU-TS-397428 - Thermostat Control 200-400\u00b0F range with capillary tube"],
		},
		{
			"problem": "There's this awful burning smell coming from the fryer even when we're not cooking anything, and I can see smoke coming from somewhere inside the unit. It's making the whole kitchen smell bad and I'm worried it might be a fire hazard. We've had to open all the windows and turn on every fan we have.",
			"solution": "Removed and replaced the burned-out heating element that had developed hot spots and was overheating the surrounding insulation.",
			"parts": ["SKU-HE-529634 - Electric Heating Element 5500W 240V with mounting brackets", "SKU-IN-441782 - High-temperature insulation padding for element housing"],
		},
		{
			"problem": "The fryer keeps cycling on and off every few minutes instead of staying at a steady temperature. Just when we get a batch going, it shuts off and we have to wait for it to heat back up again. It's impossible to maintain any kind of rhythm in the kitchen and everything is taking twice as long to cook.",
			"solution": "Adjusted the temperature differential settings and replaced the worn contactors in the control relay system.",
			"parts": ["SKU-CR-683947 - Control Relay 40-amp with normally open contacts", "SKU-CT-295168 - Contactor Assembly dual-pole for heating circuit", "SKU-TD-137852 - Temperature Differential Control Switch"],
		},
		{
			"problem": "When we try to use the built-in timer, it counts down but never actually turns off the heat when it hits zero. We've had several batches of chicken burn because we thought the timer would shut it off automatically. Now nobody trusts it and we're all using our phones, but that's not practical during busy periods.",
			"solution": "Replaced the defective timer relay switch that was not properly disconnecting power to the heating elements upon timer completion.",
			"parts": ["SKU-TR-758291 - Digital Timer Relay 99-minute countdown with output contacts"],
		},
		{
			"problem": "The oil level keeps dropping throughout the day even though we're not draining it, and I can't figure out where it's going. By closing time we're down almost a gallon from where we started. There's no visible leak on the floor but the oil is definitely disappearing somewhere and replacement oil is expensive.",
			"solution": "Located and sealed internal leak in the heat exchanger coil and replaced damaged vat seam gaskets that were allowing oil to seep into the insulation cavity.",
			"parts": ["SKU-GS-412573 - Vat Seam Gasket Kit high-temperature silicone", "SKU-SE-869341 - Heat Exchanger Sealing Compound ceramic-based"],
		},
		{
			"problem": "The control knobs are so loose they just spin freely without actually changing any settings. I can turn the temperature dial all the way around but nothing happens - it stays at whatever temperature it was before. Same thing with the timer knob. My cooks can't adjust anything and we're stuck with whatever settings were last working.",
			"solution": "Tightened control linkages and replaced stripped gear assemblies that connect the external knobs to the internal adjustment mechanisms.",
			"parts": ["SKU-GR-347692 - Control Gear Assembly plastic with metal insert", "SKU-LK-584127 - Control Linkage Rod Set with coupling springs"],
		},
		{
			"problem": "Every time we filter the oil, it comes back dirtier than when we started. The filter system runs but instead of cleaning the oil, it seems to be stirring up all the crud from the bottom and making everything worse. We're going through oil way faster because we can't get it properly cleaned.",
			"solution": "Replaced clogged filter media and rebuilt the pump impeller assembly that was creating turbulence instead of proper filtration flow.",
			"parts": ["SKU-FM-926413 - Replacement Filter Media pad 20x16 inch pleated", "SKU-IM-671058 - Pump Impeller Assembly with shaft and seals", "SKU-PM-238794 - Pump Motor 1/3 HP single-phase"],
		},
		{
			"problem": "The fryer pilot light won't stay lit no matter how many times we try to relight it. It lights up for a few seconds then just goes out, and we can't get the main burners to fire up at all. We've been running on just our electric fryer all week but it can't handle our volume during lunch rush.",
			"solution": "Replaced the faulty thermocouple that was failing to detect the pilot flame and cleaned the pilot orifice of debris buildup.",
			"parts": ["SKU-TC-248391 - Thermocouple Type K 24-inch with 3/8-inch thread", "SKU-PO-156772 - Pilot Light Orifice 0.018-inch natural gas"],
		},
		{
			"problem": "The fryer basket lift is stuck in the down position and won't raise up automatically like it's supposed to. We have to manually crank it up every single time which is burning out my staff's arms. The automatic timer still works but the lift mechanism just sits there doing nothing when time's up.",
			"solution": "Replaced the worn basket lift motor and lubricated the gear assembly that had seized due to grease buildup.",
			"parts": ["SKU-MT-334567 - Basket Lift Motor 1/4 HP 120V with mounting bracket"],
		},
		{
			"problem": "Our gas fryer burner flames are all yellow and orange instead of blue, and they're not heating the oil efficiently anymore. It takes twice as long to get up to temperature and the flames look really weak and flickering. Plus there's this weird sooty buildup around the burner area that wasn't there before.",
			"solution": "Cleaned and adjusted the gas burner orifices and replaced the primary air shutters that were blocked with grease and debris.",
			"parts": ["SKU-GO-445821 - Gas Burner Orifice Set natural gas 0.086-inch", "SKU-AS-229384 - Primary Air Shutter Assembly with adjustment screws", "SKU-BH-778295 - Burner Head Assembly stainless steel with venturi"],
		},
		{
			"problem": "The high-limit switch keeps tripping and shutting down our fryer even when the oil temperature seems fine on the display. It'll work for maybe an hour then suddenly everything shuts off and we have to wait for it to reset. This happened four times during yesterday's dinner rush and we're losing so much business.",
			"solution": "Replaced the malfunctioning high-limit safety switch that was triggering at incorrect temperatures due to internal sensor drift.",
			"parts": ["SKU-HS-667134 - High Limit Safety Switch 400\u00b0F manual reset with bracket"],
		},
		{
			"problem": "The drain valve handle broke off completely so we can't drain the oil for cleaning at all. The valve is stuck in the closed position and we've tried pliers but can't get enough grip to turn it. We haven't been able to change the oil in three days and it's getting really dark and gross.",
			"solution": "Replaced the entire drain valve assembly including the handle mechanism and installed new gaskets to prevent future leaks.",
			"parts": ["SKU-DV-123896 - Drain Valve Assembly 1.5-inch ball valve with stainless steel handle", "SKU-GK-445729 - Drain Valve Gasket Kit high-temperature resistant"],
		},
		{
			"problem": "The fryer control panel screen is completely blank and none of the buttons respond when you press them. We can't set temperatures, timers, or even see what's happening with the unit. The fryer seems to be running on some default setting but we have no control over anything.",
			"solution": "Replaced the faulty control board that had suffered moisture damage and installed a new LED display panel.",
			"parts": ["SKU-CB-889234 - Digital Control Board with temperature programming", "SKU-DP-556781 - LED Display Panel 4-digit with status indicators", "SKU-MB-332457 - Membrane Button Pad overlay with tactile feedback"],
		},
		{
			"problem": "There's this constant hissing sound coming from somewhere around the gas connections and I can smell gas near the fryer. It's not super strong but it's definitely there and getting worse. My staff is nervous about working near it and I'm worried about safety issues.",
			"solution": "Located and repaired a gas leak at the main supply line connection and replaced the deteriorated gas solenoid valve seals.",
			"parts": ["SKU-GS-774821 - Gas Solenoid Valve 3/4-inch 24V with manual reset", "SKU-GL-445923 - Gas Line Coupling 3/4-inch NPT with thread sealant"],
		},
		{
			"problem": "The oil filtration pump turns on but it's making this awful screeching noise and barely moving any oil through the filter. The whole filtering process that used to take 15 minutes now takes over an hour when it works at all. Sometimes it just stops mid-cycle and we have to restart it multiple times.",
			"solution": "Replaced the worn filtration pump motor and impeller assembly, and installed a new pump coupling that had completely failed.",
			"parts": ["SKU-FP-665432 - Oil Filter Pump Motor 1/3 HP with thermal protection", "SKU-PI-223847 - Pump Impeller Assembly stainless steel", "SKU-PC-778129 - Pump Coupling flexible jaw-type with spider insert"],
		},
		{
			"problem": "The fryer pilot light keeps going out randomly throughout the day, and then we have to wait forever for someone who knows how to relight it safely. Sometimes it stays lit for hours, other times it goes out after just 30 minutes. We're losing so much time during rushes because the fryer goes cold and takes forever to heat back up when this happens.",
			"solution": "Replaced the faulty thermocouple that was providing inconsistent flame sensing signals to the gas control valve, causing intermittent pilot light shutoffs.",
			"parts": ["SKU-TC-892341 - Thermocouple 24-inch length with universal gas valve connection", "SKU-GV-445672 - Pilot light assembly with brass orifice and ignition electrode"],
		},
		{
			"problem": "The fryer oil smells terrible and has this gross foam on top that won't go away no matter how much we skim it off. The food tastes weird and customers have been complaining. We've changed the oil twice this week but the same thing keeps happening within a few hours of fresh oil.",
			"solution": "Replaced the damaged oil return line and filtration screen that were allowing contaminants and moisture to continuously cycle back into the fresh oil.",
			"parts": ["SKU-FL-178923 - Oil filtration screen mesh 100-count stainless steel", "SKU-PL-334567 - Oil return line assembly with rubber gaskets and fittings"],
		},
		{
			"problem": "I can barely hear the fryer pump running anymore and when I do, it sounds really weak and strained. The oil filtration is taking three times longer than it used to, and sometimes the pump just stops working completely in the middle of a cycle. We're having to run shorter filter cycles more often just to keep the oil somewhat clean.",
			"solution": "Replaced the worn impeller and motor bearings in the oil filtration pump, and cleared accumulated debris from the pump housing.",
			"parts": ["SKU-MT-667889 - Oil pump motor 1/3 HP with mounting bracket", "SKU-IM-223445 - Stainless steel impeller assembly with drive shaft"],
		},
		{
			"problem": "The fryer keeps tripping the circuit breaker in our electrical panel, usually right when we're trying to heat up for the lunch rush. It'll work fine on low heat but as soon as we crank it up to cooking temperature, boom - everything shuts off and we have to reset the breaker. This has happened four times this week already.",
			"solution": "Replaced the deteriorated heating element that was drawing excessive current due to internal breakdown and installed new contactors in the control circuit.",
			"parts": ["SKU-HE-556781 - Electric heating element 240V 15KW with terminal connections", "SKU-CT-789012 - Electrical contactor 40-amp dual pole with auxiliary contacts", "SKU-WH-123678 - High-temperature wiring harness for heating element connections"],
		},
		{
			"problem": "The fryer basket gets stuck about halfway down and we have to really force it to go all the way into the oil. When we try to lift it back up, it's even worse - sometimes it takes two people pulling just to get it out. My crew is getting tired arms and I'm worried someone's going to hurt their back wrestling with this thing.",
			"solution": "Cleaned and lubricated the basket lift mechanism rails and replaced the worn lift chain and sprocket assembly that had stretched over time.",
			"parts": ["SKU-CH-445667 - Stainless steel lift chain 36-inch with master link", "SKU-SP-778823 - Drive sprocket assembly with bearing and mounting hardware"],
		},
		{
			"problem": "The digital temperature display keeps jumping around like crazy - one second it says 325, then 380, then back to 310. I have no idea what the actual oil temperature is, so my cooks are just guessing and everything is coming out wrong. We've burned so much food this week because we can't trust what the display is telling us.",
			"solution": "Replaced the faulty temperature sensor probe and recalibrated the digital control module to provide accurate temperature readings.",
			"parts": ["SKU-TS-334512 - RTD temperature sensor probe 12-inch with 1/2-inch NPT fitting"],
		},
		{
			"problem": "There's this constant hissing sound coming from somewhere around the gas connections, and I swear I can smell gas near the fryer when I walk by. It's making everyone in the kitchen nervous, and we're afraid to keep using it but we can't shut down our whole fry operation. The smell seems to get stronger when the fryer is running at full heat.",
			"solution": "Located and repaired multiple small gas leaks at threaded connections and replaced the deteriorated gas supply line with new flexible connector meeting current safety codes.",
			"parts": ["SKU-GL-667543 - Flexible gas supply line 1-inch diameter 48-inch length with safety shutoff", "SKU-GF-889776 - Gas line fitting kit with thread sealant and leak detection solution"],
		},
		{
			"problem": "The oil drain valve is completely stuck closed and won't budge no matter how hard we try to turn it. We haven't been able to change the oil in three days because we can't get the old stuff out. The oil is getting darker and nastier by the hour, and I know it's affecting the taste of everything we're cooking.",
			"solution": "Removed the seized drain valve assembly and replaced it with a new ball valve, also cleared the drain line of accumulated grease buildup.",
			"parts": ["SKU-DV-223344 - Heavy-duty drain valve 1.5-inch with lever handle and gasket kit", "SKU-PL-556789 - Drain line assembly with elbow fittings and support brackets"],
		},
		{
			"problem": "The fryer is cycling on and off constantly - it heats up for a few minutes, then shuts down, then starts up again over and over. We can't maintain steady cooking temperature and our french fries are coming out inconsistent. Some batches are perfect while others are either soggy or burnt because the temperature keeps jumping around.",
			"solution": "Replaced the faulty thermostat control that was cycling incorrectly due to worn contacts and recalibrated the temperature settings.",
			"parts": ["SKU-TH-248591 - Thermostat Control 200-400\u00b0F with SPDT contacts"],
		},
		{
			"problem": "The digital temperature display shows error codes and random numbers instead of the actual oil temperature. My cooks have no idea how hot the oil really is, so they're just guessing on cooking times. We've had several complaints about undercooked food because nobody knows when the oil is ready.",
			"solution": "Replaced the temperature sensor probe and repaired damaged wiring connections to the control board.",
			"parts": ["SKU-TS-156743 - RTD Temperature Sensor Probe 1/8-inch diameter 12-inch length", "SKU-WH-092847 - High-temperature wire harness assembly 6-pin connector"],
		},
		{
			"problem": "Hot oil keeps bubbling up and overflowing whenever we put food in the fryer, making a huge mess and wasting expensive oil. It never used to do this - we could cook full baskets without any problems. Now even small amounts of food cause it to bubble over and we're constantly cleaning oil off everything.",
			"solution": "Cleaned clogged oil return lines and replaced the oil level sensor that was giving false readings.",
			"parts": ["SKU-OL-371629 - Oil Level Sensor Float Switch with 18-inch cable", "SKU-GK-458912 - High-temp gasket kit for oil return assembly"],
		},
		{
			"problem": "The fryer takes almost an hour to heat up from cold, when it used to be ready in 15 minutes. By the time we open for lunch, we're already behind schedule. The heating elements look rusty and corroded, and I think that's why it's so slow now.",
			"solution": "Replaced corroded heating elements and cleaned mineral deposits from the heating element housing.",
			"parts": ["SKU-HE-629184 - Immersion Heating Element 240V 18kW with mounting flange", "SKU-HE-629185 - Immersion Heating Element 240V 18kW with mounting flange", "SKU-CL-074528 - Heating element cleaning compound and descaler"],
		},
		{
			"problem": "Every few hours the fryer just stops working completely - no heat, no lights, nothing - but if we wait about 30 minutes it starts working again. It's like it needs a break or something. This happened four times during our busy Saturday night and we almost ran out of fried appetizers.",
			"solution": "Replaced the overheating high-limit safety switch that was tripping due to excessive heat buildup from a blocked ventilation system.",
			"parts": ["SKU-HL-892634 - High-Limit Safety Switch 450\u00b0F manual reset"],
		},
		{
			"problem": "The oil looks dirty and gross even right after we change it - it gets dark and cloudy within an hour of cooking. Our fried food tastes burnt even when it's not overcooked. I think the filtration system isn't cleaning the oil properly anymore, but the pump seems to be running.",
			"solution": "Replaced worn filter media and cleaned the filtration housing that had accumulated carbonized oil residue blocking proper flow.",
			"parts": ["SKU-FL-516728 - Oil Filter Media Pack 20-micron pleated paper filters", "SKU-FL-516729 - Filter Housing Seal Kit with O-rings"],
		},
		{
			"problem": "The gas burner flames keep going out randomly during cooking, sometimes with a loud popping sound. When they relight automatically, there's a scary whoosh of flame that makes everyone jump. My staff is getting nervous about using this fryer because the flames are so unpredictable.",
			"solution": "Replaced malfunctioning gas solenoid valve and adjusted the gas pressure regulator to proper specifications.",
			"parts": ["SKU-GS-743821 - Gas Solenoid Valve 3/4-inch NPT 120VAC with manual shutoff", "SKU-GR-184567 - Gas Pressure Regulator 0-15 PSI adjustable"],
		},
		{
			"problem": "The drain valve at the bottom won't close all the way anymore - there's always a slow drip of hot oil coming out even when it's supposed to be shut tight. We've got a pan underneath to catch it, but it's messy and we're losing oil constantly. Plus it makes the floor slippery and dangerous.",
			"solution": "Replaced worn drain valve assembly and installed new sealing gaskets to prevent oil leakage.",
			"parts": ["SKU-DV-395174 - Ball Drain Valve 1-inch NPT full-port with lever handle", "SKU-GK-281936 - Drain Valve Gasket Set high-temperature Viton seals"],
		},
		{
			"problem": "The automatic basket lift is stuck in the down position and won't come up no matter what buttons we press. We have to manually pull the baskets out with tongs, which is dangerous with all that hot oil splashing around. One of my cooks already got a minor burn trying to fish out an order of onion rings.",
			"solution": "Repaired the pneumatic cylinder system and replaced the air solenoid valve controlling the basket lift mechanism.",
			"parts": ["SKU-PC-672148 - Pneumatic Cylinder 4-inch bore 8-inch stroke double-acting", "SKU-AS-529663 - Air Solenoid Valve 1/4-inch NPT 120VAC 3-way"],
		},
		{
			"problem": "The control panel buttons are either sticking or not responding at all - I have to press them multiple times to get anything to work. The start button is the worst - sometimes I push it ten times before the fryer actually turns on. My managers are getting frustrated because it takes forever to make simple adjustments.",
			"solution": "Replaced the membrane switch panel and cleaned corrosion from the control board connections caused by oil vapor exposure.",
			"parts": ["SKU-MS-841257 - Control Panel Membrane Switch Assembly 12-button with LED indicators"],
		},
	],
	"Mixers": [
		{
			"problem": "Our big Hobart mixer just stopped working in the middle of our dinner prep. It was making this loud grinding noise for a few days, and now it won't turn on at all. The prep cook was mixing pizza dough when it just died - now we're behind on everything and my staff is stressed.",
			"solution": "Replaced the main drive motor which had seized due to bearing failure and installed new motor control contactor that was also damaged.",
			"parts": ["SKU-MT-024789 - 5HP 3-phase mixer drive motor 1750 RPM with mounting bracket", "SKU-EC-016432 - Motor control contactor 30A 3-pole with 120V coil"],
		},
		{
			"problem": "The mixing bowl on our spiral mixer won't lift up anymore. Yesterday it was moving really slow, and today it's completely stuck at the bottom. My bakers can't get the dough out without making a huge mess, and we've got orders backing up.",
			"solution": "Rebuilt the bowl lift mechanism by replacing worn lift chains and adjusting the motor drive assembly.",
			"parts": ["SKU-BL-009876 - Bowl lift chain assembly 48-inch heavy duty with master links", "SKU-BG-013254 - Lift mechanism bushing set with grease fittings"],
		},
		{
			"problem": "Our planetary mixer keeps changing speeds on its own - one minute it's going slow like we set it, then suddenly it's whipping everything at high speed and making a mess. The kitchen staff is afraid to use it because batter keeps flying everywhere.",
			"solution": "Replaced the variable frequency drive controller that was experiencing internal component failures causing erratic speed control.",
			"parts": ["SKU-VF-018765 - Variable frequency drive 3HP with digital display and speed control potentiometer"],
		},
		{
			"problem": "The safety guard on our mixer won't stay closed, so the machine won't start. We've been having to hold it down while someone else hits the start button, which I know isn't safe. It's slowing down our bread production and my team is getting frustrated.",
			"solution": "Replaced the safety interlock switch and adjusted the guard latch mechanism to ensure proper engagement and safety compliance.",
			"parts": ["SKU-SI-027893 - Safety interlock switch with actuator arm and mounting hardware", "SKU-GD-005432 - Guard latch assembly with spring-loaded mechanism"],
		},
		{
			"problem": "The dough hook attachment keeps slipping and won't stay locked in place. During mixing, it starts wobbling and eventually falls out completely. We've ruined three batches of bread dough this week because of this.",
			"solution": "Replaced the worn attachment hub assembly and drive coupling that had excessive wear preventing proper tool retention.",
			"parts": ["SKU-AH-031287 - Attachment hub assembly with locking collar and drive pins", "SKU-DC-014569 - Drive coupling flexible joint with steel sleeve", "SKU-BG-028741 - Hub bearing set with seals for 2-inch shaft"],
		},
		{
			"problem": "There's this terrible screeching sound coming from inside our mixer whenever we use it. It's so loud the customers in the dining room can hear it. The sound gets worse when we're mixing heavy dough, and I'm worried something's going to break completely.",
			"solution": "Replaced the main gearbox bearings and applied proper lubrication to eliminate noise and prevent further damage.",
			"parts": ["SKU-BG-045612 - Gearbox bearing kit with seals for planetary drive assembly", "SKU-LU-002398 - Food grade gear lubricant 1-quart synthetic blend"],
		},
		{
			"problem": "Our mixer starts up fine but then just stops running after a few minutes. Sometimes it works for an hour, sometimes only five minutes. The kitchen crew never knows if they'll be able to finish a batch, and it's really affecting our production schedule.",
			"solution": "Replaced the motor start capacitor and cleaned corroded electrical connections that were causing intermittent power loss.",
			"parts": ["SKU-CP-019834 - Motor start capacitor 35\u03bcF 440VAC with mounting bracket"],
		},
		{
			"problem": "The mixing bowl won't lock into position anymore - it keeps turning while the paddle is mixing, which makes everything splash out. We've been having to have someone hold the bowl steady, but that's not working for our bigger batches.",
			"solution": "Replaced the bowl lock mechanism pins and tightened the locking cam assembly to restore proper bowl retention.",
			"parts": ["SKU-BL-036789 - Bowl lock pin assembly with spring-loaded mechanism and wear plates"],
		},
		{
			"problem": "Our mixer keeps tripping the circuit breaker every time we try to start it up. It worked fine yesterday, but now as soon as we hit the power button, the whole kitchen loses electricity for a few seconds. My prep team can't get any mixing done and we're falling behind on our sauce and batter prep.",
			"solution": "Replaced the damaged motor starter contactor that was drawing excessive current and causing electrical shorts during startup.",
			"parts": ["SKU-CT-004521 - Motor Starter Contactor 30A 3-Phase with Auxiliary Contacts", "SKU-CP-002847 - Motor Run Capacitor 45\u03bcF 440V Round"],
		},
		{
			"problem": "The mixer bowl tilts down really slowly now and sometimes gets stuck halfway. It used to move up and down smoothly, but now it takes forever and sometimes we have to push it manually. This is really slowing down our prep work when we need to add ingredients or clean the bowl.",
			"solution": "Rebuilt the bowl lift mechanism by replacing worn gear teeth and installing new lubrication seals in the lift assembly.",
			"parts": ["SKU-GB-007293 - Bowl Lift Gear Assembly with Bronze Bushings", "SKU-SL-001654 - Hydraulic Seal Kit for Bowl Lift Cylinder", "SKU-LB-003782 - High-Temperature Gear Lubricant 1-Quart"],
		},
		{
			"problem": "There's oil leaking all over the floor under our big mixer. It's getting really slippery and dangerous for my staff to walk around. The leak seems to be getting worse each day, and now there's a puddle every morning when we come in.",
			"solution": "Replaced failed transmission seals and gaskets in the main gearbox housing to eliminate oil leakage.",
			"parts": ["SKU-GS-005849 - Transmission Main Shaft Seal Kit with O-Rings"],
		},
		{
			"problem": "The mixer won't stop running when we press the stop button - we have to flip the main power switch to turn it off. This is really dangerous because the mixing paddle keeps spinning and we can't add ingredients or clean it properly. My kitchen manager is worried someone's going to get hurt.",
			"solution": "Replaced the faulty control relay and cleaned corroded contacts in the motor control panel to restore proper stop function.",
			"parts": ["SKU-RL-008376 - Control Relay 24V AC DPDT with Socket Base", "SKU-SW-004192 - Emergency Stop Button Red Mushroom Head", "SKU-CC-002551 - Electrical Contact Cleaner Spray 12oz"],
		},
		{
			"problem": "Our planetary mixer makes this horrible knocking sound from inside the mixing head. It's gotten so bad that we can hear it over all the other kitchen noise. The mixing still works but the sound is driving everyone crazy, and I'm afraid it's going to break down completely during our busy dinner rush.",
			"solution": "Replaced worn planetary gear bearings and realigned the gear assembly to eliminate mechanical noise and prevent further damage.",
			"parts": ["SKU-BR-006743 - Planetary Gear Bearing Set with Grease Fittings", "SKU-BH-003421 - Bearing Retainer Housing Assembly"],
		},
		{
			"problem": "The mixer starts really slow and seems like it's struggling to get up to speed. Even on the highest setting, it barely moves thick dough that it used to handle easily. My bakers are having to mix smaller batches and it's taking twice as long to get our bread production done.",
			"solution": "Diagnosed and replaced the failing variable frequency drive controller that was limiting motor power output and speed control.",
			"parts": ["SKU-VF-009284 - Variable Frequency Drive 5HP 480V with Digital Display", "SKU-CB-001827 - Control Cable Assembly 20-Pin Connector"],
		},
		{
			"problem": "The whisk attachment keeps coming loose and wobbling during mixing. We've tried tightening it but it still works its way loose after a few minutes. Yesterday it actually fell into a batch of meringue and we had to throw the whole thing out.",
			"solution": "Replaced worn attachment hub drive assembly and installed new locking mechanism with proper torque specifications.",
			"parts": ["SKU-AH-007651 - Attachment Hub Drive Assembly with Locking Pin", "SKU-SP-004298 - Drive Shaft Spring Washer Set", "SKU-TP-002134 - Torque Pin Stainless Steel with Set Screw"],
		},
		{
			"problem": "Our mixer won't turn on at all anymore, but all the lights on the control panel are working fine. We've checked that it's plugged in and the circuit breaker isn't tripped. The motor just sits there doing nothing when we press start, and we've got a huge catering order that needs to be prepped today.",
			"solution": "Replaced the burned-out motor starting capacitor and cleaned oxidized electrical connections in the motor junction box.",
			"parts": ["SKU-CP-008745 - Motor Start Capacitor 88-108\u03bcF 330V Oval", "SKU-EC-003692 - Electrical Connection Kit with Wire Nuts and Terminal Blocks"],
		},
		{
			"problem": "The mixer bowl keeps dropping down by itself while we're trying to mix. We'll lift it up to the right position, but within a few minutes it slowly sinks back down and we can't reach the dough properly. My prep cooks are getting frustrated because they have to keep stopping to readjust it, and it's making our morning bread prep take forever.",
			"solution": "Replaced worn hydraulic cylinder seals and refilled hydraulic fluid to restore proper bowl lift pressure and holding capacity.",
			"parts": ["SKU-HY-002847 - Hydraulic cylinder seal kit with O-rings and gaskets", "SKU-FL-018923 - Food-grade hydraulic fluid 32 weight 1-gallon container"],
		},
		{
			"problem": "There's this burning smell coming from our mixer every time we use it, especially when mixing heavy pizza dough. The smell is so strong that customers are starting to notice it in the dining room. I'm worried we're going to have a fire or something, but we need this mixer to keep running for our lunch prep.",
			"solution": "Replaced overheating motor windings and installed new thermal protection relay to prevent future overheating damage.",
			"parts": ["SKU-MT-007641 - 3-phase mixer motor 5HP 230V with thermal protection", "SKU-RL-003215 - Thermal overload relay 8-12 amp range", "SKU-CB-009384 - Motor cooling fan assembly with mounting bracket"],
		},
		{
			"problem": "The speed control on our spiral mixer is completely messed up - when we set it to low speed it goes medium, medium goes super fast, and high speed barely moves at all. My bakers can't get the right mixing action for different types of dough, and we've already over-mixed two batches of delicate pastry this morning.",
			"solution": "Recalibrated variable frequency drive parameters and replaced faulty speed control potentiometer to restore proper speed mapping.",
			"parts": ["SKU-VF-012567 - Variable frequency drive controller 5HP 3-phase with display"],
		},
		{
			"problem": "The mixing arm on our planetary mixer has started wobbling really bad during operation. It used to run smooth, but now it shakes the whole machine and makes this rattling noise that's getting worse every day. The uneven mixing is ruining our cake batters because some parts get over-mixed while others barely get touched.",
			"solution": "Rebuilt planetary gear assembly with new bearings and replaced worn drive shaft to eliminate wobble and restore smooth operation.",
			"parts": ["SKU-GR-045128 - Planetary gear assembly complete with housing", "SKU-BR-028463 - Heavy-duty ball bearing set for mixer drive shaft", "SKU-SF-017592 - Drive shaft with keyway for planetary mixer"],
		},
		{
			"problem": "Our mixer keeps shutting off randomly and showing some kind of error code on the display. Sometimes it runs for twenty minutes, other times it stops after just two minutes of mixing. The kitchen staff never knows if they'll be able to finish a batch, and we've had to hand-mix three batches of cookie dough because we can't rely on this thing anymore.",
			"solution": "Replaced malfunctioning control board and updated firmware to eliminate random shutdowns and error code generation.",
			"parts": ["SKU-CB-091235 - Main control board with digital display and programming", "SKU-CA-054789 - Backup capacitor bank for control system memory"],
		},
		{
			"problem": "The safety cover on our big mixer won't stay latched shut anymore, so the machine thinks it's open and won't start. We've tried pushing it down hard and jiggling the latch, but it just pops back open. My morning shift can't get any mixing done and we're already behind on our soup and sauce prep for lunch service.",
			"solution": "Adjusted safety interlock switch positioning and replaced worn latch mechanism to ensure proper cover engagement and safety compliance.",
			"parts": ["SKU-SW-063847 - Magnetic safety interlock switch with mounting bracket", "SKU-LT-029156 - Cover latch assembly with spring-loaded mechanism"],
		},
		{
			"problem": "There's grease or oil constantly dripping from somewhere inside our mixer onto the floor. It's creating a slippery mess that's dangerous for my staff, and the health inspector is coming next week. The dripping seems to get worse when we're mixing heavy bread dough, and now there's stains on the floor that won't come clean.",
			"solution": "Replaced leaking gearbox seals and replenished food-grade lubricant to eliminate oil leakage and ensure proper lubrication.",
			"parts": ["SKU-SL-084721 - Gearbox seal kit with gaskets and O-ring seals", "SKU-LB-037298 - Food-grade gear lubricant NSF certified 2-quart container", "SKU-DR-041853 - Oil drain plug with magnetic chip collector"],
		},
		{
			"problem": "The paddle attachment on our mixer keeps getting stuck and won't come off when we need to switch to the whisk. We've been using pliers to twist it off, but that's scratching up the attachment hub and making it even harder to remove. It's slowing down our prep work because we can't quickly change between different mixing jobs.",
			"solution": "Cleaned and regreased attachment hub mechanism and replaced worn quick-release collar to restore smooth attachment changes.",
			"parts": ["SKU-HB-075394 - Quick-release attachment hub with collar and spring mechanism"],
		},
		{
			"problem": "Our spiral mixer just died right in the middle of kneading a big batch of pizza dough. The display screen went completely black and now nothing happens when we press any buttons. We've got three more pizza dough batches that need to be made before dinner service and my prep team is starting to panic.",
			"solution": "Replaced the faulty main control board and updated the programming to restore all mixer functions.",
			"parts": ["SKU-CB-248751 - Main Control Board Assembly with LCD Display and Programming Chip"],
		},
		{
			"problem": "The mixer bowl won't come off no matter how hard we try to unlock it. The release handle feels loose and floppy like it's not connected to anything inside. We finished our morning bread mixing but now we can't clean the bowl properly, and there's dried dough stuck all over it that we can't reach.",
			"solution": "Repaired the bowl release mechanism by replacing the broken linkage rod and adjusting the locking cam assembly.",
			"parts": ["SKU-LK-157239 - Bowl Release Linkage Rod 12-inch Stainless Steel", "SKU-LK-157240 - Locking Cam Assembly with Spring Actuator"],
		},
		{
			"problem": "Every time we start mixing something thick like cookie dough, the mixer makes this loud chattering noise and the whole machine vibrates so much it walks across the floor. It's gotten so bad that plates are rattling on the shelves nearby. The mixing still happens but everyone's afraid to get near it when it's running.",
			"solution": "Replaced worn planetary gear assembly bearings and realigned the drive mechanism to eliminate excessive vibration.",
			"parts": ["SKU-BG-394827 - Planetary Gear Bearing Set Heavy-Duty Sealed", "SKU-BG-394828 - Drive Shaft Alignment Collar", "SKU-BG-394829 - Gear Housing Mounting Bushing"],
		},
		{
			"problem": "The mixer keeps shutting itself off after running for just a couple minutes, especially when we're doing heavy mixing. There's no warning or anything - it just stops and won't restart for about ten minutes. My pastry chef is frustrated because she can't finish mixing her cake batters without having to wait around.",
			"solution": "Replaced the overheating motor capacitor and cleaned the cooling vents to prevent thermal shutdowns.",
			"parts": ["SKU-CP-671453 - Motor Start Capacitor 45\u00b5F 370V with Mounting Bracket", "SKU-CP-671454 - Motor Run Capacitor 25\u00b5F 440V"],
		},
		{
			"problem": "There's this weird electrical buzzing sound coming from the control box every time we change speeds. Sometimes when we switch from low to medium, there's actually a little spark we can see through the vents. It's really concerning and my kitchen manager thinks we should stop using it before something bad happens.",
			"solution": "Replaced the faulty speed control contactor that was arcing and creating electrical hazards.",
			"parts": ["SKU-CT-582916 - Variable Speed Contactor 30-Amp 3-Phase with Overload Protection"],
		},
		{
			"problem": "The dough paddle keeps getting stuck in one position and won't rotate around the bowl like it's supposed to. We have to manually push it to get it unstuck, but then it just gets stuck again in a different spot. Our bread dough is coming out unevenly mixed because the paddle isn't reaching all areas of the bowl.",
			"solution": "Rebuilt the planetary drive mechanism by replacing worn drive gears and lubricating all moving components.",
			"parts": ["SKU-PG-738294 - Planetary Drive Gear Assembly Cast Steel", "SKU-PG-738295 - Drive Ring Gear with Hardened Teeth", "SKU-LB-738296 - Food-Grade Gear Lubricant 16oz Tube"],
		},
		{
			"problem": "Our mixer won't start at all when we have the safety cover closed, but it works fine with the cover open which obviously isn't safe. The red warning light stays on no matter what we do. We need to get our morning prep done but can't risk running it without the safety guards in place.",
			"solution": "Replaced the malfunctioning safety interlock switch and adjusted the guard alignment to ensure proper contact.",
			"parts": ["SKU-SF-419672 - Magnetic Safety Interlock Switch with Mounting Hardware"],
		},
		{
			"problem": "The mixer bowl tilts up and down okay, but it won't lock in the mixing position anymore. It slowly drifts down while we're mixing and we have to keep stopping to lift it back up. My prep cook says it's impossible to add ingredients properly when the bowl keeps moving around like that.",
			"solution": "Replaced the worn bowl lift cylinder seals and recharged the hydraulic system to restore proper holding pressure.",
			"parts": ["SKU-HL-863527 - Hydraulic Cylinder Seal Kit with O-Rings", "SKU-HL-863528 - Food-Grade Hydraulic Fluid 1-Quart Bottle"],
		},
		{
			"problem": "Our spiral mixer just completely seized up this morning while my baker was working on focaccia dough. She said it felt like it was getting harder to turn for the past few days, but now the mixing arm won't budge at all. We tried turning it off and back on, but nothing - it's like the whole thing is locked up solid and we can't get any bread production done.",
			"solution": "Replaced the main gearbox assembly which had suffered complete gear tooth failure due to lack of proper lubrication, and installed new transmission oil.",
			"parts": ["SKU-GB-248517 - Main spiral mixer gearbox assembly 3-speed with sealed bearings", "SKU-LU-156203 - Food grade transmission oil 2-quart synthetic blend"],
		},
		{
			"problem": "The timer on our planetary mixer keeps resetting itself back to zero randomly during mixing cycles. Yesterday it happened three times while we were making cookie dough - the mixer would just keep running way past when it should have stopped. My pastry chef had to stand there and watch it constantly because we almost over-mixed an entire batch of delicate cake batter.",
			"solution": "Replaced the faulty digital timer control module and updated the control board firmware to resolve timing inconsistencies.",
			"parts": ["SKU-TM-392847 - Digital timer control module 60-minute capacity with memory backup"],
		},
		{
			"problem": "There's this weird vibration coming from underneath our big Hobart mixer that's getting worse every week. The whole counter shakes now when we're mixing anything heavy like bread dough, and I can feel it through the floor. My prep team is worried something's going to fall off the shelves nearby, and the noise is really annoying during our morning prep.",
			"solution": "Replaced worn motor mount bushings and installed new vibration dampening pads, then realigned the motor assembly to eliminate excessive movement.",
			"parts": ["SKU-BU-174638 - Motor mount bushing set heavy-duty rubber with steel sleeves", "SKU-PD-089274 - Anti-vibration pads commercial grade 6-inch square", "SKU-MT-445192 - Motor alignment bracket kit with adjustment bolts"],
		},
		{
			"problem": "The paddle attachment on our countertop mixer keeps getting stuck and won't come off when we're done mixing. We have to use pliers and really force it, which is scratching up the attachment hub. It's taking forever to switch between different attachments, and my kitchen staff is getting frustrated with how long it takes to clean and change setups.",
			"solution": "Cleaned and lubricated the attachment hub mechanism, then replaced the worn locking collar that had developed excessive wear patterns.",
			"parts": ["SKU-HU-527163 - Attachment hub locking collar stainless steel with spring mechanism"],
		},
		{
			"problem": "Our mixer's emergency stop button got pressed yesterday and now it won't reset properly. The red button is still pushed in and won't pop back out no matter what we do. The mixer won't start at all because of this, and we've got a big wedding cake order that needs to be mixed today. I've tried everything but that stupid button just stays stuck down.",
			"solution": "Replaced the defective emergency stop switch assembly and tested all safety interlock circuits to ensure proper operation.",
			"parts": ["SKU-ES-631875 - Emergency stop switch assembly twist-to-release with LED indicator", "SKU-WH-298506 - Safety interlock wiring harness 14-gauge with connectors"],
		},
		{
			"problem": "The motor on our spiral mixer keeps overheating and shutting down after about 20 minutes of use. It used to run all day without problems, but now it gets so hot you can't even touch the housing. Every time it shuts down, we have to wait an hour for it to cool down before we can use it again, which is killing our production schedule.",
			"solution": "Replaced the motor cooling fan and cleaned out accumulated flour dust from the motor housing, then installed a new thermal overload protector with proper heat dissipation.",
			"parts": ["SKU-FN-815792 - Motor cooling fan 12-volt variable speed with dust guards", "SKU-OL-347219 - Thermal overload protector 15-amp auto-reset with temperature sensor"],
		},
		{
			"problem": "The power light comes on when we turn on our planetary mixer, but the motor won't actually start running. We can hear a humming sound like it's trying to work, but the mixing arm just sits there. This started happening intermittently last week, but now it won't start at all and we can't get any of our daily bread prep done.",
			"solution": "Replaced the failed motor start capacitor which had lost its electrical capacity, preventing the motor from achieving initial startup torque.",
			"parts": ["SKU-CP-926481 - Motor start capacitor 35-microfarad 370-volt with mounting bracket"],
		},
		{
			"problem": "The bowl lift on our big mixer moves up fine, but when we try to lower it down, it drops really fast and slams to the bottom with a loud bang. It's so violent that batter splashes everywhere and my bakers are afraid to put their hands near it. We've been having to guide it down manually, but that's not safe and it's really slowing us down.",
			"solution": "Rebuilt the hydraulic bowl lift cylinder and replaced the flow control valve to restore proper descent speed control.",
			"parts": ["SKU-HL-753418 - Hydraulic lift cylinder rebuild kit with seals and springs", "SKU-FV-482937 - Flow control valve adjustable with pressure relief"],
		},
		{
			"problem": "Our mixer's timer doesn't work anymore - we set it for 10 minutes but it just keeps running forever until we manually shut it off. Yesterday we accidentally over-mixed a batch of cookie dough because nobody noticed it was still going. My bakers are having to stand there and watch it the whole time instead of working on other prep.",
			"solution": "Replaced the defective timer relay module and recalibrated the control system timing circuits.",
			"parts": ["SKU-TM-482756 - Timer relay module 24V with 60-minute range", "SKU-EC-593847 - Electronic control board assembly with timer circuits"],
		},
		{
			"problem": "The mixer keeps overheating and shutting itself down after about 20 minutes of use. The motor housing gets so hot you can't even touch it, and then everything just stops working. We're having to let it cool down for an hour between batches, which is killing our production schedule for dinner prep.",
			"solution": "Cleaned and replaced the motor cooling fan assembly and installed new thermal protection switches with proper temperature ratings.",
			"parts": ["SKU-FN-294735 - Motor cooling fan 115V with mounting bracket", "SKU-TS-847362 - Thermal overload switch 40-amp rated"],
		},
		{
			"problem": "There's grease and oil coming out of the mixing head and dripping into our food. It started as just a few drops, but now it's making our dough and batter taste awful and we can't serve anything mixed in there. The health inspector is coming next week and I'm panicking about this mess.",
			"solution": "Rebuilt the planetary gear assembly housing with new seals and gaskets, and refilled with food-grade lubricant.",
			"parts": ["SKU-SL-638291 - Planetary gearbox seal kit with O-rings and gaskets", "SKU-LB-745829 - Food-grade gear lubricant NSF-certified 1-quart", "SKU-GB-382947 - Planetary gear bearing assembly with retainer"],
		},
		{
			"problem": "Our spiral mixer's bowl won't rotate at all - the mixing arm spins fine but the bowl just sits there completely still. The dough isn't getting mixed properly because it's all bunching up on one side. My head baker says this is ruining the gluten development in our artisan breads.",
			"solution": "Replaced the bowl rotation drive motor and repaired the damaged gear coupling that connects to the bowl drive mechanism.",
			"parts": ["SKU-MT-572938 - Bowl rotation drive motor 1/2 HP 3-phase", "SKU-CP-849573 - Flexible gear coupling with steel hubs"],
		},
		{
			"problem": "The emergency stop button is stuck and won't pop back out when we press it. We can push it in to stop the mixer, but then we have to pry it out with a screwdriver to get the machine running again. This is really dangerous and my insurance company would flip if they saw us doing this.",
			"solution": "Replaced the emergency stop switch assembly with new actuator mechanism and installed fresh contact blocks.",
			"parts": ["SKU-ES-736492 - Emergency stop switch mushroom head twist-release"],
		},
		{
			"problem": "The digital display on our mixer control panel is completely blank - no numbers, no lights, nothing. We have no idea what speed it's running at or how long it's been mixing. The mixer still works if we press buttons, but we're basically guessing at everything and it's making it impossible to follow our recipes properly.",
			"solution": "Replaced the defective LCD display module and reprogrammed the control board with updated firmware.",
			"parts": ["SKU-DP-429857 - LCD display module 4-digit with backlight", "SKU-CB-683947 - Main control board with programming interface"],
		},
		{
			"problem": "There's this constant humming noise coming from the electrical box on our mixer, and sometimes we see little sparks inside when we open the panel. The mixer still runs but I'm terrified we're going to have an electrical fire. The whole kitchen smells like burning plastic near the mixer.",
			"solution": "Replaced worn electrical contactors and burned capacitors, then cleaned and tightened all electrical connections in the control panel.",
			"parts": ["SKU-CT-857294 - Main contactor 40-amp 3-pole with auxiliary contacts", "SKU-CP-394756 - Start capacitor 250V 50-microfarad", "SKU-CP-394757 - Run capacitor 440V 30-microfarad"],
		},
		{
			"problem": "The mixer paddle height is completely wrong now - it's hitting the bottom of the bowl and making this horrible scraping sound. We used to be able to adjust it perfectly, but now even when we raise it all the way up, it's still too low and gouging scratches in our mixing bowls.",
			"solution": "Recalibrated the mixing head height adjustment mechanism and replaced the worn lift screw assembly with proper positioning stops.",
			"parts": ["SKU-LA-592847 - Height adjustment screw assembly with lock nuts", "SKU-BS-738594 - Mixing head support bushing set"],
		},
		{
			"problem": "Our mixer keeps overheating and shutting itself down right in the middle of mixing our pizza dough. It'll work for maybe 20 minutes then just stops with some kind of warning light flashing. We have to wait an hour for it to cool down before we can use it again, which is killing our prep schedule during the lunch rush.",
			"solution": "Replaced the motor cooling fan and cleaned out accumulated flour dust from the motor housing ventilation screens.",
			"parts": ["SKU-MT-002847 - Motor Cooling Fan Assembly 12V DC with mounting bracket", "SKU-FL-001923 - Motor Housing Air Filter Screen set of 3"],
		},
		{
			"problem": "The mixer won't go into reverse anymore, which we need for our spiral dough mixing. It moves forward fine but when we hit the reverse button nothing happens. Our bread dough isn't getting the proper gluten development because we can't do the reverse kneading cycle.",
			"solution": "Replaced the faulty forward/reverse contactor relay in the electrical control panel that had burned contacts preventing reverse operation.",
			"parts": ["SKU-EC-004521 - Motor Reversing Contactor 3-phase 25A with auxiliary contacts"],
		},
		{
			"problem": "There's this metallic grinding sound coming from the gearbox area of our big spiral mixer. It's not super loud but you can definitely hear it over the normal mixing noise. I'm worried it's going to seize up completely and leave us without our main dough mixer during our busiest weekend.",
			"solution": "Drained and replaced contaminated gear oil and replaced worn intermediate gear bearings in the transmission housing.",
			"parts": ["SKU-GB-007834 - Food Grade Gear Oil SAE 220 viscosity 5-gallon container", "SKU-BR-003492 - Intermediate Shaft Ball Bearing 6308-2RS sealed", "SKU-BR-003501 - Output Shaft Roller Bearing 22215-E1-K spherical"],
		},
		{
			"problem": "The timer on our mixer doesn't work right - we set it for 10 minutes but it either runs for way longer or stops after just a couple minutes. My pastry chef can't rely on it anymore and has to stand there watching the whole time instead of working on other prep.",
			"solution": "Replaced the defective electronic timer module and recalibrated the control system timing parameters.",
			"parts": ["SKU-CT-001687 - Digital Timer Module 0-60 minutes with relay output"],
		},
		{
			"problem": "The planetary head on our 20-quart mixer has developed this really bad vibration that gets worse as we increase the speed. It's shaking so much that ingredients are bouncing out of the bowl and the whole machine is walking across the floor. We've had to move it against the wall so it doesn't slide around.",
			"solution": "Replaced worn planetary gear assembly and rebalanced the mixing head unit with new counterweight.",
			"parts": ["SKU-PG-005673 - Planetary Gear Assembly complete with ring gear and pinions", "SKU-PG-005689 - Planetary Head Counterweight Balance Ring"],
		},
		{
			"problem": "Our mixer won't start unless we jiggle the power switch back and forth a bunch of times. Sometimes it takes five minutes of messing with it before it finally kicks on. My morning prep crew is wasting so much time trying to get this thing running that we're behind on everything before we even open.",
			"solution": "Replaced the worn main power switch and tightened loose electrical connections in the control panel.",
			"parts": ["SKU-SW-002341 - Main Power Switch heavy-duty 3-phase with LED indicator", "SKU-EC-007821 - Wire Terminal Connector Kit assorted sizes"],
		},
		{
			"problem": "The bowl lift is making this awful squealing noise every time it goes up or down. It sounds like metal scraping on metal and it's so loud you can hear it in the dining room. The lift still works but the noise is driving everyone crazy and I'm embarrassed when customers hear it.",
			"solution": "Lubricated the bowl lift mechanism and replaced worn lift chain guides and tensioner assembly.",
			"parts": ["SKU-BL-004782 - Bowl Lift Chain Guide Set with bronze bushings", "SKU-LB-001234 - Food Grade Chain Lubricant spray 16oz aerosol"],
		},
		{
			"problem": "The emergency stop button is stuck and won't pop back out after we press it. We have to use a screwdriver to pry it out every time, which is really dangerous because sometimes the mixer is still running when we're trying to reset it. This is definitely not safe for my kitchen staff.",
			"solution": "Replaced the seized emergency stop switch assembly and cleaned corrosion from the mounting housing.",
			"parts": ["SKU-ES-003456 - Emergency Stop Switch mushroom head twist-to-reset", "SKU-CL-008901 - Electrical Contact Cleaner degreaser 12oz spray"],
		},
		{
			"problem": "Our spiral mixer's bowl won't rotate at all anymore. The mixing arm moves fine but the bowl just sits there, so we're not getting any proper mixing action. All our dough comes out with streaks of unmixed flour and the texture is completely wrong for our artisan breads.",
			"solution": "Replaced the broken bowl drive belt and realigned the bowl rotation motor coupling.",
			"parts": ["SKU-BT-006723 - Bowl Drive Belt V-type 42-inch circumference heavy-duty"],
		},
		{
			"problem": "The mixer keeps blowing fuses in the electrical panel - we've gone through six fuses this week already. It'll work for a while then suddenly pop the fuse and everything shuts down. My electrician keeps telling me to call a service tech because he thinks there's a short circuit somewhere inside the mixer.",
			"solution": "Located and repaired damaged motor winding insulation and replaced the motor start capacitor that was causing overcurrent conditions.",
			"parts": ["SKU-CP-004587 - Motor Start Capacitor 340-408 MFD 220V with mounting bracket", "SKU-TP-007234 - Electrical Insulation Tape high-temperature rated"],
		},
	],
	"Refrigeration": [
		{
			"problem": "Our walk-in cooler is barely keeping things cold anymore - it's running at like 45 degrees instead of 38. The lettuce is wilting by lunch and we had to throw out a whole case of chicken yesterday. My staff keeps complaining that drinks aren't cold enough for customers.",
			"solution": "Replaced the worn compressor start capacitor and cleaned the condenser coils which were heavily clogged with grease and debris, restoring proper cooling capacity.",
			"parts": ["SKU-CP-002847 - Start Capacitor 108-130 MFD 370V", "SKU-CL-003921 - Condenser Coil Cleaner Heavy Duty Foaming Agent"],
		},
		{
			"problem": "The freezer door won't stay closed properly and keeps popping open throughout the day. Ice cream is getting soft and we're losing money on spoiled frozen goods. It's driving my kitchen staff crazy having to constantly push it shut.",
			"solution": "Replaced deteriorated door gaskets and adjusted door hinges to ensure proper seal and alignment.",
			"parts": ["SKU-GS-001453 - Door Gasket 24x60 inch Magnetic Seal Gray", "SKU-HG-004782 - Heavy Duty Door Hinge Kit Stainless Steel"],
		},
		{
			"problem": "There's water all over the floor under our reach-in cooler every morning when we open. It's creating a slip hazard and my prep cooks are slipping around trying to work. The puddle just keeps getting bigger each day.",
			"solution": "Cleared blocked drain line and replaced malfunctioning drain heater that was allowing ice buildup to obstruct proper drainage.",
			"parts": ["SKU-DH-005639 - Drain Heater 120V 50W with Thermostat", "SKU-DL-002918 - Flexible Drain Line Kit 3/4 inch x 6 feet"],
		},
		{
			"problem": "Our display case compressor is making this awful grinding noise that's getting louder every day. Customers are starting to complain about the noise, and I'm worried it's going to break down completely during our busy weekend rush.",
			"solution": "Replaced failing compressor with hermetic scroll compressor and updated start relay assembly.",
			"parts": ["SKU-CM-008756 - Hermetic Scroll Compressor 1.5HP R-404A", "SKU-RL-003247 - Start Relay Assembly 120V with Overload Protection", "SKU-MG-001892 - Compressor Mounting Grommets Vibration Dampening"],
		},
		{
			"problem": "The freezer is constantly running and never shuts off, which is jacking up our electric bill. The temperature stays okay but you can hear it running all night long. My manager is breathing down my neck about the energy costs.",
			"solution": "Replaced faulty temperature control thermostat that was not cycling the compressor properly, allowing continuous operation.",
			"parts": ["SKU-TC-004561 - Temperature Control Thermostat -10 to +50F Range"],
		},
		{
			"problem": "Ice keeps building up thick on the evaporator coils in our walk-in freezer and we have to manually defrost it every few days. It's taking forever to defrost and we're losing valuable freezer space. My crew is getting tired of moving everything out constantly.",
			"solution": "Replaced defective defrost timer and installed new defrost heater elements to restore automatic defrost cycling.",
			"parts": ["SKU-DT-007234 - Defrost Timer 120V 6-Hour Cycle Mechanical", "SKU-HE-005891 - Defrost Heater Element 800W 120V Sheathed"],
		},
		{
			"problem": "Our reach-in cooler temperatures keep swinging up and down - sometimes it's too cold and freezes the salad greens, other times it's too warm and the dairy goes bad. The kitchen staff never knows what temperature to expect when they open it up.",
			"solution": "Replaced malfunctioning thermostatic expansion valve and recharged refrigerant system to proper levels for consistent temperature control.",
			"parts": ["SKU-TV-003456 - Thermostatic Expansion Valve R-134a 1/2 inch", "SKU-RF-009123 - R-134a Refrigerant 30lb Cylinder"],
		},
		{
			"problem": "The fan in our display case stopped working completely and now the front glass keeps fogging up so customers can't see the food. It's embarrassing and definitely hurting our sales since people can't see what we're offering.",
			"solution": "Replaced burned out evaporator fan motor and damaged fan blade assembly to restore proper air circulation.",
			"parts": ["SKU-FM-004823 - Evaporator Fan Motor 1/20HP 115V CW Rotation", "SKU-FB-002674 - Fan Blade Assembly 8-inch Diameter Plastic"],
		},
		{
			"problem": "Our beer cooler isn't getting cold enough and the bottles are coming out lukewarm. Customers are complaining about warm beer and we're having to give out free drinks. The compressor runs but nothing seems to be happening.",
			"solution": "Diagnosed and repaired refrigerant leak in condenser coil, recharged system, and replaced damaged liquid line drier.",
			"parts": ["SKU-LD-006789 - Liquid Line Filter Drier 3/8 inch SAE", "SKU-RF-009123 - R-134a Refrigerant 30lb Cylinder", "SKU-LK-001567 - Refrigerant Leak Sealant Professional Grade"],
		},
		{
			"problem": "The compressor on our prep table cooler keeps shutting off randomly throughout the day and then starts back up hours later. My prep cooks are constantly worried about food safety and we've had to move ingredients to other coolers as backup.",
			"solution": "Replaced overheating compressor overload protector and cleaned condenser fan motor to prevent thermal shutdowns.",
			"parts": ["SKU-OP-005432 - Compressor Overload Protector 3-Wire Terminal", "SKU-CF-007891 - Condenser Fan Motor 1/6HP 208-230V"],
		},
		{
			"problem": "Our walk-in freezer door alarm keeps going off every few minutes even when the door is completely shut. It's driving everyone in the kitchen absolutely nuts and we can't concentrate on cooking. The beeping is so loud that customers in the dining room are starting to ask what's wrong.",
			"solution": "Replaced the faulty magnetic door switch that was intermittently losing contact and recalibrated the door alarm timer settings.",
			"parts": ["SKU-DS-847291 - Magnetic door switch heavy-duty with 6-foot wire leads", "SKU-TM-392847 - Digital door alarm timer 0-10 minute adjustable delay"],
		},
		{
			"problem": "The condenser coils on our sandwich prep cooler are completely caked with grease and dust - you can barely see the metal anymore. The unit is running hot and struggling to keep up during lunch rush. My sandwich station is basically unusable when it gets busy because nothing stays cold.",
			"solution": "Thoroughly cleaned the condenser coils with commercial degreaser and installed a new condenser fan motor that had seized due to debris buildup.",
			"parts": ["SKU-FM-184729 - Condenser fan motor 1/4 HP 115V 1625 RPM with mounting bracket"],
		},
		{
			"problem": "There's this weird chemical smell coming from our display freezer that gets stronger throughout the day. My customers are starting to notice it and a few have asked if the ice cream is still good to eat. I'm worried we might have a refrigerant leak or something serious going on.",
			"solution": "Located and repaired a small refrigerant leak at the evaporator coil connection and recharged the system with the proper refrigerant amount.",
			"parts": ["SKU-RF-729384 - R-404A refrigerant 25-pound cylinder", "SKU-SV-485927 - Refrigerant service valve 1/4-inch flare connection", "SKU-CL-637281 - Copper line set 1/4-inch x 3/8-inch 15-foot length"],
		},
		{
			"problem": "Our main walk-in cooler light burned out last week and it's pitch black in there. My prep cooks are using flashlights to find ingredients and it's slowing everything down. The light fixture looks old and I think the ballast might be shot too.",
			"solution": "Replaced the failed fluorescent ballast and installed new LED tube lights with updated fixtures rated for low-temperature environments.",
			"parts": ["SKU-LT-293847 - LED tube light 4-foot 32W cold-temperature rated", "SKU-BL-847392 - Electronic ballast T8 fluorescent 2-lamp instant start"],
		},
		{
			"problem": "The drain line in our ice machine area is backing up and there's nasty smelling water overflowing onto the floor. It's creating a health hazard and the smell is getting into our dining area. We've tried plunging it but the backup just keeps happening.",
			"solution": "Cleared the blocked drain line and installed a new condensate drain heater to prevent future ice blockages in the drainage system.",
			"parts": ["SKU-DH-384759 - Condensate drain heater 120V 50W with thermostat control", "SKU-DL-692847 - Flexible drain line 3/4-inch diameter 10-foot length"],
		},
		{
			"problem": "Our reach-in freezer handle broke off this morning and now we can't get the door open at all. All our frozen inventory is trapped inside and we need it for tonight's dinner service. The handle just snapped right off when my cook tried to open it.",
			"solution": "Installed a new heavy-duty door handle assembly and reinforced the mounting points with additional hardware to prevent future failures.",
			"parts": ["SKU-HD-572938 - Commercial door handle heavy-duty stainless steel with lock", "SKU-MH-847263 - Door handle mounting hardware reinforcement kit"],
		},
		{
			"problem": "The shelves in our walk-in cooler keep sagging and tilting, causing products to slide off and crash to the floor. We've lost several cases of produce this week and it's becoming a real safety issue. The shelving system seems to be falling apart.",
			"solution": "Replaced worn shelf brackets and installed new heavy-duty wire shelving rated for commercial refrigeration loads.",
			"parts": ["SKU-SH-748392 - Wire shelf 24x48 inch epoxy-coated commercial grade", "SKU-BR-395847 - Heavy-duty shelf bracket set adjustable height", "SKU-SU-684729 - Shelf support posts 74-inch height with leveling feet"],
		},
		{
			"problem": "Our beverage cooler thermostat seems to be stuck and won't respond when we try to adjust the temperature. The drinks are getting way too cold and actually starting to freeze, which is ruining our expensive craft beers. The dial just spins freely without clicking into place.",
			"solution": "Replaced the faulty mechanical thermostat with a new digital temperature controller and recalibrated the system to proper beverage storage temperatures.",
			"parts": ["SKU-TC-847293 - Digital temperature controller -10\u00b0F to 50\u00b0F with display", "SKU-TS-392746 - Temperature sensor probe 6-foot cable NTC type"],
		},
		{
			"problem": "The insulation around our freezer door is falling apart and there are gaps everywhere that you can feel cold air rushing out of. Our electric bills have been through the roof and ice crystals keep forming around the door frame. It's like trying to cool the entire kitchen.",
			"solution": "Stripped and replaced all deteriorated door insulation with new foam gasket material and installed magnetic door strips to ensure proper sealing.",
			"parts": ["SKU-IN-573849 - Door insulation foam gasket 1-inch thick 25-foot roll", "SKU-MG-847562 - Magnetic door seal strip 3/4-inch width 50-foot length"],
		},
		{
			"problem": "Our prep cooler started making this loud rattling noise yesterday and now it's vibrating so much that it's shaking the whole prep station. My cooks can't work properly because their cutting boards are bouncing around. The noise is getting worse every hour.",
			"solution": "Replaced the worn compressor mounting isolators and rebalanced the condenser fan assembly that had developed excessive vibration.",
			"parts": ["SKU-VI-284759 - Compressor vibration isolator set of 4 heavy-duty rubber", "SKU-FB-647382 - Fan blade assembly 12-inch diameter balanced", "SKU-MB-395847 - Motor mounting bracket anti-vibration design"],
		},
		{
			"problem": "The temperature readout on our walk-in cooler shows 38 degrees but when I check with my own thermometer it's actually running at 32 degrees and freezing everything. All our fresh produce is getting frost damage and the lettuce looks like garbage. My kitchen manager is furious because we're throwing away hundreds of dollars in vegetables every day.",
			"solution": "Replaced the faulty temperature sensor and recalibrated the digital temperature controller to ensure accurate readings and proper temperature control.",
			"parts": ["SKU-TS-248901 - Temperature Sensor RTD Probe 6-inch with digital output", "SKU-TC-156789 - Digital Temperature Controller with display and relay output"],
		},
		{
			"problem": "Our chest freezer lid is so heavy that my staff can barely lift it anymore and it slams shut on their hands. The pneumatic arm that's supposed to hold it up just hangs there useless. Two of my prep cooks already got their fingers pinched and now they're scared to use it.",
			"solution": "Replaced the worn pneumatic lid support cylinder and adjusted the mounting brackets for proper lid operation and safety.",
			"parts": ["SKU-PS-334567 - Pneumatic Lid Support Cylinder 150lb capacity with mounting hardware"],
		},
		{
			"problem": "The exhaust fan on top of our beverage cooler completely died and now the compressor is overheating constantly. The whole unit shuts down every few hours and we have to wait for it to cool off before it starts working again. Our customers are getting warm sodas and complaining like crazy.",
			"solution": "Installed new condenser fan motor and cleaned the condenser coils to restore proper airflow and prevent compressor overheating.",
			"parts": ["SKU-FM-445612 - Condenser Fan Motor 1/6 HP 115V with mounting bracket", "SKU-FB-782134 - Fan Blade 12-inch diameter aluminum with hub"],
		},
		{
			"problem": "Our reach-in cooler keeps tripping the circuit breaker in the middle of lunch rush and shutting down completely. It happened three times yesterday and we lost a whole batch of prepped salads. The electrician said the breaker is fine so it must be something with the cooler itself drawing too much power.",
			"solution": "Replaced the failing compressor start relay and run capacitor which were causing excessive electrical draw and circuit breaker trips.",
			"parts": ["SKU-SR-667890 - Compressor Start Relay 3-in-1 universal type", "SKU-CA-523471 - Run Capacitor 35MFD 370V oval with mounting bracket", "SKU-CA-523472 - Start Capacitor 88-108MFD 125V round"],
		},
		{
			"problem": "The automatic defrost on our display freezer isn't working at all and thick ice is building up on the coils every day. We have to manually turn it off and wait hours for it to melt, which means no frozen desserts during that time. My afternoon customers keep asking where all our ice cream went.",
			"solution": "Replaced the defrost timer and installed new defrost heater elements to restore automatic defrost cycling and prevent ice buildup.",
			"parts": ["SKU-DT-789123 - Defrost Timer 6-hour cycle with manual advance", "SKU-DH-445789 - Defrost Heater Element 500W 120V with mounting clips"],
		},
		{
			"problem": "Our wine cooler temperature keeps bouncing around between 45 and 65 degrees instead of staying at the 55 we set it to. The expensive wines are getting ruined by the temperature swings and my manager is threatening to take it out of my paycheck. The compressor seems to run randomly with no pattern.",
			"solution": "Replaced the malfunctioning thermostatic expansion valve and recharged the refrigerant system to restore stable temperature control and proper cooling cycle.",
			"parts": ["SKU-TX-334455 - Thermostatic Expansion Valve R-134a with sensing bulb", "SKU-RF-889966 - R-134a Refrigerant 15lb cylinder"],
		},
		{
			"problem": "The bottom drain in our prep sink cooler is completely clogged and gross water is backing up into the food storage area. There's a terrible smell coming from it that's making customers wrinkle their noses when they walk by. My health inspector is coming next week and this will definitely fail us.",
			"solution": "Cleared the blocked condensate drain line and replaced the drain heater to prevent future ice blockages and ensure proper drainage.",
			"parts": ["SKU-DH-778899 - Condensate Drain Heater 25W 120V with thermostat"],
		},
		{
			"problem": "Our upright freezer door keeps swinging open by itself even when we make sure to close it tight. The magnetic seal doesn't seem to hold anymore and cold air is pouring out constantly. My frozen food costs are going through the roof because everything keeps thawing out.",
			"solution": "Replaced the worn door gasket and adjusted the door hinges to ensure proper alignment and magnetic seal contact.",
			"parts": ["SKU-GS-556677 - Door Gasket Magnetic Seal 28-inch gray with corner pieces", "SKU-HG-223344 - Door Hinge Set heavy-duty with adjustment screws"],
		},
		{
			"problem": "The interior light in our salad prep cooler flickers constantly and sometimes goes completely dark for hours. My prep cooks are squinting to see what they're doing and making mistakes with portion sizes. The flickering is giving everyone headaches during the long prep shifts.",
			"solution": "Replaced the fluorescent ballast and installed new LED conversion kit to provide stable, energy-efficient lighting.",
			"parts": ["SKU-LK-445566 - LED Conversion Kit 18W 4000K with magnetic mounting", "SKU-BL-778822 - Electronic Ballast T8 fluorescent 32W instant start"],
		},
		{
			"problem": "Our walk-in freezer floor is cracking and buckling up in several spots, making it dangerous to walk on with full sheet pans. One of my bakers already twisted her ankle stepping in a hole yesterday. The floor feels spongy in some areas like the insulation underneath is failing.",
			"solution": "Removed damaged floor panels and replaced the deteriorated foam insulation underneath, then installed new insulated floor panels with proper vapor barrier.",
			"parts": ["SKU-FP-889900 - Insulated Floor Panel 4x8 feet with tongue-and-groove edges", "SKU-IN-334567 - Polyurethane Foam Insulation Board 4-inch thickness", "SKU-VB-556788 - Vapor Barrier Film 6-mil thickness with adhesive backing"],
		},
		{
			"problem": "The temperature control knob on our walk-in cooler is completely dead - we can turn it all we want but nothing changes. We're stuck at whatever temperature it was last set to and can't adjust it for different storage needs. My produce is either freezing or going bad because we can't fine-tune the temp anymore.",
			"solution": "Replaced the faulty electronic thermostat controller and calibrated the temperature settings to proper operating range.",
			"parts": ["SKU-TC-847239 - Digital Thermostat Controller with LCD Display 120V", "SKU-SE-293847 - Temperature Sensor Probe 6-foot cable NTC type"],
		},
		{
			"problem": "Our chest freezer compressor won't start up at all anymore - it just sits there silent while the temperature climbs. We lost a whole shipment of frozen seafood overnight and my boss is furious about the waste. I can hear clicking sounds but the compressor never kicks in.",
			"solution": "Diagnosed and replaced the failed compressor start relay and overload protector which were preventing the compressor from starting.",
			"parts": ["SKU-RL-583921 - Start Relay 3-in-1 Universal Compressor", "SKU-OL-749283 - Overload Protector 1/3 HP Thermal Switch", "SKU-CP-192847 - Start Capacitor 88-108 MFD 330V"],
		},
		{
			"problem": "There's this gross slimy buildup all over the evaporator coils in our salad cooler and it smells terrible. The cooling isn't working right and my lettuce is wilting faster than usual. The smell is starting to get into the food and customers are noticing.",
			"solution": "Deep cleaned the evaporator coils with antimicrobial coil cleaner and replaced the clogged air filter to restore proper airflow and eliminate odors.",
			"parts": ["SKU-AF-647291 - Antimicrobial Air Filter 16x20x1 MERV-8"],
		},
		{
			"problem": "Our display case glass keeps getting covered in condensation and water spots no matter how much we wipe it down. Customers can barely see the desserts inside and it looks really unprofessional. The problem seems worst during busy periods when we're opening it a lot.",
			"solution": "Adjusted the anti-sweat heaters around the glass perimeter and replaced the worn door gaskets to eliminate condensation issues.",
			"parts": ["SKU-AH-938472 - Anti-Sweat Heater Wire 120V 25-watt per foot", "SKU-GS-475829 - Magnetic Door Gasket 78-inch Gray Vinyl", "SKU-DF-283946 - Defrost Heater Element 240V 500W"],
		},
		{
			"problem": "The automatic defrost cycle on our freezer seems to have stopped working completely. We're getting huge ice buildups that block the vents and make it impossible to fit our normal inventory. My staff has to chip ice away every few hours just to make space.",
			"solution": "Replaced the malfunctioning defrost timer and tested the defrost cycle to ensure proper ice removal sequence.",
			"parts": ["SKU-DT-729485 - Defrost Timer 6-hour cycle 120V Mechanical", "SKU-DH-384759 - Defrost Heater 480V 1200W Finned Element"],
		},
		{
			"problem": "Our reach-in cooler fan motor died completely and there's no air circulation at all inside. The back items are staying cold but everything near the door is warming up fast. It's like having a regular cabinet instead of a refrigerator up front.",
			"solution": "Installed new evaporator fan motor and balanced the fan blade assembly to restore proper air circulation throughout the unit.",
			"parts": ["SKU-FM-592847 - Evaporator Fan Motor 1/20 HP 115V CCW", "SKU-FB-847293 - Fan Blade 8-inch Plastic 3-blade CW rotation"],
		},
		{
			"problem": "The condenser fan outside our walk-in isn't spinning anymore and the whole system is running way too hot. You can feel the heat radiating off the condenser unit and our cooling has gotten really sluggish. I'm worried the whole system is going to overheat and shut down during dinner rush.",
			"solution": "Replaced the burned-out condenser fan motor and cleaned the condenser coils to restore proper heat rejection.",
			"parts": ["SKU-CF-473829 - Condenser Fan Motor 1/4 HP 208-230V Single Phase"],
		},
		{
			"problem": "Our ice machine cooler has this weird hissing sound coming from somewhere inside and the cooling seems weaker than normal. The beverages aren't getting as cold as they used to and I can hear this constant whisper of air or gas. My bartender thinks we might be losing refrigerant or something.",
			"solution": "Located and repaired a small refrigerant leak in the evaporator coil, recharged the system with proper refrigerant levels, and replaced the faulty TXV.",
			"parts": ["SKU-TX-638294 - Thermostatic Expansion Valve R-404A 3-ton", "SKU-RF-749283 - R-404A Refrigerant 25-pound cylinder", "SKU-LC-284759 - Leak Lock Sealant Refrigeration Grade"],
		},
		{
			"problem": "The drain pan under our prep cooler is overflowing constantly and creating puddles all around the kitchen equipment. My cooks are slipping on the wet floor and we can't keep up with mopping it. The drain seems completely blocked and water is backing up everywhere.",
			"solution": "Cleared the blocked condensate drain line and installed a new drain pan heater to prevent future ice blockages and ensure proper drainage.",
			"parts": ["SKU-DP-847392 - Drain Pan Heater 120V 200W Silicone Pad", "SKU-DL-593847 - Condensate Drain Line Kit 1/2-inch PVC"],
		},
		{
			"problem": "Our freezer door won't latch properly anymore and keeps swinging open on its own throughout service. The latch mechanism feels loose and doesn't catch like it used to. We're losing tons of cold air and our frozen inventory is at risk during busy periods.",
			"solution": "Adjusted the door hinges and replaced the worn door latch assembly and strike plate to ensure proper door sealing.",
			"parts": ["SKU-DL-748593 - Door Latch Assembly Heavy Duty Magnetic", "SKU-SP-394857 - Strike Plate Adjustable Stainless Steel", "SKU-DH-857394 - Door Hinge Pin and Bushing Kit"],
		},
		{
			"problem": "The defrost cycle on our walk-in freezer isn't working right and there's a thick layer of ice covering everything inside. My staff can barely fit product on the shelves anymore and the door is getting harder to close. We're wasting so much space and it's affecting our food storage capacity during our busy season.",
			"solution": "Replaced the faulty defrost timer that was not initiating defrost cycles and installed a new defrost heater element that had burned out.",
			"parts": ["SKU-DT-445821 - Defrost Timer 120V 8-hour cycle commercial grade", "SKU-HE-778942 - Defrost Heater Element 1500W 240V with mounting brackets"],
		},
		{
			"problem": "Our reach-in cooler's temperature display shows numbers but they don't match what's actually happening inside. Yesterday it said 35 degrees but my thermometer read 50 degrees and all the milk went bad. I can't trust what the digital readout is telling me anymore and my food costs are going crazy.",
			"solution": "Calibrated and replaced the malfunctioning temperature sensor and reprogrammed the digital controller to ensure accurate temperature readings.",
			"parts": ["SKU-TS-336719 - Temperature Sensor Probe 10K Ohm NTC thermistor 6-foot cable", "SKU-TC-892014 - Digital Temperature Controller with LED display and alarm functions"],
		},
		{
			"problem": "There's this gross brown water dripping from underneath our display case and it's staining the floor tiles. The smell is getting pretty bad and customers are starting to notice. My cleaning crew mops it up but it just keeps coming back every few hours.",
			"solution": "Cleaned out the clogged evaporator drain line and replaced the damaged drain pan that had developed cracks causing the overflow.",
			"parts": ["SKU-DP-558731 - Stainless Steel Drain Pan 24x18x3 inches with drain fitting"],
		},
		{
			"problem": "Our beer walk-in has been running constantly for three days straight and I can hear the compressor struggling and getting really hot. The temperature is holding but barely, and I'm terrified it's going to die right before the weekend when we need it most. The whole unit is vibrating more than usual too.",
			"solution": "Replaced the worn compressor start capacitor and cleaned the condenser coils which were restricting airflow and causing the compressor to overwork.",
			"parts": ["SKU-CP-223847 - Start Capacitor 330-396 MFD 250V oval dual terminal", "SKU-CC-445291 - Condenser Coil Cleaning Kit with coil cleaner and brush set"],
		},
		{
			"problem": "The glass doors on our beverage cooler are completely fogged up on the inside and customers can't see any of the drinks we have. It's been like this for two days and I'm sure we're losing sales because people don't know what's available. Wiping the outside doesn't help at all.",
			"solution": "Replaced the failed anti-sweat heater elements in the door frames and repaired the broken door seal that was allowing humid air infiltration.",
			"parts": ["SKU-AS-667134 - Anti-Sweat Door Heater 75W 120V flexible heating element", "SKU-DS-881956 - Magnetic Door Gasket 26x72 inches gray vinyl", "SKU-RL-445782 - Door Seal Retainer Strip aluminum with mounting screws"],
		},
		{
			"problem": "Our sandwich prep table isn't cooling the top compartments at all and the lettuce and tomatoes are getting warm by mid-morning. My sandwich makers are having to run to the walk-in constantly to get fresh ingredients. The bottom seems fine but the top rail where we do most of our prep work is useless.",
			"solution": "Replaced the burned out evaporator fan motor and cleaned the blocked air ducts that distribute cold air to the top rail compartments.",
			"parts": ["SKU-FM-334578 - Evaporator Fan Motor 1/20 HP 115V with mounting bracket and blade"],
		},
		{
			"problem": "There's refrigerant leaking somewhere in our ice cream freezer because I can smell that chemical odor and the unit isn't staying cold enough. The ice cream is getting soft and we've had to throw away probably $200 worth of product this week. I'm worried about the health implications too.",
			"solution": "Located and repaired the refrigerant leak at the thermostatic expansion valve connection, evacuated the system, and recharged with proper refrigerant levels.",
			"parts": ["SKU-TV-778923 - Thermostatic Expansion Valve R-404A 3/8 inch inlet with equalizer line", "SKU-RF-445891 - R-404A Refrigerant 25-pound cylinder commercial grade"],
		},
		{
			"problem": "Our reach-in freezer door won't seal properly anymore and there's a gap along the bottom where you can see light coming through. Frost is building up around the edges and the motor is running way more than it should. My frozen fries are getting freezer burn really quickly.",
			"solution": "Adjusted the door hinges for proper alignment and replaced the worn door gasket that had lost its magnetic seal and flexibility.",
			"parts": ["SKU-DG-556743 - Door Gasket 23x58 inches black magnetic seal with corner welds"],
		},
		{
			"problem": "The compressor on our salad cooler clicks on for about 10 seconds then shuts right back off, over and over again. It's doing this all day long and the temperature keeps climbing. My prep vegetables are wilting and I'm afraid the whole thing is going to burn out from all this cycling.",
			"solution": "Replaced the faulty compressor start relay that was causing short cycling and installed a new overload protector to prevent future compressor damage.",
			"parts": ["SKU-SR-223456 - Compressor Start Relay 3-in-1 universal replacement 120V", "SKU-OP-667289 - Overload Protector 1/3 HP compressor with manual reset button"],
		},
		{
			"problem": "Our walk-in cooler floor is getting squishy and soft in one corner and I think the insulation underneath is getting wet somehow. You can actually feel it give when you step on that spot and I'm worried someone's going to fall through. It's been getting worse each week.",
			"solution": "Removed damaged floor panels and replaced the water-soaked insulation caused by a slow leak in the floor drain assembly, then installed new insulated floor sections.",
			"parts": ["SKU-FP-334821 - Insulated Floor Panel 4x8 feet 4-inch thick polyurethane core", "SKU-DR-778445 - Floor Drain Assembly 3-inch stainless steel with trap and gasket", "SKU-IN-556923 - Polyurethane Foam Insulation Board 2x4 feet 2-inch thickness"],
		},
	],
	"Dishwashers": [
		{
			"problem": "Our dishwasher isn't getting the dishes clean anymore - there's still food stuck on plates and grease on the glasses. The servers keep bringing stuff back from the dining room because it looks dirty. We're having to pre-rinse everything twice now which is slowing us down during rush.",
			"solution": "Replaced clogged spray arms and cleaned mineral deposits from nozzles, then adjusted wash pump pressure to manufacturer specifications.",
			"parts": ["SKU-SP-003421 - Upper Spray Arm Assembly with stainless steel nozzles", "SKU-SP-003422 - Lower Spray Arm Assembly with rotating manifold"],
		},
		{
			"problem": "The dishwasher door keeps popping open in the middle of cycles and water goes everywhere. My dishwashers are constantly mopping the floor and we've had a couple slips already. It's happening like five times a shift now.",
			"solution": "Replaced faulty door latch solenoid and adjusted door alignment mechanism to ensure proper sealing during operation.",
			"parts": ["SKU-SO-008934 - Door Latch Solenoid 24V with mounting bracket", "SKU-DM-005672 - Door Hinge Pin Kit with bushings", "SKU-GS-001245 - Door Gasket Seal 36-inch perimeter"],
		},
		{
			"problem": "The dishes aren't getting sanitized properly - the health inspector said our rinse temperature is way too low. We're worried about failing our next inspection and the staff is freaking out about serving dirty dishes to customers.",
			"solution": "Replaced defective booster heater element and recalibrated thermostat to maintain proper 180\u00b0F sanitizing rinse temperature.",
			"parts": ["SKU-HE-007823 - Booster Heater Element 6kW 240V with terminals"],
		},
		{
			"problem": "There's soap everywhere but the dishes still come out dirty - it's like the machine is dumping all the detergent at once instead of dispensing it properly. We're going through way too much chemical and making a mess. The floor is slippery from all the overflow.",
			"solution": "Replaced malfunctioning chemical dispenser pump and cleaned clogged injection lines to restore proper detergent metering.",
			"parts": ["SKU-CP-004567 - Chemical Dispenser Pump 120V with flow regulator", "SKU-TU-002134 - Chemical Injection Tubing Kit with fittings", "SKU-VL-008901 - Chemical Metering Valve with adjustment screw"],
		},
		{
			"problem": "The dishwasher won't start its cycle anymore - I press all the buttons but nothing happens. My crew is backed up washing everything by hand and we can't keep up with the dinner rush. It was working fine yesterday.",
			"solution": "Replaced failed cycle controller board and tested all input sensors to restore automatic operation sequencing.",
			"parts": ["SKU-CB-009876 - Cycle Controller Board with programming chip", "SKU-SW-003445 - Start Button Switch with LED indicator"],
		},
		{
			"problem": "Water keeps backing up and overflowing from the dishwasher onto the floor. The drain is gurgling and making weird noises, and now there's standing water that smells terrible. We've had to shut it down twice today.",
			"solution": "Replaced blocked drain pump and cleared debris from discharge valve to restore proper water evacuation.",
			"parts": ["SKU-DP-005432 - Drain Pump Motor 1/2 HP with impeller", "SKU-VL-007654 - Drain Discharge Valve 2-inch with spring return"],
		},
		{
			"problem": "The machine takes forever to fill up with water now - it used to start washing right away but now we're waiting like ten minutes just for it to fill. During lunch rush this is killing our turnaround time on clean dishes.",
			"solution": "Replaced faulty water fill valve and cleaned sediment from water level sensor to restore normal fill timing.",
			"parts": ["SKU-WV-002876 - Water Fill Valve 3/4-inch with solenoid actuator", "SKU-WS-004321 - Water Level Sensor with float mechanism", "SKU-FL-001987 - Water Fill Filter Screen stainless steel mesh"],
		},
		{
			"problem": "There's so much steam and humidity coming from the dishwasher that we can barely see in the kitchen. The exhaust fan doesn't seem to be working and everything is getting condensation on it. It's like working in a sauna back there.",
			"solution": "Replaced burned out exhaust fan motor and cleaned blocked ventilation ducts to restore proper steam evacuation.",
			"parts": ["SKU-FM-008765 - Exhaust Fan Motor 1/3 HP with mounting plate"],
		},
		{
			"problem": "The wash water is barely warm and definitely not hot enough to clean properly. I can stick my hand right in it without getting burned. Food grease isn't coming off and we're having to rewash everything multiple times.",
			"solution": "Replaced defective tank heater thermostat and heating element to restore proper 150\u00b0F wash water temperature.",
			"parts": ["SKU-TS-006543 - Tank Thermostat 150\u00b0F with capillary tube", "SKU-HE-003298 - Tank Heating Element 4.5kW immersion type"],
		},
		{
			"problem": "The dishwasher is making this awful grinding noise every time it runs - sounds like metal scraping against metal. It's so loud we can barely hear each other talk in the kitchen, and I'm worried it's going to break completely during our busy weekend. The noise just started yesterday but it's getting worse with each load.",
			"solution": "Replaced the worn wash pump motor bearings and impeller assembly that had become damaged from debris buildup.",
			"parts": ["SKU-MT-428167 - Wash Pump Motor Assembly 3HP 230V with stainless steel impeller", "SKU-BR-103945 - Motor Bearing Kit with seals for dishwasher pump"],
		},
		{
			"problem": "The spray arms aren't spinning anymore - I can see them just sitting there while water trickles out weakly. Dishes on the bottom rack still have food stuck all over them because nothing's getting blasted off. We've tried cleaning the holes but it didn't help at all.",
			"solution": "Rebuilt the spray arm assembly and cleared the blocked internal water channels, then replaced the damaged bearing mechanism.",
			"parts": ["SKU-SA-592847 - Lower Spray Arm Assembly with bearing housing and nozzles"],
		},
		{
			"problem": "The rinse aid dispenser is acting crazy - sometimes no rinse aid comes out and the dishes have water spots everywhere, other times it dumps way too much and leaves a soapy film. The customers are complaining about the taste on their glasses and we look unprofessional. It's been inconsistent for about two weeks now.",
			"solution": "Replaced the malfunctioning rinse aid dispenser pump and recalibrated the chemical feed system to proper concentration levels.",
			"parts": ["SKU-CD-367291 - Rinse Aid Dispenser Pump Assembly with flow control valve", "SKU-SN-081564 - Chemical Feed Sensor and calibration kit", "SKU-VL-749823 - Dispenser Check Valve 1/4-inch barbed fitting"],
		},
		{
			"problem": "The dishwasher keeps stopping mid-cycle and flashing some error code we don't understand. Sometimes it works fine for a few loads, then just quits randomly. My staff doesn't know when it's actually done so dishes are sitting in there getting cold and we're falling behind.",
			"solution": "Replaced the faulty cycle control board and updated the programming to correct the sensor communication errors.",
			"parts": ["SKU-CB-156489 - Digital Control Board Assembly with display and programming chip"],
		},
		{
			"problem": "The booster heater isn't working right - the water coming out for the final rinse is way cooler than it should be. We're not hitting sanitizing temperature and I'm scared the health department will shut us down. The temperature gauge shows it's trying but just can't get hot enough.",
			"solution": "Replaced the burned-out heating elements in the booster heater and installed a new high-limit thermostat for safety.",
			"parts": ["SKU-HE-834576 - Booster Heater Element 18kW 240V stainless steel", "SKU-TH-291047 - High-Limit Safety Thermostat 180\u00b0F manual reset"],
		},
		{
			"problem": "There's chemical residue building up all over the inside of the machine - white crusty stuff on the walls and racks. The dishes come out with spots and sometimes a weird smell. I think something's wrong with how the chemicals are mixing but I don't know what to do about it.",
			"solution": "Descaled the entire system and replaced the clogged detergent injector nozzles that were causing improper chemical dilution.",
			"parts": ["SKU-NZ-647183 - Detergent Injector Nozzle Set with flow restrictors", "SKU-CL-395728 - Descaling Chemical Kit for commercial dishwasher maintenance"],
		},
		{
			"problem": "The machine won't drain properly after washing - there's always dirty water sitting in the bottom that smells awful. When we try to run the next load, that nasty water gets pumped around with the clean wash water. It's disgusting and unsanitary.",
			"solution": "Replaced the failed drain pump motor and cleared the blocked drain valve that was preventing proper water evacuation.",
			"parts": ["SKU-DP-728394 - Drain Pump Motor 1/2HP with impeller and housing", "SKU-VL-452861 - Drain Valve Assembly 2-inch with actuator solenoid", "SKU-GS-168527 - Pump Gasket and Seal Kit"],
		},
		{
			"problem": "The door won't stay closed during the wash cycle - it pops open randomly and stops everything. We've tried slamming it harder but that doesn't work. Now we have to stand there and hold it shut which is ridiculous when we're trying to get ready for dinner service.",
			"solution": "Replaced the worn door latch mechanism and adjusted the strike plate alignment to ensure proper door sealing.",
			"parts": ["SKU-DL-516739 - Door Latch Assembly with strike plate and springs"],
		},
		{
			"problem": "The tank water is staying cold even though the machine has been running for hours. I can feel that it's barely lukewarm when I open it up. Without hot wash water, the grease isn't coming off the plates and pans at all. We're basically just rinsing things with cold water.",
			"solution": "Replaced the defective tank heating elements and installed a new thermostat control to maintain proper wash water temperature.",
			"parts": ["SKU-HE-673942 - Tank Heater Element 12kW 208V with mounting flange", "SKU-TC-287163 - Temperature Controller with digital readout and probe"],
		},
		{
			"problem": "The dishwasher is cycling way too fast - it finishes a full wash in like two minutes when it used to take eight or ten. The dishes come out still dirty with soap suds all over them because it's not giving enough time for each step. My dishwashers are having to run everything through twice which defeats the whole purpose of having an automatic machine.",
			"solution": "Replaced faulty cycle timer control board that was advancing through wash sequences too rapidly, restored proper timing intervals for each cycle phase.",
			"parts": ["SKU-CT-004521 - Digital cycle timer control board with 8-program memory"],
		},
		{
			"problem": "The water pressure in our dishwasher is pathetic - it's like a gentle shower instead of the powerful spray it used to have. Plates with dried cheese or sauce aren't getting clean at all. I opened it up during a cycle and barely any water is coming out of the spray holes.",
			"solution": "Rebuilt wash pump motor and replaced clogged internal filter screen, restoring full water pressure and spray force throughout the system.",
			"parts": ["SKU-WP-007892 - Wash pump motor 1.5HP 3-phase with mounting bracket", "SKU-FS-003417 - Stainless steel mesh filter screen 20-mesh"],
		},
		{
			"problem": "Our conveyor dishwasher belt keeps jamming and stopping in the middle - dishes pile up at the entrance and we can't load anything new. The motor makes a struggling sound like it's trying to move but can't. We've had to pull dishes out by hand and it's backing up our whole dish pit operation.",
			"solution": "Replaced worn drive chain and lubricated conveyor guide rails that were causing excessive friction and motor strain.",
			"parts": ["SKU-DC-009156 - Stainless steel drive chain 48-link with master connector", "SKU-LB-002834 - Food-grade conveyor rail lubricant 16oz bottle", "SKU-GR-005672 - Conveyor guide rail set left and right with mounting hardware"],
		},
		{
			"problem": "The detergent isn't getting mixed properly - sometimes the water is crystal clear with no soap at all, other times it's so thick with detergent you can't see through it. The dishes either don't get clean or come out with a slimy residue that customers definitely notice. It's been totally unpredictable for the past month.",
			"solution": "Replaced malfunctioning chemical metering pump and recalibrated detergent injection system to maintain consistent concentrate ratios.",
			"parts": ["SKU-MP-008743 - Peristaltic metering pump 0.5GPH with digital display"],
		},
		{
			"problem": "The upper spray arm fell off during service and crashed into the dishes below, breaking three plates and a coffee mug. Now I can see that the mounting is completely stripped out and loose. We can't run the machine because dishes on the top rack don't get hit with any water at all.",
			"solution": "Installed new upper spray arm assembly with reinforced mounting hub and replaced stripped mounting threads in the wash chamber ceiling.",
			"parts": ["SKU-SA-006291 - Upper spray arm assembly with reinforced hub 24-inch diameter", "SKU-MH-004185 - Threaded mounting hub insert with lock washer"],
		},
		{
			"problem": "The machine fills up with water but then just sits there forever without starting the wash cycle. All the lights are on and it seems ready to go, but the pump never kicks in. We've been waiting twenty minutes sometimes before giving up and restarting the whole thing. It's killing our productivity during breakfast prep.",
			"solution": "Replaced defective water level sensor that wasn't sending the proper fill signal to the control system, allowing normal cycle initiation.",
			"parts": ["SKU-WS-007435 - Ultrasonic water level sensor with mounting bracket and 10ft cable"],
		},
		{
			"problem": "There's a horrible burning smell coming from the dishwasher and the tank water is way too hot - like scalding hot when it should just be warm. I'm worried it's going to hurt someone or damage the dishes. The smell is so bad we can taste it in the air and customers in the dining room are asking about it.",
			"solution": "Replaced overheating tank thermostat that was stuck in the ON position and installed new high-temperature safety cutoff switch.",
			"parts": ["SKU-TH-003926 - Tank water thermostat 140-180\u00b0F range with capillary bulb", "SKU-SC-001758 - High-temp safety cutoff switch 200\u00b0F automatic reset"],
		},
		{
			"problem": "The final rinse water has no pressure at all - it's just dripping out instead of spraying. The dishes come out with spots and film because they're not getting properly rinsed. I can see the rinse arms trying to move but there's barely any water coming through them.",
			"solution": "Rebuilt rinse booster pump and replaced clogged rinse aid injection nozzles that were restricting water flow in the final rinse system.",
			"parts": ["SKU-RB-009847 - Rinse booster pump 0.75HP single phase", "SKU-RN-005123 - Rinse injection nozzle set of 6 with O-rings", "SKU-GA-002641 - Pump rebuild gasket kit with seals and impeller"],
		},
		{
			"problem": "The door handle broke off completely in my dishwasher's hand during dinner rush. Now we can't open or close the door properly and have to use pliers to grab the metal stub. It's dangerous and we're losing time on every single load trying to wrestle with this thing.",
			"solution": "Replaced broken door handle assembly and reinforced door hinge mounting points that had become loose from repeated stress.",
			"parts": ["SKU-DH-004792 - Door handle assembly stainless steel with spring mechanism", "SKU-HP-007358 - Door hinge pin set with bushings and retaining clips"],
		},
		{
			"problem": "The machine is using way too much water - it keeps filling and filling like it doesn't know when to stop. Our water bill is going through the roof and there's constantly water overflowing onto the floor. Sometimes it fills for ten minutes straight before we manually shut it off.",
			"solution": "Replaced faulty water fill solenoid valve that was sticking open and adjusted float switch mechanism to ensure proper fill level detection.",
			"parts": ["SKU-SV-008164 - Water fill solenoid valve 3/4-inch NPT with coil", "SKU-FL-003549 - Float switch assembly with adjustable arm and microswitch"],
		},
		{
			"problem": "The dishwasher keeps making this horrible screeching noise when it tries to drain - like nails on a chalkboard. It happens every time we finish a load and the water won't go down properly. My dishwashers are covering their ears and we're worried something is going to burn out completely.",
			"solution": "Replaced the seized drain pump motor and cleared debris from the impeller housing that was causing the grinding noise and poor drainage.",
			"parts": ["SKU-DP-247891 - Drain Pump Motor 1/3 HP 115V with mounting bracket", "SKU-IM-156734 - Impeller Assembly stainless steel 4-inch diameter"],
		},
		{
			"problem": "Our dishwasher won't heat up the wash water at all anymore - it's ice cold even after running for an hour. The grease just sits on everything and nothing gets clean. We tried waiting longer but it never gets warm and we're falling way behind on dishes.",
			"solution": "Replaced the faulty tank heating element and installed a new thermostat that was stuck in the open position.",
			"parts": ["SKU-HE-382945 - Immersion Heating Element 4500W 240V with gasket seal", "SKU-TH-091567 - Tank Thermostat 180\u00b0F high limit with capillary tube"],
		},
		{
			"problem": "The detergent dispenser is completely broken - no soap comes out at all during the wash cycle. We've tried refilling it and checking the lines but nothing works. Dishes come out greasy and gross because there's no detergent being used.",
			"solution": "Rebuilt the detergent dispenser pump mechanism and replaced the clogged injection nozzle in the wash tank.",
			"parts": ["SKU-CD-724538 - Chemical Dispenser Pump 24V with tubing kit"],
		},
		{
			"problem": "The conveyor belt in our dish machine stopped moving completely in the middle of lunch rush. Dishes are just sitting there getting sprayed in the same spot while we manually push racks through. The motor is running but the belt won't budge and we're totally backed up.",
			"solution": "Replaced the stripped conveyor drive gear and adjusted the belt tension mechanism that had loosened over time.",
			"parts": ["SKU-CG-459823 - Conveyor Drive Gear assembly hardened steel with keyway", "SKU-CB-678291 - Conveyor Belt food-grade PVC 18-inch width", "SKU-BT-334756 - Belt Tension Adjuster spring-loaded with mounting hardware"],
		},
		{
			"problem": "Every time we open the dishwasher door, scalding hot steam shoots out and almost burned one of my cooks yesterday. There's way too much pressure building up inside and it's dangerous. The exhaust system doesn't seem to be pulling the steam out like it should.",
			"solution": "Replaced the malfunctioning exhaust fan motor and cleaned out the blocked ventilation ductwork to restore proper airflow.",
			"parts": ["SKU-EF-892134 - Exhaust Fan Motor 1/2 HP 1725 RPM with mounting plate", "SKU-VD-445627 - Ventilation Damper assembly 12-inch diameter with actuator"],
		},
		{
			"problem": "The final rinse cycle isn't working at all - dishes come out with soap film and spots everywhere. I can tell it's skipping that step because there's no hot water spray at the end. Customers are complaining about the taste and appearance of their glasses.",
			"solution": "Replaced the defective rinse cycle solenoid valve and recalibrated the cycle timer to ensure proper rinse activation.",
			"parts": ["SKU-SV-671482 - Solenoid Valve 3/4-inch NPT 120V AC with manual override"],
		},
		{
			"problem": "The wash arms are completely clogged up - I can see buildup in all the little holes and barely any water comes out. We've tried poking them clean with toothpicks but there's too much mineral buildup. Nothing on the bottom rack gets clean anymore.",
			"solution": "Removed and descaled all spray arms, then replaced the severely corroded upper wash arm that couldn't be salvaged.",
			"parts": ["SKU-WA-558439 - Upper Wash Arm stainless steel with 42 spray holes", "SKU-WB-223781 - Wash Arm Bearing assembly with O-ring seal"],
		},
		{
			"problem": "Our undercounter dishwasher keeps flooding the prep area because water shoots out from underneath during cycles. There's a puddle every time we run it and it's creating a slip hazard. I think there's a leak somewhere but can't tell where it's coming from.",
			"solution": "Replaced the cracked door seal gasket and tightened loose water line connections at the pump assembly.",
			"parts": ["SKU-DS-334912 - Door Seal Gasket silicone rubber full perimeter", "SKU-WL-778623 - Water Line Connector Kit stainless steel with clamps"],
		},
		{
			"problem": "The temperature gauge shows the booster heater is working but our rinse water is still not hot enough for sanitizing. The health inspector is coming next week and we're panicking about failing inspection. Steam comes out but it's not actually getting to 180 degrees like it should.",
			"solution": "Replaced the faulty temperature sensor and installed a new booster heater element that had burned out internally.",
			"parts": ["SKU-TS-445829 - Temperature Sensor probe RTD with 6-foot cable", "SKU-BH-667134 - Booster Heater Element 9KW 240V triple-pass design"],
		},
		{
			"problem": "The control panel is going crazy - lights are flashing randomly and it starts cycles on its own without anyone pressing buttons. Sometimes it works normally for a few hours then acts up again. My staff doesn't trust it and we're afraid it'll break down completely.",
			"solution": "Replaced the malfunctioning control board and updated the cycle timer module that had water damage from steam exposure.",
			"parts": ["SKU-CB-291847 - Control Board PCB assembly with diagnostic LEDs", "SKU-CT-523691 - Cycle Timer Module programmable 8-cycle with display"],
		},
		{
			"problem": "Our dishwasher is leaking water all over the floor from somewhere underneath - there's a constant puddle forming and we're going through towels like crazy trying to keep it dry. The leak seems to be getting worse and now it's dripping into the storage area below. My staff is complaining about slipping hazards and we can't figure out where it's coming from.",
			"solution": "Replaced failed drain valve gasket and tightened loose water supply connections under the unit.",
			"parts": ["SKU-GK-002847 - Drain Valve Gasket Kit NBR rubber with stainless clamps", "SKU-FT-001923 - Water Supply Fitting 3/4-inch NPT brass compression"],
		},
		{
			"problem": "The dishwasher sounds like a jet engine when it's running - the noise is so loud we can't have conversations in the kitchen anymore. Customers in the dining room are complaining about the racket coming from back here. It started making this noise about a week ago and keeps getting louder.",
			"solution": "Replaced worn wash pump motor bearings and impeller assembly that were causing excessive vibration and noise.",
			"parts": ["SKU-MT-004561 - Wash Pump Motor 2HP 3-phase with thermal protection", "SKU-IM-003789 - Impeller Assembly stainless steel with wear ring", "SKU-BR-001234 - Motor Bearing Set sealed ball bearings"],
		},
		{
			"problem": "The dishes come out with this weird white film all over them that doesn't wipe off easily - glasses look cloudy and plates feel gritty. Customers have sent back drinks because the glasses look dirty even though they just came out of the dishwasher. We've tried running extra rinse cycles but it's not helping.",
			"solution": "Calibrated chemical dispenser system and replaced malfunctioning rinse aid injection pump.",
			"parts": ["SKU-CD-005672 - Chemical Dispenser Pump 24V with flow sensor"],
		},
		{
			"problem": "The conveyor belt in our dishwasher keeps jamming and stopping - dishes pile up and we have to manually push them through. Sometimes it jerks forward suddenly and breaks plates or glasses. My dishwashers are afraid to load it normally because they don't know when it's going to stop working. We're losing money on broken dishes every day.",
			"solution": "Replaced worn conveyor drive motor and realigned belt tracking system with new tension rollers.",
			"parts": ["SKU-CM-007834 - Conveyor Drive Motor 1HP variable speed", "SKU-TR-002156 - Tension Roller Assembly with adjustable brackets", "SKU-CB-004923 - Conveyor Belt food-grade rubber 18-inch width"],
		},
		{
			"problem": "Our undercounter dishwasher gets so hot that nobody can work near it - the whole area becomes unbearable and we're going through ice just to cool down the kitchen. The outside of the machine is burning hot to touch and I'm worried someone's going to get hurt. It never used to heat up the room this much.",
			"solution": "Replaced faulty thermostat and installed new exhaust blower motor to improve heat ventilation.",
			"parts": ["SKU-TH-003421 - Digital Thermostat 150-200\u00b0F with probe", "SKU-BL-006789 - Exhaust Blower Motor 1/3HP with housing"],
		},
		{
			"problem": "The wash arms keep getting clogged with food particles even though we scrape the plates - every few hours we have to stop and clean out the holes by hand with a toothpick. It's slowing down our whole operation and the arms don't seem to have enough pressure anymore. Some of the holes look damaged from all the cleaning.",
			"solution": "Installed upgraded wash arm assembly with larger debris-resistant nozzles and improved filtering system.",
			"parts": ["SKU-WA-008756 - Upper Wash Arm stainless steel with anti-clog nozzles", "SKU-WA-008757 - Lower Wash Arm reinforced with removable nozzles", "SKU-FL-001567 - Pre-filter Screen mesh stainless steel"],
		},
		{
			"problem": "The timer on our dishwasher seems totally random - sometimes cycles run for twenty minutes, sometimes they finish in three minutes with dishes still covered in soap. We never know how long to wait and keep opening the door to check, which stops the whole process. My staff is getting frustrated because they can't plan around it.",
			"solution": "Replaced faulty electronic cycle controller and recalibrated all timing sequences to manufacturer specifications.",
			"parts": ["SKU-CC-009123 - Electronic Cycle Controller programmable with display"],
		},
		{
			"problem": "There's this terrible chemical smell coming from the dishwasher that makes everyone's eyes water - it's like bleach mixed with something else that burns your nose. We're worried about breathing it in all day and customers are asking what that smell is. The dishes smell weird too even after they're dry.",
			"solution": "Replaced cracked chemical mixing chamber and recalibrated detergent concentration levels to eliminate over-dosing.",
			"parts": ["SKU-MC-007234 - Chemical Mixing Chamber polypropylene with seals", "SKU-DS-004891 - Detergent Sensor electronic concentration monitor", "SKU-SL-002345 - Seal Kit chemical-resistant for mixing system"],
		},
		{
			"problem": "The dishwasher keeps overheating and shutting itself down every couple hours - there's some kind of safety thing kicking in. We'll be in the middle of a busy lunch rush and suddenly it just stops working. My kitchen staff is panicking because we have no clean plates and the machine won't restart for like an hour.",
			"solution": "Replaced faulty high-limit thermostat that was triggering premature shutdowns and cleaned mineral buildup from temperature sensor probe.",
			"parts": ["SKU-TH-428561 - High-limit safety thermostat 180\u00b0F with automatic reset", "SKU-TS-193847 - Temperature sensor probe 6-inch stainless steel with 3/8-inch NPT thread"],
		},
		{
			"problem": "The conveyor belt in our dishwasher is moving way too slow - dishes are taking forever to go through and we're getting a huge backup. What used to take three minutes is now taking like eight or nine minutes per rack. During dinner service we can't keep up with the dirty dishes piling up.",
			"solution": "Replaced worn conveyor drive motor and adjusted belt tension to restore proper cycle timing.",
			"parts": ["SKU-MT-675239 - Conveyor drive motor 1/2 HP 115V with mounting bracket"],
		},
		{
			"problem": "Our dishwasher is making this horrible screeching sound every time the wash pump kicks on - it's so loud customers in the dining room are complaining. The noise just started last week but it's getting worse every day. I'm afraid the whole thing is going to seize up and leave us with no way to wash dishes.",
			"solution": "Replaced wash pump with seized bearings and installed new impeller assembly to eliminate noise and restore proper water circulation.",
			"parts": ["SKU-WP-847392 - Wash pump assembly 2 HP with stainless steel housing", "SKU-IM-562174 - Pump impeller with shaft seal kit", "SKU-BG-391847 - Pump bearing set with grease fittings"],
		},
		{
			"problem": "The prewash section isn't working at all - no water comes out when dishes first enter the machine. Everything goes straight to the main wash with all the food scraps still stuck on, so nothing comes out clean. My dishwashers are having to scrape every single plate by hand before loading it.",
			"solution": "Rebuilt prewash pump and replaced clogged manifold to restore proper prewash spray pressure.",
			"parts": ["SKU-PW-729583 - Prewash pump rebuild kit with seals and gaskets", "SKU-MF-481629 - Prewash manifold assembly with integrated spray nozzles"],
		},
		{
			"problem": "The chemical pumps are going crazy - sometimes no detergent comes out at all, other times it dumps way too much and we get foam everywhere. The inconsistency is driving my staff nuts because they never know if the dishes will actually get clean. We're wasting so much soap when it overdoses.",
			"solution": "Calibrated chemical feed pumps and replaced worn peristaltic pump tubes to ensure consistent detergent dispensing.",
			"parts": ["SKU-CP-356218 - Detergent feed pump with variable speed controller", "SKU-PT-194576 - Peristaltic pump tubing set for detergent and rinse aid"],
		},
		{
			"problem": "Water is leaking out from under the machine and pooling on the floor - there's a steady drip that's getting worse every day. The floor is always wet and slippery now, and I'm worried someone's going to get hurt. Plus all that water is probably damaging the floor underneath.",
			"solution": "Replaced cracked wash tank drain valve and tightened all pipe connections to eliminate water leakage.",
			"parts": ["SKU-DV-627439 - Tank drain valve 2-inch with stainless steel body and EPDM seal"],
		},
		{
			"problem": "The final rinse isn't working right - I can tell because all our glasses have terrible water spots and the silverware looks cloudy. Customers are complaining that everything looks dirty even though it just came out of the dishwasher. The rinse aid dispenser seems empty but we just filled it yesterday.",
			"solution": "Replaced malfunctioning rinse aid dispenser pump and adjusted flow rate settings to ensure proper spot-free rinsing.",
			"parts": ["SKU-RA-583647 - Rinse aid dispenser pump with adjustable flow control", "SKU-FS-294831 - Flow sensor for rinse aid system with digital readout"],
		},
		{
			"problem": "The racks keep jamming up on the conveyor track - they'll move halfway through and then just stop, backing up the whole system. My dishwashers have to manually push them through which is dangerous with all the hot water and steam. It happens multiple times every shift now.",
			"solution": "Replaced worn conveyor track guides and lubricated all roller bearings to ensure smooth rack movement through the machine.",
			"parts": ["SKU-TG-738429 - Conveyor track guide set with stainless steel rollers", "SKU-LB-452816 - Food-grade bearing lubricant for high-temperature applications"],
		},
		{
			"problem": "The dishwasher control panel is acting up - sometimes the buttons don't respond when you press them, other times it starts random cycles we didn't select. Yesterday it got stuck on prewash for twenty minutes straight. My staff doesn't trust it anymore and we're losing efficiency trying to figure out what it's actually doing.",
			"solution": "Replaced faulty control board and recalibrated all cycle timing parameters to restore reliable operation.",
			"parts": ["SKU-CB-819357 - Main control board with LCD display and cycle programming", "SKU-KB-674283 - Control panel overlay with waterproof membrane switches"],
		},
		{
			"problem": "There's not enough water pressure coming into the machine - it takes forever to fill up and when it finally does start washing, the spray is really weak. I can see dirty dishes coming out that obviously didn't get hit with enough water force. The whole cycle seems sluggish and ineffective.",
			"solution": "Replaced clogged water inlet valve and installed new pressure regulator to ensure adequate water flow and pressure throughout all wash cycles.",
			"parts": ["SKU-IV-495627 - Water inlet valve 3/4-inch with solenoid actuator", "SKU-PR-382914 - Water pressure regulator with gauge 25-80 PSI range", "SKU-SF-628193 - Inlet water strainer with backwash capability"],
		},
	],
	"Griddles": [
		{
			"problem": "Our griddle isn't heating up evenly anymore - the left side barely gets warm while the right side gets scorching hot. My cooks keep having to shuffle food around constantly just to get everything cooked properly. We're wasting so much time and burning through way more gas than usual.",
			"solution": "Replaced faulty gas control valve and cleaned blocked burner orifices to restore even heat distribution across the griddle surface.",
			"parts": ["SKU-GV-248751 - Gas Control Valve 3/4-inch NPT with pressure regulator", "SKU-BO-139264 - Burner Orifice Set #54 drill size for natural gas"],
		},
		{
			"problem": "The griddle won't stay lit - it keeps going out every few minutes and we have to keep relighting it. My staff is getting frustrated because they'll start cooking something and then lose the flame halfway through. It's been happening more and more frequently this week.",
			"solution": "Replaced worn thermocouple that was failing to maintain proper flame sensing signal to the gas valve.",
			"parts": ["SKU-TC-001834 - Thermocouple Type K 18-inch with 1/4-inch NPT fitting"],
		},
		{
			"problem": "The temperature control knob isn't working right - I turn it to medium but the griddle either stays cold or gets way too hot. There's no in-between anymore and my cooks can't control the heat properly. We've had to throw out burnt food twice today because of this.",
			"solution": "Replaced faulty thermostat assembly and recalibrated temperature control system to restore accurate heat regulation.",
			"parts": ["SKU-TH-457821 - Griddle Thermostat 200-450\u00b0F range with capillary bulb", "SKU-CK-092156 - Control Knob Assembly with temperature markings"],
		},
		{
			"problem": "Grease is overflowing everywhere from the griddle and making a huge mess on the floor. The grease tray seems full but even after we empty it, grease still spills out the sides. It's creating a safety hazard and my cleaning crew is spending forever mopping up the mess.",
			"solution": "Replaced cracked grease trough and installed new grease management channel system to properly direct waste away from cooking surface.",
			"parts": ["SKU-GT-367489 - Stainless Steel Grease Trough 36-inch with drain fitting", "SKU-GC-184752 - Grease Channel Kit with mounting brackets", "SKU-GD-295013 - Grease Drawer Assembly with removable liner"],
		},
		{
			"problem": "The griddle surface is all warped and uneven now - oil pools in certain spots and food slides to one side when we're trying to cook. My pancakes come out lopsided and eggs run all over the place. It's making breakfast service a nightmare.",
			"solution": "Replaced warped griddle plate and adjusted mounting hardware to ensure level cooking surface throughout.",
			"parts": ["SKU-GP-521847 - Chrome Griddle Plate 36x24 inch 1/2-inch thick", "SKU-ML-063291 - Griddle Mounting Hardware Kit with leveling bolts"],
		},
		{
			"problem": "The pilot light won't stay on anymore - it lights up when I hold the button but goes out as soon as I let go. We can't use the griddle at all right now because there's no way to keep the flame going. This is costing us money every minute it's down.",
			"solution": "Replaced faulty pilot assembly and cleaned pilot orifice to restore reliable pilot flame operation.",
			"parts": ["SKU-PA-418963 - Pilot Light Assembly with thermocouple and orifice"],
		},
		{
			"problem": "There's a strong gas smell coming from behind the griddle and it's getting worse. My staff is worried about safety and honestly so am I - we can smell it even when the griddle is off. I had to move my prep station because the smell is so strong back there.",
			"solution": "Replaced leaking gas manifold and tightened all gas line connections to eliminate dangerous gas leak.",
			"parts": ["SKU-GM-735124 - Gas Manifold Assembly 4-burner with safety shutoff", "SKU-GF-281457 - Gas Line Fitting Kit with thread sealant"],
		},
		{
			"problem": "The electronic ignition system isn't working - I press the ignition button and sometimes it sparks, sometimes it doesn't. My cooks have been using matches to light it which I know isn't safe. We need this fixed before someone gets hurt.",
			"solution": "Replaced faulty ignition module and spark electrode to restore reliable electronic ignition system.",
			"parts": ["SKU-IG-594162 - Electronic Ignition Module 120V with spark generator", "SKU-SE-167439 - Spark Electrode Assembly with ceramic insulator"],
		},
		{
			"problem": "The backsplash behind the griddle is loose and grease is getting behind it, creating a gross buildup that we can't clean. It's starting to smell bad and I'm worried about health department violations. The whole thing seems to be pulling away from the wall.",
			"solution": "Reinstalled backsplash with new mounting hardware and sealed gaps to prevent grease infiltration behind cooking equipment.",
			"parts": ["SKU-BS-823671 - Stainless Steel Backsplash 36-inch with mounting brackets", "SKU-SS-429138 - Food-Grade Silicone Sealant Kit for kitchen applications"],
		},
		{
			"problem": "The griddle plate has these weird black spots and scratches all over it that won't come off no matter how hard we scrub. Food sticks to those spots constantly and we're getting burnt bits mixed into everything we cook. My breakfast cook says it's impossible to make decent hash browns anymore because they just stick and tear apart.",
			"solution": "Replaced the damaged chrome griddle plate with a new unit and reseasoned the surface according to manufacturer specifications.",
			"parts": ["SKU-GP-087453 - Chrome Griddle Plate 36-inch x 24-inch with beveled edges"],
		},
		{
			"problem": "The griddle just randomly shuts off in the middle of service - no warning, just dead. Sometimes it happens twice in an hour, sometimes we're fine for a whole day. When it shuts off, we lose whatever we're cooking and have to start over. My staff never knows if they can count on it working.",
			"solution": "Replaced the faulty safety thermocouple that was intermittently triggering the automatic shutoff valve due to poor connection.",
			"parts": ["SKU-TC-124687 - Safety Thermocouple 24-inch with quick-disconnect fitting", "SKU-CV-089123 - Gas Control Valve with automatic shutoff mechanism"],
		},
		{
			"problem": "The whole griddle is tilted - oil and grease run to one corner and pool there instead of draining properly. Everything we cook slides to that side and we can't get even cooking anymore. It looks like one of the legs is shorter or something shifted underneath.",
			"solution": "Adjusted and replaced the adjustable leveling feet and realigned the griddle frame to achieve proper surface level.",
			"parts": ["SKU-LF-156742 - Adjustable Leveling Foot Set heavy-duty stainless steel", "SKU-MH-203891 - Mounting Hardware Kit with brackets and bolts", "SKU-SH-087234 - Support Shim Set various thicknesses"],
		},
		{
			"problem": "The gas burners under the griddle make this loud popping noise and the flames look all yellow and uneven instead of blue. The griddle takes forever to heat up now and doesn't get nearly as hot as it used to. My cooks are complaining about how long it takes to cook anything.",
			"solution": "Cleaned and replaced the clogged burner orifices and adjusted the air-to-gas mixture to restore proper blue flame combustion.",
			"parts": ["SKU-BO-194567 - Burner Orifice Set natural gas 0.025-inch diameter", "SKU-BM-087651 - Burner Manifold Assembly with pressure regulator"],
		},
		{
			"problem": "The control knobs are completely loose - they spin around without doing anything and I can't tell what temperature setting we're on. Sometimes turning them actually makes the heat go down when it should go up. We're basically guessing at temperatures all day long.",
			"solution": "Replaced the worn control valve stems and recalibrated the thermostat linkages to restore proper temperature control operation.",
			"parts": ["SKU-VS-234178 - Control Valve Stem Kit with spring assembly", "SKU-CK-156892 - Control Knob Set with temperature markings"],
		},
		{
			"problem": "There's this horrible burnt smell coming from inside the griddle cabinet and we can see smoke coming out the vents. It smells like electrical burning and I'm scared something's going to catch fire. We had to shut it down because the smell was getting into the food.",
			"solution": "Replaced the overheated electrical heating element that had developed internal shorts and cleaned out accumulated grease deposits from the cabinet.",
			"parts": ["SKU-HE-298734 - Electric Heating Element 240V 5000W with ceramic insulation"],
		},
		{
			"problem": "The grease channels along the edges are all cracked and split, so grease drips down onto the floor instead of going to the trap. We're constantly slipping on grease spots and it's making the whole kitchen dangerous. The health inspector is going to have a field day if they see this mess.",
			"solution": "Replaced the damaged grease collection channels and installed new gaskets to ensure proper drainage to the grease management system.",
			"parts": ["SKU-GC-087234 - Grease Channel Assembly stainless steel with drain spouts", "SKU-GT-156789 - Grease Trap Replacement with removable basket", "SKU-GS-234567 - Gasket Set for grease management system"],
		},
		{
			"problem": "The temperature gauge is stuck on 200 degrees even when the griddle is obviously way hotter than that. My cooks keep burning food because they think it's cooler than it really is. We've been having to guess temperatures all week and wasting a lot of product.",
			"solution": "Replaced the faulty temperature sensor and recalibrated the digital temperature display to provide accurate readings.",
			"parts": ["SKU-TS-145623 - Temperature Sensor RTD probe with 6-foot cable", "SKU-TD-298741 - Digital Temperature Display with LED readout"],
		},
		{
			"problem": "The griddle surface is getting these weird pits and rough spots that catch food and won't let go. Everything sticks now - bacon tears apart when we try to flip it and pancakes leave chunks behind. My morning crew is getting so frustrated because they can't get a clean flip on anything anymore.",
			"solution": "Resurfaced the chrome griddle plate using professional grinding equipment and applied new seasoning coating to restore smooth cooking surface.",
			"parts": ["SKU-GP-002847 - Chrome Griddle Plate 36-inch x 24-inch with beveled edges", "SKU-CS-001293 - Food-grade Seasoning Compound 32oz container"],
		},
		{
			"problem": "The griddle makes this awful screeching noise whenever we adjust the temperature - sounds like metal grinding on metal. It's so loud that customers can hear it from the dining room and my staff jumps every time. The noise started about two weeks ago and keeps getting worse.",
			"solution": "Replaced worn control valve stems and lubricated all moving parts in the gas control assembly.",
			"parts": ["SKU-CV-004621 - Gas Control Valve Stem Assembly with O-rings", "SKU-LB-000892 - High-temperature Valve Lubricant 4oz tube", "SKU-OR-001547 - Control Valve O-ring Kit 15-piece set"],
		},
		{
			"problem": "Our griddle won't shut off completely anymore - even when I turn all the knobs to off, one section stays warm and keeps cooking. We found burnt food stuck to that spot this morning because someone forgot it was still on. This is a fire hazard and I'm worried about leaving it unattended.",
			"solution": "Replaced faulty gas safety valve that was not properly sealing when closed, allowing gas flow to continue.",
			"parts": ["SKU-SV-003158 - Gas Safety Shutoff Valve 3/4-inch NPT with manual reset"],
		},
		{
			"problem": "The griddle takes forever to heat up now - used to be ready in 10 minutes, now it's taking almost 45 minutes to get hot enough to cook on. My breakfast rush starts at 6 AM and I have to start preheating at 5 just to be ready. This is killing our morning prep time and making everything rushed.",
			"solution": "Cleaned clogged burner orifices and adjusted gas pressure regulator to restore proper heat output and faster heating times.",
			"parts": ["SKU-BO-007412 - Burner Orifice Set #54 drill size for natural gas", "SKU-PR-002903 - Gas Pressure Regulator 11-inch WC with gauge"],
		},
		{
			"problem": "The griddle keeps clicking constantly - this rapid clicking sound that never stops as long as it's on. It's driving everyone crazy and we're worried something electrical is going wrong. The sound gets faster when we turn up the heat and my servers are complaining about the noise.",
			"solution": "Replaced malfunctioning electronic ignition control module that was continuously attempting to spark.",
			"parts": ["SKU-IC-005739 - Electronic Ignition Control Module 120V with flame sensing"],
		},
		{
			"problem": "Grease isn't draining at all anymore - it just sits on the griddle surface in puddles no matter how much we tilt the squeegee. We're having to manually scrape grease off constantly during cooking and it's making everything greasy and gross. Food is basically swimming in old grease by the end of the day.",
			"solution": "Unclogged blocked grease drain line and replaced damaged grease collection funnel with proper slope angle.",
			"parts": ["SKU-GF-003824 - Stainless Steel Grease Collection Funnel 8-inch diameter", "SKU-DL-001671 - Grease Drain Line Kit with flexible connector 24-inch"],
		},
		{
			"problem": "One corner of the griddle gets so hot it's practically glowing while the rest barely warms up. We can cook eggs in that one spot but everything else is useless. My cooks are crowding all the food into that tiny hot area and it's creating chaos during busy periods.",
			"solution": "Replaced damaged burner manifold that had a cracked distribution chamber causing uneven gas flow to individual burners.",
			"parts": ["SKU-BM-006285 - Burner Manifold Assembly 48-inch with 6 outlets", "SKU-GS-001904 - Manifold Gasket Set high-temperature silicone"],
		},
		{
			"problem": "The griddle plate is lifting up on one side and there's a gap forming between sections. Food and grease are falling through the gap into the cabinet below and we can hear it sizzling on the burners. I'm afraid something's going to catch fire down there and the smell is getting terrible.",
			"solution": "Realigned and secured griddle plate mounting brackets and replaced warped support frame underneath.",
			"parts": ["SKU-MB-004517 - Griddle Plate Mounting Bracket Set heavy-duty steel", "SKU-SF-002896 - Support Frame Assembly with adjustable leveling feet", "SKU-FB-001203 - Mounting Hardware Kit stainless steel bolts and washers"],
		},
		{
			"problem": "The chrome surface on our griddle is all bubbled up and peeling off in big chunks. Every time we scrape or clean it, more pieces flake off and get mixed into the food. My cooks are picking chrome bits out of the eggs and hash browns - this is disgusting and we can't serve food like this.",
			"solution": "Replaced the deteriorated chrome-plated griddle surface with a new heavy-duty chrome top plate and properly seasoned it before returning to service.",
			"parts": ["SKU-GP-428571 - Chrome-plated griddle plate 36-inch x 24-inch with beveled edges"],
		},
		{
			"problem": "Water keeps pooling on top of our griddle every morning and we can't figure out where it's coming from. The whole cooking surface gets rusty spots overnight and we have to spend twenty minutes scrubbing it down before we can start breakfast. It's like moisture is getting trapped somewhere inside and condensing on the plate.",
			"solution": "Sealed gaps in the griddle housing and replaced damaged insulation that was allowing moisture infiltration, then cleaned and re-seasoned the cooking surface.",
			"parts": ["SKU-IS-334729 - High-temperature ceramic fiber insulation 2-inch thickness", "SKU-SL-198456 - Food-grade silicone sealant tube 10.3-oz"],
		},
		{
			"problem": "The griddle takes forever to heat up now - we turn it on full blast and it takes almost an hour to get hot enough to cook on. My breakfast crew has to come in earlier just to wait for this thing to warm up. It used to be ready in fifteen minutes, now we're wasting time and gas every morning.",
			"solution": "Cleaned clogged burner orifices and replaced worn gas regulator valve that was restricting proper gas flow to the heating elements.",
			"parts": ["SKU-OR-267891 - Natural gas burner orifice set 0.052-inch diameter", "SKU-RG-445203 - Gas pressure regulator valve 1/2-inch NPT with 11-inch WC setting"],
		},
		{
			"problem": "Every time we turn the griddle on, it makes these loud clicking sounds like something's sparking inside. The clicking goes on for several minutes and sometimes we see little flashes of light through the vents. My staff is afraid to stand too close when we're starting it up because it sounds dangerous.",
			"solution": "Replaced faulty electronic ignition control module and damaged spark electrode that were causing erratic sparking and electrical arcing.",
			"parts": ["SKU-IG-672134 - Electronic ignition control module 120V with safety lockout", "SKU-SP-889245 - Ceramic spark electrode with stainless steel bracket"],
		},
		{
			"problem": "The griddle keeps cycling on and off every few minutes instead of maintaining steady heat. One minute it's cooking great, then it goes cold, then fires back up again. My pancakes are half-cooked on one side because the heat keeps dropping out in the middle of cooking.",
			"solution": "Replaced defective thermostat control that was short-cycling and recalibrated the temperature sensing bulb position for proper heat regulation.",
			"parts": ["SKU-TH-556789 - Heavy-duty griddle thermostat 200-450\u00b0F range with 36-inch capillary tube"],
		},
		{
			"problem": "There's this greasy buildup under the griddle that we can't reach to clean, and now it's starting to smoke and smell awful during busy periods. The smell gets into the food and customers are complaining. We've tried reaching under there but can't get to whatever's burning.",
			"solution": "Removed griddle from mounting brackets, thoroughly cleaned accumulated grease from underneath, and replaced damaged drip pan with proper drainage.",
			"parts": ["SKU-DP-123674 - Stainless steel drip pan 34-inch x 22-inch with rear drain spout", "SKU-MF-445098 - Adjustable mounting foot set of 4 with leveling capability"],
		},
		{
			"problem": "The safety valve keeps shutting off the gas supply randomly during service - the griddle will be working fine then suddenly go cold with no warning. We have to reset something underneath to get it working again. It's happened three times today alone and we're losing food every time.",
			"solution": "Replaced malfunctioning safety gas valve and cleaned the sensing line that was giving false readings, causing unnecessary shutdowns.",
			"parts": ["SKU-SV-778234 - Automatic safety gas valve 3/4-inch with thermal sensing"],
		},
		{
			"problem": "The corners of our griddle plate are starting to curl up and food slides off the edges onto the floor. When we crack eggs near the sides, they run right off before we can catch them. It's like the whole surface is warping from the heat and nothing stays put anymore.",
			"solution": "Replaced warped griddle plate and upgraded the support structure underneath to prevent future warping from thermal expansion.",
			"parts": ["SKU-GP-991456 - Heavy-gauge steel griddle plate 1/2-inch thick with reinforced edges", "SKU-SS-234567 - Structural support framework with thermal expansion joints"],
		},
		{
			"problem": "Our griddle has these deep scratches and gouges that trap grease and food particles no matter how much we scrub. Everything tastes like old grease because we can't get those grooves clean. The health inspector is coming next week and I'm worried about what they'll say when they see this mess.",
			"solution": "Professionally resurfaced the griddle plate to remove deep scratches and applied protective coating to prevent future damage.",
			"parts": ["SKU-SC-667891 - Food-grade surface coating kit with primer and topcoat"],
		},
		{
			"problem": "The gas line connection behind the griddle is making a hissing sound and I can smell gas near the wall. It's not a strong smell but it's definitely there, and the sound gets louder when we turn up the heat. I'm worried about having an open flame so close to a gas leak.",
			"solution": "Replaced deteriorated gas line flexible connector and tightened all fittings, then performed leak test to ensure complete seal integrity.",
			"parts": ["SKU-GL-445612 - Flexible gas connector 3/4-inch x 48-inch with safety coating", "SKU-FT-223478 - Brass flare fitting set with thread sealant compound"],
		},
		{
			"problem": "The griddle chrome surface has turned all discolored and blotchy - it looks terrible and customers can see it from the counter. The discoloration seems to be getting worse each week and now food tastes metallic when it touches certain spots. My staff is embarrassed to cook on it because it looks so unprofessional.",
			"solution": "Replaced the damaged chrome-plated griddle surface with a new factory-spec chrome plate and applied proper seasoning treatment to restore non-stick properties and appearance.",
			"parts": ["SKU-CP-247831 - Chrome-plated griddle surface 36-inch x 24-inch commercial grade"],
		},
		{
			"problem": "The safety shutoff system keeps triggering randomly and cutting gas to the whole griddle. We'll be in the middle of breakfast rush and suddenly everything goes cold with no warning. It happens maybe three or four times a day and we lose so much food when it shuts down mid-cook.",
			"solution": "Replaced the faulty thermocouple safety sensor that was sending intermittent signals and recalibrated the gas valve safety system.",
			"parts": ["SKU-TC-189456 - High-temperature thermocouple sensor with 24-inch lead wire", "SKU-GV-334721 - Gas safety valve assembly with automatic shutoff mechanism"],
		},
		{
			"problem": "The electric heating elements under our griddle seem to be dying one by one. First the back left went out, now the front right is barely warm, and I think another one is going too. Half the cooking surface is useless and we can only use the center section for anything that needs real heat.",
			"solution": "Replaced all failed electric heating elements and tested the electrical connections for proper voltage and amperage delivery.",
			"parts": ["SKU-HE-892347 - Electric griddle heating element 2000W 240V tubular design", "SKU-HE-892348 - Electric griddle heating element 1500W 240V compact design", "SKU-WR-156892 - High-temperature wiring harness with ceramic connectors"],
		},
		{
			"problem": "There's this grinding noise coming from under the griddle whenever the gas valves open or close, and sometimes they get stuck halfway. My cooks have to bang on the control panel to get them unstuck, which can't be good for the equipment. The whole thing feels like it's going to break completely any day now.",
			"solution": "Rebuilt the gas manifold assembly and replaced worn gas orifices that were causing pressure irregularities and mechanical binding.",
			"parts": ["SKU-GM-445672 - Gas manifold assembly with pressure regulator and mounting hardware", "SKU-GO-778234 - Gas burner orifice set #54 drill size natural gas rated"],
		},
		{
			"problem": "The griddle won't heat up fast enough anymore - it used to be ready in ten minutes but now takes almost an hour to get hot enough to cook on. My morning shift has to come in extra early just to get it warmed up before we open. Even when it finally gets hot, it feels like it's struggling to maintain temperature.",
			"solution": "Cleaned and adjusted all gas burner assemblies, replaced clogged burner ports, and recalibrated the gas pressure regulator for optimal fuel delivery.",
			"parts": ["SKU-BA-334521 - Gas burner assembly with adjustable air shutter and mounting bracket", "SKU-PR-667843 - Gas pressure regulator valve 1/2-inch NPT natural gas rated"],
		},
		{
			"problem": "Water keeps pooling on top of the griddle every morning and we can't figure out where it's coming from. It's not from cleaning - this happens even when we don't wash it the night before. The water sits in certain spots and makes the griddle smoke terribly when we first turn it on each day.",
			"solution": "Replaced damaged griddle mounting brackets and releveled the unit to eliminate low spots where condensation was collecting overnight.",
			"parts": ["SKU-MB-223847 - Adjustable griddle mounting bracket set with leveling feet and hardware"],
		},
		{
			"problem": "The flame pattern under our gas griddle looks all wrong - instead of nice even blue flames, we get these tall yellow flickering flames that don't heat evenly. You can actually see the uneven heat pattern on the cooking surface where some spots are way hotter than others. Food cooks completely unevenly now.",
			"solution": "Replaced the gas valve regulator and cleaned all burner venturi tubes to restore proper air-to-gas mixture and flame characteristics.",
			"parts": ["SKU-GR-445789 - Gas valve regulator with pressure gauge and 3/4-inch connections", "SKU-VT-887234 - Venturi tube assembly with air intake adjustment and cleaning ports"],
		},
		{
			"problem": "The griddle control panel is completely dead - none of the indicator lights work and I can't tell if anything is on or what temperature it's set to. We're flying blind and have to touch-test the surface to guess if it's hot enough. This morning someone got burned because they couldn't tell a section was still heating up.",
			"solution": "Replaced the main control board and all indicator LED lights, then recalibrated the temperature display system.",
			"parts": ["SKU-CB-556892 - Digital control board with temperature display and safety monitoring", "SKU-LD-334456 - LED indicator light assembly with multi-color status display", "SKU-TS-778901 - Temperature sensor probe with digital readout capability"],
		},
		{
			"problem": "The griddle has these dead spots where nothing cooks at all - I can crack an egg on those areas and it just sits there cold while the rest of the surface is working fine. My cooks have to avoid certain sections entirely which cuts down our cooking space by almost half. We're falling behind on orders because we can't use the whole surface anymore.",
			"solution": "Replaced faulty heating elements in the affected zones and reconnected loose electrical connections to restore even heat distribution across the entire cooking surface.",
			"parts": ["SKU-HE-243891 - Electric heating element 240V 3500W with terminal connections", "SKU-WR-156742 - High-temperature wire harness assembly for griddle zones"],
		},
		{
			"problem": "The griddle keeps clicking and trying to ignite even when it's already lit and running. It's this constant clicking noise that drives everyone crazy and customers keep asking what that sound is. Sometimes the clicking gets so loud we can't hear each other talk in the kitchen.",
			"solution": "Replaced malfunctioning ignition control module that was continuously sending spark signals and calibrated the flame sensing circuit.",
			"parts": ["SKU-IG-789234 - Electronic ignition control module with flame sensing"],
		},
		{
			"problem": "There's this gross greasy residue building up all around the edges where the griddle meets the counter, and it won't come off with normal cleaning. It's turning black and crusty and starting to smell rancid. The health department is coming next week and I'm panicking about this mess.",
			"solution": "Replaced deteriorated edge seals and gaskets that were allowing grease penetration, then performed deep degreasing of affected areas.",
			"parts": ["SKU-SL-445627 - Griddle edge seal kit with corner gaskets", "SKU-CL-298455 - Food-safe degreasing compound for commercial equipment", "SKU-GS-334782 - High-temperature silicone gasket material"],
		},
		{
			"problem": "The safety shut-off keeps kicking in randomly and killing the gas to the whole griddle - sometimes right in the middle of the breakfast rush. My staff has to wait for it to reset and relight everything, which takes forever. We've lost so many orders because of these random shutdowns.",
			"solution": "Replaced faulty thermocouple safety sensor that was giving false readings and adjusted the gas valve safety system calibration.",
			"parts": ["SKU-TC-667891 - Universal thermocouple sensor 24-inch with safety connector"],
		},
		{
			"problem": "The griddle chrome surface has these weird stains and discoloration patches that make the food look dirty even when it's perfectly clean. Customers keep sending back perfectly good food because they think it looks contaminated. My servers are getting tired of explaining that the food is fine.",
			"solution": "Performed professional chrome surface restoration using specialized compounds and applied protective coating to prevent future staining.",
			"parts": ["SKU-CR-123456 - Chrome surface restoration compound kit", "SKU-PT-789012 - Food-safe chrome protective coating"],
		},
		{
			"problem": "One of the gas control knobs fell completely off and now we can't control that burner section at all. The knob just spins freely when we try to put it back on and there's no way to adjust the flame. We're basically down to three-quarters of our cooking space until this gets fixed.",
			"solution": "Replaced damaged control valve stem and installed new control knob assembly with proper shaft engagement mechanism.",
			"parts": ["SKU-VL-445783 - Gas control valve assembly with calibrated orifice", "SKU-KN-267834 - Control knob with temperature markings and shaft coupler"],
		},
		{
			"problem": "The whole griddle shakes and vibrates when we're cooking on it, especially when flipping heavy items like burgers. It makes this rattling noise and everything on the surface bounces around. My cooks are afraid something's going to fall apart and they can't work confidently anymore.",
			"solution": "Tightened and reinforced loose mounting brackets and replaced worn vibration dampeners in the support structure.",
			"parts": ["SKU-MB-556789 - Heavy-duty mounting bracket set with reinforcement plates", "SKU-VD-223445 - Vibration dampener pads for commercial equipment"],
		},
		{
			"problem": "The griddle takes forever to cool down after service - even hours later it's still too hot to clean properly. My night cleaning crew keeps getting burned trying to scrub it and we're having to wait until morning to do a proper cleaning. This is messing up our whole cleaning schedule.",
			"solution": "Replaced malfunctioning temperature control solenoid that was keeping gas flowing at low levels and cleaned blocked cooling vents.",
			"parts": ["SKU-SV-778923 - Temperature control solenoid valve with quick-shutoff"],
		},
		{
			"problem": "There are these rusty spots appearing all over the griddle plate that keep getting worse no matter how much we clean and oil the surface. Food tastes metallic when it touches those spots and I'm worried about health issues. The rust seems to be coming from underneath somehow.",
			"solution": "Replaced corroded griddle plate with stainless steel upgrade and treated underlying support structure for rust prevention.",
			"parts": ["SKU-GP-334567 - Stainless steel griddle plate 36-inch with non-stick coating", "SKU-RS-445623 - Anti-corrosion treatment kit for griddle framework"],
		},
		{
			"problem": "The grease trap underneath is making this awful gurgling sound and occasionally burps up greasy water that splashes everywhere. The smell is horrible and it's happening more often during busy periods. My dishwashers refuse to work near it anymore because of the stench.",
			"solution": "Replaced clogged grease trap assembly and cleaned blocked drain lines, then installed improved venting system to prevent backup pressure.",
			"parts": ["SKU-GT-667834 - Commercial grease trap assembly with overflow protection", "SKU-DR-445789 - Grease drain line cleaning kit", "SKU-VT-223567 - Grease management vent system"],
		},
	],
}