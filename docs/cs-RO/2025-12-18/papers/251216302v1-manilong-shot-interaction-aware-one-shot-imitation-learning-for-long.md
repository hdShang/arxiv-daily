---
layout: default
title: "ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation"
---

# ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16302" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16302v1</a>
  <a href="https://arxiv.org/pdf/2512.16302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16302v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16302v1', 'ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixuan Chen, Chongkai Gao, Lin Shao, Jieqi Shi, Jing Huo, Yang Gao

**分类**: cs.RO

**发布日期**: 2025-12-18

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**ManiLong-Shot：交互感知的单样本模仿学习用于长时程操作任务**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `单样本模仿学习` `长时程操作` `交互感知` `视觉-语言模型` `机器人操作`

## 📋 核心要点

1. 现有单样本模仿学习方法主要局限于短时程任务，限制了其在复杂、长时程操作任务中的应用。
2. ManiLong-Shot将长时程任务分解为交互感知的原语序列，通过视觉-语言模型或规则启发式方法驱动原语分解。
3. 实验表明，ManiLong-Shot在仿真和真实机器人上均表现出优异的性能，显著提升了长时程操作任务的成功率。

## 📝 摘要（中文）

本文提出ManiLong-Shot，一个新颖的框架，旨在实现长时程灵巧操作任务的有效单样本模仿学习(OSIL)。ManiLong-Shot围绕物理交互事件构建长时程任务，将问题重新定义为对交互感知原语进行排序，而不是直接模仿连续轨迹。这种原语分解可以由视觉-语言模型(VLM)的高级推理驱动，或者由机器人状态变化推导出的基于规则的启发式方法驱动。对于每个原语，ManiLong-Shot预测对交互至关重要的不变区域，建立演示和当前观察之间的对应关系，并计算目标末端执行器姿态，从而实现有效的任务执行。大量的仿真实验表明，ManiLong-Shot仅在10个短时程任务上训练，即可通过单样本模仿泛化到20个未见过的长时程任务，跨越三个难度级别，相对于SOTA方法实现了22.8%的相对改进。此外，真实机器人实验验证了ManiLong-Shot通过OSIL稳健地执行三个长时程操作任务的能力，证实了其在实际应用中的可行性。

## 🔬 方法详解

**问题定义**：现有单样本模仿学习方法难以处理长时程操作任务，因为直接模仿连续轨迹在长序列中容易累积误差，并且难以泛化到新的场景。痛点在于缺乏对任务结构的理解和有效的分解策略。

**核心思路**：将长时程任务分解为一系列交互感知的原语。每个原语代表一个基本的物理交互动作，例如抓取、放置等。通过对这些原语进行排序和模仿，可以有效地完成长时程任务。这种分解降低了模仿的难度，并提高了泛化能力。

**技术框架**：ManiLong-Shot包含以下主要模块：1) 任务分解模块：利用视觉-语言模型或规则启发式方法将长时程任务分解为交互原语序列。2) 交互区域预测模块：预测每个原语中对交互至关重要的不变区域。3) 对应关系建立模块：建立演示和当前观察之间的对应关系，例如通过特征匹配。4) 末端执行器姿态计算模块：根据对应关系计算目标末端执行器姿态，驱动机器人执行动作。

**关键创新**：ManiLong-Shot的关键创新在于将长时程任务分解为交互感知的原语，并利用视觉-语言模型或规则启发式方法进行任务分解。与直接模仿连续轨迹的方法相比，这种方法更具结构化，更容易泛化到新的场景。

**关键设计**：任务分解模块可以使用预训练的视觉-语言模型，例如CLIP，来理解任务描述并生成原语序列。交互区域预测模块可以使用卷积神经网络来预测图像中与交互相关的区域。对应关系建立模块可以使用SIFT或ORB等特征匹配算法。末端执行器姿态计算模块可以使用逆运动学算法将目标姿态转换为关节角度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16302v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16302v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16302v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在仿真实验中，ManiLong-Shot在20个未见过的长时程任务上，相对于SOTA方法实现了22.8%的相对改进。在真实机器人实验中，ManiLong-Shot成功地执行了三个长时程操作任务，验证了其在实际应用中的可行性。这些结果表明，ManiLong-Shot是一种有效的长时程操作任务单样本模仿学习方法。

## 🎯 应用场景

ManiLong-Shot在工业自动化、家庭服务机器人、医疗机器人等领域具有广泛的应用前景。例如，它可以用于训练机器人完成复杂的装配任务、清洁任务或辅助手术任务。通过单样本模仿学习，可以大大降低机器人编程的成本和难度，提高机器人的智能化水平。

## 📄 摘要（原文）

> One-shot imitation learning (OSIL) offers a promising way to teach robots new skills without large-scale data collection. However, current OSIL methods are primarily limited to short-horizon tasks, thus limiting their applicability to complex, long-horizon manipulations. To address this limitation, we propose ManiLong-Shot, a novel framework that enables effective OSIL for long-horizon prehensile manipulation tasks. ManiLong-Shot structures long-horizon tasks around physical interaction events, reframing the problem as sequencing interaction-aware primitives instead of directly imitating continuous trajectories. This primitive decomposition can be driven by high-level reasoning from a vision-language model (VLM) or by rule-based heuristics derived from robot state changes. For each primitive, ManiLong-Shot predicts invariant regions critical to the interaction, establishes correspondences between the demonstration and the current observation, and computes the target end-effector pose, enabling effective task execution. Extensive simulation experiments show that ManiLong-Shot, trained on only 10 short-horizon tasks, generalizes to 20 unseen long-horizon tasks across three difficulty levels via one-shot imitation, achieving a 22.8% relative improvement over the SOTA. Additionally, real-robot experiments validate ManiLong-Shot's ability to robustly execute three long-horizon manipulation tasks via OSIL, confirming its practical applicability.

