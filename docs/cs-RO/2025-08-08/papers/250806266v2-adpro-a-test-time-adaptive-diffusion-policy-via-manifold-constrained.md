---
layout: default
title: "ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation"
---

# ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06266" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06266v2</a>
  <a href="https://arxiv.org/pdf/2508.06266.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06266v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06266v2', 'ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zezeng Li, Rui Yang, Ruochen Chen, ZhongXuan Luo, Liming Chen

**分类**: cs.RO

**发布日期**: 2025-08-08 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出自适应扩散策略以解决机器人操作中的动作生成问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自适应扩散策略` `机器人操作` `动作生成` `几何约束` `任务感知初始化` `性能提升` `智能机器人`

## 📋 核心要点

1. 现有的扩散策略在动作生成时未能有效利用几何和控制结构的先验知识，导致性能受限。
2. 本文提出的自适应扩散策略通过引入几何流形约束和任务感知初始化，优化了去噪过程，提升了动作生成的效率和准确性。
3. 实验结果显示，ADPro在多个数据集上相较于强基线提升了成功率和采样效率，执行速度提高了25%。

## 📝 摘要（中文）

扩散策略最近成为机器人操作中强大的视觉运动控制器，提供稳定的训练和多模态动作建模。然而，现有方法通常将动作生成视为无约束的去噪过程，忽视了几何和控制结构的先验知识。本文提出自适应扩散策略（ADP），在测试时引入几何流形约束和任务感知初始化，优化去噪过程。ADP兼容预训练的扩散策略，无需重新训练，能够针对特定任务进行适应，从而提高在新任务和环境中的泛化能力。实验结果表明，ADPro（ADP的实现）在RLBench、CALVIN和真实数据集上显著提高了成功率和采样效率，执行速度提升高达25%，成功率提高9%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有扩散策略在机器人操作中动作生成时缺乏几何和控制结构先验知识的问题，导致性能不佳。

**核心思路**：提出自适应扩散策略（ADP），通过引入几何流形约束和任务感知初始化来优化去噪过程，确保生成的动作与任务相关。

**技术框架**：ADP的整体架构包括两个主要模块：几何流形约束模块和任务感知初始化模块。前者通过对去噪更新进行约束，后者则通过粗略配准生成初始噪声动作。

**关键创新**：ADP的核心创新在于引入几何流形约束，使得去噪过程沿着操作流形的测地线进行，从而提高了动作生成的有效性和准确性。

**关键设计**：在设计中，采用了基于相对姿态的几何约束和粗略配准的任务感知初始化，确保了生成的动作更具针对性，减少了不必要的探索。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，ADPro在RLBench、CALVIN和真实数据集上相较于强基线提升了成功率和采样效率，执行速度提高了25%，成功率提升了9个百分点，显示出显著的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括工业机器人、服务机器人及其他需要精确操作的自动化系统。通过提高机器人在复杂环境中的适应能力，ADP有望在实际应用中显著提升操作效率和成功率，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Diffusion policies have recently emerged as a powerful class of visuomotor controllers for robot manipulation, offering stable training and expressive multi-modal action modeling. However, existing approaches typically treat action generation as an unconstrained denoising process, ignoring valuable a priori knowledge about geometry and control structure. In this work, we propose the Adaptive Diffusion Policy (ADP), a test-time adaptation method that introduces two key inductive biases into the diffusion. First, we embed a geometric manifold constraint that aligns denoising updates with task-relevant subspaces, leveraging the fact that the relative pose between the end-effector and target scene provides a natural gradient direction, and guiding denoising along the geodesic path of the manipulation manifold. Then, to reduce unnecessary exploration and accelerate convergence, we propose an analytically guided initialization: rather than sampling from an uninformative prior, we compute a rough registration between the gripper and target scenes to propose a structured initial noisy action. ADP is compatible with pre-trained diffusion policies and requires no retraining, enabling test-time adaptation that tailors the policy to specific tasks, thereby enhancing generalization across novel tasks and environments. Experiments on RLBench, CALVIN, and real-world datasets show that ADPro, an implementation of ADP, improves success rates, generalization, and sampling efficiency, achieving up to 25% faster execution and 9% points over strong diffusion baselines.

