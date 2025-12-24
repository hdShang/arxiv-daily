---
layout: default
title: "SNOW: Spatio-Temporal Scene Understanding with World Knowledge for Open-World Embodied Reasoning"
---

# SNOW: Spatio-Temporal Scene Understanding with World Knowledge for Open-World Embodied Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16461" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16461v1</a>
  <a href="https://arxiv.org/pdf/2512.16461.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16461v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16461v1', 'SNOW: Spatio-Temporal Scene Understanding with World Knowledge for Open-World Embodied Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tin Stribor Sohn, Maximilian Dillitzer, Jason J. Corso, Eric Sax

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**SNOW：利用世界知识进行时空场景理解，实现开放世界具身推理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时空场景理解` `具身推理` `视觉-语言模型` `点云处理` `4D场景图`

## 📋 核心要点

1. 现有方法在机器人时空场景理解中，要么缺乏语义信息，要么缺乏几何和时间动态的精确建模，限制了其在复杂环境中的应用。
2. SNOW框架通过融合视觉-语言模型的语义知识、点云几何信息和时间一致性，构建统一的4D场景图，为机器人提供更丰富的环境理解。
3. 实验结果表明，SNOW在多个基准测试中取得了最先进的性能，验证了其在具身推理和自主机器人领域的有效性。

## 📝 摘要（中文）

自主机器人系统需要对动态环境进行时空理解，以确保可靠的导航和交互。视觉-语言模型(VLMs)提供了开放世界的语义先验，但缺乏3D几何和时间动态的 grounding。相反，几何感知捕捉了结构和运动，但语义仍然稀疏。我们提出了SNOW（Scene Understanding with Open-World Knowledge），一个无需训练且与骨干网络无关的框架，用于统一的4D场景理解，它集成了VLM衍生的语义与点云几何和时间一致性。SNOW处理同步的RGB图像和3D点云，使用HDBSCAN聚类生成对象级别的提议，指导基于SAM2的分割。每个分割区域通过我们提出的时空Token化Patch编码(STEP)进行编码，产生多模态tokens，捕捉局部语义、几何和时间属性。这些tokens被增量地集成到4D场景图(4DSG)中，作为下游推理的4D先验。轻量级的SLAM后端在环境中空间地锚定所有STEP tokens，提供全局参考对齐，并确保跨时间无歧义的空间grounding。由此产生的4DSG形成了一个可查询的统一世界模型，通过该模型，VLMs可以直接解释空间场景结构和时间动态。在各种基准测试上的实验表明，SNOW能够实现精确的4D场景理解和空间grounding的推理，从而在多个设置中设置了新的最先进的性能，突出了结构化4D先验对于具身推理和自主机器人的重要性。

## 🔬 方法详解

**问题定义**：现有机器人场景理解方法面临的挑战在于如何有效地融合语义信息（例如，物体类别、属性）与几何信息（例如，物体形状、位置）以及时间信息（例如，物体运动轨迹）。视觉-语言模型（VLM）虽然具备强大的语义理解能力，但缺乏对3D几何和时间动态的精确建模。而传统的几何感知方法虽然能够捕捉场景的结构和运动，但语义信息较为稀疏，难以支持复杂的推理任务。

**核心思路**：SNOW的核心思路是将VLM的语义先验知识与点云几何信息和时间一致性相结合，构建一个统一的4D场景图（4DSG）。通过将场景中的物体表示为包含语义、几何和时间属性的多模态tokens，并利用SLAM技术将这些tokens在空间中进行对齐，从而实现对动态环境的全面理解。这种方法能够充分利用VLM的语义推理能力，同时保证场景理解的几何精度和时间一致性。

**技术框架**：SNOW框架主要包含以下几个模块：1) 对象提议生成：利用HDBSCAN聚类算法对点云进行分割，生成对象级别的提议区域。2) 基于SAM2的分割：使用SAM2模型对提议区域进行精确分割，提取每个物体的像素级掩码。3) 时空Token化Patch编码（STEP）：将分割后的物体区域编码为多模态tokens，包含语义、几何和时间属性。4) 4D场景图构建：将STEP tokens增量式地集成到4DSG中，形成一个可查询的统一世界模型。5) SLAM后端：利用SLAM技术将所有STEP tokens在环境中进行空间对齐，提供全局参考坐标系。

**关键创新**：SNOW的关键创新在于提出了时空Token化Patch编码（STEP）方法，能够将分割后的物体区域编码为包含语义、几何和时间属性的多模态tokens。这些tokens不仅包含了VLM的语义信息，还包含了点云的几何信息和时间信息，从而实现了对场景的全面理解。此外，SNOW框架还利用SLAM技术将所有STEP tokens在环境中进行空间对齐，保证了场景理解的几何精度和时间一致性。

**关键设计**：在STEP编码中，论文可能使用了特定的网络结构来提取语义、几何和时间特征，例如，使用Transformer网络来捕捉tokens之间的关系。损失函数的设计可能包括语义一致性损失、几何一致性损失和时间一致性损失，以保证tokens的语义、几何和时间属性的一致性。SLAM后端可能采用了基于图优化的方法，将STEP tokens作为节点，将它们之间的空间关系作为边，通过优化图结构来提高空间对齐的精度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16461v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16461v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16461v1/02_Figures/RoboSpatial_1.jpeg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SNOW在多个基准测试中取得了最先进的性能，证明了其在4D场景理解方面的有效性。具体而言，SNOW在空间grounding的推理任务中表现出色，能够准确地将语义信息与几何信息进行关联。此外，SNOW还能够有效地处理动态环境，对物体的运动轨迹进行精确建模。这些实验结果表明，SNOW框架能够为机器人提供更全面、更精确的环境理解，从而提高其在复杂环境中的适应性和鲁棒性。

## 🎯 应用场景

SNOW框架具有广泛的应用前景，例如，可以应用于自主导航、机器人操作、增强现实和虚拟现实等领域。通过提供精确的4D场景理解，SNOW能够帮助机器人更好地理解周围环境，从而实现更智能的导航和交互。此外，SNOW还可以用于构建虚拟环境，为用户提供更逼真的沉浸式体验。未来，SNOW有望成为机器人和人工智能领域的重要基础设施。

## 📄 摘要（原文）

> Autonomous robotic systems require spatio-temporal understanding of dynamic environments to ensure reliable navigation and interaction. While Vision-Language Models (VLMs) provide open-world semantic priors, they lack grounding in 3D geometry and temporal dynamics. Conversely, geometric perception captures structure and motion but remains semantically sparse. We propose SNOW (Scene Understanding with Open-World Knowledge), a training-free and backbone-agnostic framework for unified 4D scene understanding that integrates VLM-derived semantics with point cloud geometry and temporal consistency. SNOW processes synchronized RGB images and 3D point clouds, using HDBSCAN clustering to generate object-level proposals that guide SAM2-based segmentation. Each segmented region is encoded through our proposed Spatio-Temporal Tokenized Patch Encoding (STEP), producing multimodal tokens that capture localized semantic, geometric, and temporal attributes. These tokens are incrementally integrated into a 4D Scene Graph (4DSG), which serves as 4D prior for downstream reasoning. A lightweight SLAM backend anchors all STEP tokens spatially in the environment, providing the global reference alignment, and ensuring unambiguous spatial grounding across time. The resulting 4DSG forms a queryable, unified world model through which VLMs can directly interpret spatial scene structure and temporal dynamics. Experiments on a diverse set of benchmarks demonstrate that SNOW enables precise 4D scene understanding and spatially grounded inference, thereby setting new state-of-the-art performance in several settings, highlighting the importance of structured 4D priors for embodied reasoning and autonomous robotics.

