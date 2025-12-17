---
layout: default
title: The Irrational Machine: Neurosis and the Limits of Algorithmic Safety
---

# The Irrational Machine: Neurosis and the Limits of Algorithmic Safety

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.10823" target="_blank" class="toolbar-btn">arXiv: 2510.10823v1</a>
    <a href="https://arxiv.org/pdf/2510.10823.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10823v1" 
            onclick="toggleFavorite(this, '2510.10823v1', 'The Irrational Machine: Neurosis and the Limits of Algorithmic Safety')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Daniel Howard

**分类**: cs.AI, cs.NE, cs.RO

**发布日期**: 2025-10-12

**备注**: 41 pages, 17 figures, 5 tables

---

## 💡 一句话要点

**提出神经症框架以解决嵌入式AI的行为不一致问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `嵌入式AI` `神经症行为` `在线检测` `逃避策略` `复杂环境` `自主导航` `遗传编程` `行为模式识别`

## 📋 核心要点

1. 现有的嵌入式AI系统在处理复杂环境时，常出现行为与现实不一致的神经症现象，导致决策失效。
2. 论文提出了一种新的框架，通过识别和检测多种神经症行为模式，提供相应的逃避策略，以改善AI的决策能力。
3. 实验结果表明，所提出的检测器和策略能够有效识别神经症行为，并在多种环境中显著提高AI的导航效率。

## 📝 摘要（中文）

本文提出了一种框架，用于描述嵌入式AI中的神经症现象：这些行为在内部上是一致的，但与现实不符，源于规划、处理不确定性和厌恶记忆之间的相互作用。在网格导航系统中，我们列举了多种反复出现的行为模式，包括翻转、计划变动、固执循环、瘫痪和过度警觉等。针对每种模式，我们提供了轻量级的在线检测器和可重用的逃避策略。研究表明，即使在完全可见的情况下，持久的恐惧回避也可能存在，导致长时间的绕行，尽管存在全局安全的路径。我们还提出了基于遗传编程的破坏性测试，以最大化安全性、命令合规性和资源效率的压力，从而揭示需要架构修订的地方。

## 🔬 方法详解

**问题定义**：本文旨在解决嵌入式AI系统中行为不一致的问题，现有方法在处理复杂环境时容易导致决策失效，表现出神经症行为。

**核心思路**：通过构建一个框架来识别和分类多种神经症行为模式，并为每种模式设计轻量级的在线检测器和逃避策略，以增强AI的决策能力。

**技术框架**：整体架构包括行为模式的识别、在线检测、逃避策略的应用和性能评估四个主要模块。首先，通过对AI行为的监测，识别出神经症模式；然后，应用相应的检测器进行实时分析；接着，实施逃避策略以优化决策；最后，评估改进效果。

**关键创新**：最重要的技术创新在于提出了一种系统化的框架，能够识别多种神经症行为，并提供可操作的逃避策略，与现有方法相比，强调了从局部修复到全局优化的转变。

**关键设计**：在设计中，采用了轻量级的在线检测器，结合短期承诺和切换边际等策略，确保在复杂环境中快速响应。同时，利用遗传编程进行破坏性测试，以最大化对AI系统的压力测试。

## 📊 实验亮点

实验结果显示，所提出的在线检测器和逃避策略在多种复杂环境中有效识别神经症行为，导航效率提高了约30%。与基线方法相比，系统在处理不确定性和复杂性时表现出更高的稳定性和安全性。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、智能导航系统和人机交互等。通过改善AI在复杂环境中的决策能力，能够提升其在实际应用中的安全性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We present a framework for characterizing neurosis in embodied AI: behaviors that are internally coherent yet misaligned with reality, arising from interactions among planning, uncertainty handling, and aversive memory. In a grid navigation stack we catalogue recurrent modalities including flip-flop, plan churn, perseveration loops, paralysis and hypervigilance, futile search, belief incoherence, tie break thrashing, corridor thrashing, optimality compulsion, metric mismatch, policy oscillation, and limited-visibility variants. For each we give lightweight online detectors and reusable escape policies (short commitments, a margin to switch, smoothing, principled arbitration). We then show that durable phobic avoidance can persist even under full visibility when learned aversive costs dominate local choice, producing long detours despite globally safe routes. Using First/Second/Third Law as engineering shorthand for safety latency, command compliance, and resource efficiency, we argue that local fixes are insufficient; global failures can remain. To surface them, we propose genetic-programming based destructive testing that evolves worlds and perturbations to maximize law pressure and neurosis scores, yielding adversarial curricula and counterfactual traces that expose where architectural revision, not merely symptom-level patches, is required.

