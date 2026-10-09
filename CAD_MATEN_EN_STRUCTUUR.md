# CAD Maten, Toleranties & Structuurlay-out (3D-Print)

Dit document bevat alle exacte maatvoeringen, toleranties, schroefdraden en bajonet-specificaties die direct overgenomen kunnen worden in 3D CAD-software (zoals Fusion 360, SolidWorks of FreeCAD).

---

## 1. Top Plate & Kooi Interface Maten

* **Top Plate Buitendiameter:** $\varnothing 120.00\text{ mm}$.
* **Top Plate Binnendiameter (Afgedraaid):** **$\varnothing 41.20\text{ mm}$** ($\pm 0.05\text{ mm}$).
* **Gatenpatroon Top Plate:** **8x M5** op een steekcirkel van **$\varnothing 108.00\text{ mm}$** ($45^\circ$ hoek tussen de gaten).
* **Kooi Onderflens (Basket Base Flange):**
  * Buitendiameter flens: $\varnothing 124.00\text{ mm}$.
  * Dikte flens: $6.00\text{ mm}$.
  * Gaten in flens: 8x $\varnothing 5.50\text{ mm}$ verzonken voor M5 inbusbouten.
  * **Registratie-kraag:** Een onderstaande centreerrand van $\varnothing 41.20\text{ mm}$ (+0.00 / -0.10 mm clearance) die exact strak in de top plate valt voor $100\%$ herhaalbare centrering.

---

## 2. Kooi Spaken & Hoogte (Basket Geometry)

* **Totale Kooi Hoogte (van top plate tot surround-flens):** $52.00\text{ mm}$.
* **Spider Montage Flens (Kooi Midden-ring):**
  * Hoogte boven top plate: $18.00\text{ mm}$.
  * Binnendiameter spider-zitting: $\varnothing 84.00\text{ mm}$.
  * Buitendiameter spider-klemring: $\varnothing 92.00\text{ mm}$.
  * Verbinding: **3D-Geprinte Bajonet (3 nokken, $30^\circ$ draaiing)** met stop-lip.
* **Surround Montage Flens (Kooi Boven-ring):**
  * Buitendiameter: $\varnothing 135.00\text{ mm}$.
  * Binnendiameter: $\varnothing 112.00\text{ mm}$.
  * Verbinding: **M125 x 2.0 mm 3D-geprinte grof-schroefdraad** of 4-nokken bajonet-klemring.

---

## 3. Conus & Externe Onder-Ribben (Cone Geometry)

* **Conus Buitendiameter (tot surround-zitting):** $\varnothing 108.00\text{ mm}$.
* **Conus Binnendiameter (stofkap-naaf):** $\varnothing 38.60\text{ mm}$.
* **Conus Hoogte / Diepte:** $24.00\text{ mm}$ (Exponentieel gekromde trechter).
* **Conus Wanddikte:** $0.60\text{ mm}$ (of $0.40\text{ mm}$ bij LW-PLA vase mode).
* **Onderzijde Verstevigingsribben:**
  * **Aantal:** 8 radiale ribben verdeeld om de $45^\circ$.
  * **Dikte:** $0.80\text{ mm}$ aan de basis, verlopend naar $0.50\text{ mm}$ bij de conusrand.
  * **Hoogte rib:** $3.00\text{ mm}$ bij de stofkap-naaf, taps aflopend naar $0.50\text{ mm}$ bij de rand.

---

## 4. Stofkap & Spreekspoel-Naaf (Core Hub)

* **Spreekspoel Drager Binnendiameter:** $\varnothing 38.10\text{ mm}$ (1.5 inch).
* **Aluminium Drager Dikte:** $0.10\text{ mm}$ (Buitendiameter drager = $\varnothing 38.30\text{ mm}$).
* **Koperwikkeling (2-laags $0.30\text{ mm}$):** Buitendiameter spoel = $\varnothing 39.50\text{ mm}$.
* **Stofkap-Naaf Verbinding met Conus:**
  * **M24 x 1.5 mm 3D-geprinte schroefdraad** op de buitenzijde van de stofkap-naaf.
  * De conus binnennaven heeft de bijbehorende binnendraad.
* **Schroefbaar Stofkap-Deksel (Dust Cap Lid):**
  * **Buitendiameter deksel:** $\varnothing 32.00\text{ mm}$.
  * **Verbinding:** 3D-geprinte M28 x 1.0 mm draad of $1/4$-slag bajonet.
  * **Intern Binnencompartiment:** $\varnothing 26.00\text{ mm} \times 8.00\text{ mm}$ diep voor het plaatsen van M3/M4 test-gewichtjes ($0.5 - 5.0\text{ gram}$).

---

## 5. TPU Flexibele Onderdelen (Spider & Surround CAD Specs)

### A. TPU Surround (Soepelrand)
* **Binnendiameter (Conus-zitting):** $\varnothing 107.50\text{ mm}$ met een $1.5\text{ mm}$ dikke klem-kraag (bead).
* **Buitendiameter (Kooi-zitting):** $\varnothing 125.00\text{ mm}$ met een $2.0\text{ mm}$ dikke klem-kraag.
* **Golf-Profiel (High-Roll):** Halve bol met breedte $8.50\text{ mm}$ en hoogte $6.00\text{ mm}$.
* **Wanddikte:** **$0.40\text{ mm}$** (Exact 1 perimeter printen met $0.4\text{ mm}$ nozzle).

### B. TPU Spider (Centreerspin)
* **Binnendiameter (Conus-naaf zitting):** $\varnothing 38.60\text{ mm}$ met een $1.2\text{ mm}$ dikke versterkte ring.
* **Buitendiameter (Kooi-zitting):** $\varnothing 84.00\text{ mm}$ met een $1.5\text{ mm}$ dikke buitenring.
* **Golf-Profiel:** 3 concentrische rimpels met hoogte van $3.50\text{ mm}$ en steek van $6.50\text{ mm}$.
* **Geometrische Uitsparingen:** 6 radiale spaken-gleuven van $2.50\text{ mm}$ breed per rimpel voor maximale flexibiliteit bij TPU 90A/95A.
* **Wanddikte:** **$0.40 - 0.50\text{ mm}$**.

---

## 6. Aanbevolen 3D-Print Toleranties (Clearances)

* **Schroefdraad (3D-Geprint):**
  * Geef op de binnendraad (Female Thread) een extra **$0.15 - 0.20\text{ mm}$ offset** op de flanken, zodat geprinte draden soepel in elkaar draaien zonder te binden.
* **Bajonet / Klik-Pasvormen:**
  * **$0.15\text{ mm}$ speling** op draaiende vlakken.
* **TPU Klemgroeven:**
  * Maak de stijve PLA/ABS klemgroef **$0.10\text{ mm}$ narrower** dan de TPU kraag. TPU 90A/95A laat zich licht indrukken, waardoor de verbinding $100\%$ luchtdicht en spelingsvrij vastklemt!
