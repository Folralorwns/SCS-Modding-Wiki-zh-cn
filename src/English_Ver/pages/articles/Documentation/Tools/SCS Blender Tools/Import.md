# Documentation/Tools/SCS Blender Tools/Import

Through import one can import models and other elements which were previously exported to *SCS intermediate-format* data.

All these files uses ***PIX*** file extensions: ***PIM*** files are considered as main files containing model geometries, other extensions are ***PIT*** (trait data), ***PIC*** (colliders data), ***PIP*** (prefab data), ***PIS*** (skeleton data) and ***PIA*** (animation data).

[![SCS_Tools_Import_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Import/SCS_Tools_Import_01.280.png)](../../../../files/SCS%20Tools%20Import%2001.280.png.md)

The import functionality can be found in Blender's import menu as **SCS Game Object (.pim)**, which opens file browser dialog and enables user to import desired SCS Game Object. On the right side of the dialog one can set import options by his desire.

## Import Options

[![SCS_Tools_Import_02.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Import/SCS_Tools_Import_02.280.png)](../../../../files/SCS%20Tools%20Import%2002.280.png.md)

- **SCS Project Base Path** - enables setting proper SCS Project Base Path prior to import with usage of *Set Current Dir as Project Base*. Operator sets currently selected path in file browser as SCS Project Base Path (for more info see: [SCS Project Base Path](Global%20Settings.md#SCS_Project_Base_Path)).
- **Scale** - scale of imported meshes and other elements.
- **Preserve Path for Export** - automatically sets custom export path for imported SCS Game Object, which enables you to easily export it to same place it was imported from.
- **Import Model (PIM)** - you can turn *Model* file loading **ON** and **OFF**.
- **Use Normals** - if this property is ticked, mesh will be imported with normals written in file. Otherwise normals are recalculated by Blender itself.
- **Use Welding** - if this property is ticked, automatic vertex welding operation is performed on all imported meshes. It is sometimes necessary, because mesh geometries in ***PIX*** files are exported in a form, which can be called like "graphics-card-friendly". It means, that vertices are doubled in many cases – on all places where hard edges are, UVs are not continuous, vertex colors are different for neighboring faces, etc. Auto Welding tries to make geometries as compact as possible.
- **Welding Precision** - threshold in decimal numbers to which values has to be the same that welding can take place. So in case of default value 4, values have to match up to for decimals which is in millimetre measurement 0.1 mm.
- **Import Trait (PIT)** - you can turn *Trait* file loading ***ON*** and ***OFF***.
- **Load Textures** - if this property is ticked, all image textures will be loaded.
- **Import Collision (PIC)** - you can turn *Collision* file loading ***ON*** and ***OFF***.
- **Import Prefab (PIP)** - you can turn *Prefab* file loading ***ON*** and ***OFF***.
- **Import Skeleton (PIS)** - you can turn *Skeleton* file loading ***ON*** and ***OFF***.
- **Bone Scale** - here you can specify the size of imported bones. It is usually rather complicated to change their size later.
- **Import Animations (PIA)** - you can turn *Animation files* loading ***ON*** and ***OFF***.
- **Search Subdirectories** - if this property is ticked, all available subdirectories will be searched for animation files.
- **Log Level** - enables setting logging level prior the import.

> > **Note:** Only animation files which belongs to an actual skeleton can be loaded. If they are not placed beside PIX files or any subdirectory, then you can still import animations later from [Animation system#SCS Animations panel](Animation%20system.md#SCS_Animations_panel).

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Import | revision: 4363 | captured: 2026-10-21 23:56:14 -->
