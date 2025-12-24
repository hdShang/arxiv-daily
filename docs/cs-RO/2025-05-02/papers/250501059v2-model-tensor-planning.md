---
layout: default
title: Model Tensor Planning
---

# Model Tensor Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01059" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01059v2</a>
  <a href="https://arxiv.org/pdf/2505.01059.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01059v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01059v2', 'Model Tensor Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: An T. Le, Khai Nguyen, Minh Nhat Vu, João Carvalho, Jan Peters

**分类**: cs.RO, cs.AI, cs.LG, eess.SY

**发布日期**: 2025-05-02 (更新: 2025-08-02)

**备注**: 24 pages, 9 figures. Accepted to TMLR

---

## 💡 一句话要点

**提出模型张量规划以解决采样效率低下问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `张量采样` `机器人控制` `高熵轨迹` `实时控制` `在线领域随机化` `B样条` `Akima样条`

## 📋 核心要点

1. 现有的基于采样的模型预测控制方法在探索能力上存在不足，导致在复杂任务中的表现受限。
2. 论文提出的模型张量规划（MTP）通过结构化张量采样和高熵控制轨迹生成，增强了探索能力。
3. 实验结果显示，MTP在多种复杂机器人任务中表现优于传统MPC和进化策略，提升了任务成功率和控制鲁棒性。

## 📝 摘要（中文）

基于采样的模型预测控制（MPC）在非线性和接触丰富的机器人任务中表现出色，但由于局部贪婪采样方案，探索能力常常不足。我们提出了模型张量规划（MTP），这是一个新颖的基于采样的MPC框架，通过结构化张量采样引入高熵控制轨迹生成。MTP通过在随机化的多部分图上采样，并使用B样条和Akima样条插值控制轨迹，确保了平滑和全球多样化的控制候选。实验结果表明，MTP在任务成功率和控制鲁棒性方面超越了标准MPC和进化策略基线。

## 🔬 方法详解

**问题定义**：本论文旨在解决基于采样的模型预测控制（MPC）在非线性和接触丰富的机器人任务中探索能力不足的问题。现有方法常常依赖于局部贪婪采样，导致控制轨迹的多样性和全局性不足。

**核心思路**：模型张量规划（MTP）通过引入结构化张量采样和高熵控制轨迹生成，旨在提高控制候选的多样性和光滑性。通过在随机化的多部分图上进行采样，并使用B样条和Akima样条进行轨迹插值，MTP能够生成更具探索性的控制策略。

**技术框架**：MTP的整体架构包括高熵控制轨迹生成、基于张量的采样策略和混合策略。首先，通过随机化的多部分图进行采样，然后使用B样条和Akima样条进行轨迹插值，最后结合局部和全局样本的混合策略进行控制更新。

**关键创新**：MTP的主要创新在于其结构化张量采样方法和混合策略，这与传统的MPC方法形成鲜明对比，后者通常缺乏有效的全局探索能力。MTP在理论上证明了在无限张量深度和宽度的极限下，能够实现路径覆盖和最大熵。

**关键设计**：MTP的设计包括简单的β混合策略，该策略在修改的交叉熵方法（CEM）更新中平衡了局部利用和全局探索。此外，MTP的实现完全向量化，使用JAX并兼容MuJoCo XLA，支持即时编译和批量回放，以实现实时控制。实验中对张量采样结构、样条插值选择和混合策略进行了设计和敏感性消融实验，验证了其有效性。

## 📊 实验亮点

实验结果表明，MTP在多种复杂机器人任务中超越了标准MPC和进化策略基线，任务成功率和控制鲁棒性显著提升。具体而言，MTP在灵巧操作和人形机器人行走任务中表现出更高的成功率，验证了其在实际应用中的有效性。

## 🎯 应用场景

模型张量规划（MTP）在机器人控制领域具有广泛的应用潜力，尤其是在需要高效探索和复杂任务执行的场景中，如灵巧的手部操作和人形机器人行走。其可扩展性和鲁棒性使其适合于实时控制和在线领域随机化，未来可能在自主机器人、智能制造和人机交互等领域发挥重要作用。

## 📄 摘要（原文）

> Sampling-based model predictive control (MPC) offers strong performance in nonlinear and contact-rich robotic tasks, yet often suffers from poor exploration due to locally greedy sampling schemes. We propose \emph{Model Tensor Planning} (MTP), a novel sampling-based MPC framework that introduces high-entropy control trajectory generation through structured tensor sampling. By sampling over randomized multipartite graphs and interpolating control trajectories with B-splines and Akima splines, MTP ensures smooth and globally diverse control candidates. We further propose a simple $β$-mixing strategy that blends local exploitative and global exploratory samples within the modified Cross-Entropy Method (CEM) update, balancing control refinement and exploration. Theoretically, we show that MTP achieves asymptotic path coverage and maximum entropy in the control trajectory space in the limit of infinite tensor depth and width.
>   Our implementation is fully vectorized using JAX and compatible with MuJoCo XLA, supporting \emph{Just-in-time} (JIT) compilation and batched rollouts for real-time control with online domain randomization. Through experiments on various challenging robotic tasks, ranging from dexterous in-hand manipulation to humanoid locomotion, we demonstrate that MTP outperforms standard MPC and evolutionary strategy baselines in task success and control robustness. Design and sensitivity ablations confirm the effectiveness of MTP tensor sampling structure, spline interpolation choices, and mixing strategy. Altogether, MTP offers a scalable framework for robust exploration in model-based planning and control.

