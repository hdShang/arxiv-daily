---
layout: default
title: "RoboView-Bias: Benchmarking Visual Bias in Embodied Agents for Robotic Manipulation"
---

# RoboView-Bias: Benchmarking Visual Bias in Embodied Agents for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22356" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22356v1</a>
  <a href="https://arxiv.org/pdf/2509.22356.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22356v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22356v1', 'RoboView-Bias: Benchmarking Visual Bias in Embodied Agents for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Enguang Liu, Siyuan Liang, Liming Lu, Xiyu Zeng, Xiaochun Cao, Aishan Liu, Shuchao Pang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**RoboView-Bias：首个机器人操作中具身智能体视觉偏见评测基准**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `具身智能体` `视觉偏见` `机器人操作` `评测基准` `因子隔离` `感知公平性` `语义 grounding`

## 📋 核心要点

1. 现有具身智能体评测缺乏对视觉偏见的系统性量化，限制了对感知如何影响决策稳定性的理解。
2. RoboView-Bias 采用因子隔离原则，通过结构化变体生成和感知公平性验证，系统量化视觉偏见。
3. 实验表明，所有智能体都存在显著视觉偏见，视角是关键因素，且偏见存在不对称耦合，语义 grounding 层可有效缓解偏见。

## 📝 摘要（中文）

具身智能体的安全性和可靠性依赖于准确且无偏见的视觉感知。然而，现有的评测基准主要强调泛化性和在扰动下的鲁棒性，而对视觉偏见的系统性量化仍然不足。这种差距限制了对感知如何影响决策稳定性的更深层理解。为了解决这个问题，我们提出了 RoboView-Bias，这是第一个专门设计用于系统性量化机器人操作中视觉偏见的评测基准，遵循了因子隔离原则。利用结构化的变体生成框架和感知公平性验证协议，我们创建了 2127 个任务实例，能够可靠地测量由单个视觉因素及其相互作用引起的偏见。使用这个基准，我们系统地评估了两种主流范式中的三个代表性具身智能体，并报告了三个关键发现：（i）所有智能体都表现出显著的视觉偏见，其中相机视角是最关键的因素；（ii）智能体在高度饱和的颜色上实现了最高的成功率，表明它们继承了底层 VLM 的视觉偏好；（iii）视觉偏见表现出强烈的、不对称的耦合，视角强烈地放大了与颜色相关的偏见。最后，我们证明了基于语义 grounding 层的缓解策略在 MOKA 上将视觉偏见显著降低了约 54.5%。我们的结果表明，对视觉偏见的系统分析是开发安全可靠的通用具身智能体的先决条件。

## 🔬 方法详解

**问题定义**：现有具身智能体在机器人操作任务中，其视觉感知模块存在偏见，导致决策不稳定和安全性问题。现有的评测基准主要关注泛化性和鲁棒性，缺乏对视觉偏见的系统性量化，难以深入理解感知对决策的影响。

**核心思路**：RoboView-Bias 的核心思路是通过因子隔离的方式，系统性地量化不同视觉因素（如视角、颜色等）对具身智能体决策的影响。通过控制变量，分析单个因素及其相互作用如何引入偏见，从而为后续的偏见缓解提供指导。

**技术框架**：RoboView-Bias 包含以下主要模块：1) 结构化变体生成框架：用于生成包含不同视觉因素变体的任务实例；2) 感知公平性验证协议：用于评估智能体在不同视觉因素下的表现，并量化偏见程度；3) 偏见缓解策略：提出基于语义 grounding 层的缓解策略，减少视觉偏见。整体流程为：首先，利用变体生成框架创建任务实例；然后，使用感知公平性验证协议评估智能体表现；最后，应用偏见缓解策略，并重新评估。

**关键创新**：RoboView-Bias 的关键创新在于：1) 首次提出针对机器人操作中具身智能体视觉偏见的系统性评测基准；2) 采用因子隔离原则，能够量化单个视觉因素及其相互作用对偏见的影响；3) 提出结构化的变体生成框架和感知公平性验证协议，实现了偏见的可靠测量。

**关键设计**：在变体生成框架中，论文设计了多种视觉因素的变体，如相机视角、光照条件、物体颜色等。在感知公平性验证协议中，论文定义了偏见的量化指标，如成功率差异、公平性指标等。此外，论文还设计了基于语义 grounding 层的偏见缓解策略，通过将视觉信息与语义信息对齐，减少视觉偏见的影响。具体的参数设置和网络结构等细节在论文中有详细描述。

## 📊 实验亮点

RoboView-Bias 评测结果表明，所有受测智能体都存在显著的视觉偏见，其中相机视角是最关键的因素。智能体在高度饱和的颜色上表现更好，表明其继承了底层 VLM 的视觉偏好。提出的基于语义 grounding 层的缓解策略在 MOKA 上将视觉偏见显著降低了约 54.5%。

## 🎯 应用场景

该研究成果可应用于提升机器人操作任务中具身智能体的安全性、可靠性和公平性。通过系统性地评估和缓解视觉偏见，可以提高机器人在复杂环境中的适应能力，并减少因视觉感知偏差导致的错误决策。该研究对开发通用型、可靠的机器人系统具有重要意义。

## 📄 摘要（原文）

> The safety and reliability of embodied agents rely on accurate and unbiased visual perception. However, existing benchmarks mainly emphasize generalization and robustness under perturbations, while systematic quantification of visual bias remains scarce. This gap limits a deeper understanding of how perception influences decision-making stability. To address this issue, we propose RoboView-Bias, the first benchmark specifically designed to systematically quantify visual bias in robotic manipulation, following a principle of factor isolation. Leveraging a structured variant-generation framework and a perceptual-fairness validation protocol, we create 2,127 task instances that enable robust measurement of biases induced by individual visual factors and their interactions. Using this benchmark, we systematically evaluate three representative embodied agents across two prevailing paradigms and report three key findings: (i) all agents exhibit significant visual biases, with camera viewpoint being the most critical factor; (ii) agents achieve their highest success rates on highly saturated colors, indicating inherited visual preferences from underlying VLMs; and (iii) visual biases show strong, asymmetric coupling, with viewpoint strongly amplifying color-related bias. Finally, we demonstrate that a mitigation strategy based on a semantic grounding layer substantially reduces visual bias by approximately 54.5\% on MOKA. Our results highlight that systematic analysis of visual bias is a prerequisite for developing safe and reliable general-purpose embodied agents.

