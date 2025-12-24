---
layout: default
title: "MovSemCL: Movement-Semantics Contrastive Learning for Trajectory Similarity"
---

# MovSemCL: Movement-Semantics Contrastive Learning for Trajectory Similarity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12061" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12061v1</a>
  <a href="https://arxiv.org/pdf/2511.12061.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12061v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.12061v1', 'MovSemCL: Movement-Semantics Contrastive Learning for Trajectory Similarity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhichen Lai, Hua Lu, Huan Li, Jialiang Li, Christian S. Jensen

**分类**: cs.CV, cs.AI, cs.DB

**发布日期**: 2025-11-15

**备注**: 8 pages, 6 figures; accepted by AAAI 2026 as an Oral paper

---

## 💡 一句话要点

**提出MovSemCL框架，通过运动语义对比学习提升轨迹相似度计算性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `轨迹相似度` `对比学习` `运动语义` `注意力机制` `数据增强` `轨迹聚类` `异常检测`

## 📋 核心要点

1. 现有轨迹相似度计算方法在轨迹语义建模、计算效率和数据增强策略上存在不足。
2. MovSemCL通过运动语义特征提取、分层注意力编码和曲率引导增强来提升轨迹相似度计算。
3. 实验表明，MovSemCL在相似度搜索和启发式近似任务上优于现有方法，并降低了推理延迟。

## 📝 摘要（中文）

轨迹相似度计算是聚类、预测和异常检测等任务的基础。然而，现有的基于学习的方法存在三个主要限制：(1) 轨迹语义和层次结构建模不足，缺乏运动动态提取和多尺度结构表示；(2) 由于逐点编码导致计算成本高昂；(3) 使用物理上不合理的增强方式，扭曲了轨迹语义。为了解决这些问题，我们提出了MovSemCL，一个用于轨迹相似度计算的运动语义对比学习框架。MovSemCL首先将原始GPS轨迹转换为运动语义特征，然后将其分割成patches。接下来，MovSemCL采用patch内和patch间的注意力机制来编码局部和全局轨迹模式，从而实现高效的分层表示并降低计算成本。此外，MovSemCL包含一种曲率引导的增强策略，该策略保留信息丰富的片段（例如，转弯和交叉口）并屏蔽冗余片段，从而生成物理上合理的增强视图。在真实世界数据集上的实验表明，MovSemCL能够优于最先进的方法，在相似度搜索任务中实现接近理想值1的平均排名，并在启发式近似方面提高高达20.3%，同时将推理延迟降低高达43.4%。

## 🔬 方法详解

**问题定义**：现有基于学习的轨迹相似度计算方法，无法充分建模轨迹的运动语义和层次结构，导致相似度计算精度不高。同时，逐点编码方式计算成本高昂，且数据增强方法不合理，会扭曲轨迹的真实语义。因此，需要一种能够有效提取轨迹语义、降低计算成本并进行合理数据增强的轨迹相似度计算方法。

**核心思路**：MovSemCL的核心思路是通过运动语义特征提取，将原始GPS轨迹转换为更具表达力的特征表示。然后，利用分层注意力机制，对轨迹的局部和全局模式进行编码，从而实现高效的层次化表示。此外，采用曲率引导的数据增强策略，保留轨迹中的关键信息，并屏蔽冗余信息，生成物理上合理的增强视图。

**技术框架**：MovSemCL框架主要包含以下几个阶段：1) 运动语义特征提取：将原始GPS轨迹转换为运动语义特征。2) 轨迹分块：将轨迹分割成patches。3) 分层注意力编码：利用patch内和patch间的注意力机制，对局部和全局轨迹模式进行编码。4) 曲率引导数据增强：根据轨迹的曲率，保留信息丰富的片段，并屏蔽冗余片段。5) 对比学习：通过对比学习，学习轨迹的相似度表示。

**关键创新**：MovSemCL的关键创新在于：1) 提出了运动语义特征，能够更好地表达轨迹的运动信息。2) 采用了分层注意力机制，能够有效地编码轨迹的局部和全局模式。3) 设计了曲率引导的数据增强策略，能够生成物理上合理的增强视图。

**关键设计**：MovSemCL的关键设计包括：1) 运动语义特征的具体计算方法，例如速度、加速度、方向等。2) patch的大小和数量。3) 注意力机制的具体实现方式，例如Transformer。4) 曲率的计算方法和阈值设定。5) 对比学习的损失函数，例如InfoNCE。

## 📊 实验亮点

实验结果表明，MovSemCL在真实世界数据集上优于最先进的方法，在相似度搜索任务中实现了接近理想值1的平均排名，并在启发式近似方面提高了高达20.3%，同时将推理延迟降低了高达43.4%。这些结果表明，MovSemCL能够有效地提高轨迹相似度计算的精度和效率。

## 🎯 应用场景

MovSemCL可应用于轨迹聚类、轨迹预测、异常轨迹检测等领域。例如，在交通管理中，可以利用MovSemCL对车辆轨迹进行聚类，从而分析交通模式；在自动驾驶中，可以利用MovSemCL预测车辆的未来轨迹，从而提高驾驶安全性；在金融风控中，可以利用MovSemCL检测异常交易轨迹，从而防止欺诈行为。该研究具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Trajectory similarity computation is fundamental functionality that is used for, e.g., clustering, prediction, and anomaly detection. However, existing learning-based methods exhibit three key limitations: (1) insufficient modeling of trajectory semantics and hierarchy, lacking both movement dynamics extraction and multi-scale structural representation; (2) high computational costs due to point-wise encoding; and (3) use of physically implausible augmentations that distort trajectory semantics. To address these issues, we propose MovSemCL, a movement-semantics contrastive learning framework for trajectory similarity computation. MovSemCL first transforms raw GPS trajectories into movement-semantics features and then segments them into patches. Next, MovSemCL employs intra- and inter-patch attentions to encode local as well as global trajectory patterns, enabling efficient hierarchical representation and reducing computational costs. Moreover, MovSemCL includes a curvature-guided augmentation strategy that preserves informative segments (e.g., turns and intersections) and masks redundant ones, generating physically plausible augmented views. Experiments on real-world datasets show that MovSemCL is capable of outperforming state-of-the-art methods, achieving mean ranks close to the ideal value of 1 at similarity search tasks and improvements by up to 20.3% at heuristic approximation, while reducing inference latency by up to 43.4%.

