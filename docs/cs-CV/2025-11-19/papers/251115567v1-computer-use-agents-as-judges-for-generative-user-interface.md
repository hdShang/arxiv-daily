---
layout: default
title: Computer-Use Agents as Judges for Generative User Interface
---

# Computer-Use Agents as Judges for Generative User Interface

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15567" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15567v1</a>
  <a href="https://arxiv.org/pdf/2511.15567.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15567v1" onclick="toggleFavorite(this, '2511.15567v1', 'Computer-Use Agents as Judges for Generative User Interface')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kevin Qinghong Lin, Siyuan Hu, Linjie Li, Zhengyuan Yang, Lijuan Wang, Philip Torr, Mike Zheng Shou

**分类**: cs.CV, cs.CL, cs.HC

**发布日期**: 2025-11-19

**备注**: Project: https://showlab.github.io/AUI Github: https://github.com/showlab/AUI

**🔗 代码/项目**: [GITHUB](https://github.com/showlab/AUI)

---

## 💡 一句话要点

**提出Coder-CUA协同框架，利用计算机代理辅助代码生成GUI的设计，提升任务解决能力。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自动GUI设计` `计算机使用代理` `人机协作` `语言模型` `基准测试`

## 📋 核心要点

1. 现有GUI设计主要面向人类，导致计算机代理执行任务时效率低下，需要针对代理进行优化。
2. 提出Coder-CUA协同框架，Coder负责GUI设计，CUA负责评估和改进，以提升代理的任务解决能力。
3. 构建AUI-Gym基准测试，包含52个应用和1560个任务，并设计CUA仪表盘，提供可视化指导。

## 📝 摘要（中文）

计算机使用代理(CUA)在通过图形用户界面(GUI)自主操作数字环境方面的能力日益增强。然而，大多数GUI仍然主要为人类设计，优先考虑美观和可用性，迫使代理采用以人为本的行为，这对高效的任务执行是不必要的。同时，面向编码的语言模型(Coder)的快速发展已经改变了自动GUI设计。这就提出了一个根本问题：CUA能否作为评判者来辅助Coder进行自动GUI设计？为了研究这个问题，我们引入了AUI-Gym，这是一个用于自动GUI开发的基准，涵盖了跨不同领域的52个应用程序。利用语言模型，我们合成了1560个模拟真实场景的任务。为了确保任务的可靠性，我们进一步开发了一个验证器，以编程方式检查每个任务是否可以在其环境中执行。在此基础上，我们提出了一个Coder-CUA协同框架：Coder作为设计者，生成和修改网站，而CUA作为评判者，评估功能并改进设计。成功的衡量标准不是视觉外观，而是任务的可解决性和CUA导航成功率。为了将CUA反馈转化为可用的指导，我们设计了一个CUA仪表板，将多步骤导航历史压缩成简洁的可视化摘要，为迭代重新设计提供可解释的指导。通过将代理定位为设计者和评判者，我们的框架将界面设计转向代理原生的效率和可靠性。我们的工作朝着代理从被动使用转向积极参与数字环境迈出了一步。我们的代码和数据集可在https://github.com/showlab/AUI获得。

## 🔬 方法详解

**问题定义**：现有GUI设计主要面向人类，忽略了计算机代理的特性，导致代理在执行任务时需要模拟人类行为，效率较低。现有方法缺乏针对代理的GUI自动设计和评估机制，无法充分发挥代理的潜力。

**核心思路**：将GUI设计过程分解为设计和评估两个阶段，分别由Coder和CUA承担。Coder负责生成和修改GUI，CUA负责评估GUI的功能性和导航成功率，并提供反馈指导Coder进行改进。这种协同方式能够充分利用Coder的代码生成能力和CUA的自主导航能力，实现针对代理优化的GUI设计。

**技术框架**：整体框架包含以下几个主要模块：1) **AUI-Gym基准测试**：提供包含多个应用和任务的测试环境，用于评估GUI设计的性能。2) **Coder (设计者)**：利用语言模型生成和修改GUI代码。3) **CUA (评判者)**：评估GUI的功能性和导航成功率，并生成反馈。4) **CUA仪表盘**：将CUA的导航历史压缩成可视化摘要，为Coder提供可解释的指导。

**关键创新**：1) **Coder-CUA协同框架**：将GUI设计过程分解为设计和评估两个阶段，由Coder和CUA协同完成。2) **CUA作为评判者**：利用CUA的自主导航能力评估GUI的功能性和导航成功率，避免了人工评估的局限性。3) **CUA仪表盘**：将CUA的导航历史压缩成可视化摘要，为Coder提供可解释的指导。

**关键设计**：1) **任务验证器**：用于验证任务是否可以在环境中执行，确保任务的可靠性。2) **CUA导航成功率**：作为评估GUI性能的关键指标，反映了GUI对代理的友好程度。3) **CUA仪表盘的可视化摘要**：将多步骤导航历史压缩成简洁的图像，方便Coder理解CUA的导航过程。

## 📊 实验亮点

论文构建了AUI-Gym基准测试，包含52个应用和1560个任务，为自动GUI设计提供了评估平台。实验结果表明，Coder-CUA协同框架能够有效提升GUI的任务解决能力和CUA导航成功率。CUA仪表盘能够提供可解释的指导，帮助Coder进行迭代改进。

## 🎯 应用场景

该研究成果可应用于自动化GUI设计、人机协作界面优化、智能助手开发等领域。通过将计算机代理纳入GUI设计流程，可以设计出更符合代理需求的界面，提升代理的工作效率和智能化水平。未来，该技术有望应用于智能家居、工业自动化、虚拟现实等领域，实现更高效、智能的人机交互。

## 📄 摘要（原文）

> Computer-Use Agents (CUA) are becoming increasingly capable of autonomously operating digital environments through Graphical User Interfaces (GUI). Yet, most GUI remain designed primarily for humans--prioritizing aesthetics and usability--forcing agents to adopt human-oriented behaviors that are unnecessary for efficient task execution. At the same time, rapid advances in coding-oriented language models (Coder) have transformed automatic GUI design. This raises a fundamental question: Can CUA as judges to assist Coder for automatic GUI design? To investigate, we introduce AUI-Gym, a benchmark for Automatic GUI development spanning 52 applications across diverse domains. Using language models, we synthesize 1560 tasks that simulate real-world scenarios. To ensure task reliability, we further develop a verifier that programmatically checks whether each task is executable within its environment. Building on this, we propose a Coder-CUA in Collaboration framework: the Coder acts as Designer, generating and revising websites, while the CUA serves as Judge, evaluating functionality and refining designs. Success is measured not by visual appearance, but by task solvability and CUA navigation success rate. To turn CUA feedback into usable guidance, we design a CUA Dashboard that compresses multi-step navigation histories into concise visual summaries, offering interpretable guidance for iterative redesign. By positioning agents as both designers and judges, our framework shifts interface design toward agent-native efficiency and reliability. Our work takes a step toward shifting agents from passive use toward active participation in digital environments. Our code and dataset are available at https://github.com/showlab/AUI.

