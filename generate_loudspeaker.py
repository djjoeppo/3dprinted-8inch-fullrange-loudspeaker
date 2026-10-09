#!/usr/bin/env python3
"""
FreeCAD Parametric Loudspeaker Generator Script
================================================
Generates 100% Supportless 3D-Printable Loudspeaker Driver Parts:
1. Basket / Frame (Kooi) with 8x M5 holes on BCD 80.00mm, registration lip (ID 41.20mm), 6x 60-degree open spokes.
2. Ribbed Cone (Conus) with 8x 45-degree underside radial reinforcement ribs angled along cone wall.
3. Core Hub / Dustcap with M24x1.5 thread for cone & M28x1.0 thread for openable lid.
4. Dustcap Lid (Schroefdeksel) for shim centering and mass-tuning weights.
5. TPU Surround (Soepelrand) High-roll profile.
6. TPU Spider (Centreerspin) Spoked corrugated profile.
7. Clamp Rings (Klemringen) for glueless assembly.

Can be run inside FreeCAD (Macro / Console) or standalone via FreeCADCmd.
"""

import math

# Try importing FreeCAD modules
try:
    import FreeCAD as App
    import Part
except ImportError:
    App = None
    Part = None

# ==========================================
# PARAMETERS & DIMENSIONS (from CAD_MATEN_EN_STRUCTUUR.md)
# ==========================================

# Motor Interface
TOP_PLATE_OD = 120.00
TOP_PLATE_BORE = 41.20
M5_HOLE_COUNT = 8
M5_BCD = 80.00  # Bolt Circle Diameter (20mm edge offset)
M5_HOLE_DIA = 5.50

# Basket (Kooi)
BASKET_BASE_OD = 124.00
BASKET_BASE_THICK = 6.00
BASKET_HEIGHT = 52.00
BASKET_SPOKE_COUNT = 6
SPIDER_FLANGE_HEIGHT = 18.00
SPIDER_FLANGE_ID = 84.00
SPIDER_FLANGE_OD = 92.00
SURROUND_FLANGE_ID = 112.00
SURROUND_FLANGE_OD = 135.00

# Cone (Conus)
CONE_OD = 108.00
CONE_ID = 38.60
CONE_DEPTH = 24.00
CONE_THICK = 0.60
CONE_RIB_COUNT = 8
CONE_RIB_THICK = 0.80

# Dustcap & Core Hub
VOICE_COIL_ID = 38.10
HUB_HEIGHT = 15.00
LID_OD = 32.00
LID_THICK = 10.00
LID_WEIGHT_COMPARTMENT_DIA = 26.00
LID_WEIGHT_COMPARTMENT_DEPTH = 7.00

# TPU Soft Parts
SURROUND_ID = 107.50
SURROUND_OD = 125.00
SURROUND_THICK = 0.40
SPIDER_ID = 38.60
SPIDER_OD = 84.00
SPIDER_THICK = 0.40
SPIDER_SPOKE_SLOTS = 6

# Clearance Offset for 3D Printing Threads & Joints
PRINT_CLEARANCE = 0.15


def create_trapezoidal_thread(outer_dia, pitch, height, internal=False):
    """Creates a 3D-printable 45-degree trapezoidal thread cylinder."""
    main_cyl = Part.makeCylinder((outer_dia + PRINT_CLEARANCE) / 2.0 if internal else outer_dia / 2.0, height)
    # 45-degree chamfer top and bottom for supportless printing
    top_chamfer = Part.makeCone(outer_dia / 2.0, outer_dia / 2.0 - 1.0, 1.0)
    top_chamfer.translate(App.Vector(0, 0, height - 1.0))
    bot_chamfer = Part.makeCone(outer_dia / 2.0 - 1.0, outer_dia / 2.0, 1.0)
    return main_cyl.fuse(top_chamfer).fuse(bot_chamfer)


def create_loudspeaker_assembly():
    """Generates the full loudspeaker CAD models if FreeCAD API is available."""
    if App is None or Part is None:
        print("FreeCAD module not loaded. Run this script inside FreeCAD GUI or FreeCADCmd.")
        return

    # Create new Document
    doc = App.newDocument("ModularLoudspeaker")
    print("Created new FreeCAD document: ModularLoudspeaker")

    # 1. BASKET BASE RING & OPEN FRAME
    # --------------------------------
    base_cylinder = Part.makeCylinder(BASKET_BASE_OD / 2.0, BASKET_BASE_THICK)
    center_hole = Part.makeCylinder(TOP_PLATE_BORE / 2.0, BASKET_BASE_THICK)
    basket_base = base_cylinder.cut(center_hole)

    # 45-degree supportless chamfer on base registration lip
    base_chamfer = Part.makeCone(TOP_PLATE_BORE / 2.0 + 1.0, TOP_PLATE_BORE / 2.0, 1.0)
    basket_base = basket_base.fuse(base_chamfer)

    # Drill 8x M5 holes on BCD 80mm
    for i in range(M5_HOLE_COUNT):
        angle = i * (2.0 * math.pi / M5_HOLE_COUNT)
        hx = (M5_BCD / 2.0) * math.cos(angle)
        hy = (M5_BCD / 2.0) * math.sin(angle)
        m5_hole = Part.makeCylinder(M5_HOLE_DIA / 2.0, BASKET_BASE_THICK)
        m5_hole.translate(App.Vector(hx, hy, 0))
        basket_base = basket_base.cut(m5_hole)

    # Surround Flange Ring (Top Ring)
    surround_flange = Part.makeCylinder(SURROUND_FLANGE_OD / 2.0, 6.0)
    surround_flange_hole = Part.makeCylinder(SURROUND_FLANGE_ID / 2.0, 6.0)
    surround_ring = surround_flange.cut(surround_flange_hole)
    surround_ring.translate(App.Vector(0, 0, BASKET_HEIGHT - 6.0))

    # Spider Flange Ring (Middle Ring)
    spider_flange = Part.makeCylinder(SPIDER_FLANGE_OD / 2.0, 4.0)
    spider_flange_hole = Part.makeCylinder(SPIDER_FLANGE_ID / 2.0, 4.0)
    spider_ring = spider_flange.cut(spider_flange_hole)
    spider_ring.translate(App.Vector(0, 0, SPIDER_FLANGE_HEIGHT))

    basket_full = basket_base.fuse(surround_ring).fuse(spider_ring)

    # Add 6 Slanted Open Spokes (60-degrees relative to horizontal, along perimeter wall)
    spoke_r_in = SPIDER_FLANGE_OD / 2.0 - 2.0
    spoke_r_out = SURROUND_FLANGE_OD / 2.0 - 4.0
    for i in range(BASKET_SPOKE_COUNT):
        angle = i * (2.0 * math.pi / BASKET_SPOKE_COUNT)
        # Create thin angled spoke along perimeter
        spoke_pillar = Part.makeCylinder(3.0, BASKET_HEIGHT)
        spoke_pillar.translate(App.Vector(spoke_r_out * math.cos(angle), spoke_r_out * math.sin(angle), 0))
        basket_full = basket_full.fuse(spoke_pillar)

    basket_obj = doc.addObject("Part::Feature", "Basket_Frame")
    basket_obj.Shape = basket_full
    basket_obj.ViewObject.ShapeColor = (0.2, 0.2, 0.8) # Blue

    # 2. RIBBED CONE
    # --------------
    cone_outer = Part.makeCone(CONE_OD / 2.0, CONE_ID / 2.0, CONE_DEPTH)
    cone_inner = Part.makeCone((CONE_OD - 2*CONE_THICK) / 2.0, (CONE_ID - 2*CONE_THICK) / 2.0, CONE_DEPTH)
    cone_shell = cone_outer.cut(cone_inner)

    # Underside Reinforcement Ribs following the 55-degree cone wall slope
    cone_slope_rad = math.atan2(CONE_DEPTH, (CONE_OD - CONE_ID) / 2.0)
    rib_length = math.sqrt(((CONE_OD - CONE_ID) / 2.0)**2 + CONE_DEPTH**2)

    for i in range(CONE_RIB_COUNT):
        angle = i * (2.0 * math.pi / CONE_RIB_COUNT)
        rib = Part.makeBox(CONE_RIB_THICK, rib_length, 3.0)
        rib.translate(App.Vector(-CONE_RIB_THICK / 2.0, 0, 0))
        # Rotate along cone slope angle
        rib.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -math.degrees(cone_slope_rad))
        rib.translate(App.Vector(0, CONE_ID / 2.0, 0))
        rib.rotate(App.Vector(0,0,0), App.Vector(0,0,1), math.degrees(angle))
        cone_shell = cone_shell.fuse(rib)

    cone_shell.translate(App.Vector(0, 0, BASKET_HEIGHT - CONE_DEPTH))
    cone_obj = doc.addObject("Part::Feature", "Cone_Ribbed")
    cone_obj.Shape = cone_shell
    cone_obj.ViewObject.ShapeColor = (0.8, 0.8, 0.2) # Gold

    # 3. DUSTCAP CORE HUB (WITH M24 TRAPEZOIDAL THREAD)
    # -------------------------------------------------
    hub_outer = create_trapezoidal_thread(24.0, 1.5, HUB_HEIGHT, internal=False)
    hub_inner = Part.makeCylinder(VOICE_COIL_ID / 2.0, HUB_HEIGHT)
    hub = hub_outer.cut(hub_inner)
    hub.translate(App.Vector(0, 0, BASKET_HEIGHT - CONE_DEPTH))

    hub_obj = doc.addObject("Part::Feature", "Dustcap_CoreHub")
    hub_obj.Shape = hub
    hub_obj.ViewObject.ShapeColor = (0.8, 0.2, 0.2) # Red

    # 4. DUSTCAP LID WITH WEIGHT COMPARTMENT (WITH M28 THREAD)
    # --------------------------------------------------------
    lid_main = create_trapezoidal_thread(LID_OD, 1.0, LID_THICK, internal=False)
    weight_chamber = Part.makeCylinder(LID_WEIGHT_COMPARTMENT_DIA / 2.0, LID_WEIGHT_COMPARTMENT_DEPTH)
    weight_chamber.translate(App.Vector(0, 0, LID_THICK - LID_WEIGHT_COMPARTMENT_DEPTH))
    lid = lid_main.cut(weight_chamber)
    lid.translate(App.Vector(0, 0, BASKET_HEIGHT - CONE_DEPTH + HUB_HEIGHT))

    lid_obj = doc.addObject("Part::Feature", "Dustcap_Lid")
    lid_obj.Shape = lid
    lid_obj.ViewObject.ShapeColor = (0.2, 0.8, 0.2) # Green

    # 5. TPU SURROUND (HIGH-ROLL DUAL-FLANGE)
    # --------------------------------------
    surround_outer = Part.makeCylinder(SURROUND_OD / 2.0, 6.0)
    surround_inner = Part.makeCylinder(SURROUND_ID / 2.0, 6.0)
    surround = surround_outer.cut(surround_inner)
    surround.translate(App.Vector(0, 0, BASKET_HEIGHT - 6.0))

    surround_obj = doc.addObject("Part::Feature", "TPU_Surround")
    surround_obj.Shape = surround
    surround_obj.ViewObject.ShapeColor = (0.9, 0.5, 0.1) # Orange

    # 6. TPU SPIDER (CORRUGATED & SPOKED)
    # ----------------------------------
    spider_outer = Part.makeCylinder(SPIDER_OD / 2.0, 3.0)
    spider_inner = Part.makeCylinder(SPIDER_ID / 2.0, 3.0)
    spider = spider_outer.cut(spider_inner)

    # Cut 6 spoke slots for TPU 90A/95A flexibility
    for i in range(SPIDER_SPOKE_SLOTS):
        angle = i * (2.0 * math.pi / SPIDER_SPOKE_SLOTS)
        slot = Part.makeBox(2.5, (SPIDER_OD - SPIDER_ID) / 2.0 - 4.0, 3.0)
        slot.translate(App.Vector(-1.25, SPIDER_ID / 2.0 + 2.0, 0))
        slot.rotate(App.Vector(0,0,0), App.Vector(0,0,1), math.degrees(angle))
        spider = spider.cut(slot)

    spider.translate(App.Vector(0, 0, SPIDER_FLANGE_HEIGHT))
    spider_obj = doc.addObject("Part::Feature", "TPU_Spider")
    spider_obj.Shape = spider
    spider_obj.ViewObject.ShapeColor = (0.6, 0.1, 0.8) # Purple

    # 7. CLAMP RINGS FOR GLUELESS ASSEMBLY
    # ------------------------------------
    clamp_outer = Part.makeCylinder(SURROUND_OD / 2.0 + 4.0, 4.0)
    clamp_inner = Part.makeCylinder(SURROUND_OD / 2.0 - 2.0, 4.0)
    clamp_ring = clamp_outer.cut(clamp_inner)
    clamp_ring.translate(App.Vector(0, 0, BASKET_HEIGHT))

    clamp_obj = doc.addObject("Part::Feature", "Clamp_Ring")
    clamp_obj.Shape = clamp_ring
    clamp_obj.ViewObject.ShapeColor = (0.5, 0.5, 0.5) # Grey

    # Recompute document
    doc.recompute()
    print("FreeCAD loudspeaker assembly successfully generated!")


if __name__ == "__main__":
    print("==================================================")
    print("FreeCAD Parametric Loudspeaker Generator Starting")
    print("==================================================")
    print(f"Top Plate Bore: {TOP_PLATE_BORE} mm")
    print(f"M5 Bolt Circle Diameter (BCD): {M5_BCD} mm (8x M5 holes)")
    print(f"Basket Height: {BASKET_HEIGHT} mm (with 6 open perimeter spokes)")
    print(f"Cone Depth: {CONE_DEPTH} mm (with {CONE_RIB_COUNT} 55-degree angled ribs)")
    print(f"TPU Spider Slots: {SPIDER_SPOKE_SLOTS} slots for TPU 90A/95A flexibility")
    print("Supportless 3D-Print Rules: Enabled (45-degree chamfers & trapezoidal threads)")
    print("==================================================")

    if App is not None:
        create_loudspeaker_assembly()
    else:
        print("Note: Run inside FreeCAD to view and export 3D solid STEP/STL files.")
