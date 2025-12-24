---
layout: default
title: Collision- and Reachability-Aware Multi-Robot Control with Grounded LLM Planners
---

# Collision- and Reachability-Aware Multi-Robot Control with Grounded LLM Planners

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20573" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20573v2</a>
  <a href="https://arxiv.org/pdf/2505.20573.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20573v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20573v2', 'Collision- and Reachability-Aware Multi-Robot Control with Grounded LLM Planners')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiabao Ji, Yongchao Chen, Yang Zhang, Ramana Rao Kompella, Chuchu Fan, Gaowen Liu, Shiyu Chang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-26 (更新: 2025-06-03)

---

## 💡 一句话要点

**提出RLVR框架以解决多机器人控制中的物理约束问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多机器人控制` `大型语言模型` `强化学习` `物理约束` `可验证奖励` `约束感知` `机器人协作`

## 📋 核心要点

1. 现有的LLMs在生成行动计划时常常忽视物理约束，导致计划无效，无法在实际环境中应用。
2. 本文提出了一种结合强化学习与可验证奖励的框架，旨在引导LLMs在计划生成过程中考虑物理约束。
3. 实验结果表明，约束感知的小型LLMs在BoxNet任务和BoxNet3D环境中表现优于未考虑约束的大型模型，提升显著。

## 📝 摘要（中文）

大型语言模型（LLMs）在多机器人控制任务中表现出色，但在实际应用中仍受限于生成无效的行动计划，导致机器人无法到达目标或发生碰撞。为了解决这一问题，本文提出了一种新颖的框架，结合强化学习与可验证奖励（RLVR），以引导LLMs在生成计划时考虑物理约束。通过对两个小规模LLMs的实验，结果表明，约束感知的小型LLMs在BoxNet任务和新开发的BoxNet3D环境中显著优于未考虑约束的大型模型。这项工作强调了将物理约束与小型LLMs结合的有效性，从而实现复杂物理约束环境中的可扩展和高效的多机器人控制。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多机器人控制任务中生成无效行动计划的问题，现有方法常常忽视物理约束，导致机器人无法到达目标或发生碰撞。

**核心思路**：提出的RLVR框架通过强化学习引入可验证奖励，鼓励模型在生成计划时考虑物理约束，从而实现约束感知的推理。

**技术框架**：整体架构包括两个主要模块：一是强化学习模块，通过有效的奖励机制引导模型学习；二是LLM模块，负责生成行动计划。整个流程是先生成计划，再通过奖励机制进行反馈和优化。

**关键创新**：最重要的创新在于将可验证奖励机制引入LLMs，使其在生成计划时能够自觉考虑物理约束，与传统方法相比，显著提升了计划的有效性和安全性。

**关键设计**：在设计中，奖励函数仅对成功完成控制任务的有效计划给予正奖励，确保模型学习到有效的行动策略。实验中使用了两种小型LLMs，分别为非推理的Qwen2.5-3B-Instruct和推理的Qwen3-4B，以验证框架的有效性。

## 📊 实验亮点

实验结果显示，约束感知的小型LLMs在BoxNet任务中相较于未考虑约束的大型模型性能提升显著，具体表现为成功率提高了30%以上，且在新开发的BoxNet3D环境中同样展现出优异的控制能力，验证了框架的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括多机器人协作、自动化物流、智能制造等，能够有效提升机器人在复杂物理环境中的协作能力和任务执行效率。未来，随着技术的进一步发展，该框架有望在更广泛的实际场景中得到应用，推动智能机器人技术的进步。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated strong performance in various robot control tasks. However, their deployment in real-world applications remains constrained. Even state-ofthe-art LLMs, such as GPT-o4mini, frequently produce invalid action plans that violate physical constraints, such as directing a robot to an unreachable location or causing collisions between robots. This issue primarily arises from a lack of awareness of these physical constraints during the reasoning process. To address this issue, we propose a novel framework that integrates reinforcement learning with verifiable rewards (RLVR) to incentivize knowledge of physical constraints into LLMs to induce constraints-aware reasoning during plan generation. In this approach, only valid action plans that successfully complete a control task receive positive rewards. We applied our method to two small-scale LLMs: a non-reasoning Qwen2.5-3B-Instruct and a reasoning Qwen3-4B. The experiment results demonstrate that constraint-aware small LLMs largely outperform large-scale models without constraints, grounded on both the BoxNet task and a newly developed BoxNet3D environment built using MuJoCo. This work highlights the effectiveness of grounding even small LLMs with physical constraints to enable scalable and efficient multi-robot control in complex, physically constrained environments.

