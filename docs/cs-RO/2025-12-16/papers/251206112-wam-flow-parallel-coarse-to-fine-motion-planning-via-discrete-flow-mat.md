---
layout: default
title: WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving
---

# WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.06112" class="toolbar-btn" target="_blank">📄 arXiv: 2512.06112</a>
  <a href="https://arxiv.org/pdf/2512.06112.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06112" onclick="toggleFavorite(this, '2512.06112', 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifang Xu, Jiahao Cui, Feipeng Cai, Zhihao Zhu, Hanlin Shang, Shan Luan, Mingwang Xu, Neng Zhang, Yaoyi Li, Jia Cai, Siyu Zhu

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出WAM-Flow，通过离散流匹配实现自动驾驶并行粗到精运动规划**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `轨迹规划` `流匹配` `视觉语言动作模型` `并行计算`

## 📋 核心要点

1. 现有自回归模型在轨迹规划中存在推理速度慢、难以并行化的问题，限制了其在自动驾驶中的应用。
2. WAM-Flow通过离散流匹配，将轨迹规划转化为并行去噪过程，实现粗到精的轨迹优化，提升计算效率。
3. 实验表明，WAM-Flow在闭环性能上优于自回归和扩散模型，在NAVSIM v1上取得了显著的PDMS指标提升。

## 📝 摘要（中文）

本文介绍了一种视觉-语言-动作(VLA)模型WAM-Flow，它将自车轨迹规划视为结构化token空间上的离散流匹配问题。与自回归解码器不同，WAM-Flow执行完全并行的双向去噪，从而实现具有可调计算-精度权衡的粗到精细化。具体来说，该方法结合了通过三元组边际学习保留标量几何的度量对齐数值分词器、几何感知流目标以及模拟器引导的GRPO对齐，该对齐集成了安全性、自车进度和舒适性奖励，同时保留了并行生成。多阶段自适应将预训练的自回归骨干网络(Janus-1.5B)从因果解码转换为非因果流模型，并通过持续的多模态预训练加强道路场景能力。由于一致性模型训练和并行解码推理的固有特性，WAM-Flow在闭环性能方面优于自回归和基于扩散的VLA基线，在NAVSIM v1基准测试中，单步推理达到89.1 PDMS，五步推理达到90.3 PDMS。这些结果确立了离散流匹配作为端到端自动驾驶的一个新的有希望的范例。代码即将公开。

## 🔬 方法详解

**问题定义**：论文旨在解决端到端自动驾驶中轨迹规划的效率问题。现有的自回归模型通常采用串行解码方式，推理速度较慢，难以满足自动驾驶对实时性的要求。此外，基于扩散的模型虽然可以并行生成，但训练和推理成本较高。因此，需要一种既能并行生成又能保证精度的轨迹规划方法。

**核心思路**：论文的核心思路是将轨迹规划问题转化为离散流匹配问题。通过将轨迹离散化为token序列，并利用流匹配模型学习token之间的转移概率，从而实现轨迹的并行生成和优化。这种方法借鉴了计算机视觉和自然语言处理领域中流匹配模型的成功经验，并将其应用于自动驾驶领域。

**技术框架**：WAM-Flow的整体框架包括以下几个主要模块：1) 度量对齐数值分词器：将连续的轨迹数据转换为离散的token序列，并保证token之间的几何关系；2) 几何感知流目标：设计损失函数，引导模型学习token之间的合理转移；3) 模拟器引导的GRPO对齐：利用模拟器环境，对模型进行强化学习，优化轨迹的安全性、自车进度和舒适性；4) 多阶段自适应：将预训练的自回归模型转换为流模型，并进行多模态预训练，提升模型在道路场景下的表现。

**关键创新**：WAM-Flow的关键创新在于将离散流匹配引入到自动驾驶的轨迹规划中。与传统的自回归模型相比，WAM-Flow可以并行生成轨迹，显著提升了推理速度。与基于扩散的模型相比，WAM-Flow的训练和推理成本更低。此外，WAM-Flow还设计了度量对齐数值分词器和几何感知流目标，保证了轨迹的几何合理性。

**关键设计**：在度量对齐数值分词器中，使用了三元组边际学习来保证token之间的几何关系。在几何感知流目标中，设计了基于流匹配的损失函数，引导模型学习token之间的合理转移。在模拟器引导的GRPO对齐中，使用了强化学习算法，优化轨迹的安全性、自车进度和舒适性。此外，还采用了多阶段自适应策略，将预训练的自回归模型转换为流模型，并进行多模态预训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.06112/fig/Figure_2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.06112/fig/Figure_3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.06112/fig/navsim_comp.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

WAM-Flow在NAVSIM v1基准测试中取得了显著的性能提升。单步推理达到89.1 PDMS，五步推理达到90.3 PDMS，优于现有的自回归和基于扩散的VLA基线。这些结果表明，离散流匹配是一种很有前途的端到端自动驾驶轨迹规划方法。

## 🎯 应用场景

WAM-Flow具有广泛的应用前景，可用于各种自动驾驶场景，例如城市道路、高速公路和停车场等。该方法可以显著提升自动驾驶系统的决策效率和安全性，并为未来的自动驾驶技术发展提供新的思路。此外，该方法还可以应用于机器人导航、游戏AI等领域。

## 📄 摘要（原文）

> We introduce WAM-Flow, a vision-language-action (VLA) model that casts ego-trajectory planning as discrete flow matching over a structured token space. In contrast to autoregressive decoders, WAM-Flow performs fully parallel, bidirectional denoising, enabling coarse-to-fine refinement with a tunable compute-accuracy trade-off. Specifically, the approach combines a metric-aligned numerical tokenizer that preserves scalar geometry via triplet-margin learning, a geometry-aware flow objective and a simulator-guided GRPO alignment that integrates safety, ego progress, and comfort rewards while retaining parallel generation. A multi-stage adaptation converts a pre-trained auto-regressive backbone (Janus-1.5B) from causal decoding to non-causal flow model and strengthens road-scene competence through continued multimodal pretraining. Thanks to the inherent nature of consistency model training and parallel decoding inference, WAM-Flow achieves superior closed-loop performance against autoregressive and diffusion-based VLA baselines, with 1-step inference attaining 89.1 PDMS and 5-step inference reaching 90.3 PDMS on NAVSIM v1 benchmark. These results establish discrete flow matching as a new promising paradigm for end-to-end autonomous driving. The code will be publicly available soon.

