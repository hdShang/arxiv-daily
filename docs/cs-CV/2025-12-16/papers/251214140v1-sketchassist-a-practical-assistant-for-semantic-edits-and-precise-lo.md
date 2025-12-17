---
layout: default
title: SketchAssist: A Practical Assistant for Semantic Edits and Precise Local Redrawing
---

# SketchAssist: A Practical Assistant for Semantic Edits and Precise Local Redrawing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14140" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14140v1</a>
  <a href="https://arxiv.org/pdf/2512.14140.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14140v1" onclick="toggleFavorite(this, '2512.14140v1', 'SketchAssist: A Practical Assistant for Semantic Edits and Precise Local Redrawing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Han Zou, Yan Zhang, Ruiqi Yu, Cong Xie, Jie Huang, Zhenpeng Zhan

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**SketchAssist：用于语义编辑和精确局部重绘的实用草图辅助工具**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `草图编辑` `语义编辑` `局部重绘` `可控生成` `混合专家`

## 📋 核心要点

1. 现有图像编辑系统难以兼顾草图线条艺术的风格结构，同时支持高级语义修改和精确局部重绘。
2. SketchAssist通过统一指令引导的全局编辑和线条引导的局部重绘，在保持整体构图的同时，加速草图创作。
3. 实验表明，SketchAssist在指令遵循和风格/结构保持方面优于现有方法，为草图编辑提供实用助手。

## 📝 摘要（中文）

草图编辑是数字插图的核心，但现有的图像编辑系统难以在支持高级语义更改和精确局部重绘的同时，保持线条艺术的稀疏、风格敏感的结构。我们提出了SketchAssist，一个交互式草图绘制助手，通过统一指令引导的全局编辑和线条引导的区域重绘来加速创作，同时保持不相关的区域和整体构图完整。为了大规模地实现这个助手，我们引入了一个可控的数据生成流程，该流程（i）从无属性的基础草图构建属性添加序列，（ii）通过跨序列采样形成多步编辑链，以及（iii）通过应用于各种草图的风格保持属性移除模型来扩展风格覆盖。基于这些数据，SketchAssist采用了一个统一的草图编辑框架，对基于DiT的编辑器进行了最小的更改。我们重新利用RGB通道来编码输入，从而可以在单个输入界面中无缝切换指令引导的编辑和线条引导的重绘。为了进一步专门化跨模式的行为，我们将任务引导的混合专家集成到LoRA层中，通过文本和视觉线索进行路由，以提高语义可控性、结构保真度和风格保持。大量的实验表明，在两项任务上都取得了最先进的结果，与最近的基线相比，具有卓越的指令遵循和风格/结构保持能力。我们的数据集和SketchAssist共同为草图创建和修改提供了一个实用、可控的助手。

## 🔬 方法详解

**问题定义**：现有图像编辑系统在处理草图时，难以同时满足高层次的语义编辑需求和精细的局部重绘需求，并且容易破坏草图原有的风格和结构。这限制了数字插画创作的效率和质量。

**核心思路**：SketchAssist的核心思路是将指令引导的全局语义编辑与线条引导的局部重绘相结合，通过统一的框架实现对草图的精确控制。通过可控的数据生成流程和任务引导的混合专家模型，提升语义可控性、结构保真度和风格保持能力。

**技术框架**：SketchAssist的整体框架包含三个主要部分：可控数据生成流程、统一的草图编辑框架和任务引导的混合专家模型。数据生成流程用于构建训练数据，编辑框架基于DiT模型实现全局和局部编辑，混合专家模型用于专门化不同编辑模式的行为。

**关键创新**：SketchAssist的关键创新在于：1) 统一了指令引导的全局编辑和线条引导的局部重绘，实现了对草图的精细控制。2) 提出了可控的数据生成流程，能够生成高质量的训练数据。3) 引入了任务引导的混合专家模型，提升了语义可控性、结构保真度和风格保持能力。

**关键设计**：SketchAssist的关键设计包括：1) 使用RGB通道编码输入，实现指令引导和线条引导的无缝切换。2) 将任务引导的混合专家模型集成到LoRA层中，通过文本和视觉线索进行路由。3) 数据生成流程中，使用风格保持属性移除模型来扩展风格覆盖。

## 📊 实验亮点

实验结果表明，SketchAssist在指令遵循和风格/结构保持方面均优于现有方法。具体而言，SketchAssist能够更好地根据文本指令修改草图的语义内容，同时保持草图原有的风格和结构特征。该方法在两项任务上都取得了最先进的结果。

## 🎯 应用场景

SketchAssist可应用于数字绘画、游戏美术设计、动漫制作等领域，能够显著提升草图创作和修改的效率，降低创作门槛。该研究的成果有助于推动人机协作的艺术创作模式，并为未来的图像编辑工具提供新的思路。

## 📄 摘要（原文）

> Sketch editing is central to digital illustration, yet existing image editing systems struggle to preserve the sparse, style-sensitive structure of line art while supporting both high-level semantic changes and precise local redrawing. We present SketchAssist, an interactive sketch drawing assistant that accelerates creation by unifying instruction-guided global edits with line-guided region redrawing, while keeping unrelated regions and overall composition intact. To enable this assistant at scale, we introduce a controllable data generation pipeline that (i) constructs attribute-addition sequences from attribute-free base sketches, (ii) forms multi-step edit chains via cross-sequence sampling, and (iii) expands stylistic coverage with a style-preserving attribute-removal model applied to diverse sketches. Building on this data, SketchAssist employs a unified sketch editing framework with minimal changes to DiT-based editors. We repurpose the RGB channels to encode the inputs, enabling seamless switching between instruction-guided edits and line-guided redrawing within a single input interface. To further specialize behavior across modes, we integrate a task-guided mixture-of-experts into LoRA layers, routing by text and visual cues to improve semantic controllability, structural fidelity, and style preservation. Extensive experiments show state-of-the-art results on both tasks, with superior instruction adherence and style/structure preservation compared to recent baselines. Together, our dataset and SketchAssist provide a practical, controllable assistant for sketch creation and revision.

