---
layout: default
title: "REALM: A Real-to-Sim Validated Benchmark for Generalization in Robotic Manipulation"
---

# REALM: A Real-to-Sim Validated Benchmark for Generalization in Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19562" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19562v1</a>
  <a href="https://arxiv.org/pdf/2512.19562.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19562v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19562v1', 'REALM: A Real-to-Sim Validated Benchmark for Generalization in Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Martin Sedlacek, Pavlo Yefanov, Georgy Ponimatkin, Jai Bardhan, Simon Pilc, Mederic Fourmy, Evangelos Kazakos, Cees G. M. Snoek, Josef Sivic, Vladimir Petrik

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-22

**备注**: 9 pages, 10 figures

---

## 💡 一句话要点

**REALM：用于机器人操作泛化能力的真实-模拟验证基准**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视觉-语言-动作模型` `泛化能力` `模拟环境` `基准测试`

## 📋 核心要点

1. 现有VLA模型在真实机器人操作任务中泛化能力不足，且真实环境评估成本高昂。
2. REALM通过高保真模拟环境和对齐的机器人控制，建立模拟与真实世界性能的强相关性。
3. 实验评估了多个VLA模型在REALM基准上的泛化能力，揭示了现有模型的局限性。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型使机器人能够理解和执行自然语言指令描述的任务。然而，一个关键挑战在于它们泛化到训练环境之外的能力，这在现实世界中评估既困难又昂贵。为了解决这个问题，我们提出了REALM，一个新的模拟环境和基准，旨在评估VLA模型的泛化能力，特别强调通过高保真视觉效果和对齐的机器人控制，在模拟和真实世界性能之间建立强大的相关性。我们的环境提供了15个扰动因子、7个操作技能和超过3500个对象。最后，我们建立了两个任务集作为基准，并评估了π_{0}、π_{0}-FAST和GR00T N1.5 VLA模型，表明泛化和鲁棒性仍然是一个开放的挑战。更广泛地说，我们还表明，模拟为我们提供了现实世界的宝贵代理，并允许我们系统地探测和量化VLA的弱点和失败模式。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型在机器人操作任务中，难以泛化到未见过的环境和物体。在真实环境中评估这些模型的泛化能力成本高昂，且难以系统性地控制各种扰动因素。因此，需要一个能够有效评估VLA模型泛化能力的基准，并且该基准需要与真实世界具有较强的相关性。

**核心思路**：REALM的核心思路是构建一个高保真度的模拟环境，该环境能够尽可能地模拟真实世界的视觉效果和机器人控制。通过精心设计的扰动因子和多样化的物体，来模拟真实世界中可能遇到的各种情况，从而评估VLA模型的泛化能力。同时，通过实验验证模拟环境与真实世界性能的相关性，确保评估结果的有效性。

**技术框架**：REALM包含以下几个主要组成部分：1）一个基于模拟器的环境，提供高保真度的视觉效果和物理模拟；2）一个包含15个扰动因子的集合，用于模拟真实世界中的各种干扰；3）一个包含7个操作技能的集合，用于评估VLA模型在不同任务上的表现；4）一个包含超过3500个物体的集合，用于增加环境的多样性；5）两个任务集，用于构成基准，评估VLA模型的泛化能力。

**关键创新**：REALM的关键创新在于其高保真度的模拟环境和与真实世界性能的强相关性。通过精心设计的扰动因子和多样化的物体，REALM能够有效地模拟真实世界中的各种情况，从而评估VLA模型的泛化能力。此外，REALM还提供了一个标准化的基准，方便研究人员比较不同VLA模型的性能。

**关键设计**：REALM的关键设计包括：1）使用高分辨率的纹理和光照模型，以提高视觉效果的逼真度；2）使用精确的物理引擎，以模拟真实的机器人控制；3）精心选择15个扰动因子，包括光照变化、物体位置变化、噪声等；4）使用多样化的物体集合，包括不同形状、大小和材质的物体；5）设计两个任务集，分别评估VLA模型在不同难度级别上的泛化能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19562v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19562v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19562v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文评估了π_{0}、π_{0}-FAST和GR00T N1.5等VLA模型在REALM基准上的性能，结果表明现有模型在泛化能力和鲁棒性方面仍有提升空间。实验还验证了模拟环境与真实世界性能之间的相关性，表明REALM可以作为评估VLA模型泛化能力的有效代理。

## 🎯 应用场景

REALM可用于评估和改进视觉-语言-动作模型的泛化能力，推动机器人技术在复杂和动态环境中的应用。例如，在家庭服务机器人、工业自动化、自动驾驶等领域，REALM可以帮助开发更鲁棒和可靠的机器人系统。该基准还有助于研究人员更好地理解VLA模型的弱点，并开发更有效的训练方法。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models empower robots to understand and execute tasks described by natural language instructions. However, a key challenge lies in their ability to generalize beyond the specific environments and conditions they were trained on, which is presently difficult and expensive to evaluate in the real-world. To address this gap, we present REALM, a new simulation environment and benchmark designed to evaluate the generalization capabilities of VLA models, with a specific emphasis on establishing a strong correlation between simulated and real-world performance through high-fidelity visuals and aligned robot control. Our environment offers a suite of 15 perturbation factors, 7 manipulation skills, and more than 3,500 objects. Finally, we establish two task sets that form our benchmark and evaluate the π_{0}, π_{0}-FAST, and GR00T N1.5 VLA models, showing that generalization and robustness remain an open challenge. More broadly, we also show that simulation gives us a valuable proxy for the real-world and allows us to systematically probe for and quantify the weaknesses and failure modes of VLAs. Project page: https://martin-sedlacek.com/realm

