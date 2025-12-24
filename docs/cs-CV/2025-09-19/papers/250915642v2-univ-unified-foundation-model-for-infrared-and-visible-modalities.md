---
layout: default
title: "UNIV: Unified Foundation Model for Infrared and Visible Modalities"
---

# UNIV: Unified Foundation Model for Infrared and Visible Modalities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15642" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15642v2</a>
  <a href="https://arxiv.org/pdf/2509.15642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15642v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15642v2', 'UNIV: Unified Foundation Model for Infrared and Visible Modalities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fangyuan Mao, Shuo Wang, Jilin Mei, Shun Lu, Chen Min, Fuyang Liu, Xiaokun Feng, Meiqi Wu, Yu Hu

**分类**: cs.CV

**发布日期**: 2025-09-19 (更新: 2025-11-19)

---

## 💡 一句话要点

**提出UNIV以解决红外与可见光模态的跨模态对齐问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `红外感知` `可见光模态` `跨模态对齐` `对比学习` `多模态融合` `基础模型` `智能监控` `自动驾驶`

## 📋 核心要点

1. 现有基础模型在跨模态感知中存在显著的降级，主要是由于模式偏差导致的表面特征优先于底层语义。
2. 本文提出的UNIV模型通过补丁跨模态对比学习（PCCL）策略，构建统一的跨模态特征空间，增强语义对齐。
3. 实验结果显示，UNIV在红外任务上提升了1.7 mIoU用于语义分割和0.7 mAP用于检测，同时在RGB任务上保持竞争力。

## 📝 摘要（中文）

联合RGB-红外感知对于在多样的天气和光照条件下实现鲁棒性至关重要。尽管基础模型在单一模态中表现出色，但在跨模态时却遭遇显著的降级，主要由于模式偏差导致的表面传感器模式优先于底层语义。为了解决这一问题，本文提出了UNIV，一个统一的红外与可见光基础模型。UNIV的核心是补丁跨模态对比学习（PCCL），这是一种自监督对比学习策略，构建了统一的跨模态特征空间。PCCL利用冻结的预训练模型，根据语义相似性采样伪补丁对，通过吸引语义相关的对并排斥无关的对来对齐红外-可见光表示。实验结果表明，UNIV在红外任务上表现优越，同时在RGB任务上保持竞争力。

## 🔬 方法详解

**问题定义**：本文旨在解决红外与可见光模态之间的跨模态对齐问题，现有方法在此方面存在显著的性能下降，主要由于模式偏差导致的表面特征优先于底层语义。

**核心思路**：UNIV通过补丁跨模态对比学习（PCCL）策略，构建一个统一的跨模态特征空间，旨在增强红外与可见光之间的语义对齐，避免模型陷入模式偏差。

**技术框架**：UNIV的整体架构包括一个冻结的预训练模型，用于生成伪补丁对，并通过对比学习策略对红外和可见光表示进行对齐。主要模块包括伪补丁采样、语义对齐和对比损失计算。

**关键创新**：最重要的技术创新点在于引入了补丁跨模态对比学习（PCCL），该方法通过吸引语义相关的补丁对并排斥无关的补丁对，显著提升了跨模态对齐的效果。

**关键设计**：在技术细节上，PCCL使用了冻结的预训练模型进行伪补丁对的生成，损失函数设计为对比损失，以增强语义结构的关注，同时确保跨模态特征的分离性。具体参数设置和网络结构的细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，UNIV在红外任务上实现了1.7 mIoU的提升用于语义分割，以及0.7 mAP的提升用于检测，显示出其在红外领域的优越性能。同时，UNIV在RGB任务上也保持了竞争力，证明了其跨模态学习的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、无人机视觉等场景，这些领域需要在不同光照和天气条件下进行有效的目标检测和识别。UNIV模型的鲁棒性和准确性将为这些应用提供更可靠的技术支持，推动多模态感知技术的发展。

## 📄 摘要（原文）

> Joint RGB-infrared perception is essential for achieving robustness under diverse weather and illumination conditions. Although foundation models excel within single modalities, they suffer from substantial cross-modal degradation, an issue we attribute to a pattern shortcut, i.e., a modal bias that prioritizes superficial sensor patterns over underlying semantics. To address this problem, we introduce UNIV, a Unified foundation model for Infrared and Visible modalities. At the core of UNIV lies Patch Cross-modal Contrastive Learning (PCCL), a self-supervised contrastive learning strategy that constructs a unified cross-modal feature space. PCCL employs a frozen pre-trained model to sample pseudo patch pairs based on semantic similarity, and aligns infrared-visible representations by attracting semantically related pairs while repelling unrelated ones. This process simultaneously enhances cross-modal alignment and inter-class semantic separability, guiding the model to focus on semantic structure rather than falling into pattern shortcuts. To further enable cross-modal learning, we introduce MVIP, the most comprehensive visible-infrared benchmark to date, containing 98,992 precisely aligned image pairs across diverse scenes. Extensive experiments demonstrate UNIV's superior performance on infrared tasks (+1.7 mIoU for semantic segmentation and +0.7 mAP for detection), while maintaining competitive accuracy on RGB tasks.

