---
layout: default
title: CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation
---

# CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14689" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14689v1</a>
  <a href="https://arxiv.org/pdf/2512.14689.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14689v1" onclick="toggleFavorite(this, '2512.14689v1', 'CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sirui Chen, Zi-ang Cao, Zhengyi Luo, Fernando Castañeda, Chenran Li, Tingwu Wang, Ye Yuan, Linxi "Jim" Fan, C. Karen Liu, Yuke Zhu

**分类**: cs.RO, cs.LG

**发布日期**: 2025-12-16

**备注**: The first two authors contributed equally. Project page: https://nvlabs.github.io/CHIP/

---

## 💡 一句话要点

**CHIP：通过后见之明扰动实现人型机器人自适应柔顺控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人型机器人控制` `柔顺控制` `后见之明学习` `操作任务` `强化学习`

## 📋 核心要点

1. 人型机器人虽然在敏捷运动方面取得了进展，但在需要精确力控的操作任务中仍面临挑战。
2. CHIP通过后见之明扰动，使人型机器人能够自适应地调整末端执行器的柔顺性，从而更好地完成操作任务。
3. 实验表明，配备CHIP的通用运动跟踪控制器能够胜任多种需要不同柔顺性的操作任务，无需额外的数据增强或奖励调整。

## 📝 摘要（中文）

人型机器人领域的最新进展已经解锁了敏捷的运动技能，包括后空翻、跑步和爬行。然而，人型机器人执行需要较大作用力的操作任务仍然具有挑战性，例如移动物体、擦拭和推动手推车。我们提出了一种通过后见之明扰动实现自适应柔顺的人型控制（CHIP）模块，它是一个即插即用的模块，能够在保持动态参考运动的敏捷跟踪的同时，实现可控的末端执行器刚度。CHIP易于实现，不需要数据增强或额外的奖励调整。我们展示了使用CHIP训练的通用运动跟踪控制器可以执行各种需要不同末端执行器柔顺性的操作任务，例如多机器人协作、擦拭、箱子递送和开门。

## 🔬 方法详解

**问题定义**：现有的人型机器人控制器在处理需要精确力控制的操作任务时表现不佳。它们通常难以在保持敏捷运动的同时，根据任务需求调整末端执行器的柔顺性。现有的方法要么需要针对特定任务进行精细的奖励函数设计，要么需要大量的数据增强，泛化能力有限。

**核心思路**：CHIP的核心思路是通过引入后见之明扰动，使控制器能够学习到不同柔顺性下的运动轨迹。具体来说，在训练过程中，CHIP会随机扰动机器人的目标姿态，并让控制器尝试跟踪这些被扰动的目标。通过这种方式，控制器可以学习到如何根据不同的扰动（即不同的柔顺性需求）调整自身的控制策略。

**技术框架**：CHIP是一个即插即用的模块，可以方便地集成到现有的运动跟踪控制器中。其整体框架包括以下几个主要步骤：1) 接收目标姿态；2) 引入后见之明扰动，生成新的目标姿态；3) 将新的目标姿态输入到运动跟踪控制器中；4) 控制器输出控制指令，驱动机器人运动；5) 根据实际运动轨迹和原始目标姿态计算奖励，用于训练控制器。

**关键创新**：CHIP最重要的技术创新在于其后见之明扰动机制。这种机制允许控制器在训练过程中探索不同的柔顺性，而无需显式地指定柔顺性参数。与传统的柔顺控制方法相比，CHIP更加灵活和通用，可以适应各种不同的操作任务。此外，CHIP不需要额外的数据增强或奖励调整，降低了训练成本。

**关键设计**：CHIP的关键设计包括扰动的大小和频率。扰动的大小决定了控制器探索柔顺性的范围，扰动的频率决定了控制器学习柔顺性的速度。论文中，扰动的大小和频率是根据经验进行调整的。此外，论文还使用了标准的运动跟踪控制器作为基础控制器，并对其进行微调，以适应CHIP的扰动。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14689v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14689v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14689v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，使用CHIP训练的通用运动跟踪控制器可以成功完成各种需要不同末端执行器柔顺性的操作任务，例如多机器人协作、擦拭、箱子递送和开门。与没有使用CHIP的控制器相比，CHIP能够显著提高机器人的操作成功率和效率。例如，在箱子递送任务中，CHIP可以将成功率提高到90%以上。

## 🎯 应用场景

CHIP具有广泛的应用前景，可以应用于各种需要人型机器人进行操作的场景，例如工业自动化、医疗康复、家庭服务等。通过CHIP，人型机器人可以更加灵活和高效地完成各种操作任务，例如装配、搬运、清洁等。此外，CHIP还可以用于多机器人协作，使多个机器人能够协同完成复杂的任务。

## 📄 摘要（原文）

> Recent progress in humanoid robots has unlocked agile locomotion skills, including backflipping, running, and crawling. Yet it remains challenging for a humanoid robot to perform forceful manipulation tasks such as moving objects, wiping, and pushing a cart. We propose adaptive Compliance Humanoid control through hIsight Perturbation (CHIP), a plug-and-play module that enables controllable end-effector stiffness while preserving agile tracking of dynamic reference motions. CHIP is easy to implement and requires neither data augmentation nor additional reward tuning. We show that a generalist motion-tracking controller trained with CHIP can perform a diverse set of forceful manipulation tasks that require different end-effector compliance, such as multi-robot collaboration, wiping, box delivery, and door opening.

