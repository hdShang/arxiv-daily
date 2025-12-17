---
layout: default
title: DoGCLR: Dominance-Game Contrastive Learning Network for Skeleton-Based Action Recognition
---

# DoGCLR: Dominance-Game Contrastive Learning Network for Skeleton-Based Action Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14179" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14179v2</a>
  <a href="https://arxiv.org/pdf/2511.14179.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14179v2" onclick="toggleFavorite(this, '2511.14179v2', 'DoGCLR: Dominance-Game Contrastive Learning Network for Skeleton-Based Action Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanshan Li, Ke Ma, Miaomiao Wei, Linhui Dai

**分类**: cs.CV

**发布日期**: 2025-11-18 (更新: 2025-11-19)

**备注**: 14 pages, 7 figures, journal

---

## 💡 一句话要点

**提出DoGCLR，通过支配博弈对比学习提升骨骼动作识别性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `骨骼动作识别` `对比学习` `自监督学习` `支配博弈` `时空权重` `负样本选择` `深度学习`

## 📋 核心要点

1. 现有骨骼动作识别的对比学习方法对所有骨骼区域进行统一处理，忽略了关键运动信息。
2. DoGCLR通过支配博弈建模正负样本构建，利用时空权重定位和熵驱动策略选择信息丰富的负样本。
3. 在NTU RGB+D和PKU-MMD数据集上，DoGCLR的性能超越了现有方法，尤其在更具挑战性的场景中表现出更强的鲁棒性。

## 📝 摘要（中文）

本文提出了一种基于支配博弈对比学习的骨骼动作识别自监督框架DoGCLR。该方法将正负样本的构建建模为一个动态的支配博弈，通过样本间的相互作用达到语义保持和判别能力之间的平衡。具体而言，时空双重权重定位机制用于识别关键运动区域，并指导区域相关的增强，从而在保持语义的同时增强运动多样性。同时，一种熵驱动的支配策略管理记忆库，保留高熵（难）负样本，替换低熵（弱）负样本，确保持续暴露于信息丰富的对比信号。在NTU RGB+D和PKU-MMD数据集上的大量实验表明，DoGCLR优于现有方法。

## 🔬 方法详解

**问题定义**：现有基于骨骼的动作识别自监督对比学习方法，通常对所有骨骼区域进行无差别处理，忽略了不同区域对动作识别的重要性。此外，使用先进先出（FIFO）队列存储负样本，导致信息量不足的负样本被保留，而更有价值的负样本被替换，影响了对比学习的效果。

**核心思路**：DoGCLR的核心思想是将正负样本的构建过程建模为一个动态的支配博弈。在这个博弈中，正样本和负样本相互作用，通过迭代更新达到一个平衡状态，从而同时保证语义信息的保留和判别能力的提升。通过这种方式，模型能够学习到更具区分性的特征表示。

**技术框架**：DoGCLR框架主要包含两个核心模块：时空双重权重定位机制和熵驱动的支配策略。时空双重权重定位机制用于识别骨骼序列中的关键运动区域，并根据这些区域的重要性进行数据增强。熵驱动的支配策略则用于管理记忆库中的负样本，保留信息量大的“难”负样本，替换信息量小的“弱”负样本。这两个模块共同作用，提升对比学习的效果。

**关键创新**：DoGCLR的关键创新在于将支配博弈理论引入到对比学习框架中，并设计了时空双重权重定位机制和熵驱动的支配策略。与传统的对比学习方法相比，DoGCLR能够更有效地利用骨骼序列中的运动信息，并选择更具信息量的负样本，从而提升模型的性能。

**关键设计**：时空双重权重定位机制通过学习每个关节在不同时间和空间上的权重，来确定关键运动区域。熵驱动的支配策略使用交叉熵来衡量负样本的信息量，并根据熵值的大小来决定是否保留或替换负样本。损失函数采用InfoNCE损失，用于最大化正样本之间的相似性，同时最小化正样本与负样本之间的相似性。

## 📊 实验亮点

DoGCLR在NTU RGB+D 60 X-Sub/X-View上分别取得了81.1%/89.4%的准确率，在NTU RGB+D 120 X-Sub/X-Set上分别取得了71.2%/75.5%的准确率，相较于现有最优方法分别提升了0.1%、2.7%、1.1%和2.3%。在PKU-MMD Part II上，DoGCLR的准确率提升了1.9%，表明其在更具挑战性的场景下具有更强的鲁棒性。

## 🎯 应用场景

DoGCLR在骨骼动作识别领域具有广泛的应用前景，可应用于智能监控、人机交互、康复训练、游戏娱乐等领域。通过识别和理解人体的动作，可以实现异常行为检测、手势控制、运动评估等功能，具有重要的实际应用价值和商业潜力。

## 📄 摘要（原文）

> Existing self-supervised contrastive learning methods for skeleton-based action recognition often process all skeleton regions uniformly, and adopt a first-in-first-out (FIFO) queue to store negative samples, which leads to motion information loss and non-optimal negative sample selection. To address these challenges, this paper proposes Dominance-Game Contrastive Learning network for skeleton-based action Recognition (DoGCLR), a self-supervised framework based on game theory. DoGCLR models the construction of positive and negative samples as a dynamic Dominance Game, where both sample types interact to reach an equilibrium that balances semantic preservation and discriminative strength. Specifically, a spatio-temporal dual weight localization mechanism identifies key motion regions and guides region-wise augmentations to enhance motion diversity while maintaining semantics. In parallel, an entropy-driven dominance strategy manages the memory bank by retaining high entropy (hard) negatives and replacing low-entropy (weak) ones, ensuring consistent exposure to informative contrastive signals. Extensive experiments are conducted on NTU RGB+D and PKU-MMD datasets. On NTU RGB+D 60 X-Sub/X-View, DoGCLR achieves 81.1%/89.4% accuracy, and on NTU RGB+D 120 X-Sub/X-Set, DoGCLR achieves 71.2%/75.5% accuracy, surpassing state-of-the-art methods by 0.1%, 2.7%, 1.1%, and 2.3%, respectively. On PKU-MMD Part I/Part II, DoGCLR performs comparably to the state-of-the-art methods and achieves a 1.9% higher accuracy on Part II, highlighting its strong robustness on more challenging scenarios.

