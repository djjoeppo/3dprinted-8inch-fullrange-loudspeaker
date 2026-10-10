# Prompts voor de Luidspreker Basket / Kooi (100% Supportless 3D-Print)

Dit document bevat kant-en-klare, gedetailleerde prompts die je kunt gebruiken in AI-modellen (zoals ChatGPT, Claude, DeepSeek, Midjourney of CAD AI-assistenten) om 3D CAD-modellen, scripts (Fusion 360, FreeCAD, OpenSCAD) of visuele weergaven van de **basket (kooi)** van de luidspreker te genereren.

---

## 1. Uitgebreide CAD / Code Generatie Prompt (Voor LLMs & CAD Script Generators)

Gebruik onderstaande prompt als je een LLM vraagt om Python-scripts (Fusion 360 / FreeCAD) of OpenSCAD code te schrijven voor de basket:

```text
Genereer een CAD 3D-model / script voor een 100% supportless 3D-printbare luidspreker basket (kooi / korf) met de volgende exacte specificaties en ontwerpregels:

### 1. Algemene Ontwerpregels & 3D-Print Optimalisatie:
- 100% Supportless: Gebruik de 45-graden overhangregel. Alle overgangen en vellingkanten (chamfers) moeten een hoek van minimaal 45° t.o.v. de printas hebben.
- Ondersteboven/Rechtop te printen zonder enige ondersteuningsstructuur (support material).

### 2. Motor Interface & Base Flange (Onderflens):
- Buitendiameter flens: Ø 124.00 mm.
- Flens dikte: 6.00 mm.
- Centreer- / Registratie-kraag: Binnendiameter Ø 41.20 mm (+0.00 / -0.10 mm clearance) met een 1.00 mm x 45° zoek-schuinte (chamfer) voor exacte klempassing op een afgedraaide stalen top plate.
- Gatenpatroon (8x M5): 8x Ø 5.50 mm doorgaande gaten gelijk verdeeld om de 45.0° op een Bolt Circle Diameter (BCD) van Ø 80.00 mm (steekcirkel radius R = 40.00 mm). Inclusief 45° verzonken kamers voor M5 inbusbouten.

### 3. Midden-Flens (Spider / Centreerspin Montage):
- Hoogte spider-flens boven de basis: 28.00 mm.
- Binnendiameter spider-zitting: Ø 80.00 mm.
- Buitendiameter spider-ring: Ø 88.00 mm.
- Ring dikte/hoogte: 4.00 mm.
- Geïntegreerde bajonet-nokken / schroefdraad-zitting met 45° schuine onderzijde voor een supportless 3D-geprinte bajonet klemring (kwartslag draai-klik).

### 4. Boven-Flens (Surround / Soepelrand Montage):
- Totale basket hoogte: 52.00 mm (bovenkant surround-flens bevindt zich op Z = 52.00 mm).
- Buitendiameter surround-flens: Ø 130.00 mm.
- Binnendiameter: Ø 110.00 mm.
- Dikte: 6.00 mm (van Z = 46.00 mm tot Z = 52.00 mm).
- Verbinding: M125 x 2.0 mm 3D-geprinte trapezoïdale schroefdraad met 45° flanken en 0.15 mm print-clearance voor de opgeschroefde klemring.

### 5. Spaken & Structuur (Supportless Frame):
- 6 radiale verticale pijlers / spaken verdeeld om de 60°.
- Pijler/Spaak radius: Bevindt zich op R = 61.50 mm (strak onder de buitenzijde van de surround-flens).
- De spaken verbinden de onderflens rechtstreeks met de bovenflens en dragen de spider-middenring via radiale dwarsverbindingen met 45° inloophoeken voor maximale akoestische openheid en minimale luchtweerstand aan de achterzijde van de conus.
```

---

## 2. Beknopte Prompt (Voor Snel Gebruik / Chatbots)

Gebruik deze korte prompt voor een snelle vraag of schets in een AI-chat:

```text
Ontwerp een 3D-geprinte luidspreker basket (kooi) in CAD:
- Totale hoogte 52mm, onderflens Ø124mm met 8x M5 gaten op Ø80mm BCD en Ø41.2mm centreerrand.
- Middenring voor TPU spider op Z=28mm (ID Ø80mm, OD Ø88mm).
- Bovenring voor TPU surround op Z=52mm (ID Ø110mm, OD Ø130mm) met M125x2.0 trapezoïdale schroefdraad.
- 6 slanke open pijlers om de 60° voor maximale luchtstroom.
- 100% supportless geoptimaliseerd volgens de 45-graden overhangregel.
```

---

## 3. Visuele Visualisatie Prompt (Voor Midjourney / DALL-E / Stable Diffusion)

Als je een realistische of technische 3D-rendering van de basket wilt genereren:

```text
3D CAD render of a futuristic 3D-printable loudspeaker basket driver frame, industrial design, precision engineered PLA plastic, dark gray finish, 6 open-air structural spokes, bottom mounting flange with 8 counter-bored M5 bolt holes on an 80mm pitch circle, middle ring for spider mounting, top threaded ring for surround clamping, supportless 45-degree chamfered geometry, technical studio lighting, clean background, 8k resolution, photorealistic.
```

---

## 4. LLM Engineering & Aanpassings-Prompt (Voor Verdere Doorontwikkeling)

Als je de basket wilt aanpassen of uitbreiden (bijvoorbeeld ander aantal spaken of gewijzigde hoogtematen):

```text
Ik werk aan een modulaire 3D-geprinte luidspreker. Ik wil de basket (kooi) aanpassen met behoud van de volgende randvoorwaarden:
1. De basis blijft passen op een Ø41.20mm top plate centreerrand met 8x M5 boutgaten op Ø80mm BCD.
2. Alle overhangen moeten minimaal 45° t.o.v. het printbed blijven voor 100% supportless 3D-printen.
3. De spider-flens staat op Z=28.00mm en de surround-flens op Z=52.00mm.
Geef advies of schrijf de aangepaste code voor [vul hier je CAD software in: Fusion 360 / FreeCAD / OpenSCAD].
```
