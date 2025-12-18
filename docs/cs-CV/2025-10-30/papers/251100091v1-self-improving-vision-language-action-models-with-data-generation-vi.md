---
layout: default
title: Self-Improving Vision-Language-Action Models with Data Generation via Residual RL
---

# Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00091" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00091v1</a>
  <a href="https://arxiv.org/pdf/2511.00091.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00091v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.00091v1', 'Self-Improving Vision-Language-Action Models with Data Generation via Residual RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenli Xiao, Haotian Lin, Andy Peng, Haoru Xue, Tairan He, Yuqi Xie, Fengyuan Hu, Jimmy Wu, Zhengyi Luo, Linxi "Jim" Fan, Guanya Shi, Yuke Zhu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-30

**备注**: 26 pages

---

## 💡 一句话要点

**提出PLD框架，通过残差强化学习和数据生成自提升视觉-语言-动作模型**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `残差强化学习` `数据生成` `自提升学习` `机器人操作`

## 📋 核心要点

1. 现有VLA模型依赖于昂贵的人工标注数据进行监督微调，限制了模型的可扩展性和泛化能力。
2. PLD框架通过残差强化学习探索模型失败区域，并利用分布感知的数据收集方法生成高质量训练数据。
3. 实验表明，PLD在多个机器人操作任务上显著提升了VLA模型的性能，包括模拟和真实环境。

## 📝 摘要（中文）

监督微调(SFT)已成为大型视觉-语言-动作(VLA)模型的事实标准后训练策略，但其对昂贵的人工演示的依赖限制了可扩展性和泛化性。我们提出了Probe, Learn, Distill (PLD)，一个三阶段即插即用框架，通过残差强化学习(RL)和分布感知数据收集来改进VLA模型。在第一阶段，我们训练轻量级残差actor来探测VLA通用模型的失败区域。在第二阶段，我们使用混合rollout方案，该方案将收集到的轨迹与通用模型的部署分布对齐，同时捕获恢复行为。在第三阶段，我们使用标准SFT将精心设计的轨迹提炼回通用模型。PLD在LIBERO上实现了接近饱和的99%的任务成功率，在SimplerEnv上获得了超过50%的收益，并在真实世界的Franka和YAM机械臂操作任务上实现了100%的成功率。消融实验表明，残差探测和分布感知回放是收集部署对齐数据的关键，这些数据可以改进已见和未见任务，从而为自提升VLA模型提供可扩展的路径。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言-动作（VLA）模型依赖大量人工标注数据进行监督微调的问题。现有方法的痛点在于数据获取成本高昂，限制了模型在复杂环境下的泛化能力和可扩展性。

**核心思路**：论文的核心思路是通过残差强化学习（RL）自动探索VLA模型的失败区域，并生成高质量的训练数据，从而实现模型的自提升。通过学习残差策略，模型能够更有效地纠正自身的错误，并提升在未见任务上的表现。

**技术框架**：PLD框架包含三个主要阶段：Probe（探测）、Learn（学习）和Distill（提炼）。
1. **Probe阶段**：训练轻量级的残差actor，用于探测VLA通用模型在执行任务时的失败区域。
2. **Learn阶段**：使用混合rollout策略，收集与通用模型部署分布对齐的轨迹，同时捕捉模型从失败中恢复的行为。
3. **Distill阶段**：利用收集到的高质量轨迹，通过标准的监督微调（SFT）方法，将知识提炼回通用模型。

**关键创新**：该论文的关键创新在于利用残差强化学习来指导数据生成过程，并采用分布感知的回放策略，确保生成的数据与模型的实际部署环境相符。这种方法能够有效地提升模型在真实世界任务中的性能，并降低对人工标注数据的依赖。

**关键设计**：
* **残差Actor**：轻量级的神经网络，学习在VLA模型的基础上进行动作调整，以纠正错误。
* **混合Rollout策略**：结合VLA模型的策略和残差Actor的策略，平衡探索和利用，确保数据质量。
* **分布感知回放**：根据VLA模型的部署分布选择训练数据，避免引入偏差。

## 📊 实验亮点

PLD框架在LIBERO数据集上实现了接近饱和的99%任务成功率，在SimplerEnv数据集上获得了超过50%的性能提升，并在真实世界的Franka和YAM机械臂操作任务上实现了100%的成功率。消融实验证明，残差探测和分布感知回放是提升模型性能的关键因素。

## 🎯 应用场景

该研究成果可广泛应用于机器人操作、自动驾驶、智能家居等领域。通过自提升VLA模型，可以降低对人工干预的需求，提高机器人在复杂环境中的适应性和鲁棒性，实现更智能、更高效的自动化解决方案。未来，该方法有望推动机器人技术的普及和应用。

## 📄 摘要（原文）

> Supervised fine-tuning (SFT) has become the de facto post-training strategy for large vision-language-action (VLA) models, but its reliance on costly human demonstrations limits scalability and generalization. We propose Probe, Learn, Distill (PLD), a three-stage plug-and-play framework that improves VLAs through residual reinforcement learning (RL) and distribution-aware data collection. In Stage 1, we train lightweight residual actors to probe failure regions of the VLA generalist. In Stage 2, we use a hybrid rollout scheme that aligns collected trajectories with the generalist's deployment distribution while capturing recovery behaviors. In Stage 3, we distill the curated trajectories back into the generalist with standard SFT. PLD achieves near-saturated 99% task success on LIBERO, over 50% gains in SimplerEnv, and 100% success on real-world Franka and YAM arm manipulation tasks. Ablations show that residual probing and distribution-aware replay are key to collecting deployment-aligned data that improves both seen and unseen tasks, offering a scalable path toward self-improving VLA models.

