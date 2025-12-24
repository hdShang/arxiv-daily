---
layout: default
title: "Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation"
---

# Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23919" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23919v2</a>
  <a href="https://arxiv.org/pdf/2506.23919.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23919v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23919v2', 'Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haonan Chen, Jingxiang Guo, Bangjun Wang, Tianrui Zhang, Xuchuan Huang, Boren Zheng, Yiwen Hou, Chenrui Tie, Jiajun Deng, Lin Shao

**分类**: cs.RO

**发布日期**: 2025-06-30 (更新: 2025-09-30)

**🔗 代码/项目**: [PROJECT_PAGE](https://nus-lins-lab.github.io/goalvlaweb/)

---

## 💡 一句话要点

**提出Goal-VLA以解决机器人操作中的泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视觉-语言模型` `零-shot学习` `图像生成` `泛化能力`

## 📋 核心要点

1. 现有的视觉-语言-动作模型在零-shot能力上表现不佳，无法覆盖多样化的场景和任务。
2. 提出的Goal-VLA框架利用图像生成VLMs生成目标状态，从而实现高效的物体操作。
3. 实验结果表明，Goal-VLA在模拟和真实环境中的操作任务中表现优异，具有良好的泛化能力。

## 📝 摘要（中文）

泛化能力仍然是机器人操作中的一个基本挑战。为了解决这一挑战，近期的视觉-语言-动作（VLA）模型在视觉-语言模型（VLMs）之上构建策略，试图转移其开放世界的语义知识。然而，由于指令-视觉-动作数据的限制，其零-shot能力远远落后于基础VLMs。本文提出了Goal-VLA，一个零-shot框架，利用图像生成VLMs作为世界模型生成期望的目标状态，从中推导出目标物体的姿态，以实现可泛化的操作。关键见解在于物体状态表示是一个理想的接口，自然地将操作系统分为高层和低层策略。这种表示抽象了显式的动作注释，允许使用高度可泛化的VLMs，同时为无训练的低层控制提供空间线索。模拟和真实世界实验表明，Goal-VLA在操作任务中表现出色，具有令人鼓舞的泛化能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人操作中的泛化能力不足问题。现有的VLA模型由于数据限制，无法有效应对多样化的操作场景和任务。

**核心思路**：Goal-VLA框架的核心思想是利用图像生成VLMs作为世界模型，生成期望的目标状态，从而推导出物体的姿态，实现可泛化的操作。通过将物体状态表示作为高低层策略的接口，避免了对显式动作注释的依赖。

**技术框架**：该框架主要包括两个阶段：首先生成目标状态图像，然后通过反思-合成过程对生成的图像进行验证和优化，确保在执行前的准确性。

**关键创新**：最重要的创新在于将图像生成VLMs作为操作的核心，利用其强大的泛化能力和空间线索，显著提升了机器人操作的灵活性和准确性。

**关键设计**：在设计中，采用了反思-合成过程，通过迭代验证生成的目标图像，确保其在实际操作中的有效性。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，Goal-VLA在多种操作任务中表现出色，相较于基线模型，其零-shot操作能力提升了显著的百分比，展示了良好的泛化能力和实际应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、工业自动化和服务机器人等。通过提升机器人在复杂环境中的操作能力，Goal-VLA能够在实际应用中实现更高的灵活性和适应性，推动机器人技术的发展。

## 📄 摘要（原文）

> Generalization remains a fundamental challenge in robotic manipulation. To tackle this challenge, recent Vision-Language-Action (VLA) models build policies on top of Vision-Language Models (VLMs), seeking to transfer their open-world semantic knowledge. However, their zero-shot capability lags significantly behind the base VLMs, as the instruction-vision-action data is too limited to cover diverse scenarios, tasks, and robot embodiments. In this work, we present Goal-VLA, a zero-shot framework that leverages Image-Generative VLMs as world models to generate desired goal states, from which the target object pose is derived to enable generalizable manipulation. The key insight is that object state representation is the golden interface, naturally separating a manipulation system into high-level and low-level policies. This representation abstracts away explicit action annotations, allowing the use of highly generalizable VLMs while simultaneously providing spatial cues for training-free low-level control. To further improve robustness, we introduce a Reflection-through-Synthesis process that iteratively validates and refines the generated goal image before execution. Both simulated and real-world experiments demonstrate that our \name achieves strong performance and inspiring generalizability in manipulation tasks. Supplementary materials are available at https://nus-lins-lab.github.io/goalvlaweb/.

