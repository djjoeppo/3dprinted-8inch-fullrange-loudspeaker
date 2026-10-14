# Ontwerpbeslissingen 8-Inch Fullrange Luidspreker Driver

Dit document bevat alle definitieve ontwerpbeslissingen en specificaties voor de luidsprekermotor, spreekspoel, geometrie en **3D-geprinte onderdelen** (kooi, conus, surround, spider) voor de **8-inch (200 mm) fullrange luidspreker driver**.

---

## 1. Magneet & Motorgeometrie (8-Inch Klasse)

* **Magneet:** Ferriet ring ($120 \times 20 \times 60\text{ mm}$).
* **Poolkern (Yoke Outer Diameter):** $\varnothing 37.70\text{ mm}$.
* **Bodemplaat Dikte:** $5.0\text{ mm}$.
* **Top Plate Origineel:** Dikte $4.0\text{ mm}$, binnendiameter $\varnothing 40.80\text{ mm}$.
* **Top Plate Bewerking (Draaibank):**
  * **Snijdiepte per zijde (radius):** $0.20\text{ mm}$ afdraaien.
  * **Eindmaat Binnendiameter:** **$\varnothing 41.20\text{ mm}$**.
* **Nieuwe Luchtspleet Breedte:** $\frac{41.20 - 37.70}{2} = \mathbf{1.75\text{ mm}}$.

---

## 2. Spreekspoel & Draad Specificaties (Definitief Gekozen 2-Laags 4 Ohm)

* **Draadtype:** $0.34\text{ mm}$ geëmailleerd koper met lak ($0.30\text{ mm}$ koperkern, $QA-1/155$).
* **Weerstand Koperdraad:** $0.40\,\Omega/\text{meter}$.
* **Drager Materiaal:** Aluminium ($0.10\text{ mm}$ dik).
* **Drager Binnendiameter:** $38.10\text{ mm}$ (1.5 inch).
* **Drager Optimalisatie:** Verticale zaagsnede/gleuf ($0.5 - 1.0\text{ mm}$) over de lengte van het aluminium om wervelstromen (eddy currents) te onderbreken en $Q_{ms}$ / hoogweergave te behouden. Optioneel 4 ventilatiegaatjes ($\varnothing 2.0\text{ mm}$) vlak boven de wikkeling voor actieve spoelkoeling.

### Definitieve Wikkeling Specificaties:
* **Aantal Lagen:** 2 lagen.
* **Totaal Aantal Windingen:** **66 windingen** (33 windingen per laag).
* **Wikkelhoogte:** **11.2 mm** ($33 \times 0.34\text{ mm}$).
* **Benodigde Draadlengte:** Exact **8.0 meter**.
* **Gelijkstroomweerstand ($R_e$):** ca. **$3.2\,\Omega$** (Nominaal **4.0 Ohm** luidspreker).
* **Lineaire Uitslag ($X_{\max}$):** $\frac{11.2 - 4.0}{2} = \mathbf{3.6\text{ mm}}$ (enkele slag).
* **Gewicht Koper:** ca. **$5.1\text{ gram}$**.
* **Thermische Belastbaarheid (op 8-inch chassis):** **40 tot 50 Watt RMS continu** (Muziek- / Piekvermogen: **120 Watt**).
  * *Toelichting:* De grote 8-inch conus verplaatst veel lucht onder de spider en kooi, wat werkt als een actieve pompkoeling rondom de spreekspoel.

---

## 3. Luchtspleet Speling & Toleranties

* **Totale Spoeldikte:** $0.10\text{ mm}$ (drager) $+ (2 \times 0.34\text{ mm}) = \mathbf{0.78\text{ mm}}$.
* **Binnenste Speling (tussen poolkern $\varnothing 37.70\text{ mm}$ en drager ID $\varnothing 38.10\text{ mm}$):** $\mathbf{0.20\text{ mm}}$ speling aan weerszijden ($0.40\text{ mm}$ totale speling).
* **Buitenste Speling (tussen spoel OD $\varnothing 39.66\text{ mm}$ en top plate ID $\varnothing 41.20\text{ mm}$):** $\mathbf{0.77\text{ mm}}$ vrije speling rondom (zeer veilige marge tegen aanlopen).

---

## 4. 3D-Geprinte Luidspreker Chassis Onderdelen (8-Inch Supportless)

* **Supportless 3D-Print Regel:** Alle geometrieën zijn geoptimaliseerd voor **100% supportless printen** door gebruik van de $45^\circ$-regel, $45^\circ$ afschuiningen (chamfers) op overhangingen en gehoekte spaken/pijlers.
* **Kooi / Korf (Basket):** 8-inch chassis ($\varnothing 210\text{ mm}$) in PETG/PLA+ met 6 verticale drager-pijlers en gehoekte spaken.
* **Conus:** 8-inch conus ($\varnothing 185\text{ mm}$) in LW-PLA / PLA met 8 radiale verstevigingsribben aan de onderzijde.
* **Ophanging (TPU 90A/95A):**
  * **Surround (Soepelrand):** High-roll profiel ($\varnothing 200\text{ mm}$) single-wall ($0.40\text{ mm}$).
  * **Spider (Centreerspin):** Gespaakte golfring ($\varnothing 84\text{ mm}$) single/double perimeter ($0.40 - 0.50\text{ mm}$).
