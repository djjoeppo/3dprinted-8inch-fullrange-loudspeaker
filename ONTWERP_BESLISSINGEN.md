# Ontwerpbeslissingen Fullrange Luidspreker Driver

Dit document bevat alle definitieve ontwerpbeslissingen en specificaties voor de luidsprekermotor, spreekspoel, geometrie en **3D-geprinte onderdelen** (kooi, conus, surround, spider).

---

## 1. Magneet & Motorgeometrie

* **Magneet:** Ferriet ring ($120 \times 20 \times 60\text{ mm}$).
* **Poolkern (Yoke Outer Diameter):** $\varnothing 37.70\text{ mm}$.
* **Bodemplaat Dikte:** $5.0\text{ mm}$.
* **Top Plate Origineel:** Dikte $4.0\text{ mm}$, binnendiameter $\varnothing 40.80\text{ mm}$.
* **Top Plate Bewerking (Draaibank):**
  * **Snijdiepte per zijde (radius):** $0.20\text{ mm}$ afdraaien.
  * **Eindmaat Binnendiameter:** **$\varnothing 41.20\text{ mm}$**.
* **Nieuwe Luchtspleet Breedte:** $\frac{41.20 - 37.70}{2} = \mathbf{1.75\text{ mm}}$.

---

## 2. Spreekspoel & Draad Specificaties

* **Draadtype:** $0.30\text{ mm}$ geëmailleerd koper ($QA-1/155$).
* **Drager Materiaal:** Aluminium ($0.10\text{ mm}$ dik).
* **Drager Binnendiameter:** $38.10\text{ mm}$ (1.5 inch).
* **Drager Optimalisatie:** Dunne verticale zaagsnede/gleuf ($0.5 - 1.0\text{ mm}$) over de lengte van het aluminium om wervelstromen (eddy currents) te onderbreken en $Q_{ms}$ / hoogweergave te behouden.

### Opties voor Wikkeling (2-laags, $0.30\text{ mm}$ draad):

1. **Optie A (Korte Spoel - Maximale Gevoeligheid & Snelheid):**
   * **Wikkelhoogte:** $7.2\text{ mm}$ (48 windingen totaal).
   * **Gelijkstroomweerstand ($R_e$):** ca. $1.5\,\Omega$ (Nominaal ~2.2 Ohm).
   * **Lineaire Uitslag ($X_{\max}$):** $1.6\text{ mm}$ (enkele slag).
   * **Gewicht Koper:** ca. $3.6\text{ gram}$.
   * **Thermische Belastbaarheid:** ca. $35\text{ Watt RMS}$.

2. **Optie B (Hoge Spoel - Universele 4 Ohm & Hoge $X_{\max}$):**
   * **Wikkelhoogte:** $15.0\text{ mm}$ (100 windingen totaal).
   * **Gelijkstroomweerstand ($R_e$):** ca. $3.1\,\Omega$ (Nominaal ~4.0 Ohm).
   * **Lineaire Uitslag ($X_{\max}$):** $5.5\text{ mm}$ (enkele slag).
   * **Gewicht Koper:** ca. $7.9\text{ gram}$.
   * **Thermische Belastbaarheid:** ca. $75\text{ Watt RMS}$.

---

## 3. Luchtspleet Speling & Toleranties

Met de afgedraaide Top Plate ($\varnothing 41.20\text{ mm}$) en 2-laags $0.30\text{ mm}$ draad ($0.70\text{ mm}$ totale spoeldikte incl. drager):
* **Binnenste Speling (tussen poolkern en drager):** $\mathbf{0.35\text{ mm}}$ (voldoende veilige marge tegen aanlopen bij assemblage).
* **Buitenste Speling (tussen spoel en top plate):** $\mathbf{0.70\text{ mm}}$.

---

## 4. 3D-Geprinte Luidspreker Onderdelen (Productie-instellingen)

### A. Kooi / Korf (Basket / Chassis)
* **Materiaal:** PETG of PLA+ (stijf, stevig en vormvast om de zware $120\text{ mm}$ ferrietmagneet te dragen).
* **Ontwerp:** Open verstevigde spaken (minstens 4-6 spaken) met ruime ventilatieopeningen onder de spider voor luchtdrukverplaatsing en koeling van de spoel.

### B. Conus & Stofkap (Cone & Dust Cap)
* **Materiaal:** **LW-PLA (Lightweight foamed PLA)**.
* **Wanddikte & Printmodus:** **Single-wall / Spiral Vase Mode ($0.40 - 0.50\text{ mm}$ nozzle)**.
* **Vorm:** Exponentieel gekromde trechter voor maximale stijfheid bij een minimale massa ($M_{ms} \approx 3.5 - 4.5\text{ gram}$).

### C. Surround / Soepelrand & Spider / Centreerspin
* **Materiaal:** **TPU Flexibel Filament** (TPU 85A voor extra soepele surround, TPU 90A/95A voor de spider).
* **Wanddikte:** **1-perimeter / single-wall ($0.40\text{ mm}$ nozzle)**.
* **Geometrie Surround:** Halve rol (Half-roll) of M-roll geplooid.
* **Geometrie Spider:** Concentrische rimpels met progressieve stijfheid.

---

## 5. Extra Motor-Features

* **Shorting Ring (Faraday Ring):** Niet verplicht / weggelaten voor de eerste fase van de bouw.
