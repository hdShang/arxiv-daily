---
layout: default
title: "FloraForge: LLM-Assisted Procedural Generation of Editable and Analysis-Ready 3D Plant Geometric Models For Agricultural Applications"
---

# FloraForge: LLM-Assisted Procedural Generation of Editable and Analysis-Ready 3D Plant Geometric Models For Agricultural Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11925" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11925v1</a>
  <a href="https://arxiv.org/pdf/2512.11925.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11925v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.11925v1', 'FloraForge: LLM-Assisted Procedural Generation of Editable and Analysis-Ready 3D Plant Geometric Models For Agricultural Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mozhgan Hadadi, Talukder Z. Jubery, Patrick S. Schnable, Arti Singh, Bedrich Benes, Adarsh Krishnamurthy, Baskar Ganapathysubramanian

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-11

---

## 💡 一句话要点

**FloraForge：LLM辅助生成可编辑、分析就绪的3D植物几何模型，用于农业应用**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D植物建模` `程序化生成` `大型语言模型` `农业应用` `计算表型分析`

## 📋 核心要点

1. 现有3D植物建模方法依赖大量特定物种数据，或需专业几何建模知识，限制了领域专家的使用。
2. FloraForge利用LLM辅助，通过自然语言迭代优化Python脚本，生成参数化、可编辑的3D植物模型。
3. 该框架生成双重输出：可视化网格和带参数元数据的网格，适用于光模拟、流体动力学等分析。

## 📝 摘要（中文）

精确的3D植物模型对于计算表型分析和基于物理的模拟至关重要；然而，目前的方法面临着显著的局限性。基于学习的重建方法需要大量的物种特定训练数据，并且缺乏可编辑性。程序化建模提供了参数化控制，但需要几何建模方面的专业知识和对复杂程序规则的深入理解，这使得领域科学家难以使用。我们提出了FloraForge，一个LLM辅助的框架，使领域专家能够通过迭代的自然语言植物细化（PR）生成生物学上精确的、完全参数化的3D植物模型，从而最大限度地减少编程专业知识的需求。我们的框架利用LLM支持的协同设计来改进Python脚本，这些脚本生成参数化的植物几何体，作为具有植物约束的分层B样条曲面表示，具有显式控制点和参数化变形函数。这种表示可以很容易地细分为具有任意精度的多边形网格，确保与功能结构植物分析工作流程（如光模拟、计算流体动力学和有限元分析）的兼容性。我们展示了该框架在玉米、大豆和绿豆上的应用，通过手动细化植物描述符（PD）（人类可读的文件）将程序模型拟合到经验点云数据。该流程生成双重输出：用于可视化的三角形网格和带有附加参数元数据的三角形网格，用于定量分析。这种方法独特地结合了LLM辅助的模板创建、实现表型分析和渲染的数学连续表示，以及通过PD进行的直接参数控制。该框架在保持数学严谨性的同时，普及了植物科学的复杂几何建模。

## 🔬 方法详解

**问题定义**：现有3D植物建模方法存在局限性。基于学习的方法需要大量物种特定数据，且模型缺乏可编辑性。程序化建模虽然提供参数化控制，但需要专业的几何建模知识和对复杂规则的理解，使得植物学等领域专家难以应用。因此，如何降低3D植物建模的技术门槛，同时保证模型的生物学准确性和可分析性，是一个亟待解决的问题。

**核心思路**：FloraForge的核心思路是利用大型语言模型（LLM）作为桥梁，连接领域专家和复杂的几何建模过程。通过自然语言的“植物细化”（Plant Refinement, PR），领域专家可以迭代地改进由LLM生成的Python脚本，这些脚本负责生成参数化的3D植物几何模型。这种方式降低了对编程和几何建模专业知识的要求，使得领域专家能够更方便地创建和定制植物模型。

**技术框架**：FloraForge框架包含以下主要阶段：1) **LLM辅助脚本生成**：根据用户提供的植物描述信息，LLM生成初始的Python脚本，该脚本能够创建基本的植物几何模型。2) **自然语言植物细化（PR）**：领域专家使用自然语言描述对模型进行改进，例如调整叶片大小、改变分支角度等。LLM解析这些描述，并相应地修改Python脚本。3) **参数化几何模型生成**：修改后的Python脚本生成参数化的3D植物几何模型，采用分层B样条曲面表示，具有显式控制点和参数化变形函数。4) **模型输出**：生成两种类型的模型：用于可视化的三角形网格，以及带有参数元数据的三角形网格，后者用于后续的定量分析。

**关键创新**：FloraForge的关键创新在于将LLM引入到程序化植物建模流程中，实现了LLM辅助的协同设计。这使得领域专家能够通过自然语言交互来控制复杂的几何建模过程，而无需深入了解编程和几何建模的细节。此外，该框架生成的模型采用参数化的B样条曲面表示，既保证了模型的生物学准确性，又方便进行编辑和分析。

**关键设计**：植物描述符（Plant Descriptor, PD）是框架中的一个关键设计。PD是一个人类可读的文件，包含了植物的各种参数信息，例如叶片形状、分支角度、茎的粗细等。领域专家可以通过修改PD来调整模型的整体形态。此外，框架还采用了植物约束，确保生成的模型在生物学上是合理的。例如，叶片的排列方式、分支的角度等都符合植物生长的规律。

## 📊 实验亮点

该论文在玉米、大豆和绿豆三种植物上验证了FloraForge框架的有效性。通过手动细化植物描述符，将程序模型拟合到经验点云数据。实验结果表明，该框架能够生成生物学上准确、可编辑的3D植物模型，并能输出用于可视化和定量分析的双重模型。

## 🎯 应用场景

FloraForge在农业领域具有广泛的应用前景。它可以用于计算表型分析，帮助研究人员分析植物的生长发育过程，从而筛选优良品种。此外，该框架还可以用于基于物理的模拟，例如光照模拟、计算流体动力学分析等，帮助研究人员优化种植方案，提高作物产量。未来，FloraForge有望成为植物科学研究的重要工具。

## 📄 摘要（原文）

> Accurate 3D plant models are crucial for computational phenotyping and physics-based simulation; however, current approaches face significant limitations. Learning-based reconstruction methods require extensive species-specific training data and lack editability. Procedural modeling offers parametric control but demands specialized expertise in geometric modeling and an in-depth understanding of complex procedural rules, making it inaccessible to domain scientists. We present FloraForge, an LLM-assisted framework that enables domain experts to generate biologically accurate, fully parametric 3D plant models through iterative natural language Plant Refinements (PR), minimizing programming expertise. Our framework leverages LLM-enabled co-design to refine Python scripts that generate parameterized plant geometries as hierarchical B-spline surface representations with botanical constraints with explicit control points and parametric deformation functions. This representation can be easily tessellated into polygonal meshes with arbitrary precision, ensuring compatibility with functional structural plant analysis workflows such as light simulation, computational fluid dynamics, and finite element analysis. We demonstrate the framework on maize, soybean, and mung bean, fitting procedural models to empirical point cloud data through manual refinement of the Plant Descriptor (PD), human-readable files. The pipeline generates dual outputs: triangular meshes for visualization and triangular meshes with additional parametric metadata for quantitative analysis. This approach uniquely combines LLM-assisted template creation, mathematically continuous representations enabling both phenotyping and rendering, and direct parametric control through PD. The framework democratizes sophisticated geometric modeling for plant science while maintaining mathematical rigor.

