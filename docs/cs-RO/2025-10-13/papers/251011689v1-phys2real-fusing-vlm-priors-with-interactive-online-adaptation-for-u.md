---
layout: default
title: Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for Uncertainty-Aware Sim-to-Real Manipulation
---

# Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for Uncertainty-Aware Sim-to-Real Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11689" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11689v1</a>
  <a href="https://arxiv.org/pdf/2510.11689.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11689v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.11689v1', 'Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for Uncertainty-Aware Sim-to-Real Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**Phys2Real：融合VLM先验与交互式在线自适应，实现不确定性感知的Sim-to-Real操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `Sim-to-Real` `强化学习` `视觉语言模型` `物理参数估计` `不确定性量化`

## 📋 核心要点

1. 现有机器人操作的Sim-to-Real迁移方法在精确动力学任务中面临挑战，难以有效适应真实世界的物理参数不确定性。
2. Phys2Real通过融合VLM先验知识和在线交互数据，实现物理参数的精确估计和不确定性量化，从而提升策略的泛化能力。
3. 实验表明，Phys2Real在平面推移任务中显著优于域随机化基线，验证了VLM先验和在线自适应的有效性。

## 📝 摘要（中文）

直接在真实世界中学习机器人操作策略成本高昂且耗时。虽然在模拟环境中训练的强化学习（RL）策略提供了一种可扩展的替代方案，但有效的sim-to-real迁移仍然具有挑战性，特别是对于需要精确动力学的任务。为了解决这个问题，我们提出了Phys2Real，一种real-to-sim-to-real的RL流程，它结合了视觉语言模型（VLM）推断的物理参数估计与通过不确定性感知融合进行的交互式自适应。我们的方法包括三个核心组成部分：（1）使用3D高斯溅射进行高保真几何重建，（2）VLM推断的物理参数先验分布，以及（3）从交互数据中进行的在线物理参数估计。Phys2Real以可解释的物理参数为条件来训练策略，并通过基于集成的的不确定性量化，利用在线估计来细化VLM预测。在具有不同质心（CoM）的T型块的平面推移任务以及具有偏心质量分布的锤子的推移任务中，Phys2Real相比于域随机化基线取得了显著的改进：底部加权T型块的成功率为100% vs 79%，具有挑战性的顶部加权T型块的成功率为57% vs 23%，锤子推移的平均任务完成速度提高了15%。消融研究表明，VLM和交互信息的结合对于成功至关重要。

## 🔬 方法详解

**问题定义**：现有的Sim-to-Real方法在处理需要精确动力学的操作任务时，往往难以克服模拟环境与真实环境之间的差异。特别是当物体的物理参数（如质心、质量分布）未知或难以精确建模时，训练得到的策略在真实世界中的表现会显著下降。域随机化是一种常用的方法，但其效率较低，且难以覆盖所有可能的物理参数组合。

**核心思路**：Phys2Real的核心思路是利用视觉语言模型（VLM）提供物理参数的先验知识，并结合在线交互数据进行参数估计和策略优化。VLM能够从视觉信息中推断出物体的物理属性，从而缩小搜索空间。在线交互则允许策略在真实环境中不断学习和适应，最终实现鲁棒的Sim-to-Real迁移。通过融合VLM先验和在线估计，Phys2Real能够更有效地处理物理参数的不确定性。

**技术框架**：Phys2Real包含三个主要模块：1) **高保真几何重建**：使用3D高斯溅射技术重建真实环境的几何模型，确保模拟环境与真实环境在视觉上的一致性。2) **VLM先验推断**：利用VLM从视觉信息中推断物体的物理参数分布，为后续的在线估计提供先验知识。3) **在线物理参数估计**：通过与真实环境的交互，收集数据并使用集成方法进行物理参数估计，同时量化估计的不确定性。最终，策略以可解释的物理参数为条件，并利用在线估计细化VLM预测。

**关键创新**：Phys2Real的关键创新在于融合了VLM先验知识和在线交互数据，实现了一种不确定性感知的Sim-to-Real迁移方法。与传统的域随机化方法相比，Phys2Real能够更有效地利用先验知识，并根据真实环境的反馈进行自适应调整。此外，Phys2Real还通过集成方法量化了物理参数估计的不确定性，从而提高了策略的鲁棒性。

**关键设计**：在VLM先验推断阶段，论文使用了CLIP等预训练的VLM模型，并针对特定任务进行了微调。在线物理参数估计阶段，论文采用了集成方法，例如Bootstrap或Dropout，来估计参数的不确定性。策略网络以物理参数和不确定性作为输入，并使用强化学习算法（如PPO）进行训练。损失函数的设计考虑了任务的奖励和物理参数估计的准确性。

## 📊 实验亮点

Phys2Real在平面推移任务中取得了显著的性能提升。对于底部加权的T型块，Phys2Real的成功率为100%，而域随机化基线为79%。对于更具挑战性的顶部加权T型块，Phys2Real的成功率为57%，而域随机化基线仅为23%。此外，Phys2Real在锤子推移任务中，平均任务完成速度比域随机化基线提高了15%。

## 🎯 应用场景

Phys2Real具有广泛的应用前景，例如在工业自动化、家庭服务机器人和医疗机器人等领域。该方法可以用于训练机器人执行各种操作任务，例如装配、抓取和操作工具。通过结合VLM先验和在线自适应，Phys2Real可以显著提高机器人在真实世界中的操作性能和鲁棒性，降低部署成本。

## 📄 摘要（原文）

> Learning robotic manipulation policies directly in the real world can be expensive and time-consuming. While reinforcement learning (RL) policies trained in simulation present a scalable alternative, effective sim-to-real transfer remains challenging, particularly for tasks that require precise dynamics. To address this, we propose Phys2Real, a real-to-sim-to-real RL pipeline that combines vision-language model (VLM)-inferred physical parameter estimates with interactive adaptation through uncertainty-aware fusion. Our approach consists of three core components: (1) high-fidelity geometric reconstruction with 3D Gaussian splatting, (2) VLM-inferred prior distributions over physical parameters, and (3) online physical parameter estimation from interaction data. Phys2Real conditions policies on interpretable physical parameters, refining VLM predictions with online estimates via ensemble-based uncertainty quantification. On planar pushing tasks of a T-block with varying center of mass (CoM) and a hammer with an off-center mass distribution, Phys2Real achieves substantial improvements over a domain randomization baseline: 100% vs 79% success rate for the bottom-weighted T-block, 57% vs 23% in the challenging top-weighted T-block, and 15% faster average task completion for hammer pushing. Ablation studies indicate that the combination of VLM and interaction information is essential for success. Project website: https://phys2real.github.io/ .

