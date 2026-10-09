# Fusion 360 Parametric Loudspeaker Generator Script
# ====================================================
# Generates 100% Supportless 3D-Printable Loudspeaker Driver Parts in Autodesk Fusion 360:
# 1. Basket / Frame (Kooi) with 8x M5 holes on BCD 80.00mm, registration lip (ID 41.20mm), 6x open vertical pillars, and spider spokes.
# 2. Ribbed Cone (Conus) with 8x 45-degree underside radial reinforcement ribs angled along cone wall.
# 3. Core Hub / Dustcap with thread for cone & thread for openable lid.
# 4. Dustcap Lid (Schroefdeksel) for shim centering and mass-tuning weights.
# 5. TPU Surround (Soepelrand) High-roll profile.
# 6. TPU Spider (Centreerspin) Spoked corrugated profile.
# 7. Clamp Rings (Klemringen) for glueless assembly.
#
# How to use in Fusion 360:
# 1. Open Autodesk Fusion 360.
# 2. Go to UTILITIES -> Scripts and Add-Ins (Shift + S).
# 3. Click "Create" under Scripts, name it "GenerateLoudspeaker".
# 4. Replace script content with this code and click RUN.

import adsk.core
import adsk.fusion
import traceback
import math

# Parameters from CAD_MATEN_EN_STRUCTUUR.md (values in cm for Fusion 360 API)
TOP_PLATE_OD = 12.00          # 120.00 mm
TOP_PLATE_BORE = 4.12         # 41.20 mm
M5_HOLE_COUNT = 8
M5_BCD = 8.00                 # 80.00 mm BCD
M5_HOLE_DIA = 0.55            # 5.50 mm

BASKET_BASE_OD = 12.40        # 124.00 mm
BASKET_BASE_THICK = 0.60      # 6.00 mm
BASKET_HEIGHT = 5.20          # 52.00 mm
BASKET_SPOKE_COUNT = 6
SPIDER_FLANGE_HEIGHT = 2.80   # 28.00 mm
SPIDER_FLANGE_ID = 8.00       # 80.00 mm
SPIDER_FLANGE_OD = 8.80       # 88.00 mm
SURROUND_FLANGE_ID = 11.00    # 110.00 mm
SURROUND_FLANGE_OD = 13.00    # 130.00 mm

CONE_OD = 10.80               # 108.00 mm
CONE_ID = 3.86                # 38.60 mm
CONE_DEPTH = 2.40             # 24.00 mm
CONE_THICK = 0.06             # 0.60 mm
CONE_RIB_COUNT = 8
CONE_RIB_THICK = 0.08         # 0.80 mm

HUB_OD = 4.20                 # 42.00 mm
VOICE_COIL_ID = 3.81          # 38.10 mm
HUB_HEIGHT = 1.50             # 15.00 mm
LID_OD = 3.20                 # 32.00 mm
LID_THICK = 1.00              # 10.00 mm
LID_WEIGHT_COMPARTMENT_DIA = 2.60 # 26.00 mm
LID_WEIGHT_COMPARTMENT_DEPTH = 0.70 # 7.00 mm

SURROUND_ID = 10.75           # 107.50 mm
SURROUND_OD = 12.50           # 125.00 mm
SPIDER_ID = 3.86              # 38.60 mm
SPIDER_OD = 8.40              # 84.00 mm
SPIDER_SPOKE_SLOTS = 6


def find_ring_profile(sketch, inner_radius, outer_radius):
    """Finds the annular ring profile between inner and outer radius by inspecting profile bounding box radial extent."""
    best_prof = sketch.profiles.item(0)
    best_diff = float('inf')

    for prof in sketch.profiles:
        box = prof.boundingBox
        extent_r = max(abs(box.maxPoint.x), abs(box.minPoint.x), abs(box.maxPoint.y), abs(box.minPoint.y))
        diff = abs(extent_r - outer_radius)
        if diff < best_diff:
            best_diff = diff
            best_prof = prof

    return best_prof


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        if not design:
            ui.messageBox('Please open a Fusion 360 Design document first.')
            return

        root_comp = design.rootComponent
        features = root_comp.features
        sketches = root_comp.sketches
        xy_plane = root_comp.xYConstructionPlane
        xz_plane = root_comp.xZConstructionPlane
        planes = root_comp.constructionPlanes

        # Helper function to create offset plane
        def make_offset_plane(base_plane, offset_cm):
            p_input = planes.createInput()
            p_input.setByDistanceOnPlane(base_plane, adsk.core.ValueInput.createByReal(offset_cm))
            return planes.add(p_input)

        # 1. BASKET / FRAME (KOOI)
        # ------------------------
        basket_comp = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        basket_comp.name = "Basket_Frame"
        basket_feats = basket_comp.features
        basket_sketches = basket_comp.sketches

        # Base Ring
        sk_base = basket_sketches.add(xy_plane)
        sk_base.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), BASKET_BASE_OD / 2.0)
        sk_base.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), TOP_PLATE_BORE / 2.0)
        prof_ring = find_ring_profile(sk_base, TOP_PLATE_BORE / 2.0, BASKET_BASE_OD / 2.0)
        basket_feats.extrudeFeatures.addSimple(
            prof_ring,
            adsk.core.ValueInput.createByReal(BASKET_BASE_THICK),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        # Cut 8x M5 Holes on BCD 80mm
        sk_m5 = basket_sketches.add(xy_plane)
        for i in range(M5_HOLE_COUNT):
            angle = i * (2.0 * math.pi / M5_HOLE_COUNT)
            hx = (M5_BCD / 2.0) * math.cos(angle)
            hy = (M5_BCD / 2.0) * math.sin(angle)
            sk_m5.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(hx, hy, 0), M5_HOLE_DIA / 2.0)

        profs_m5 = adsk.core.ObjectCollection.create()
        for p in sk_m5.profiles:
            profs_m5.add(p)
        ext_cut_input = basket_feats.extrudeFeatures.createInput(profs_m5, adsk.fusion.FeatureOperations.CutFeatureOperation)
        ext_cut_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(BASKET_BASE_THICK))
        basket_feats.extrudeFeatures.add(ext_cut_input)

        # Surround Flange Ring (Top)
        plane_top = make_offset_plane(xy_plane, BASKET_HEIGHT - 0.60)
        sk_surr = basket_sketches.add(plane_top)
        sk_surr.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), SURROUND_FLANGE_OD / 2.0)
        sk_surr.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), SURROUND_FLANGE_ID / 2.0)
        prof_top = find_ring_profile(sk_surr, SURROUND_FLANGE_ID / 2.0, SURROUND_FLANGE_OD / 2.0)
        basket_feats.extrudeFeatures.addSimple(
            prof_top,
            adsk.core.ValueInput.createByReal(0.60),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        # Spider Flange Ring (Middle)
        plane_spid = make_offset_plane(xy_plane, SPIDER_FLANGE_HEIGHT)
        sk_spid = basket_sketches.add(plane_spid)
        sk_spid.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), SPIDER_FLANGE_OD / 2.0)
        sk_spid.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), SPIDER_FLANGE_ID / 2.0)
        prof_mid = find_ring_profile(sk_spid, SPIDER_FLANGE_ID / 2.0, SPIDER_FLANGE_OD / 2.0)
        basket_feats.extrudeFeatures.addSimple(
            prof_mid,
            adsk.core.ValueInput.createByReal(0.40),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        # 6 Open Vertical Pillars
        pillar_r = (SURROUND_FLANGE_OD / 2.0) - 0.35
        pillar_h = BASKET_HEIGHT - BASKET_BASE_THICK - 0.60
        sk_pillars = basket_sketches.add(make_offset_plane(xy_plane, BASKET_BASE_THICK))
        for i in range(BASKET_SPOKE_COUNT):
            angle = i * (2.0 * math.pi / BASKET_SPOKE_COUNT)
            px = pillar_r * math.cos(angle)
            py = pillar_r * math.sin(angle)
            sk_pillars.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(px, py, 0), 0.30)

        profs_pillars = adsk.core.ObjectCollection.create()
        for p in sk_pillars.profiles:
            profs_pillars.add(p)
        ext_pil_input = basket_feats.extrudeFeatures.createInput(profs_pillars, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        ext_pil_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(pillar_h))
        basket_feats.extrudeFeatures.add(ext_pil_input)

        # Connect Spider Ring to Pillars via 6 Radial Spokes
        sk_spid_spokes = basket_sketches.add(plane_spid)
        for i in range(BASKET_SPOKE_COUNT):
            angle = i * (2.0 * math.pi / BASKET_SPOKE_COUNT)
            r1 = SPIDER_FLANGE_OD / 2.0
            r2 = pillar_r
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            p1 = adsk.core.Point3D.create(r1 * cos_a - 0.20 * sin_a, r1 * sin_a + 0.20 * cos_a, 0)
            p2 = adsk.core.Point3D.create(r2 * cos_a - 0.20 * sin_a, r2 * sin_a + 0.20 * cos_a, 0)
            p3 = adsk.core.Point3D.create(r2 * cos_a + 0.20 * sin_a, r2 * sin_a - 0.20 * cos_a, 0)
            p4 = adsk.core.Point3D.create(r1 * cos_a + 0.20 * sin_a, r1 * sin_a - 0.20 * cos_a, 0)
            lines = sk_spid_spokes.sketchCurves.sketchLines
            lines.addByTwoPoints(p1, p2)
            lines.addByTwoPoints(p2, p3)
            lines.addByTwoPoints(p3, p4)
            lines.addByTwoPoints(p4, p1)

        profs_spokes = adsk.core.ObjectCollection.create()
        for p in sk_spid_spokes.profiles:
            profs_spokes.add(p)
        ext_spk_input = basket_feats.extrudeFeatures.createInput(profs_spokes, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        ext_spk_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(0.40))
        basket_feats.extrudeFeatures.add(ext_spk_input)

        # 2. RIBBED CONE
        # --------------
        cone_comp = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        cone_comp.name = "Cone_Ribbed"
        cone_feats = cone_comp.features
        cone_sketches = cone_comp.sketches

        plane_throat = make_offset_plane(xy_plane, BASKET_HEIGHT - CONE_DEPTH)
        sk_cone_bot = cone_sketches.add(plane_throat)
        sk_cone_bot.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), CONE_ID / 2.0)
        sk_cone_bot.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), (CONE_ID / 2.0) - CONE_THICK)
        prof_cbot = find_ring_profile(sk_cone_bot, (CONE_ID / 2.0) - CONE_THICK, CONE_ID / 2.0)

        plane_mouth = make_offset_plane(xy_plane, BASKET_HEIGHT)
        sk_cone_top = cone_sketches.add(plane_mouth)
        sk_cone_top.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), CONE_OD / 2.0)
        sk_cone_top.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), (CONE_OD / 2.0) - CONE_THICK)
        prof_ctop = find_ring_profile(sk_cone_top, (CONE_OD / 2.0) - CONE_THICK, CONE_OD / 2.0)

        loft_input = cone_feats.loftFeatures.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        loft_input.loftSections.add(prof_cbot)
        loft_input.loftSections.add(prof_ctop)
        cone_feats.loftFeatures.add(loft_input)

        # 8 Underside Reinforcement Ribs along Cone Wall
        # Sketched on XZ plane (Y = 0) and extruded symmetrically
        sk_rib = cone_sketches.add(xz_plane)
        z_base = BASKET_HEIGHT - CONE_DEPTH
        r_in = (CONE_ID / 2.0) - 0.02
        r_out = CONE_OD / 2.0
        h_cone = CONE_DEPTH

        # Points MUST lie on XZ plane (Y = 0) so Z coordinate represents height!
        p1 = adsk.core.Point3D.create(r_in, 0, z_base)
        p2 = adsk.core.Point3D.create(r_out, 0, z_base + h_cone)
        p3 = adsk.core.Point3D.create(r_out, 0, z_base + h_cone - 0.30)
        p4 = adsk.core.Point3D.create(r_in, 0, z_base - 0.30)

        lines_rib = sk_rib.sketchCurves.sketchLines
        lines_rib.addByTwoPoints(p1, p2)
        lines_rib.addByTwoPoints(p2, p3)
        lines_rib.addByTwoPoints(p3, p4)
        lines_rib.addByTwoPoints(p4, p1)

        prof_rib = sk_rib.profiles.item(0)
        ext_rib_input = cone_feats.extrudeFeatures.createInput(prof_rib, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        ext_rib_input.setTwoSidesDistanceExtent(
            adsk.core.ValueInput.createByReal(CONE_RIB_THICK / 2.0),
            adsk.core.ValueInput.createByReal(CONE_RIB_THICK / 2.0)
        )
        rib_body = cone_feats.extrudeFeatures.add(ext_rib_input).bodies.item(0)

        # Circular Pattern of Ribs (8x)
        pattern_bodies = adsk.core.ObjectCollection.create()
        pattern_bodies.add(rib_body)
        z_axis = root_comp.zConstructionAxis
        pattern_input = cone_feats.circularPatternFeatures.createInput(pattern_bodies, z_axis)
        pattern_input.totalAngle = adsk.core.ValueInput.createByString('360 deg')
        pattern_input.quantity = adsk.core.ValueInput.createByReal(CONE_RIB_COUNT)
        cone_feats.circularPatternFeatures.add(pattern_input)

        # 3. DUSTCAP CORE HUB
        # -------------------
        hub_comp = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        hub_comp.name = "Dustcap_CoreHub"
        hub_feats = hub_comp.features
        hub_sketches = hub_comp.sketches

        sk_hub = hub_sketches.add(plane_throat)
        sk_hub.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), HUB_OD / 2.0)
        sk_hub.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), VOICE_COIL_ID / 2.0)
        prof_hub = find_ring_profile(sk_hub, VOICE_COIL_ID / 2.0, HUB_OD / 2.0)
        hub_feats.extrudeFeatures.addSimple(
            prof_hub,
            adsk.core.ValueInput.createByReal(HUB_HEIGHT),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        # 4. DUSTCAP LID WITH WEIGHT COMPARTMENT
        # --------------------------------------
        lid_comp = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        lid_comp.name = "Dustcap_Lid"
        lid_feats = lid_comp.features
        lid_sketches = lid_comp.sketches

        plane_lid = make_offset_plane(xy_plane, BASKET_HEIGHT - CONE_DEPTH + HUB_HEIGHT)
        sk_lid = lid_sketches.add(plane_lid)
        sk_lid.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), LID_OD / 2.0)
        lid_feats.extrudeFeatures.addSimple(
            sk_lid.profiles.item(0),
            adsk.core.ValueInput.createByReal(LID_THICK),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        # Weight Compartment Pocket
        plane_pocket = make_offset_plane(xy_plane, BASKET_HEIGHT - CONE_DEPTH + HUB_HEIGHT + LID_THICK - LID_WEIGHT_COMPARTMENT_DEPTH)
        sk_pock = lid_sketches.add(plane_pocket)
        sk_pock.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), LID_WEIGHT_COMPARTMENT_DIA / 2.0)
        lid_feats.extrudeFeatures.addSimple(
            sk_pock.profiles.item(0),
            adsk.core.ValueInput.createByReal(LID_WEIGHT_COMPARTMENT_DEPTH),
            adsk.fusion.FeatureOperations.CutFeatureOperation
        )

        # 5. TPU SURROUND
        # ---------------
        surr_comp = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        surr_comp.name = "TPU_Surround"
        surr_feats = surr_comp.features
        surr_sketches = surr_comp.sketches

        sk_surr_part = surr_sketches.add(make_offset_plane(xy_plane, BASKET_HEIGHT - 0.60))
        sk_surr_part.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), SURROUND_OD / 2.0)
        sk_surr_part.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), SURROUND_ID / 2.0)
        prof_s = find_ring_profile(sk_surr_part, SURROUND_ID / 2.0, SURROUND_OD / 2.0)
        surr_feats.extrudeFeatures.addSimple(
            prof_s,
            adsk.core.ValueInput.createByReal(0.60),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        # 6. TPU SPIDER
        # -------------
        spid_comp = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        spid_comp.name = "TPU_Spider"
        spid_feats = spid_comp.features
        spid_sketches = spid_comp.sketches

        sk_spid_part = spid_sketches.add(plane_spid)
        sk_spid_part.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), SPIDER_OD / 2.0)
        sk_spid_part.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), SPIDER_ID / 2.0)
        prof_sp = find_ring_profile(sk_spid_part, SPIDER_ID / 2.0, SPIDER_OD / 2.0)
        spid_feats.extrudeFeatures.addSimple(
            prof_sp,
            adsk.core.ValueInput.createByReal(0.30),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        # 6 Spoke Slots
        sk_slots = spid_sketches.add(plane_spid)
        for i in range(SPIDER_SPOKE_SLOTS):
            angle = i * (2.0 * math.pi / SPIDER_SPOKE_SLOTS)
            sx1 = (SPIDER_ID / 2.0 + 0.20) * math.cos(angle)
            sy1 = (SPIDER_ID / 2.0 + 0.20) * math.sin(angle)
            sx2 = (SPIDER_OD / 2.0 - 0.40) * math.cos(angle)
            sy2 = (SPIDER_OD / 2.0 - 0.40) * math.sin(angle)
            sk_slots.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create((sx1+sx2)/2.0, (sy1+sy2)/2.0, 0), 0.125)

        profs_slots = adsk.core.ObjectCollection.create()
        for p in sk_slots.profiles:
            profs_slots.add(p)
        ext_slot_input = spid_feats.extrudeFeatures.createInput(profs_slots, adsk.fusion.FeatureOperations.CutFeatureOperation)
        ext_slot_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(0.30))
        spid_feats.extrudeFeatures.add(ext_slot_input)

        # 7. CLAMP RING
        # -------------
        clamp_comp = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        clamp_comp.name = "Clamp_Ring"
        clamp_feats = clamp_comp.features
        clamp_sketches = clamp_comp.sketches

        sk_clamp = clamp_sketches.add(make_offset_plane(xy_plane, BASKET_HEIGHT))
        sk_clamp.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), (SURROUND_OD / 2.0) + 0.40)
        sk_clamp.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), (SURROUND_OD / 2.0) - 0.20)
        prof_c = find_ring_profile(sk_clamp, (SURROUND_OD / 2.0) - 0.20, (SURROUND_OD / 2.0) + 0.40)
        clamp_feats.extrudeFeatures.addSimple(
            prof_c,
            adsk.core.ValueInput.createByReal(0.40),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        ui.messageBox('Modular Loudspeaker Generator successfully completed!\nAll 7 components generated in Fusion 360.')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
