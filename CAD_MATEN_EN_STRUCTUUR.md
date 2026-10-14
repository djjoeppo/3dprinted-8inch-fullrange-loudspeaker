# CAD Maten, Toleranties & Structuurlay-out (8-Inch 100% Supportless 3D-Print)

Dit document bevat alle exacte maatvoeringen, toleranties, schroefdraden en bajonet-specificaties voor de **8-inch (200 mm) luidspreker driver** die direct overgenomen kunnen worden in 3D CAD-software (zoals Fusion 360, FreeCAD of SolidWorks), volledig geoptimaliseerd voor **100% supportless 3D-printen**.

---

## 1. Supportless 3D-Print Ontwerpregels (Geen Support Noodzakelijk)

Om alle onderdelen zonder enige support-structuur strak te kunnen printen:
* **$45^\circ$ Overhang Regel:** Geen enkele horizontale overhanging groter dan $0.80\text{ mm}$. Alle overgangen gebruiken een schuine hoek van $\ge 45^\circ$ t.o.v. het printbed.
* **Trapezium Schroefdraad:** Alle 3D-geprinte schroefdraden gebruiken een trapezoïdaal/ $45^\circ$ flankprofiel met afgeschuinde toppen ($0.30\text{ mm}$ chamfer).
* **Bajonet Nokken:** Alle bajonet-nokken hebben een onderzijde met een $45^\circ$ schuine inloop (chamfer) zodat ze ondersteboven/in de lucht printen zonder uitstulpingen.

---

## 2. Top Plate & Kooi Interface Maten (Motor Interface)

* **Top Plate Buitendiameter:** $\varnothing 120.00\text{ mm}$ (Radius $R = 60.00\text{ mm}$).
* **Top Plate Binnendiameter (Afgedraaid):** **$\varnothing 41.20\text{ mm}$** ($\pm 0.05\text{ mm}$, Radius $r = 20.60\text{ mm}$).
* **Gatenpatroon Top Plate (8x M5):**
  * **Aantal gaten:** 8 stuks gelijk verdeeld om de **$45.0^\circ$**.
  * **Afstand hart gat tot buitencirkel:** **$20.00\text{ mm}$**.
  * **Steekcirkel Diameter (BCD):** **$\varnothing 80.00\text{ mm}$**.
* **Kooi Onderflens (Basket Base Flange):**
  * Buitendiameter flens: $\varnothing 124.00\text{ mm}$.
  * Dikte flens: $6.00\text{ mm}$.
  * Gaten in flens: 8x $\varnothing 5.50\text{ mm}$ op $\varnothing 80.00\text{ mm}$ BCD met $45^\circ$ verzonken kamers voor M5 inbusbouten.
  * **Supportless Registratie-kraag:** Een onderstaande centreerrand van $\varnothing 41.20\text{ mm}$ (+0.00 / -0.10 mm clearance) voorzien van een **$1.00\text{ mm} \times 45^\circ$ zoek-schuinte** (chamfer).

---

## 3. 8-Inch Kooi Spaken & Hoogte (Supportless Basket Geometry)

* **Totale Kooi Hoogte:** $75.00\text{ mm}$.
* **Kooi Bovenflens (Surround Montage):** Buitendiameter $\varnothing 210.00\text{ mm}$, Binnendiameter $\varnothing 185.00\text{ mm}$.
* **Kooi Middenflens (Spider Montage):**
  * Hoogte boven top plate: $28.00\text{ mm}$ (gelijk aan conus keel/hals-hoogte).
  * Binnendiameter spider-zitting: $\varnothing 80.00\text{ mm}$.
  * Buitendiameter spider-flens: $\varnothing 88.00\text{ mm}$.
* **Kooi Draagpijlers / Spaken:** 6 radiale pijlers gehoekt op $60^\circ$ t.o.v. het printbed voor 100% supportless printen.

---

## 4. 8-Inch Conus & Externe Onder-Ribben (Supportless Cone Geometry)

* **Conus Buitendiameter:** $\varnothing 185.00\text{ mm}$ (8-inch klasse).
* **Conus Binnendiameter (stofkap-naaf):** $\varnothing 38.60\text{ mm}$.
* **Conus Hoogte / Diepte:** $47.00\text{ mm}$ (Exponentieel gekromde trechter op $50^\circ - 55^\circ$ hoek t.o.v. printbed $\rightarrow$ 100% supportless!).
* **Conus Wanddikte:** $0.60\text{ mm}$ (of $0.40\text{ mm}$ bij LW-PLA vase mode).
* **Onderzijde Verstevigingsribben:**
  * **Aantal:** 8 radiale ribben om de $45^\circ$.
  * **Cross-section:** Driehoekig/trapezoïdaal profiel ($0.80\text{ mm}$ dik) met $45^\circ$ schuine zijwanden.

---

## 5. Stofkap & Spreekspoel-Naaf (Core Hub)

* **Spreekspoel Drager Binnendiameter:** $\varnothing 38.10\text{ mm}$ (1.5 inch).
* **Aluminium Drager Dikte:** $0.10\text{ mm}$.
* **Koperwikkeling (2-laags $0.34\text{ mm}$ met lak):** Buitendiameter spoel = $\varnothing 39.66\text{ mm}$.
* **Stofkap-Naaf Buitendiameter:** $\varnothing 42.00\text{ mm}$.
* **Stofkap-Naaf Verbinding met Conus:**
  * **M24 x 1.5 mm 3D-geprinte trapezoïdale schroefdraad**.
* **Schroefbaar Stofkap-Deksel (Dust Cap Lid):**
  * **Buitendiameter deksel:** $\varnothing 32.00\text{ mm}$.
  * **Verbinding:** 3D-geprinte M28 x 1.0 mm draad met $45^\circ$ inloop-chamfer.
  * **Intern Binnencompartiment:** $\varnothing 26.00\text{ mm} \times 7.00\text{ mm}$ met $45^\circ$ schuine bodemhoek.

---

## 6. TPU Flexibele Onderdelen (Spider & Surround CAD Specs)

### A. 8-Inch TPU Surround (Soepelrand)
* **Binnendiameter (Conus-zitting):** $\varnothing 184.00\text{ mm}$ met $1.5\text{ mm}$ klem-kraag.
* **Buitendiameter (Kooi-zitting):** $\varnothing 202.00\text{ mm}$ met $2.0\text{ mm}$ klem-kraag.
* **Golf-Profiel (High-Roll):** Halve bol met $45^\circ$ glooiende overgangen naar de flenzen.
* **Wanddikte:** **$0.40\text{ mm}$** (Exact 1 perimeter).

### B. TPU Spider (Centreerspin)
* **Binnendiameter:** $\varnothing 38.60\text{ mm}$ met $1.2\text{ mm}$ versterkte ring.
* **Buitendiameter:** $\varnothing 84.00\text{ mm}$ met $1.5\text{ mm}$ buitenring.
* **Golf-Profiel:** 3 concentrische rimpels met $45^\circ$ flankhoeken.
* **Geometrische Uitsparingen:** 6 radiale spaken-gleuven van $2.50\text{ mm}$ breed voor TPU 90A/95A flexibiliteit.
* **Wanddikte:** **$0.40 - 0.50\text{ mm}$**.

---

## 7. Aanbevolen 3D-Print Toleranties (Clearances)

* **Schroefdraad (3D-Geprint):** $0.15 - 0.20\text{ mm}$ offset op binnendraad-flanken.
* **Bajonet / Klik-Pasvormen:** $0.15\text{ mm}$ speling op draaiende vlakken met $45^\circ$ afschuining op alle hoeken.
* **TPU Klemgroeven:** Stijve PLA/ABS klemgroef $0.10\text{ mm}$ smaller dan de TPU kraag voor $100\%$ luchtdichte klemming.
