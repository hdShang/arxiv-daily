---
layout: default
title: Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt
---

# Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20795" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20795v1</a>
  <a href="https://arxiv.org/pdf/2505.20795.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20795v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20795v1', 'Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiang Zhu, Yichen Liu, Hezhong Li, Jianyu Chen

**分类**: cs.RO

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出一种新框架以利用人类示范视频学习通用机器人策略**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人类示范` `机器人学习` `通用策略` `视频生成` `对比损失` `灵巧操作` `任务泛化`

## 📋 核心要点

1. 现有的机器人学习方法依赖于大量的遥控操作数据，收集新数据和微调策略的过程繁琐且昂贵。
2. 本文提出一种两阶段框架，利用人类示范视频直接学习通用机器人策略，无需新数据和微调。
3. 实验证明该方法在真实世界的灵巧操作任务中具有良好的有效性和泛化能力。

## 📝 摘要（中文）

近年来的机器人学习方法通常依赖于从大量通过遥控操作收集的机器人数据中进行模仿学习。当面临新任务时，这些方法通常需要收集一组新的遥控数据并对策略进行微调。此外，遥控数据收集流程也十分繁琐且昂贵。相较之下，人类能够通过观察他人高效学习新任务。本文提出了一种新颖的两阶段框架，利用人类示范学习通用的机器人策略。该策略可以直接将人类示范视频作为提示，执行新任务，而无需任何新的遥控数据和模型微调。在第一阶段，我们训练了一个视频生成模型，通过交叉预测捕捉人类和机器人示范视频数据的联合表示。在第二阶段，我们使用新颖的原型对比损失将学习到的表示与人类和机器人之间的共享动作空间融合。实证评估表明我们提出的方法在真实世界的灵巧操作任务中表现出有效性和良好的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有机器人学习方法在面对新任务时需要收集新遥控数据和进行微调的痛点。这种方法不仅耗时且成本高昂。

**核心思路**：论文提出的核心思路是通过人类示范视频来学习通用的机器人策略，避免了传统方法的繁琐数据收集过程。通过观察他人执行任务，人类能够快速学习，而机器人也可以借此进行有效的学习。

**技术框架**：整体架构分为两个主要阶段：第一阶段是训练视频生成模型，捕捉人类和机器人示范视频的联合表示；第二阶段是通过原型对比损失将学习到的表示与共享动作空间进行融合。

**关键创新**：最重要的技术创新在于提出了利用人类示范视频作为提示的方式，使机器人能够在没有新遥控数据和微调的情况下执行新任务。这与现有方法的本质区别在于减少了对数据收集的依赖。

**关键设计**：在技术细节上，采用了交叉预测的方法来训练视频生成模型，并设计了原型对比损失来实现人类与机器人之间的动作空间共享。

## 📊 实验亮点

实验结果表明，所提出的方法在真实世界的灵巧操作任务中表现出色，相较于传统方法，能够在没有新遥控数据的情况下实现任务执行，展现出良好的泛化能力。具体性能数据和对比基线尚未详细列出，需进一步查阅原文。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和家庭助理等场景。通过减少对遥控数据的依赖，机器人能够更快速地适应新任务，提高工作效率，降低成本，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent robot learning methods commonly rely on imitation learning from massive robotic dataset collected with teleoperation. When facing a new task, such methods generally require collecting a set of new teleoperation data and finetuning the policy. Furthermore, the teleoperation data collection pipeline is also tedious and expensive. Instead, human is able to efficiently learn new tasks by just watching others do. In this paper, we introduce a novel two-stage framework that utilizes human demonstrations to learn a generalizable robot policy. Such policy can directly take human demonstration video as a prompt and perform new tasks without any new teleoperation data and model finetuning at all. In the first stage, we train video generation model that captures a joint representation for both the human and robot demonstration video data using cross-prediction. In the second stage, we fuse the learned representation with a shared action space between human and robot using a novel prototypical contrastive loss. Empirical evaluations on real-world dexterous manipulation tasks show the effectiveness and generalization capabilities of our proposed method.

