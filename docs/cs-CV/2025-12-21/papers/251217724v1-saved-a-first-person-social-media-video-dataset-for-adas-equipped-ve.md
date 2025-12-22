---
layout: default
title: SAVeD: A First-Person Social Media Video Dataset for ADAS-equipped vehicle Near-Miss and Crash Event Analyses
---

# SAVeD: A First-Person Social Media Video Dataset for ADAS-equipped vehicle Near-Miss and Crash Event Analyses

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17724" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17724v1</a>
  <a href="https://arxiv.org/pdf/2512.17724.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17724v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17724v1', 'SAVeD: A First-Person Social Media Video Dataset for ADAS-equipped vehicle Near-Miss and Crash Event Analyses')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaoyan Zhai, Mohamed Abdel-Aty, Chenzhu Wang, Rodrigo Vena Garcia

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**SAVeD：用于ADAS车辆近失和碰撞事件分析的第一人称社交媒体视频数据集**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `ADAS` `数据集` `近失事件` `碰撞分析` `社交媒体视频` `深度估计` `风险建模`

## 📋 核心要点

1. 现有ADAS车辆驾驶行为研究缺乏真实风险场景数据，现有数据集多为模拟环境或人类驾驶数据。
2. SAVeD数据集通过收集社交媒体视频，提供包含碰撞、近失和脱离等高风险场景的真实ADAS车辆数据。
3. 实验证明，SAVeD数据集能够有效提升VLLM在复杂近失场景中的性能，并为风险建模提供支持。

## 📝 摘要（中文）

本文提出了SAVeD，一个大规模视频数据集，专门用于配备ADAS车辆的碰撞、近失事件和脱离场景分析，数据来源于公开的社交媒体内容。SAVeD包含2119个第一人称视角视频，捕捉了ADAS车辆在不同地点、光照和天气条件下的运行情况。数据集包含碰撞、规避动作和脱离等事件的视频帧级别标注，从而能够分析感知和决策方面的故障。论文通过多项分析展示了SAVeD的效用：(1) 提出了一个新框架，集成了语义分割和单目深度估计，以计算动态对象的实时碰撞时间(TTC)。(2) 利用广义极值(GEV)分布来建模和量化不同道路类型中碰撞和近失事件的极端风险。(3) 为最先进的VLLM（VideoLLaMA2和InternVL2.5 HiCo R16）建立了基准，表明SAVeD的详细标注通过复杂近失场景中的领域自适应显著提高了模型性能。

## 🔬 方法详解

**问题定义**：现有ADAS研究缺乏真实且包含高风险边缘案例（如近失事件和系统故障）的数据集。现有数据集主要集中在模拟环境或人类驾驶车辆数据，缺少真实ADAS车辆在风险条件下的行为数据。

**核心思路**：通过挖掘公开的社交媒体视频，构建一个包含ADAS车辆相关碰撞、近失事件和脱离场景的大规模数据集。利用该数据集，可以分析ADAS系统的感知和决策缺陷，并为相关算法的开发和评估提供支持。

**技术框架**：SAVeD数据集构建流程主要包括：1) 从社交媒体平台收集视频数据；2) 对视频进行筛选，选择包含ADAS车辆相关事件的视频；3) 对视频进行帧级别标注，标注内容包括碰撞、规避动作和脱离等事件；4) 利用标注数据进行模型训练和评估，例如训练VLLM模型，并评估其在近失场景中的性能。此外，论文还提出了一个基于语义分割和单目深度估计的实时TTC计算框架，以及利用GEV分布进行风险建模的方法。

**关键创新**：SAVeD数据集本身就是一个重要的创新点，它填补了ADAS研究领域真实高风险场景数据集的空白。此外，论文提出的基于语义分割和单目深度估计的实时TTC计算框架，以及利用GEV分布进行风险建模的方法，也具有一定的创新性。与现有方法相比，SAVeD数据集提供了更真实、更全面的数据，能够更有效地支持ADAS系统的研究和开发。

**关键设计**：SAVeD数据集包含2119个第一人称视角视频，覆盖了不同的地点、光照条件和天气场景。视频帧级别标注包括碰撞、规避动作和脱离等事件。在TTC计算框架中，语义分割用于识别场景中的动态对象，单目深度估计用于估计动态对象的距离。GEV分布用于建模碰撞和近失事件的极端风险，其参数通过最大似然估计方法进行估计。VLLM模型的训练采用领域自适应方法，利用SAVeD数据集的标注数据对模型进行微调。

## 📊 实验亮点

论文通过实验证明，SAVeD数据集能够显著提升VLLM在复杂近失场景中的性能。例如，通过在SAVeD数据集上进行领域自适应，VideoLLaMA2和InternVL2.5 HiCo R16等模型的性能得到了显著提升。此外，论文还利用GEV分布对不同道路类型中的碰撞和近失事件的极端风险进行了建模和量化，为风险评估和安全策略制定提供了依据。

## 🎯 应用场景

SAVeD数据集可应用于ADAS系统的开发和测试，例如用于评估ADAS系统的感知和决策能力，提高系统在复杂和危险场景下的安全性。此外，该数据集还可用于研究驾驶员在ADAS系统干预下的行为模式，从而更好地设计人机交互界面，提升驾驶体验。该数据集的发布将促进自动驾驶和智能交通领域的研究进展。

## 📄 摘要（原文）

> The advancement of safety-critical research in driving behavior in ADAS-equipped vehicles require real-world datasets that not only include diverse traffic scenarios but also capture high-risk edge cases such as near-miss events and system failures. However, existing datasets are largely limited to either simulated environments or human-driven vehicle data, lacking authentic ADAS (Advanced Driver Assistance System) vehicle behavior under risk conditions. To address this gap, this paper introduces SAVeD, a large-scale video dataset curated from publicly available social media content, explicitly focused on ADAS vehicle-related crashes, near-miss incidents, and disengagements. SAVeD features 2,119 first-person videos, capturing ADAS vehicle operations in diverse locations, lighting conditions, and weather scenarios. The dataset includes video frame-level annotations for collisions, evasive maneuvers, and disengagements, enabling analysis of both perception and decision-making failures. We demonstrate SAVeD's utility through multiple analyses and contributions: (1) We propose a novel framework integrating semantic segmentation and monocular depth estimation to compute real-time Time-to-Collision (TTC) for dynamic objects. (2) We utilize the Generalized Extreme Value (GEV) distribution to model and quantify the extreme risk in crash and near-miss events across different roadway types. (3) We establish benchmarks for state-of-the-art VLLMs (VideoLLaMA2 and InternVL2.5 HiCo R16), showing that SAVeD's detailed annotations significantly enhance model performance through domain adaptation in complex near-miss scenarios.

