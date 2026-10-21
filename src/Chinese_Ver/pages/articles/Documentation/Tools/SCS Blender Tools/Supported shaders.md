# 文档/工具/SCS Blender Tools/支持的着色器

从 1.0 版本开始，Blender Tools 在材质中引入了 flavor。flavor 用于多个着色器共用的通道。每个着色器可启用的 flavor 各不相同。

着色器预设列表现在只包含基础着色器类型，之后可通过开启和关闭不同的 flavor 对其进行调整。因此本页面现在相当于基础着色器类型与 flavor 的说明。

## 基础着色器类型

### building.add.env.day

如果希望建筑窗户在白天产生反射、在夜晚发光，请使用此材质。它大体上应用于远处的“全景”建筑，因为这些建筑不需要 window.day / window.night 的高级特性。

它会根据一天中的时间在两个材质之间切换。白天使用带反射纹理的 dif.spec.add.env 材质，夜晚则切换到 dif.lum.spec，以使窗户在夜间发光。

纹理在需要反射和夜间发光的位置必须具有 alpha 通道。

### building.day

与 building.add.env.day 相同，但不含反射成分。

它会根据一天中的时间在两个材质之间切换。白天使用 dif.spec 材质，其中 alpha 用作高光贴图；夜晚则切换到 dif.lum.spec，以使窗户在夜间发光。

### building.lvcol.day

与 building.day 相同，并额外乘以顶点色。

白天顶点色与高光贴图相乘，夜晚顶点色则与亮度相乘。

### decalshadow

用于透明的静态烘焙阴影。表面颜色由基础纹理乘以材质漫反射颜色和顶点色得到。

而透明度则由顶点色 alpha 与基础纹理 alpha 通道相乘得到。

### dif

这是最基础的着色器之一，具有漫反射与高光，并使用一张纹理。高光直接取自材质中指定的值。

#### 常用 flavor 组合

1. **"dif.a"** - 几何体上纹理 alpha 值为 0 的区域将变为透明。用例：远处建筑上的格栅、栏杆和梯子。
2. **"dif.shadow"** - 将几何体同时用作阴影投射体。此类着色器应仅用于复杂的动画几何体，因为动画计算的开销可能大于直接在高多边形网格上计算阴影。
3. **"dif.shadow.a"** - 是 "dif.shadow" 与 "dif.a" 的组合，意味着将会变为透明的几何体区域同时也不会投射阴影。此着色器可用于栅栏模型，这类模型除了要透明之外还应投射阴影。
4. **"dif.over"** - 此时 alpha 贴图表示材质的透明混合，其中 alpha 值为 0 表示完全透明，alpha 值为 255 表示不透明。

### dif.anim

与 dif 相同，并额外具有在基础纹理与 over 纹理之间随时间混合的行为。

此着色器中的额外辅助设置用于定义动画速度，即纹理切换的快慢。

### dif.lum

与 dif 相同，并额外在 "dif" 着色器的结果与基础纹理 RGB 颜色之间，按基础纹理 alpha 通道作为系数进行线性插值计算。因此该着色器可让表面在夜间发光，发光强度由基础纹理 alpha 通道决定。

该着色器的用例包括 Euro Truck Simulator 2 游戏中卡车内部的仪表盘和 GPS 表面。

#### 常用 flavor 组合

1. **"dif.lum.decal.over"** - 着色器名称中的 decal 部分表示可以使用位于该着色器所作用几何体后方表面的光照模型，over 部分则表示材质的透明混合，其中 alpha 值为 0 表示完全透明，alpha 值为 255 表示不透明。该着色器的用例包括卡车驾驶室中按键上的发光图标，这些图标应：
  - 发光以体现背光效果，
  - 图标周围透明，以便与下方的按键混合，
  - 再次使用下方表面的光照模型，以便在按键表面进行混合。

### dif.lum.spec

与 dif.lum 类似，区别在于表面还像 dif.spec 一样具有额外的高光贴图着色。

### dif.spec

基础着色器，具有漫反射与高光，并使用一张纹理。纹理的 alpha 表示高光强度。

#### 常用 flavor 组合

1. **"dif.spec.a"** - 在纹理 alpha 值为 0 的区域产生透明。
2. **"dif.spec.over"** - 纹理 alpha 通道同样表示材质的透明混合，其中 alpha 值为 0 表示完全透明，alpha 值为 255 表示不透明。
3. **"dif.spec.shadow"** - 将几何体同时用作阴影投射体。此类着色器应仅用于复杂的动画几何体，因为动画计算的开销可能大于直接在高多边形网格上计算阴影。
4. **"dif.spec.shadow.a"** - 启用基于 alpha 通道的阴影计算，意味着将会变为透明的几何体区域同时也不会投射阴影。
5. **"dif.spec.tsnmap.shadow"** - 额外使用定义法线贴图的纹理，并将几何体用作阴影投射体。两张纹理使用同一 UV 层。此类着色器应仅用于复杂的动画几何体，因为动画计算的开销可能大于直接在高多边形网格上计算阴影。

### dif.spec.add.env

与 dif.spec 相同，并额外增加反射通道和纹理。

#### 常用 flavor 组合

1. **"dif.spec.add.env.paint"** - 使用定义文件中定义的额外颜色。基础纹理上的所有区域在游戏内都会与额外颜色相乘。该着色器用于 AI 车辆，或需要用卡车基础色涂装的卡车部件。

### dif.spec.add.env.nofresnel

与 dif.spec.add.env 相同，但不含 fresnel 属性与计算，因此计算开销略低。

### dif.spec.fade.dif.spec

主要用于岩石的着色器，其中一张纹理可同时用作基础纹理和细节纹理。

该着色器在基础纹理与细节纹理之间淡入淡出，前提是细节纹理表示基础纹理的细节（类似于分形）。因此基础纹理与细节纹理应使用同一纹理文件，且该文件必须具有自相似性。

不过混合细节由以下辅助值定义：

- From - 细节纹理开始淡出的位置，以米为单位的 Z 距离表示
- Range - 细节纹理的淡出范围，以米为单位
- Bias - 细节纹理与基础纹理混合的强度
- UV Scale - 细节层的 UV 层缩放系数（由于该着色器对基础层和细节层使用相同纹理，此系数颇为实用：用户可让基础层与细节层共用同一个 UV 层，再由该系数决定细节纹理的 UV 层如何重新缩放）

### dif.spec.mult.dif.spec

与 dif.spec 相同，并多出一张纹理，其颜色和 alpha 会与基础纹理相乘。

在 Euro Truck Simulator 2 中的用例是挂车，其中公司标识纹理与挂车的基础纹理相乘。

#### 常用 flavor 组合

1. **"dif.spec.mult.dif.spec.tsnmap.shadow"** - 除法线贴图外，使用此材质的几何体还将投射阴影。此类着色器应仅用于复杂的动画几何体，因为动画计算的开销可能大于直接在高多边形网格上计算阴影。

### dif.spec.mult.dif.spec.add.env

与 dif.spec.mult.dif.spec 相同，并额外增加反射通道和纹理。

### dif.spec.mult.dif.spec.iamod.dif.spec

基于 dif.spec.mult.dif.spec 的特殊用途着色器，通常用于建筑墙面。

该着色器将两张相乘的不透明纹理与第三张反向顶点 alpha（iamod）纹理组合。第三张纹理应表示贴花/污渍/磨损层，其纹理 alpha 通道与顶点 alpha 控制该贴花作用的强度。顶点色 alpha 值为 0 时作用最强，值为 0.5 时则完全不应用第三层。

### dif.spec.oclu

行为与 dif.spec.mult.dif.spec 类似，但此处的第二张纹理使用灰度图像（仅一个通道），从而获得更好的性能。

该着色器的常见用法相当于使用带有“环境光遮蔽”纹理的 dif.spec。

### dif.spec.oclu.add.env

与 dif.spec.oclu 相同，并额外增加反射通道和纹理。

### dif.spec.over.dif.opac

与 dif.spec 相同，并额外增加遮罩纹理，其颜色按遮罩纹理的 alpha 作为系数与基础纹理颜色混合。

### dif.spec.weight

与 dif.spec 相同，但高光经过修改。

它主要用于道路和沥青，因为这类表面的高光与漫反射属性有其独特表现。

### dif.spec.weight.add.env

与 dif.spec.weight 相同的着色器，并额外增加反射通道和纹理。

### dif.spec.weight.mult2

专为路面创建的特殊着色器，将基础纹理与“涂抹状顶层”结合。涂抹层由相乘纹理表示，并通过两张纹理的 alpha 通道进行混合。

如有可能，应改用简单的 dif.spec.weight 替代此着色器。

### dif.spec.weight.mult2.weight2

在两个 dif.spec.weight.mult2 着色器之间过渡的着色器，用于模拟过渡区域（通常是路肩）。

第一与第二个着色器之间的淡入淡出由顶点色 alpha 完成：值为 0 时仅使用第一层，值为 0.5 时仅使用第二层，介于两者之间的任意值会按比例混合两层。

如有可能，应改用 dif.spec.weight.weight.dif.spec.weight 替代此着色器。

### dif.spec.weight.weight.dif.spec.weight

在两个 dif.spec.weight 着色器之间过渡的着色器，其中第一个着色器的纹理作为基础纹理，第二个着色器的纹理作为 over 纹理。

两者之间的淡入淡出由顶点色 alpha 完成：值为 0 时仅使用基础纹理层，值为 0.5 时仅使用 over 纹理层，介于两者之间的任意值会按比例混合两层。

此外，该着色器还支持次级高光（颜色与光泽度），因此即使高光表现不同的着色器之间也可进行过渡。

在创建带有路肩过渡的道路时，此着色器通常是首选。

### dif.weight.dif

在两个 dif 着色器之间过渡的着色器，其中基础纹理是第一个着色器的纹理，over 纹理是第二个着色器的纹理。

两者之间的淡入淡出由顶点色 alpha 完成：值为 0 时仅使用基础纹理层，值为 0.5 时仅使用 over 纹理层，介于两者之间的任意值会按比例混合两层。

### fakeshadow

使用此材质的几何体用于勾勒车辆轮廓，阴影体积的投射由此开始。由于车轮存在垂直运动，此材质也必须出现在车轮场景中。它必须勾勒出整个车轮的轮廓。

### flare

用于模拟光散射和/或视网膜眩光的着色器。

该着色器的结果是叠加的、不受光照影响的表面：其颜色部分由基础纹理乘以顶点色和材质漫反射属性构成，alpha 部分则由纹理 alpha 通道与顶点色 alpha 相乘构成。

### glass

玻璃材质，使用基础纹理 alpha 作为高光贴图，并受以下色调参数控制：

- Tint - 玻璃颜色
- Tint Opacity - 透明玻璃与不透明玻璃之间的混合系数

应根据玻璃的类型及其用途妥善选择反射纹理。

### grass

用于特殊场合的静态、不运动草地的着色器。

其结果与 dif 相同，透明度由顶点 alpha 色与基础纹理 alpha 通道相乘来控制。

使用此着色器的网格上的法线会被忽略，因为该着色器始终使用朝上的法线，使应用于网格的光照大致与地面一致（假设地面是平的）。

### lamp

用于车灯、辅助灯和交通信号灯的灯具材质。借助第二张遮罩纹理，该材质定义特定灯光点亮时的遮罩区域。

有关灯具的更多信息，请参阅[灯具系统](Materials/Lamp%20system.md)。

#### 常用 flavor 组合

1. **"lamp.add.env"** - 额外增加反射通道和纹理。

### light.tex

光照贴图着色器，通过为下方表面叠加漫反射和高光来充当假光源。此着色器变体的光照贴图始终开启，不区分白天与夜晚。

用例之一是创建从建筑内部灯光投射到地面上的光照贴图。

### lightmap.night

它是 light.tex 的夜晚变体，意味着使用此着色器的表面仅在夜晚可见。白天时此光照贴图将被关闭。

### mlaaweight

使用此着色器的几何体本身不可见，而是会关闭位于其下方、使用此着色器材质的几何体上的 MLAA 处理。

用例之一是在卡车仪表盘上方放置一个使用此着色器材质的简单平面，使显示速度文字、转速文字等的纹理保持锐利。

### none

特殊情况下的空着色器。使用此着色器的表面不会在游戏内绘制，可能仅对测试有用。

### reflective

特殊的叠加表面，用于模拟玩家卡车灯光在反射面上的反应。

此着色器主要用于道路反光板或车辆上的任何反光区域。

### shadowmap

用于透明的静态烘焙阴影。表面颜色由基础纹理乘以材质漫反射颜色得到。阴影贴图的透明度由基础纹理 alpha 通道决定。

### shadowonly

表示阴影投射体材质，用于在几何体上投射太阳阴影。

### sign

用于标志表面的特殊着色器。与 reflective 类似，此着色器模拟与玩家前照灯的交互。

### sky

仅用于天空盒的特殊着色器。基本上，此着色器将三张纹理按 Layer Blend 系数定义的混合方式组合，并在昼夜循环中变化。

### truckpaint

顾名思义，Truckpaint 着色器用于卡车漆色。该着色器将基础纹理与涂装纹理组合。由于该着色器支持不同的输出类型，其最终结果取决于定义文件中卡车涂装的配置。若卡车由玩家驾驶，着色器由该卡车的 "paint job" 定义文件配置；否则卡车涂装由 AI 卡车颜色调色板配置。

#### 涂装模式

此外，材质内的 "aux" 参数仅用于预览目的。它们在 3D 视图中的用法取决于 truckpaint 模式：

1. "Default" 模式（既未使用 "colormask" 也未使用 "airbrush" flavor 时），不带任何额外颜色设置。此处涂装纹理仅用于导出目的，以便为涂装设置正确的 UV 映射。
2. "Color mask" 模式（使用 "colormask" flavor 时），其中涂装纹理的 RGB 通道用于对基础 truckpaint 输出进行颜色遮罩。辅助属性在 3D 视口中的用法如下：
  - Paintjob R Color -> 以涂装纹理的 B 通道进行遮罩的颜色，
  - Paintjob G Color -> 以涂装纹理的 G 通道进行遮罩的颜色，
  - Paintjob B Color -> 以涂装纹理的 R 通道进行遮罩的颜色，
  - Paintjob Base Color -> 基础涂装颜色。
3. "Airbrush" 模式（使用 "airbrush" flavor 时）将涂装纹理用作基础 truckpaint 输出上的喷绘遮罩。辅助属性在 3D 视口中的用法如下：
  - Paintjob Base Color -> 基础涂装颜色。

> > **注意：** 还有另外两种模式 "flipflake" 和 "airbrush.flipflake"，它们尚未在 3D 视口中实现，但仍可在定义文件中定义，因为无需为它们导出额外数据。

#### 常用 flavor 组合

1. **"truckpaint.altuv"** - 为涂装导出备用 UV 层。备用 UV 层必须在涂装纹理中指定。> > **注意：** 不使用此扩展时，备用 UV 将不会被导出，因而无法在涂装定义文件中使用。
2. **"truckpaint.airbrush"** - 将涂装用作喷绘遮罩。涂装纹理按涂装纹理 alpha 通道作为系数与卡车基础漆色相乘。> > **注意：** 可用可不用；只要在定义文件中指定使用此扩展，着色器就会给出相同结果，且该扩展不影响导出的数据。
3. **"truckpaint.airbrush.altuv"** - 组合了 "truckpaint.altuv" 与 "truckpaint.airbrush" 扩展。
4. **"truckpaint.tsnmap"** - 额外使用定义法线贴图的纹理。两张纹理使用同一 UV 层。
5. **"truckpaint.tsnmap.altuv"** - 额外使用定义法线贴图的纹理。两张纹理使用同一 UV 层。除法线贴图外，该着色器还具有 "truckpaint.altuv" 扩展。
6. **"truckpaint.tsnmap.airbrush"** - 额外使用定义法线贴图的纹理。两张纹理使用同一 UV 层。除法线贴图外，该着色器还具有 "truckpaint.airbrush" 扩展。
7. **"truckpaint.tsnmap.airbrush.altuv"** - 额外使用定义法线贴图的纹理。两张纹理使用同一 UV 层。除法线贴图外，该着色器还具有 "truckpaint.altuv" 与 "truckpaint.airbrush" 扩展。
8. **"truckpaint.tsnmapuv"** - 额外使用定义法线贴图的纹理，该纹理使用自己的 UV 层。
9. **"truckpaint.tsnmapuv.altuv"** - 额外使用定义法线贴图的纹理，该纹理使用自己的 UV 层。除法线贴图外，该着色器还具有 "truckpaint.altuv" 扩展。
10. **"truckpaint.tsnmapuv.airbrush"** - 额外使用定义法线贴图的纹理，该纹理使用自己的 UV 层。除法线贴图外，该着色器还具有 "truckpaint.airbrush" 扩展。
11. **"truckpaint.tsnmapuv.airbrush.altuv"** - 额外使用定义法线贴图的纹理，该纹理使用自己的 UV 层。除法线贴图外，该着色器还具有 "truckpaint.altuv" 与 "truckpaint.airbrush" 扩展。

### unlit.tex

在世界光照完成后绘制表面的着色器，意味着使用此着色器的表面将直接以纹理颜色乘以材质漫反射参数输出，不施加任何光照。

### unlit.vcol.tex

与 unlit.tex 类似，并额外乘以顶点色。

至于透明 flavor 组合，此着色器使用顶点色 alpha 与基础纹理 alpha 通道相乘。

#### 常用 flavor 组合

- **"unlit.vcol.tex.a.over"** - 适用于 [Euro Truck Simulator 2](../../../Games.md) 中卡车内部仪表盘的动画指示器，因为 alpha over flavor 组合会在纹理 alpha 通道或顶点色为 0 处产生透明区域。

### water

由两个独立滚动的水波层组成的着色器，并附加环境反射以及近处/地平线水色插值。第一个水波由 layer0 纹理定义，第二个由 layer1 纹理定义。

此外，该着色器还具有许多额外参数：

1. 距离：
  - Near - 插值起点的距离
  - Far - 地平线的距离
  - Scramble - 水面会使反射扭曲，scramble 系数表示扭曲的程度
2. Near Color - 基础水色
3. Horizon Color - 地平线处的水色
4. Layer0 - 第一个水波的设置：
  - Yaw - 水波层朝向，以绕垂直轴逆时针旋转的角度定义
  - Speed - 水波层流动速度，单位为米每秒
  - ScaleX - 水波层纹理生成的 U 方向缩放系数
  - ScaleY - 水波层纹理生成的 V 方向缩放系数
5. Layer1 - 第二个水波的设置：
  - Yaw - 水波层朝向，以绕垂直轴逆时针旋转的角度定义
  - Speed - 水波层流动速度，单位为米每秒
  - ScaleX - 水波层纹理生成的 U 方向缩放系数
  - ScaleY - 水波层纹理生成的 V 方向缩放系数

### window.day

窗户效果的白天变体，旨在用于建筑模型上的窗户内部。此着色器的主要特性是室内映射，它会随视角变化而偏移（玩家会感觉窗户后的室内在移动）。偏移量由基础纹理上的 UV 映射定义。此变体预览的是仅使用基础纹理的白天版本。

由于白天/夜晚变体在游戏内会自动切换，因此使用并导出哪个变体并无实质影响。

### window.night

窗户效果的夜晚变体，旨在用于建筑模型上的窗户内部。此着色器的主要特性是室内映射，它会随视角变化而偏移（玩家会感觉窗户后的室内在移动）。偏移量由基础纹理上的 UV 映射定义。此变体预览的是使用基础纹理与光照贴图相乘的夜晚版本。

由于白天/夜晚变体在游戏内会自动切换，因此使用并导出哪个变体并无实质影响。

## Flavors

### a

该 flavor 在着色器上启用 alpha 测试，意味着不透明度值大于 0 的表面将变为透明。不透明度通常由基础纹理 alpha 通道给出。

### add.env

在着色器上启用额外反射通道的 flavor。这会为着色器添加反射纹理和 environment factor 参数，后者控制环境立方体贴图的类型以及所添加环境光照的量。

### altuv

仅用于 truckpaint 着色器类型的特殊 flavor。它指示着色器为涂装纹理使用第二套 UV 映射。

### airbrush

仅用于 truckpaint 着色器类型的特殊 flavor。它指示着色器应将涂装纹理作为喷绘涂装应用。

有关喷绘涂装行为的更多信息，请参阅：涂装模式

### asafew

用于安全加权 alpha 测试的 flavor，允许基础纹理 alpha 通道同时编码不透明度 [0,32] 和高光贴图 [32,255]。着色器会将 [32,255] 的 alpha 值重映射为 [0, 255] 用于高光贴图。目前支持 dif.spec、dif.spec.weight 和 dif.lum.spec。

> **注意：** 仍必须指定 "a" flavor 才能启用 alpha 测试行为。

用于在高光贴图与压缩后的 asafew 空间之间转换的 Photoshop 曲线预设：[File:Asafew spec remap curves.zip](../../../../files/Asafew%20spec%20remap%20curves.zip.md)

### awhite

仅用于 unlit.vcol.tex 的特殊 flavor，并且只应与乘法混合模式结合使用（参见 #add & over & mult）。

这一特定组合会在基础纹理 alpha 通道为 0 处混合为白色。

### add & over & mult

定义着色器特殊混合模式的 flavor。这三种模式都会切换着色器的透明模式，并将其与下方表面混合：

1. **Add** - 结果为累积缓冲区与使用此混合模式的表面之和，
2. **Over** - 仅将使用此混合模式表面的不透明区域叠加到累积缓冲区之上，
3. **Mult** - 将累积缓冲区与使用此混合模式的表面相乘。

### colormask

仅用于 truckpaint 着色器类型的特殊 flavor。它指示着色器应将涂装纹理作为 colormask 涂装应用。

有关颜色遮罩涂装行为的更多信息，请参阅：涂装模式

### decal

此 flavor 会将使用它的表面标记为在所有其他表面之后绘制。因此，所有使用此 flavor 的着色器都将最后绘制。

此行为在某种程度上类似于普通着色器与带 decal flavor 的着色器之间的 z 深度排序，因此该 flavor 应大体上用于任何使用混合模式的着色器（参见 #add & over & mult）。

### flat

在使用此 flavor 的着色器上移除全局高光与漫反射光照计算的 flavor，从而得到平坦着色的表面，并很可能获得更好的性能。

### indenv

用于 dif.spec.add.env 的特殊 flavor，表示环境反射独立于材质高光颜色。

这使用户也能在高光无法到达的表面上使用反射。在 [Euro Truck Simulator 2](../../../Games.md) 中的用例是反射性内饰中阳光永远照不到的任何部位。

### linv

用于反转 dif.lum.spec 亮度着色器中亮度混合的 flavor。

亮度着色器通常使基础纹理 alpha 通道为 255 的表面发光，而 alpha 值为 0 的表面则不发光。此 flavor 会反转该行为，使 alpha 值为 0 时完全发光、alpha 值为 255 时不发光。

### lvcol

在亮度着色器上启用亮度与顶点色相乘的 flavor：dif.lum 或 dif.lum.spec。

### tsnmap & tsnmap16 & tsnmapuv & tsnmapuv16

为法线贴图添加额外着色器通道的 flavor：

1. **tsnmap** - 为 8 位法线贴图纹理添加额外纹理槽，并使用与基础纹理相同的 UV 映射，
2. **tsnmap16** - 为 16 位法线贴图纹理添加额外纹理槽，并使用与基础纹理相同的 UV 映射，
3. **tsnmapuv** - 为 8 位法线贴图纹理添加额外纹理槽，并使用自己的 UV 映射层，
4. **tsnmapuv16** - 为 16 位法线贴图纹理添加额外纹理槽，并使用自己的 UV 映射层。

### nocull

在 shadowonly 或 fakeshadow 着色器上关闭阴影投射体背面剔除的特殊 flavor。

这基本上意味着阴影投射体将在两侧都投射阴影，而不只是在表面法线所朝的一侧。

### paint

启用使用游戏定义颜色对表面进行额外颜色遮罩的 flavor。

通常用于 AI 车辆的着色器，这些车辆在游戏过程中会被涂成不同颜色。

### shadow

在着色器上启用阴影投射通道的 flavor。

由于已有名为 shadowonly 的独立阴影投射体着色器，此 flavor 应作为例外使用。通常可用于动画模型，因为为额外阴影投射体网格计算动画的开销可能大于直接从 "high" 多边形网格计算阴影投射体。

### tg0

用于自动生成全局纹理映射并将其用于第一个纹理槽的 flavor。启用此 flavor 将忽略已设置的任何 UV 映射，改用自动生成的平面 UV。

此模式通常用于平铺的地形纹理，如草地或沥青。

### tg1

用于自动生成全局纹理映射并将其用于第二个纹理槽的 flavor。启用此 flavor 将忽略已设置的任何 UV 映射，改用自动生成的平面 UV。

此模式通常用于平铺的地形纹理，如草地或沥青。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Supported_shaders | revision: 5676 | captured: 2026-10-21 23:56:14 -->
