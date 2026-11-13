import bpy
import os
import math

def setup_kulityea_scene(variant="orange"):
    """
    Sets up a photorealistic studio product mockup for KulitYea Tea Box in Blender.
    Supports variants: 'orange', 'dragonfruit', 'mangosteen', 'salak'
    """
    # 1. Clear existing objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Base texture directory: check local relative path first, fallback to original path
    script_dir = ""
    if bpy.data.filepath:
        script_dir = os.path.dirname(bpy.data.filepath)
    elif "__file__" in globals():
        script_dir = os.path.dirname(os.path.abspath(__file__))

    local_tex = os.path.join(script_dir, "textures") if script_dir else ""
    if local_tex and os.path.exists(local_tex):
        tex_dir = local_tex
    else:
        tex_dir = r"C:\Users\hamdi\.gemini\antigravity\brain\cbc864da-3ff1-46ed-9d5e-b25bbaf7a7cd\textures"
    
    # 2. Dimensions in meters (Real-world size: 7.5cm x 7.5cm x 13.5cm)
    WIDTH = 0.075
    DEPTH = 0.075
    HEIGHT = 0.135

    # Create Box Mesh centered on ground
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, HEIGHT / 2.0))
    box = bpy.context.active_object
    box.name = f"KulitYea_Box_{variant.capitalize()}"
    box.scale = (WIDTH, DEPTH, HEIGHT)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    # 3. Add Bevel Modifier for realistic paper fold/edge rounding
    bevel = box.modifiers.new(name="PackagingBevel", type='BEVEL')
    bevel.width = 0.0012  # 1.2 mm subtle curve
    bevel.segments = 4
    bevel.limit_method = 'ANGLE'
    bevel.angle_limit = math.radians(30)
    bpy.ops.object.shade_smooth()

    # 4. Helper function to create Principled BSDF Material for each face
    def create_face_material(mat_name, img_filename):
        mat = bpy.data.materials.new(name=mat_name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        nodes.clear()

        # Output node
        out_node = nodes.new(type='ShaderNodeOutputMaterial')
        out_node.location = (400, 0)

        # Principled BSDF
        bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
        bsdf.location = (100, 0)
        # Cardboard paper physical properties
        bsdf.inputs['Roughness'].default_value = 0.42
        if 'Specular IOR Level' in bsdf.inputs:
            bsdf.inputs['Specular IOR Level'].default_value = 0.35
        elif 'Specular' in bsdf.inputs:
            bsdf.inputs['Specular'].default_value = 0.35

        # Image Texture
        img_path = os.path.join(tex_dir, img_filename)
        if os.path.exists(img_path):
            tex_img = nodes.new(type='ShaderNodeTexImage')
            tex_img.location = (-250, 0)
            tex_img.image = bpy.data.images.load(img_path)
            links.new(tex_img.outputs['Color'], bsdf.inputs['Base Color'])
        else:
            # Fallback color
            bsdf.inputs['Base Color'].default_value = (0.95, 0.88, 0.78, 1.0)

        links.new(bsdf.outputs['BSDF'], out_node.inputs['Surface'])
        return mat

    # Create materials for 6 faces
    mat_front = create_face_material(f"Mat_{variant}_Front", f"{variant}_front.png")
    mat_back = create_face_material(f"Mat_{variant}_Back", f"{variant}_back.png")
    mat_right = create_face_material(f"Mat_{variant}_Right", f"{variant}_side_right.png")
    mat_left = create_face_material(f"Mat_{variant}_Left", f"{variant}_side_left.png")
    mat_top = create_face_material(f"Mat_{variant}_Top", f"{variant}_top.png")
    mat_bottom = create_face_material(f"Mat_{variant}_Bottom", f"{variant}_bottom.png")

    # Add materials to box slots
    box.data.materials.append(mat_front)   # slot 0
    box.data.materials.append(mat_back)    # slot 1
    box.data.materials.append(mat_right)   # slot 2
    box.data.materials.append(mat_left)    # slot 3
    box.data.materials.append(mat_top)     # slot 4
    box.data.materials.append(mat_bottom)  # slot 5

    # Assign faces based on surface normals
    for poly in box.data.polygons:
        n = poly.normal
        if n.y < -0.5:     # Front (-Y)
            poly.material_index = 0
        elif n.y > 0.5:    # Back (+Y)
            poly.material_index = 1
        elif n.x > 0.5:    # Right (+X)
            poly.material_index = 2
        elif n.x < -0.5:   # Left (-X)
            poly.material_index = 3
        elif n.z > 0.5:    # Top (+Z)
            poly.material_index = 4
        elif n.z < -0.5:   # Bottom (-Z)
            poly.material_index = 5

    # 5. Add Studio Ground / Curved Backdrop (Cyclorama)
    bpy.ops.mesh.primitive_plane_add(size=3.0, location=(0, 0.4, 0))
    floor = bpy.context.active_object
    floor.name = "Studio_Backdrop"
    floor_mat = bpy.data.materials.new(name="Mat_StudioFloor")
    floor_mat.use_nodes = True
    floor_bsdf = floor_mat.node_tree.nodes.get("Principled BSDF")
    if floor_bsdf:
        floor_bsdf.inputs['Base Color'].default_value = (0.94, 0.94, 0.95, 1.0)
        floor_bsdf.inputs['Roughness'].default_value = 0.25 # subtle satin sheen
    floor.data.materials.append(floor_mat)

    # 6. Studio Lighting Setup (3-Point Lighting)
    # Key Light (Upper Front-Left, soft warm white)
    bpy.ops.object.light_add(type='AREA', location=(-0.35, -0.45, 0.4))
    key_light = bpy.context.active_object
    key_light.name = "Light_Key"
    key_light.data.energy = 45.0
    key_light.data.size = 0.4
    key_light.data.color = (1.0, 0.97, 0.93)
    key_light.rotation_euler = (math.radians(45), math.radians(20), math.radians(-35))

    # Fill Light (Front-Right, softer, cool tint)
    bpy.ops.object.light_add(type='AREA', location=(0.4, -0.35, 0.25))
    fill_light = bpy.context.active_object
    fill_light.name = "Light_Fill"
    fill_light.data.energy = 18.0
    fill_light.data.size = 0.5
    fill_light.data.color = (0.93, 0.96, 1.0)
    fill_light.rotation_euler = (math.radians(50), math.radians(-20), math.radians(40))

    # Rim / Kicker Light (High Back-Right, highlights top & side edge)
    bpy.ops.object.light_add(type='AREA', location=(0.3, 0.35, 0.35))
    rim_light = bpy.context.active_object
    rim_light.name = "Light_Rim"
    rim_light.data.energy = 30.0
    rim_light.data.size = 0.3
    rim_light.data.color = (1.0, 1.0, 1.0)
    rim_light.rotation_euler = (math.radians(-45), math.radians(15), math.radians(135))

    # 7. Studio Product Camera Setup
    bpy.ops.object.camera_add(location=(-0.24, -0.48, 0.26))
    cam = bpy.context.active_object
    cam.name = "Camera_ProductShowcase"
    cam.rotation_euler = (math.radians(68), math.radians(0), math.radians(-26))
    cam.data.lens = 85  # 85mm portrait / product photography lens
    bpy.context.scene.camera = cam

    # 8. Render Engine & Quality settings
    scene = bpy.context.scene
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    
    if hasattr(scene, 'eevee'):
        scene.eevee.use_gtao = True
        scene.eevee.use_bloom = True
        scene.eevee.use_ssr = True

    print(f"KulitYea {variant.capitalize()} 3D Studio Setup Complete!")

if __name__ == "__main__":
    setup_kulityea_scene("orange")
