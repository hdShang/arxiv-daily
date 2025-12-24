---
layout: default
title: "DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration"
---

# DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05064" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05064v2</a>
  <a href="https://arxiv.org/pdf/2506.05064.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05064v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05064v2', 'DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingxiao Guo, Zhengrong Xue, Zijing Xu, Huazhe Xu

**分类**: cs.RO

**发布日期**: 2025-06-05 (更新: 2025-06-10)

---

## 💡 一句话要点

**提出DemoSpeedup以加速视觉运动策略执行**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `视觉运动` `策略加速` `熵引导` `机器人操作` `自我监督学习`

## 📋 核心要点

1. 现有的模仿学习方法在机器人操作中执行速度较慢，难以满足高效性的需求。
2. DemoSpeedup通过熵引导的演示加速，利用动作熵估计来优化策略执行速度。
3. 实验结果表明，所提出的方法使策略执行速度提高至3倍，同时提高了任务成功率。

## 📝 摘要（中文）

模仿学习在机器人操作中展现了巨大的潜力，但由于人类操作员收集的演示通常较慢，策略执行往往不够迅速。本文提出了DemoSpeedup，一种通过熵引导的演示加速方法，自我监督地加速视觉运动策略的执行。DemoSpeedup首先在正常速度的演示上训练任意生成策略（如ACT或扩散策略），作为每帧动作熵的估计器。关键见解在于，低熵估计的帧需要更一致的策略行为，通常意味着对高精度操作的需求；而高熵估计的帧则对应于更随意的部分，因此可以更安全地加速。通过根据估计的熵对原始演示进行分段，并以熵值增加的速率进行下采样加速，训练出的策略执行速度提高了3倍，同时保持任务完成性能。值得注意的是，这些策略的成功率甚至高于使用正常速度演示训练的策略，得益于决策时间的减少。

## 🔬 方法详解

**问题定义**：本文旨在解决模仿学习中由于人类演示速度慢导致的机器人策略执行效率低下的问题。现有方法在处理演示时未能有效利用动作熵信息，导致策略执行不够快速和精准。

**核心思路**：DemoSpeedup的核心思路是通过熵引导的方式对演示进行加速。具体而言，低熵估计的帧需要更一致的策略行为，而高熵估计的帧则可以安全加速，从而优化整体执行速度。

**技术框架**：该方法的整体架构包括三个主要模块：首先，训练生成策略以估计每帧的动作熵；其次，根据熵值对演示进行分段；最后，针对不同熵值的帧进行下采样加速。

**关键创新**：DemoSpeedup的创新在于利用动作熵作为加速的依据，显著提高了策略执行的速度和成功率。这一方法与传统的模仿学习方法相比，能够更有效地利用演示数据。

**关键设计**：在设计中，采用了适应性下采样策略，熵值越高的帧下采样率越大。此外，损失函数的设计也考虑了熵的影响，以确保训练过程中的策略一致性。

## 📊 实验亮点

实验结果显示，DemoSpeedup训练出的策略执行速度提高了3倍，同时在任务完成性能上保持不变，甚至在某些情况下成功率高于使用正常速度演示训练的策略。这表明该方法在提升决策效率方面具有显著优势。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在机器人操作、自动化生产线和人机协作等领域。通过加速视觉运动策略的执行，能够显著提高机器人在复杂任务中的效率和灵活性，推动智能机器人技术的进一步发展。

## 📄 摘要（原文）

> Imitation learning has shown great promise in robotic manipulation, but the policy's execution is often unsatisfactorily slow due to commonly tardy demonstrations collected by human operators. In this work, we present DemoSpeedup, a self-supervised method to accelerate visuomotor policy execution via entropy-guided demonstration acceleration. DemoSpeedup starts from training an arbitrary generative policy (e.g., ACT or Diffusion Policy) on normal-speed demonstrations, which serves as a per-frame action entropy estimator. The key insight is that frames with lower action entropy estimates call for more consistent policy behaviors, which often indicate the demands for higher-precision operations. In contrast, frames with higher entropy estimates correspond to more casual sections, and therefore can be more safely accelerated. Thus, we segment the original demonstrations according to the estimated entropy, and accelerate them by down-sampling at rates that increase with the entropy values. Trained with the speedup demonstrations, the resulting policies execute up to 3 times faster while maintaining the task completion performance. Interestingly, these policies could even achieve higher success rates than those trained with normal-speed demonstrations, due to the benefits of reduced decision-making horizons. Project Page: https://demospeedup.github.io/

