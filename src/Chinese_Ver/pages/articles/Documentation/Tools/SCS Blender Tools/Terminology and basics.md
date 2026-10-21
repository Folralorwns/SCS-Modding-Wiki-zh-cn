# 文档/工具/SCS Blender Tools/术语与基础

## 术语

### SCS Root Object

它是 Blender 中的“**EMPTY**”对象，并在 SCS Tools 中进行了相应设置。它充当根对象，任何以它为父级的对象都会成为它的内容。它还承载针对整个此类实体的一组设置，这些设置最终可作为“SCS Game Object”导出（参见下文“SCS Game Object”一章）。有关“SCS Root Object”的更多细节，请参见“SCS Root Objects”一章。

### SCS Game Object

这是对单元的统称，它由一个设置正确的“SCS Root Object”及其有效内容组成。如果该实体中的一个或多个组件在导出期间因任何原因被视为无效，控制台会向用户提示，这些项目会被自动跳过。如果所有组件都无效，整个“SCS Game Object”都会被跳过。

### 模型

“模型”一词简单指代任何 **MESH** 类型的 Blender 对象。

### 定位器

我们将任何 **EMPTY** 类型、且在 SCS Blender Tools 中被设为定位器的 Blender 对象称为“定位器”。

[![SCS_Tools_Locators_-_initial_03.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Terminology%20and%20basics/SCS_Tools_Locators_-_initial_03.280.png)](../../../../files/SCS%20Tools%20Locators%20-%20initial%2003.280.png.md)

定位器有三种类型：

1. **模型定位器**（Model Locator）- 可用于放置（引用）游戏中现有的模型。有关模型定位器的详细信息，请参见 [模型定位器](Locators/Model%20Locators.md)。
2. **预制件定位器**（Prefab Locator）- 可用于创建多种类型的特殊项目，供预制件模型使用。有关预制件定位器的详细信息，请参见 [预制件定位器](Locators/Prefab%20Locators.md)。
3. **碰撞定位器**（Collision Locator）- 可用于创建多种类型的碰撞包络，用于游戏中物体的物理交互。有关碰撞定位器的详细信息，请参见 [碰撞定位器](Locators/Collision%20Locators.md)。

## 基本原则

为 SCS 游戏引擎创建和处理模型时，需要牢记一些技巧：

### 部件

场景中的每个对象都分配有一个部件名称。通过这种方式，可以定义能够组成更大单元的对象集合。有关部件的详细信息，请参见 [部件系统](Part%20system.md)。

### 变体

部件必须分配到分组中，这些分组被恰如其分地称为变体。通过创建新的变体并将一些现有部件分配给它，即可轻松为任何 SCS Game Object 创建不同的变化形式。这样，此类模型的每个变体都会被导出，并可在游戏中使用。有关变体的详细信息，请参见 [变体系统](Variant%20system.md)。

### 多模型工作流程

与通常的模型创建方式相比，主要区别在于：所谓的“SCS Game Object”可以在单个场景中无限量地创建。任何“SCS Game Object”都可以由许多独立的模型对象组成，并带有自己的部件列表与变体列表以及一些其他设置。唯一条件是，构成此类“SCS Game Object”的任何内容都必须直接或间接地以“SCS Root Object”为父级。这些 SCS Game Object 可以单独或批量导出到游戏中。

### 材质

要正确设置能在游戏中使用的材质，必须仅使用专用面板“SCS Materials”中包含的设置。如果你使用 Blender 标准的材质面板更改材质属性，材质在 3D 视图中的外观会改变，但 SCS Materials 的设置保持不变。有关材质的详细信息，请参见 [材质](Materials.md)。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Terminology_and_basics | revision: 4271 | captured: 2026-10-21 23:56:14 -->
