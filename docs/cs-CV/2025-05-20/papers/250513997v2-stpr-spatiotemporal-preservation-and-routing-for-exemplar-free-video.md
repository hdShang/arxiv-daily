---
layout: default
title: StPR: Spatiotemporal Preservation and Routing for Exemplar-Free Video Class-Incremental Learning
---

# StPR: Spatiotemporal Preservation and Routing for Exemplar-Free Video Class-Incremental Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13997" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13997v2</a>
  <a href="https://arxiv.org/pdf/2505.13997.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13997v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13997v2', 'StPR: Spatiotemporal Preservation and Routing for Exemplar-Free Video Class-Incremental Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huaijie Wang, De Cheng, Guozhang Li, Zhipeng Xu, Lingfeng He, Jie Li, Nannan Wang, Xinbo Gao

**分类**: cs.CV

**发布日期**: 2025-05-20 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出StPR框架以解决视频类增量学习中的遗忘问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视频类增量学习` `时空建模` `无示例学习` `帧共享语义` `专家混合模型` `灾难性遗忘` `动态路由` `深度学习`

## 📋 核心要点

1. 现有视频类增量学习方法依赖示例重演或静态图像方法，导致内存和隐私问题，且无法有效捕捉时空动态。
2. 论文提出的StPR框架通过帧共享语义蒸馏和时间分解的专家混合模型，解决了时空信息的保留与路由问题。
3. 在UCF101、HMDB51和Kinetics400数据集上的实验表明，StPR在性能上超越了现有基线，并提高了可解释性和效率。

## 📝 摘要（中文）

视频类增量学习（VCIL）旨在开发能够持续学习新动作类别的模型，而不遗忘先前获得的知识。与传统的类增量学习（CIL）不同，VCIL引入了时空结构的复杂性，使得在有效捕捉帧共享语义和时间动态的同时，减轻灾难性遗忘变得尤为困难。现有方法依赖于示例重演，存在内存和隐私问题，或采用静态图像方法，忽视了时间建模。为了解决这些局限性，我们提出了时空保留与路由（StPR）框架，明确解耦并保留时空信息。我们引入了帧共享语义蒸馏（FSSD），通过联合考虑语义敏感性和分类贡献，识别出语义稳定的重要通道。其次，我们设计了基于时间分解的专家混合模型（TD-MoE），根据时间动态动态路由任务特定专家，实现无任务ID或存储示例的推理。StPR有效利用空间语义和时间动态，达成统一的无示例VCIL框架。

## 🔬 方法详解

**问题定义**：论文要解决的问题是视频类增量学习中的灾难性遗忘，现有方法往往依赖示例重演或静态图像方法，无法有效捕捉时空动态，导致知识遗忘和隐私问题。

**核心思路**：论文的核心思路是提出一个统一的无示例VCIL框架StPR，通过帧共享语义蒸馏和时间分解的专家混合模型，明确解耦并保留时空信息，从而有效应对灾难性遗忘。

**技术框架**：整体架构包括两个主要模块：帧共享语义蒸馏（FSSD）用于识别和保留重要的语义通道，时间分解的专家混合模型（TD-MoE）用于动态路由任务特定专家。

**关键创新**：最重要的技术创新点在于无示例的学习方式，FSSD和TD-MoE的结合使得模型能够在不依赖存储示例的情况下，灵活适应新任务并保留旧知识。

**关键设计**：关键设计包括对FSSD的正则化策略，以保持语义通道的稳定性，以及TD-MoE的动态路由机制，确保根据时间动态选择最合适的专家进行推理。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，StPR在UCF101、HMDB51和Kinetics400数据集上均超越了现有基线，具体提升幅度达到XX%，同时在可解释性和效率方面也有显著改善，验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、运动分析和人机交互等场景，能够帮助系统在不断变化的环境中持续学习新动作类别，提升智能系统的适应能力和实用性。未来，StPR框架有望推动视频理解和增量学习技术的进一步发展。

## 📄 摘要（原文）

> Video Class-Incremental Learning (VCIL) seeks to develop models that continuously learn new action categories over time without forgetting previously acquired knowledge. Unlike traditional Class-Incremental Learning (CIL), VCIL introduces the added complexity of spatiotemporal structures, making it particularly challenging to mitigate catastrophic forgetting while effectively capturing both frame-shared semantics and temporal dynamics. Existing approaches either rely on exemplar rehearsal, raising concerns over memory and privacy, or adapt static image-based methods that neglect temporal modeling. To address these limitations, we propose Spatiotemporal Preservation and Routing (StPR), a unified and exemplar-free VCIL framework that explicitly disentangles and preserves spatiotemporal information. First, we introduce Frame-Shared Semantics Distillation (FSSD), which identifies semantically stable and meaningful channels by jointly considering semantic sensitivity and classification contribution. These important semantic channels are selectively regularized to maintain prior knowledge while allowing for adaptation. Second, we design a Temporal Decomposition-based Mixture-of-Experts (TD-MoE), which dynamically routes task-specific experts based on their temporal dynamics, enabling inference without task ID or stored exemplars. Together, StPR effectively leverages spatial semantics and temporal dynamics, achieving a unified, exemplar-free VCIL framework. Extensive experiments on UCF101, HMDB51, and Kinetics400 show that our method outperforms existing baselines while offering improved interpretability and efficiency in VCIL. Code is available in the supplementary materials.

