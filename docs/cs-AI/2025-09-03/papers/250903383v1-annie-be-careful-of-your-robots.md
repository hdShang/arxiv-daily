---
layout: default
title: "ANNIE: Be Careful of Your Robots"
---

# ANNIE: Be Careful of Your Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03383" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03383v1</a>
  <a href="https://arxiv.org/pdf/2509.03383.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03383v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03383v1', 'ANNIE: Be Careful of Your Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiyang Huang, Zixuan Wang, Zishen Wan, Yapeng Tian, Haobo Xu, Yinhe Han, Yiming Gan

**分类**: cs.AI, cs.RO

**发布日期**: 2025-09-03

**🔗 代码/项目**: [GITHUB](https://github.com/RLCLab/Annie)

---

## 💡 一句话要点

**ANNIE：针对具身AI系统的对抗性安全攻击研究与基准测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身AI` `对抗攻击` `安全性` `机器人安全` `视觉-语言-动作模型`

## 📋 核心要点

1. 现有方法难以应对具身AI系统面临的物理世界安全风险，需要重新定义安全标准和评估方法。
2. 提出ANNIE框架，通过任务感知的对抗攻击，评估具身AI系统在安全关键场景下的鲁棒性。
3. 实验表明，该攻击框架在多种EAI模型上取得了超过50%的攻击成功率，验证了现实世界的影响。

## 📝 摘要（中文）

具身AI(EAI)机器人与视觉-语言-动作(VLA)模型的集成正迅速提升其在以人为中心的环境中执行复杂、长时程任务的能力。然而，EAI系统也带来了严重的安全风险：被攻击的VLA模型可以直接将感官输入上的对抗性扰动转化为不安全的物理动作。传统的机器学习安全定义和方法已不再适用。EAI系统提出了新的问题，例如什么是安全，如何衡量安全，以及如何在物理交互环境中设计有效的攻击和防御机制。本文首次系统地研究了具身AI系统上的对抗性安全攻击，并以ISO人机交互标准为基础。(1) 我们基于分离距离、速度和碰撞边界等物理约束，形式化了安全违规行为的分类(严重、危险、有风险)；(2) 引入了ANNIEBench，一个包含九个安全关键场景和2400个视频-动作序列的基准，用于评估具身安全性；(3) ANNIE-Attack，一个任务感知的对抗性框架，包含一个攻击引导模型，将长时程目标分解为帧级别的扰动。在代表性的EAI模型上的评估表明，所有安全类别中的攻击成功率均超过50%。我们进一步展示了稀疏和自适应的攻击策略，并通过物理机器人实验验证了现实世界的影响。这些结果揭示了具身AI系统中一个先前未被充分探索但影响重大的攻击面，突出了在物理AI时代对安全驱动防御的迫切需求。

## 🔬 方法详解

**问题定义**：论文旨在解决具身AI系统中，视觉-语言-动作模型容易受到对抗攻击，导致机器人产生不安全行为的问题。现有方法主要关注机器学习模型的对抗鲁棒性，但忽略了具身AI系统与物理环境交互的特殊性，缺乏针对物理安全性的评估和防御机制。

**核心思路**：论文的核心思路是构建一个任务感知的对抗攻击框架，通过在视觉输入上添加微小的扰动，诱导机器人执行不安全的动作。该框架模拟了攻击者利用VLA模型的漏洞，将对抗性扰动转化为实际的物理风险。

**技术框架**：ANNIE框架包含两个主要组成部分：ANNIEBench和ANNIE-Attack。ANNIEBench是一个包含九个安全关键场景的基准测试，用于评估具身AI系统的安全性。ANNIE-Attack是一个任务感知的对抗攻击框架，包含一个攻击引导模型，该模型将长时程目标分解为帧级别的扰动。整体流程是，首先利用ANNIEBench定义安全场景和评估指标，然后使用ANNIE-Attack生成对抗性扰动，最后评估EAI模型在对抗性扰动下的表现。

**关键创新**：论文的关键创新在于提出了一个任务感知的对抗攻击框架，该框架能够有效地利用VLA模型的漏洞，生成能够诱导机器人产生不安全行为的对抗性扰动。此外，论文还提出了一个基于ISO标准的具身AI安全分类体系，为评估和防御具身AI系统的安全性提供了理论基础。

**关键设计**：ANNIE-Attack中的攻击引导模型采用强化学习算法，通过最大化攻击成功率来优化对抗性扰动。损失函数的设计考虑了安全违规的程度，例如，碰撞的损失高于接近的损失。对抗性扰动的生成采用投影梯度下降法，并限制扰动的幅度，以保证其隐蔽性。此外，论文还探索了稀疏和自适应的攻击策略，以提高攻击的效率和鲁棒性。

## 📊 实验亮点

实验结果表明，ANNIE-Attack在代表性的EAI模型上取得了超过50%的攻击成功率，证明了具身AI系统容易受到对抗性攻击。稀疏攻击策略能够在保持攻击成功率的同时，显著减少扰动的数量。自适应攻击策略能够根据环境变化动态调整扰动，提高攻击的鲁棒性。物理机器人实验验证了对抗性攻击在现实世界中的可行性和危害性。

## 🎯 应用场景

该研究成果可应用于评估和提升具身AI系统在各种实际场景中的安全性，例如自动驾驶、医疗机器人、家庭服务机器人等。通过对抗性攻击测试，可以发现系统潜在的安全漏洞，并指导开发更鲁棒的防御机制，从而保障人机交互的安全性和可靠性。未来的研究可以进一步探索针对物理世界攻击的防御方法，例如对抗训练、输入过滤等。

## 📄 摘要（原文）

> The integration of vision-language-action (VLA) models into embodied AI (EAI) robots is rapidly advancing their ability to perform complex, long-horizon tasks in humancentric environments. However, EAI systems introduce critical security risks: a compromised VLA model can directly translate adversarial perturbations on sensory input into unsafe physical actions. Traditional safety definitions and methodologies from the machine learning community are no longer sufficient. EAI systems raise new questions, such as what constitutes safety, how to measure it, and how to design effective attack and defense mechanisms in physically grounded, interactive settings. In this work, we present the first systematic study of adversarial safety attacks on embodied AI systems, grounded in ISO standards for human-robot interactions. We (1) formalize a principled taxonomy of safety violations (critical, dangerous, risky) based on physical constraints such as separation distance, velocity, and collision boundaries; (2) introduce ANNIEBench, a benchmark of nine safety-critical scenarios with 2,400 video-action sequences for evaluating embodied safety; and (3) ANNIE-Attack, a task-aware adversarial framework with an attack leader model that decomposes long-horizon goals into frame-level perturbations. Our evaluation across representative EAI models shows attack success rates exceeding 50% across all safety categories. We further demonstrate sparse and adaptive attack strategies and validate the real-world impact through physical robot experiments. These results expose a previously underexplored but highly consequential attack surface in embodied AI systems, highlighting the urgent need for security-driven defenses in the physical AI era. Code is available at https://github.com/RLCLab/Annie.

