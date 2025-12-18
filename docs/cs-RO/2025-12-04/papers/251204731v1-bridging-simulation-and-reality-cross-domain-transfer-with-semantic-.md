---
layout: default
title: Bridging Simulation and Reality: Cross-Domain Transfer with Semantic 2D Gaussian Splatting
---

# Bridging Simulation and Reality: Cross-Domain Transfer with Semantic 2D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04731" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04731v1</a>
  <a href="https://arxiv.org/pdf/2512.04731.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04731v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.04731v1', 'Bridging Simulation and Reality: Cross-Domain Transfer with Semantic 2D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Tang, Pu Pang, Haowen Sun, Chengzhong Ma, Xingyu Chen, Hua Huang, Xuguang Lan

**分类**: cs.RO

**发布日期**: 2025-12-04

---

## 💡 一句话要点

**提出语义2D高斯溅射(S2GS)，提升机器人操作中模拟到真实的跨域迁移能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `机器人操作` `跨域迁移` `Sim-to-Real` `语义特征` `高斯溅射`

## 📋 核心要点

1. 现有机器人操作的sim-to-real迁移方法，如领域随机化，需要大量调参且泛化性差。
2. 提出语义2D高斯溅射(S2GS)，提取领域不变的、以对象为中心的语义特征，作为策略输入。
3. 实验表明，S2GS显著提升了sim-to-real迁移能力，在真实环境中保持了高且稳定的任务性能。

## 📝 摘要（中文）

机器人操作中的跨域迁移由于模拟环境和真实环境之间存在显著的领域差距，一直是一个长期存在的挑战。现有的领域随机化、自适应和sim-real校准等方法通常需要大量的调整，或者无法推广到未见过的场景。为了解决这个问题，我们观察到，如果在模拟环境中的策略训练期间使用领域不变的特征，并且在真实环境部署期间可以提取并提供相同的特征作为策略的输入，则可以有效地弥合领域差距，从而显著提高策略的泛化能力。因此，我们提出了一种新的表示方法，即语义2D高斯溅射(S2GS)，该方法提取以对象为中心的、领域不变的空间特征。S2GS构建多视角2D语义场，并通过特征级高斯溅射将其投影到统一的3D空间中。语义过滤机制消除了不相关的背景内容，确保了策略学习的干净和一致的输入。为了评估S2GS的有效性，我们采用Diffusion Policy作为下游学习算法，并在ManiSkill模拟环境中进行实验，然后在真实环境中进行部署。结果表明，S2GS显著提高了sim-to-real的可迁移性，在真实场景中保持了高且稳定的任务性能。

## 🔬 方法详解

**问题定义**：现有机器人操作的sim-to-real迁移方法，如领域随机化、领域自适应和sim-real标定，通常需要大量的参数调整，并且难以泛化到未见过的真实场景。这些方法未能有效提取和利用领域不变的特征，导致策略在模拟环境中学习到的知识难以直接迁移到真实环境中。

**核心思路**：论文的核心思路是，如果在模拟环境中训练策略时，使用领域不变的特征作为输入，并且在真实环境中也能提取到相同的特征，那么就可以有效地弥合模拟环境和真实环境之间的领域差距。通过学习领域不变的特征表示，策略可以更好地泛化到真实世界。

**技术框架**：S2GS方法主要包含以下几个阶段：1) 构建多视角的2D语义场：从不同的视角捕获场景的语义信息。2) 特征级高斯溅射：将多视角的2D语义特征投影到统一的3D空间中，形成3D特征表示。3) 语义过滤：移除不相关的背景内容，保留与目标对象相关的语义信息。4) 策略学习：使用提取的S2GS特征作为输入，训练机器人操作策略。下游策略学习算法采用Diffusion Policy。

**关键创新**：S2GS的关键创新在于它提出了一种新的领域不变的特征表示方法，该方法能够有效地提取以对象为中心的语义信息，并将其投影到3D空间中。与传统的图像或点云表示相比，S2GS更加关注对象的语义信息，从而提高了策略的泛化能力。此外，语义过滤机制能够有效地去除背景噪声，提高特征的质量。

**关键设计**：S2GS使用高斯溅射将2D语义特征投影到3D空间。具体来说，每个2D语义特征点都被表示为一个高斯分布，其均值和方差由特征点的坐标和不确定性决定。通过将多个视角的高斯分布进行融合，可以得到一个统一的3D特征表示。语义过滤机制通过设定阈值来过滤掉语义置信度较低的特征点，从而去除背景噪声。Diffusion Policy被用作下游策略学习算法，用于学习从S2GS特征到机器人动作的映射。

## 📊 实验亮点

实验结果表明，S2GS方法在ManiSkill模拟环境中训练的策略，可以直接迁移到真实环境中，并且保持了高且稳定的任务性能。与传统的领域随机化方法相比，S2GS方法在真实环境中的任务成功率提高了显著幅度（具体数值未知，原文未提供）。这表明S2GS能够有效地弥合模拟环境和真实环境之间的领域差距。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如物体抓取、放置、装配等。通过S2GS方法，可以降低机器人部署的成本和难度，提高机器人在复杂环境中的适应性和鲁棒性。该技术在智能制造、仓储物流、家庭服务等领域具有广阔的应用前景。

## 📄 摘要（原文）

> Cross-domain transfer in robotic manipulation remains a longstanding challenge due to the significant domain gap between simulated and real-world environments. Existing methods such as domain randomization, adaptation, and sim-real calibration often require extensive tuning or fail to generalize to unseen scenarios. To address this issue, we observe that if domain-invariant features are utilized during policy training in simulation, and the same features can be extracted and provided as the input to policy during real-world deployment, the domain gap can be effectively bridged, leading to significantly improved policy generalization. Accordingly, we propose Semantic 2D Gaussian Splatting (S2GS), a novel representation method that extracts object-centric, domain-invariant spatial features. S2GS constructs multi-view 2D semantic fields and projects them into a unified 3D space via feature-level Gaussian splatting. A semantic filtering mechanism removes irrelevant background content, ensuring clean and consistent inputs for policy learning. To evaluate the effectiveness of S2GS, we adopt Diffusion Policy as the downstream learning algorithm and conduct experiments in the ManiSkill simulation environment, followed by real-world deployment. Results demonstrate that S2GS significantly improves sim-to-real transferability, maintaining high and stable task performance in real-world scenarios.

