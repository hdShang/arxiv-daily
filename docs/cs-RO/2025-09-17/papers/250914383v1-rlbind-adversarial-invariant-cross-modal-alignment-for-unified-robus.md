---
layout: default
title: "RLBind: Adversarial-Invariant Cross-Modal Alignment for Unified Robust Embeddings"
---

# RLBind: Adversarial-Invariant Cross-Modal Alignment for Unified Robust Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14383" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14383v1</a>
  <a href="https://arxiv.org/pdf/2509.14383.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14383v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14383v1', 'RLBind: Adversarial-Invariant Cross-Modal Alignment for Unified Robust Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhong Lu

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-17

**备注**: This paper is submitted to IEEE International Conference on Robotics and Automation (ICRA) 2026

---

## 💡 一句话要点

**RLBind：对抗不变跨模态对齐，用于统一鲁棒嵌入**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `对抗鲁棒性` `跨模态对齐` `机器人感知` `对比学习`

## 📋 核心要点

1. 现有方法在CLIP类编码器中对齐干净和对抗样本的视觉特征，忽略了跨模态信息，鲁棒性提升有限。
2. RLBind通过两阶段的对抗不变跨模态对齐，首先增强视觉编码器，然后利用文本锚点进行跨模态对齐。
3. 实验表明，RLBind在多种模态数据上，相比LanguageBind和微调基线，显著提升了干净准确性和对抗鲁棒性。

## 📝 摘要（中文）

统一的多模态编码器将视觉、音频和其他传感器绑定到共享的嵌入空间中，是机器人感知和决策的理想构建块。然而，在机器人上的部署使视觉分支暴露于对抗性和自然损坏，使得鲁棒性成为安全性的先决条件。先前的防御通常在CLIP风格的编码器中对齐干净和对抗性特征，而忽略了更广泛的跨模态对应关系，导致增益有限，并且常常降低零样本迁移性能。我们引入了RLBind，这是一个用于鲁棒统一嵌入的两阶段对抗不变跨模态对齐框架。第一阶段对干净-对抗样本对进行无监督微调，以增强视觉编码器。第二阶段通过最小化干净/对抗特征与文本锚点之间的差异，同时强制跨模态的类别分布对齐，来利用跨模态对应关系。在图像、音频、热成像和视频数据上的大量实验表明，RLBind在干净准确性和范数有界对抗鲁棒性方面始终优于LanguageBind骨干网络和标准微调基线。通过在不牺牲泛化能力的情况下提高弹性，RLBind为导航、操作和其他自主设置中具身机器人的更安全的多传感器感知堆栈提供了一条实用的途径。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态机器人感知系统中，视觉分支易受对抗攻击影响，导致整体系统鲁棒性不足的问题。现有方法主要关注视觉模态内部的对抗防御，忽略了跨模态信息，导致防御效果有限，且可能损害零样本迁移能力。

**核心思路**：论文的核心思路是利用跨模态信息来增强视觉模态的对抗鲁棒性。具体来说，通过将视觉特征与文本锚点对齐，并强制跨模态的类别分布一致，从而提高视觉编码器在对抗攻击下的不变性。这种方法充分利用了不同模态之间的互补信息，从而提升了整体的鲁棒性。

**技术框架**：RLBind框架包含两个主要阶段：第一阶段是无监督的视觉编码器强化，通过在干净-对抗样本对上进行微调，提高视觉编码器自身的鲁棒性。第二阶段是跨模态对齐，通过最小化干净/对抗视觉特征与文本锚点之间的差异，并强制跨模态的类别分布对齐，进一步增强视觉特征的对抗不变性。

**关键创新**：RLBind的关键创新在于其跨模态对齐策略。与以往仅关注视觉模态内部对抗防御的方法不同，RLBind充分利用了文本模态作为锚点，通过跨模态对齐来提高视觉特征的鲁棒性。此外，两阶段的训练策略也保证了视觉编码器在对抗攻击下的稳定性和泛化能力。

**关键设计**：在第一阶段，使用自监督学习方法（具体方法未知）在干净-对抗样本对上微调视觉编码器。在第二阶段，使用对比学习损失来最小化干净/对抗视觉特征与文本锚点之间的距离。同时，使用分布对齐损失（具体形式未知）来强制跨模态的类别分布一致。文本锚点可能是通过文本编码器获得的类别描述嵌入。

## 📊 实验亮点

实验结果表明，RLBind在图像、音频、热成像和视频数据上，相比LanguageBind骨干网络和标准微调基线，在干净准确性和范数有界对抗鲁棒性方面均取得了显著提升。具体性能数据和提升幅度在论文中详细给出（未知）。

## 🎯 应用场景

RLBind可应用于各种需要多传感器融合的机器人应用场景，例如导航、操作和自主系统。通过提高多模态感知的鲁棒性，可以提升机器人在复杂和不确定环境中的安全性和可靠性。该研究对于推动机器人技术在现实世界中的广泛应用具有重要意义。

## 📄 摘要（原文）

> Unified multi-modal encoders that bind vision, audio, and other sensors into a shared embedding space are attractive building blocks for robot perception and decision-making. However, on-robot deployment exposes the vision branch to adversarial and natural corruptions, making robustness a prerequisite for safety. Prior defenses typically align clean and adversarial features within CLIP-style encoders and overlook broader cross-modal correspondence, yielding modest gains and often degrading zero-shot transfer. We introduce RLBind, a two-stage adversarial-invariant cross-modal alignment framework for robust unified embeddings. Stage 1 performs unsupervised fine-tuning on clean-adversarial pairs to harden the visual encoder. Stage 2 leverages cross-modal correspondence by minimizing the discrepancy between clean/adversarial features and a text anchor, while enforcing class-wise distributional alignment across modalities. Extensive experiments on Image, Audio, Thermal, and Video data show that RLBind consistently outperforms the LanguageBind backbone and standard fine-tuning baselines in both clean accuracy and norm-bounded adversarial robustness. By improving resilience without sacrificing generalization, RLBind provides a practical path toward safer multi-sensor perception stacks for embodied robots in navigation, manipulation, and other autonomy settings.

