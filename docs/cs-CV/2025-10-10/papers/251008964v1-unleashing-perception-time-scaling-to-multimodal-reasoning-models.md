---
layout: default
title: Unleashing Perception-Time Scaling to Multimodal Reasoning Models
---

# Unleashing Perception-Time Scaling to Multimodal Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08964" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08964v1</a>
  <a href="https://arxiv.org/pdf/2510.08964.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08964v1" onclick="toggleFavorite(this, '2510.08964v1', 'Unleashing Perception-Time Scaling to Multimodal Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Li, Zhenghao Chen, Ziheng Wu, Kun Zhou, Ruipu Luo, Can Zhang, Zhentao He, Yufei Zhan, Wayne Xin Zhao, Minghui Qiu

**分类**: cs.CV, cs.CL

**发布日期**: 2025-10-10

---

## 💡 一句话要点

**提出感知时间尺度调整(PTS)，提升多模态推理模型在视觉感知任务中的精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `视觉感知` `感知时间尺度调整` `强化学习` `视觉语言模型`

## 📋 核心要点

1. 现有LVLMs在视觉感知上采用快速感知范式，缺乏对底层感知过程的建模，导致估计精度不足。
2. 论文提出感知时间尺度调整(PTS)范式，通过token丰富的感知和问题分解，使感知与推理时尺度调整对齐。
3. 实验表明，PTS显著提高了感知精度，在DisTANCE上从8.0%提升到64.7%，并泛化到域外任务和真实世界感知任务。

## 📝 摘要（中文）

近年来，推理时尺度调整技术显著提升了大型视觉语言模型(LVLMs)的推理能力。受此启发，类似策略也被应用于多模态推理，但其对视觉感知的影响尚不明确。本文提出了一个以感知为中心的基准测试DisTANCE，用于评估视觉估计任务。实验结果表明，LVLMs的估计精度有限，且推理时尺度调整带来的增益甚微。作者认为这是由于当前LVLMs的快速感知范式，即将视觉理解视为一次性输出，而没有对底层感知过程进行建模。为了解决这个问题，作者提出了一种新的范式——感知时间尺度调整(PTS)，鼓励token丰富的感知，并将复杂的感知问题分解为中间可处理的子问题，从而使感知能够与推理时尺度调整对齐并从中受益。结合强化学习技术，PTS显著提高了感知精度，在DisTANCE上的高精度性能从8.0%提高到64.7%，并很好地泛化到域外任务。令人惊讶的是，即使PTS数据是纯粹合成的，将它们与数学推理数据相结合，也能在推理和真实世界感知基准测试中获得一致的收益。进一步的分析表明，PTS引入了更多与感知相关的token，并增加了模型对图像token的关注。代码和数据将公开发布。

## 🔬 方法详解

**问题定义**：论文旨在解决大型视觉语言模型(LVLMs)在视觉感知任务中精度不足的问题。现有LVLMs通常采用“快速感知”范式，即直接将图像作为输入，一次性输出结果，缺乏对底层感知过程的建模和迭代优化。这种方式限制了模型利用推理时尺度调整技术提升感知能力。

**核心思路**：论文的核心思路是引入“感知时间尺度调整”(Perception-Time Scaling, PTS) 范式。PTS鼓励模型进行token丰富的感知，将复杂的感知问题分解为一系列中间可处理的子问题。通过这种方式，模型可以逐步细化对图像的理解，并更好地利用推理时尺度调整技术来提升感知精度。PTS的核心在于将感知过程从“一步到位”转变为一个迭代优化的过程。

**技术框架**：PTS的技术框架主要包含以下几个阶段：1) **问题分解**：将复杂的视觉感知任务分解为一系列更简单的子问题。例如，对于目标定位任务，可以分解为目标检测、区域分割、坐标估计等子问题。2) **Token丰富的感知**：鼓励模型生成更多的与感知相关的token，例如目标描述、属性描述、关系描述等。这些token可以帮助模型更好地理解图像内容。3) **迭代优化**：通过强化学习等技术，训练模型逐步优化感知过程，使其能够更好地解决子问题，并最终完成整个感知任务。

**关键创新**：论文最重要的技术创新点在于提出了感知时间尺度调整(PTS)范式。与现有的快速感知范式相比，PTS更加注重对底层感知过程的建模和迭代优化。通过问题分解和token丰富的感知，PTS使模型能够更好地利用推理时尺度调整技术来提升感知精度。此外，论文还提出了一个以感知为中心的基准测试DisTANCE，用于评估LVLMs在视觉估计任务中的性能。

**关键设计**：在具体实现上，论文使用了强化学习技术来训练PTS模型。奖励函数的设计至关重要，需要能够引导模型生成高质量的感知token，并逐步解决子问题。此外，论文还探索了不同的网络结构和参数设置，以优化PTS模型的性能。例如，可以使用Transformer模型来处理图像和文本信息，并使用注意力机制来关注图像中的关键区域。

## 📊 实验亮点

实验结果表明，PTS显著提高了感知精度，在DisTANCE基准测试中，高精度性能从8.0%提升到64.7%。此外，PTS还表现出良好的泛化能力，能够有效应用于域外任务和真实世界感知任务。更令人惊讶的是，即使使用纯合成数据训练PTS模型，也能在数学推理任务中获得一致的性能提升。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、智能监控、医学图像分析等领域。通过提升视觉感知精度，可以提高机器人在复杂环境中的适应性和决策能力，从而实现更安全、更高效的自动化应用。未来，该方法有望扩展到更多模态和更复杂的感知任务中。

## 📄 摘要（原文）

> Recent advances in inference-time scaling, particularly those leveraging reinforcement learning with verifiable rewards, have substantially enhanced the reasoning capabilities of Large Vision-Language Models (LVLMs). Inspired by this success, similar strategies have been applied to multimodal reasoning, yet their impact on visual perception remains unclear. To investigate this gap, we introduce DisTANCE, a perception-centric benchmark for visual estimation tasks. Evaluation results show that LVLMs exhibit limited estimation precision, and inference-time scaling offers only marginal gains. We attribute this to the fast perception paradigm of current LVLMs, where visual understanding is treated as a one-shot output without modeling the underlying perceptual process. To address this, we propose Perception-Time Scaling (PTS), a novel paradigm that encourages token-rich perception and decomposes complex perception problems into intermediate tractable sub-problems, thereby enabling perception to align with and benefit from inference-time scaling. Combined with reinforcement learning techniques, PTS significantly improves perception accuracy, raising high-precision performance on DisTANCE from 8.0% to 64.7%, and generalizes well to out-of-domain tasks. Surprisingly, even though PTS data are purely synthetic, combining them with math reasoning data yields consistent gains in both reasoning and real-world perception benchmarks. Further analysis reveals that PTS introduces more perception-related tokens and increases the model's attention to image tokens. Our code and data will be publicly released.

