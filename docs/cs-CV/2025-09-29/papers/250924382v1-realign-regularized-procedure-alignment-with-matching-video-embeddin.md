---
layout: default
title: "REALIGN: Regularized Procedure Alignment with Matching Video Embeddings via Partial Gromov-Wasserstein Optimal Transport"
---

# REALIGN: Regularized Procedure Alignment with Matching Video Embeddings via Partial Gromov-Wasserstein Optimal Transport

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24382" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24382v1</a>
  <a href="https://arxiv.org/pdf/2509.24382.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24382v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24382v1', 'REALIGN: Regularized Procedure Alignment with Matching Video Embeddings via Partial Gromov-Wasserstein Optimal Transport')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Soumyadeep Chandra, Kaushik Roy

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-29

**备注**: 10 pages, 4 figures, 6 tables

---

## 💡 一句话要点

**REALIGN：基于正则化融合偏Gromov-Wasserstein最优传输的程序视频对齐方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `程序视频学习` `自监督学习` `最优传输` `Gromov-Wasserstein` `视频对齐` `时间关系建模` `对比学习`

## 📋 核心要点

1. 现有程序视频学习方法难以处理真实世界教学视频中常见的背景片段、重复动作和乱序步骤。
2. REALIGN通过正则化融合偏Gromov-Wasserstein最优传输，联合建模视觉对应关系和时间关系，实现鲁棒对齐。
3. 实验表明，REALIGN在多个基准测试中显著提升了F1分数和时间IoU，并生成了更易解释的传输图。

## 📝 摘要（中文）

从程序视频中学习是自监督表征学习的核心挑战，因为真实世界的教学数据通常包含背景片段、重复动作和乱序步骤。这种可变性违反了许多对齐方法所基于的强单调性假设。现有的先进方法，如OPEL，利用Kantorovich最优传输（KOT）来构建帧到帧的对应关系，但仅依赖于特征相似性，而未能捕捉任务的更高阶时间结构。本文提出了REALIGN，一个基于正则化融合偏Gromov-Wasserstein最优传输（R-FPGWOT）的程序学习自监督框架。与KOT相比，我们的公式在部分对齐方案下联合建模视觉对应关系和时间关系，从而能够稳健地处理教学视频中常见的无关帧、重复动作和非单调步骤顺序。为了稳定训练，我们将FPGWOT距离与序列间对比学习相结合，避免了对多个正则化器的需求，并防止崩溃到退化解。在以自我为中心的（EgoProceL）和第三人称（ProceL，CrossTask）基准测试中，REALIGN实现了高达18.9%的平均F1分数提升和超过30%的时间IoU增益，同时产生了更易于解释的传输图，这些传输图保留了关键步骤顺序并滤除了噪声。

## 🔬 方法详解

**问题定义**：论文旨在解决程序视频学习中，由于视频包含无关帧、重复动作和乱序步骤，导致现有对齐方法性能下降的问题。现有方法如OPEL仅依赖特征相似性，忽略了视频的时间结构，无法有效处理这些问题。

**核心思路**：论文的核心思路是利用正则化融合偏Gromov-Wasserstein最优传输（R-FPGWOT），在部分对齐方案下，同时考虑视觉特征的相似性和视频帧之间的时间关系。通过偏最优传输，可以处理无关帧和重复动作；通过Gromov-Wasserstein最优传输，可以建模时间结构。

**技术框架**：REALIGN框架包含以下主要步骤：1) 使用视频嵌入模型提取视频帧的视觉特征；2) 构建视觉相似性矩阵和时间关系矩阵；3) 使用R-FPGWOT计算两个视频之间的传输矩阵，该矩阵表示帧之间的对应关系；4) 使用传输矩阵进行程序学习任务，如视频检索或步骤预测。同时，为了稳定训练，引入了序列间对比学习。

**关键创新**：最重要的创新点在于R-FPGWOT的使用，它将视觉相似性和时间关系融合到一个统一的优化框架中，并允许部分对齐。与传统的Kantorovich最优传输相比，R-FPGWOT能够更好地处理真实世界程序视频中的噪声和变化。

**关键设计**：R-FPGWOT的损失函数包含三部分：视觉相似性损失、时间关系损失和正则化项。视觉相似性损失衡量对应帧的视觉特征相似度；时间关系损失衡量对应帧之间时间关系的匹配程度；正则化项用于防止传输矩阵过于稀疏或集中。序列间对比学习通过最大化相似视频嵌入的相似度，最小化不相似视频嵌入的相似度，来稳定训练过程。

## 📊 实验亮点

REALIGN在EgoProceL、ProceL和CrossTask三个基准数据集上进行了评估，结果表明，REALIGN显著优于现有方法。在平均F1分数上，REALIGN取得了高达18.9%的提升；在时间IoU上，REALIGN取得了超过30%的增益。此外，REALIGN生成的传输图更易于解释，能够准确地反映视频的关键步骤顺序，并有效地滤除噪声。

## 🎯 应用场景

REALIGN在机器人学习、自动驾驶、医疗手术分析等领域具有广泛的应用前景。例如，可以用于训练机器人执行复杂任务，通过学习人类的演示视频，自动生成机器人的控制策略。在医疗领域，可以用于分析手术视频，评估医生的操作水平，并提供手术指导。该研究有助于提高人工智能系统的自主学习能力和泛化能力。

## 📄 摘要（原文）

> Learning from procedural videos remains a core challenge in self-supervised representation learning, as real-world instructional data often contains background segments, repeated actions, and steps presented out of order. Such variability violates the strong monotonicity assumptions underlying many alignment methods. Prior state-of-the-art approaches, such as OPEL, leverage Kantorovich Optimal Transport (KOT) to build frame-to-frame correspondences, but rely solely on feature similarity and fail to capture the higher-order temporal structure of a task. In this paper, we introduce REALIGN, a self-supervised framework for procedure learning based on Regularized Fused Partial Gromov-Wasserstein Optimal Transport (R-FPGWOT). In contrast to KOT, our formulation jointly models visual correspondences and temporal relations under a partial alignment scheme, enabling robust handling of irrelevant frames, repeated actions, and non-monotonic step orders common in instructional videos. To stabilize training, we integrate FPGWOT distances with inter-sequence contrastive learning, avoiding the need for multiple regularizers and preventing collapse to degenerate solutions. Across egocentric (EgoProceL) and third-person (ProceL, CrossTask) benchmarks, REALIGN achieves up to 18.9% average F1-score improvements and over 30% temporal IoU gains, while producing more interpretable transport maps that preserve key-step orderings and filter out noise.

