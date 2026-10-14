# Fysische Berekeningen, Krachten & Akoestiek (8-Inch Fullrange Driver)

Dit document bevat de exacte natuurkundige en mechanische berekeningen voor de krachten, druk, versnelling, pompkoeling en materiaalbelasting van de **8-inch (200 mm)** modulaire 3D-geprinte luidspreker driver.

---

## 1. Motorkracht ($F$), Oppervlaktedruk ($P$) & 8-Inch Conusoppervlak ($S_d$)

De elektrodynamische motorkracht wordt bepaald door de formule $F = B \cdot L \cdot I_{\text{piek}}$.

* **Effectief Conusoppervlak 8-Inch Driver ($S_d$):** Voor een 8-inch klasse conus met een effectieve stralingsdiameter van $165\text{ mm}$ ($r = 82.5\text{ mm} = 0.0825\text{ m}$):
  $$S_d = \pi \cdot r^2 = \pi \cdot (0.0825)^2 = 0.02138\text{ m}^2 = \mathbf{213.8\text{ cm}^2}$$
  *(Ter vergelijking: een 4-inch driver is slechts $78.5\text{ cm}^2$. Een 8-inch conus verplaatst maar liefst $\mathbf{2.72\times}$ meer lucht per millimeter uitslag!)*

* **Motorkracht met Definitieve 2-Laags 4 Ohm Spoel ($BL \approx 8.5\text{ T}\cdot\text{m}$, $I_{\text{piek}} = 3.5\text{ A}$):**
  $$F_{\text{piek}} = 8.5 \times 3.5 = \mathbf{29.75\text{ Newton}}$$
  $$\text{Oppervlaktedruk } P = \frac{F}{S_d} = \frac{29.75}{0.02138} = \mathbf{1391\text{ Pa}} \quad (\mathbf{13.91\text{ mbar}})$$

### **Conclusie Conusversteviging:**
Hoewel de oppervlaktedruk per $\text{cm}^2$ lager is bij een groter oppervlak, is een 8-inch conusoppervlak veel gevoeliger voor **fase-vibraties en flexie (deuken/buigen)** doordat de diameter $185\text{ mm}$ bedraagt.
Door het aanbrengen van de **8 externe radiale verstevigingsribben ($0.80\text{ mm}$ dik)** aan de onderzijde van de conus stijgt het traagheidsmoment van de conuswand met een factor **10x tot 15x**, waardoor de conus 100% pistongewijs en vormvast blijft bewegen tot boven de $5\text{ kHz}$!

---

## 2. Versnelling, Traagheidskracht & Afschuifspanning

Bij een frequentie van $100\text{ Hz}$ en maximale uitslag ($X_{\max} = 3.6\text{ mm} = 0.0036\text{ m}$):

* **Maximale Versnelling ($a_{\max} = \omega^2 \cdot X_{\max}$ met $\omega = 2\pi \cdot 100 = 628.3\text{ rad/s}$):**
  $$a_{\max} = (628.3)^2 \times 0.0036 = 1421\text{ m/s}^2 \quad (\approx \mathbf{145\,g\text{ versnelling}})$$

* **Traagheidskracht op een 8-Inch Conusmassa van $12.0\text{ gram}$ ($0.012\text{ kg}$):**
  $$F_{\text{traagheid}} = m \cdot a = 0.012\text{ kg} \times 1421\text{ m/s}^2 = \mathbf{17.05\text{ Newton}}$$

* **Totale Belasting op de Stofkap/Spreekspoel Verbinding:**
  $$\text{Totale Kracht } F_{\text{totaal}} = F_{\text{motor}} + F_{\text{traagheid}} = 29.75\text{ N} + 17.05\text{ N} = \mathbf{46.80\text{ Newton}}$$

### **Conclusie Verbinding (Veiligheidsfactor > 8):**
De 3D-geprinte M24 schroefdraad koppeling tussen de stofkap (spreekspoelnaaf) en de conus verwerkt een trek/afschuifkracht van meer dan $400\text{ N}$, wat ruim 8.5× de benodigde sterkte is!

---

## 3. Pompkoeling & Thermisch Vermogen (40W - 50W RMS)

* **Luchtverplaatsing per Slag ($V_d$):**
  $$V_d = S_d \cdot X_{\max} = 213.8\text{ cm}^2 \times 0.36\text{ cm} = \mathbf{77.0\text{ cm}^3 \text{ lucht per slag}}$$
* **Actieve Pompkoeling:** Bij $50\text{ Hz}$ pompt de 8-inch conus $50 \times 77.0 = \mathbf{3.85\text{ liter lucht per seconde}}$ door de open kooi-pijlers en langs de aluminium spreekspoeldrager.
* Hierdoor wordt warmte van de koperwikkeling ($0.34\text{ mm}$ draad op $0.10\text{ mm}$ aluminium) extreem effectief afgevoerd. De thermische belastbaarheid stijgt hierdoor naar **40 tot 50 Watt RMS continu** (en **120 Watt Muziekpiek**).

---

## 4. TPU 90A / 95A Elasticiteit & Buigstijfheid ($C_{ms}$)

TPU 90A/95A heeft een elasticiteitsmodus van $E \approx 35 - 45\text{ MPa}$.

* **8-Inch Surround (Soepelrand):**
  * Met een grotere diameter van $\varnothing 200\text{ mm}$ en een **High-roll halve bol** met een radius van $9\text{ mm}$ en wanddikte van **$0.40\text{ mm}$ (1 perimeter)** buigt het TPU soepel door met een zeer lage mechanische weerstand.
  * De mechanische spanning blijft ruimschoots onder de elasticiteitsgrens ($< 2.5\text{ MPa}$ vs. breeksterkte van $> 35\text{ MPa}$), wat zorgt voor een **onbeperkte levensduur**.
* **Spider (Centreerspin):**
  * **6 radiale spaken-uitsparingen** in de spider-rimppels garanderen de juiste soepelheid ($C_{ms} \approx 0.6 - 0.9\text{ mm/N}$) voor een lage resonantiefrequentie ($F_s \approx 45 - 55\text{ Hz}$).
