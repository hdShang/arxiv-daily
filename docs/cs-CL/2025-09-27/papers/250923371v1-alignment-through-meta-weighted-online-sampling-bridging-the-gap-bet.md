---
layout: default
title: "Alignment through Meta-Weighted Online Sampling: Bridging the Gap between Data Generation and Preference Optimization"
---

# Alignment through Meta-Weighted Online Sampling: Bridging the Gap between Data Generation and Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23371" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23371v1</a>
  <a href="https://arxiv.org/pdf/2509.23371.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23371v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23371v1', 'Alignment through Meta-Weighted Online Sampling: Bridging the Gap between Data Generation and Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junming Yang, Ning Xu, Biao Liu, Shiqi Qiao, Xin Geng

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出MetaAPO，通过元加权在线采样弥合数据生成与偏好优化之间的差距**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏好优化` `大型语言模型对齐` `元学习` `在线采样` `数据分布匹配`

## 📋 核心要点

1. 现有偏好优化方法难以适应模型动态学习状态，导致离线数据与在线策略之间存在分布不匹配。
2. MetaAPO通过引入元学习器动态评估在线采样的收益，指导数据生成并分配样本权重，平衡数据质量与分布。
3. 实验表明，MetaAPO在多个基准测试中超越现有方法，并显著降低了在线标注成本。

## 📝 摘要（中文）

偏好优化对于使大型语言模型（LLMs）与人类价值观和意图对齐至关重要。此过程中的一个重大挑战是预先收集的离线偏好数据与不断演变的模型策略之间的分布不匹配。现有方法试图使用静态启发式方法或解耦的在线采样策略来缩小这种差距，但它们通常无法适应模型的动态学习状态。为了弥合这一差距，我们提出了一种新颖的框架Meta加权自适应偏好优化（MetaAPO），该框架动态地将数据生成与模型训练相结合。MetaAPO采用轻量级元学习器，作为“对齐差距估计器”，以评估在线策略采样相对于离线数据的潜在益处。这指导有针对性的在线生成，并将样本级元权重分配给优化目标，从而动态平衡在线和离线数据的质量和分布。在AlpacaEval 2、Arena-Hard和MT-Bench上的实验表明，MetaAPO在各种设置下始终优于现有的偏好优化方法，同时降低了42%的在线标注成本。

## 🔬 方法详解

**问题定义**：现有偏好优化方法在对齐大型语言模型时，面临离线偏好数据与模型策略演进之间的分布差异问题。静态启发式或解耦的在线采样策略无法有效适应模型学习状态，导致对齐效果受限。

**核心思路**：MetaAPO的核心在于动态耦合数据生成与模型训练，通过元学习器估计在线采样的价值，从而指导数据生成并动态调整在线和离线数据的权重。这种自适应方法旨在弥合数据分布差异，提升对齐效果。

**技术框架**：MetaAPO框架包含以下主要模块：1) 偏好数据收集模块，包括离线数据和在线采样数据；2) 元学习器，用于估计在线采样的收益；3) 权重分配模块，根据元学习器的输出，为在线和离线数据分配样本级权重；4) 偏好优化模块，使用加权后的数据训练语言模型。整体流程是，模型训练过程中，元学习器动态评估在线采样的价值，指导在线数据生成，并调整优化目标中在线和离线数据的权重。

**关键创新**：MetaAPO的关键创新在于引入了元学习器作为“对齐差距估计器”，动态评估在线采样的价值。与现有方法采用静态策略或解耦方式不同，MetaAPO实现了数据生成与模型训练的动态耦合，从而更好地适应模型学习状态。

**关键设计**：Meta学习器是一个轻量级网络，输入是当前模型的策略和离线数据，输出是在线采样的预期收益。损失函数设计为最大化在线采样的收益，同时最小化与离线数据的差异。样本级权重根据元学习器的输出进行调整，高收益的在线样本获得更高的权重。

## 📊 实验亮点

实验结果表明，MetaAPO在AlpacaEval 2、Arena-Hard和MT-Bench等基准测试中，始终优于现有的偏好优化方法。更重要的是，MetaAPO在提升性能的同时，还降低了42%的在线标注成本，表明其在实际应用中具有更高的效率和经济性。

## 🎯 应用场景

MetaAPO可应用于各种需要对齐大型语言模型与人类价值观和意图的场景，例如对话系统、内容生成、智能助手等。通过降低在线标注成本并提升对齐效果，MetaAPO有助于开发更安全、更可靠、更符合人类期望的AI系统。该方法也为其他强化学习对齐任务提供了借鉴。

## 📄 摘要（原文）

> Preference optimization is crucial for aligning large language models (LLMs) with human values and intentions. A significant challenge in this process is the distribution mismatch between pre-collected offline preference data and the evolving model policy. Existing methods attempt to reduce this gap using static heuristics or decoupled online sampling strategies, but they often fail to adapt to the model's dynamic learning state. To bridge this gap, we propose Meta-Weighted Adaptive Preference Optimization (MetaAPO), a novel framework that dynamically couples data generation with model training. MetaAPO employs a lightweight meta-learner, as an "alignment gap estimator", to evaluate the potential benefits of on-policy sampling in relation to offline data. This guides targeted online generation and assigns sample-wise meta-weights to the optimization objective, dynamically balancing the quality and distribution of online and offline data. Experiments on AlpacaEval 2, Arena-Hard and MT-Bench demonstrate that MetaAPO consistently outperforms existing preference optimization approaches across various settings, while reducing 42% in online annotation costs.

