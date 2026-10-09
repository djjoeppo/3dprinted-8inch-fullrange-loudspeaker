# Modulair & Lijmloos 3D-Geprint Luidspreker Ontwerp

Dit document bevat de volledige mechanische specificaties voor het modulair, klikbaar, schroefbaar en demontabel 3D-geprint luidsprekerchassis en conussysteem.

---

## 1. Kooi / Korf (Basket) & Top Plate Montage

* **Materiaal:** PLA, PLA+ of ABS.
* **Montage op Motor:** Geschroefd op de stalen top plate met M3/M4 bouten via verzonken gaten in de onderring van de kooi.
* **Positionering & Registratie:**
  * Gebruik van **paspennetjes (alignment pins / dowel pins)** of ingeprinte positionerings-nokken op de top plate interface.
  * Hierdoor kan de kooi keer op keer **100% exact op dezelfde positie** gemonteerd en gedemonteerd worden voor perfecte centrering van de spreekspoel.
* **Demontabele Ophangpunten:**
  * De buitenrand van de spider en de buitenrand van de surround worden geklemd met **geschroefde klemringen (screw rings)** voorzien van M3 boutjes of een bayonet/schroefdraad kliksysteem.

---

## 2. Modulaire Conus, Stofkap & Spreekspoel

* **Conus Constructie:**
  * **Materiaal:** PLA of ABS.
  * **Versteviging:** Buitenzijde voorzien van **3D-geprinte radiale verstevigingsribben** (0.6 - 0.8 mm dik) die van het midden naar de buitenrand lopen voor extreme buigstijfheid.
* **Uitneembare Stofkap & Spreekspoel-unit:**
  * De spreekspoel met aluminium drager is vast gemonteerd op de **uitneembare stofkap (core hub / dustcap unit)**.
  * De stofkap sluit op de conus aan via een **press-fit bayonet/schroefdraad of klik-systeem** met een O-ring of klempassing.
  * **Voordeel:** Je kunt de spreekspoel/stofkap loskoppelen van de conus zonder de hele driver te slopen!

---

## 3. Demontabele Koppeling van Spider & Surround (Lijmloos)

Om verschillende soorten en vormen spiders en surrounds te testen zonder te lijmen:

* **Conus <-> Surround Koppeling (Buitenrand Conus):**
  * De conusrand is voorzien van een **klemgroef of een 2-delige schroefring-flens**.
  * De TPU surround heeft een dikkere binnen- en buiten-kraag (bead) die in de groef geklemd/geschroefd wordt.
* **Conus <-> Spider Koppeling (Binnenrand Conus):**
  * De onderzijde van de conus heeft een **kraag met M2.5/M3 schroefdraad of een borgring**.
  * De TPU spider heeft een verstevigde hart-ring die op de conuskraag geklemd wordt met een schroefsluiting.

---

## 4. TPU 90A / 95A Flexibele Onderdelen (Spider & Surround)

Aangezien **TPU 90A/95A** vrij stijf is, wordt de gewenste flexibiliteit ($C_{ms}$) bereikt door slimme **geometrische sturing**:

* **TPU Surround (Soepelrand):**
  * **Wanddikte:** Exact **1 perimeter ($0.40\text{ mm}$ nozzle)**.
  * **Geometrie:** Hoge, slanke halve rol (High-roll) of dubbele M-roll. Door de dunne $0.4\text{ mm}$ enkele wand buigt TPU 90A uiterst soepel, terwijl het scheurvast en duurzaam blijft.
* **TPU Spider (Centreerspin):**
  * **Wanddikte:** **1 tot 2 perimeters ($0.40 - 0.60\text{ mm}$)** met uitgespaarde spaken of diepe concentrische golven.
  * **Geometrie:** Geometrische uitsparingen (geperforeerde/open spaken-spider) om de mechanische stijfheid bij TPU 95A precies op de juiste veerconstante af te stemmen.

---

## 5. Overzicht van de Demontabele Assemblage (Exploded View Concept)

1. **Top Plate** (stalen motor met afgedraaide $\varnothing 41.20\text{ mm}$ spleet).
2. **Basket Base Ring** (geschroefd op top plate met paspennen).
3. **Spider Lower Clamp Ring** (schroeft spider vast aan basket).
4. **TPU Spider** (geklemd op basket-ring en geklemd aan conus-basis).
5. **Conus** (met externe ribben en klemflenzen).
6. **TPU Surround** (geklemd op conus-buitenrand en geklemd op basket-bovenring).
7. **Basket Top Ring** (schroeft surround vast aan basket).
8. **Stofkap + Spreekspoel Unit** (klikt/schroeft in het midden van de conus).
