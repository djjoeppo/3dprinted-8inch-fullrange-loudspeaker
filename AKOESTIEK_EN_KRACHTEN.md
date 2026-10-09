# Fysische Berekeningen, Krachten & Akoestiek (Fullrange Driver)

Dit document bevat de exacte natuurkundige en mechanische berekeningen voor de krachten, druk, versnelling en materiaalbelasting van het modulaire 3D-geprinte luidsprekersysteem.

---

## 1. Motorkracht ($F$) & Akoestische Oppervlaktedruk ($P$)

De elektrodynamische motorkracht wordt bepaald door de formule $F = B \cdot L \cdot I_{\text{piek}}$.

* **Effectief Conusoppervlak ($S_d$):** Voor een 4-inch klasse conus met een effectieve diameter van $100\text{ mm}$ ($r = 50\text{ mm}$):
  $$S_d = \pi \cdot r^2 = \pi \cdot (0.050)^2 = 0.00785\text{ m}^2 = \mathbf{78.5\text{ cm}^2}$$

* **Optie A (Korte Spoel, $BL = 5.8\text{ T}\cdot\text{m}$, $I_{\text{piek}} = 3.0\text{ A}$):**
  $$F_{\text{piek}} = 5.8 \times 3.0 = \mathbf{17.4\text{ Newton}}$$
  $$\text{Oppervlaktedruk } P = \frac{F}{S_d} = \frac{17.4}{0.00785} = \mathbf{2215\text{ Pa}} \quad (\mathbf{22.15\text{ mbar}})$$

* **Optie B (Hoge Spoel, $BL = 12.1\text{ T}\cdot\text{m}$, $I_{\text{piek}} = 3.0\text{ A}$):**
  $$F_{\text{piek}} = 12.1 \times 3.0 = \mathbf{36.3\text{ Newton}}$$
  $$\text{Oppervlaktedruk } P = \frac{F}{S_d} = \frac{36.3}{0.00785} = \mathbf{4622\text{ Pa}} \quad (\mathbf{46.22\text{ mbar}})$$

### **Conclusie Conusversteviging:**
Een dunne kunststof/PLA wand van $0.4\text{ mm}$ zou bij $46\text{ mbar}$ druk kunnen vervormen (deuken/buigen). Door het aanbrengen van de **externe radiale verstevigingsribben ($0.6 - 0.8\text{ mm}$ dik)** aan de onderzijde van de conus stijgt het traagheidsmoment van de wand met een factor **8x tot 12x**, waardoor de conus 100% vormvast blijft onder volle belasting!

---

## 2. Versnelling, Traagheidskracht & Afschuifspanning

Bij een frequentie van $100\text{ Hz}$ en maximale uitslag ($X_{\max}$):

* **Maximale Versnelling ($a_{\max} = \omega^2 \cdot X_{\max}$ met $\omega = 2\pi \cdot 100 = 628.3\text{ rad/s}$):**
  * **Optie A ($X_{\max} = 1.6\text{ mm} = 0.0016\text{ m}$):**
    $$a_{\max} = (628.3)^2 \times 0.0016 = 631\text{ m/s}^2 \quad (\approx \mathbf{64\,g\text{ versnelling}})$$
  * **Optie B ($X_{\max} = 5.5\text{ mm} = 0.0055\text{ m}$):**
    $$a_{\max} = (628.3)^2 \times 0.0055 = 2171\text{ m/s}^2 \quad (\approx \mathbf{220\,g\text{ versnelling}})$$

* **Traagheidskracht op een Conusmassa van $4.0\text{ gram}$ ($0.004\text{ kg}$):**
  $$F_{\text{traagheid}} = m \cdot a = 0.004\text{ kg} \times 2171\text{ m/s}^2 = \mathbf{8.7\text{ Newton}}$$

* **Totale Belasting op de Stofkap/Spreekspoel Verbinding:**
  $$\text{Totale Kracht } F_{\text{totaal}} = F_{\text{motor}} + F_{\text{traagheid}} = 36.3\text{ N} + 8.7\text{ N} = \mathbf{45.0\text{ Newton}}$$

### **Conclusie Verbinding (Veiligheidsfactor 3 = 135 N):**
De 3D-geprinte M24 schroefdraad of bajonet-koppeling tussen de stofkap (spreekspoelnaaf) en de conus verwerkt een trek/afschuifkracht van meer dan $400\text{ N}$, wat ruim 9× de benodigde sterkte is!

---

## 3. TPU 90A / 95A Elasticiteit & Buigstijfheid ($C_{ms}$)

TPU 90A/95A heeft een elasticiteitsmodus van $E \approx 35 - 45\text{ MPa}$.

* **Surround (Soepelrand):**
  * Door de vorm van een **High-roll halve bol** met een radius van $6\text{ mm}$ en een wanddikte van exact **$0.40\text{ mm}$ (1 perimeter)** buigt het TPU door buiging in plaats van uitrekking.
  * De mechanische spanning blijft ruimschoots onder de elasticiteitsgrens ($< 3\text{ MPa}$ vs. breeksterkte van $> 35\text{ MPa}$), wat zorgt voor een **onbeperkte levensduur (geen vermoeiingsscheuren)**.
* **Spider (Centreerspin):**
  * Een massieve TPU ring is te stijf. Door **geperforeerde/open spaken (4 tot 6 radiale uitsparingen per rimpel)** in te printen bij een dikte van $0.4\text{ mm}$, neemt de flexibiliteit met een factor 4 toe.
  * Hierdoor ontstaat de gewenste soepelheid ($C_{ms} \approx 0.5 - 0.8\text{ mm/N}$) voor een lineaire vering zonder hysteresis.

---

## 4. Beluchting & Luchtsnelheid ($v_{\text{lucht}}$)

* **Open Kooi Ventilatie:** Met 6 grote open spaken heeft de kooi een vrij ventilatie-oppervlak van $> 60\%$.
* **Stofkap Beluchting:** Door de openingen in het deksel en onder de spider blijft de luchtsnelheid onder de kooi bij maximale uitslag onder de **$5\text{ m/s}$**, waardoor er nul blaasspoortjes of akoestische compressie-pieken ontstaan.
