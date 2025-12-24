---
layout: default
title: Proactive Guidance of Multi-Turn Conversation in Industrial Search
---

# Proactive Guidance of Multi-Turn Conversation in Industrial Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24251" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24251v1</a>
  <a href="https://arxiv.org/pdf/2505.24251.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24251v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24251v1', 'Proactive Guidance of Multi-Turn Conversation in Industrial Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyu Li, Xiao Li, Li Gao, Yiding Liu, Xiaoyang Wang, Shuaiqiang Wang, Junfeng Wang, Dawei Yin

**分类**: cs.CL, cs.IR

**发布日期**: 2025-05-30

**备注**: ACL'25 (Industry)

---

## 💡 一句话要点

**提出双阶段框架以主动引导工业搜索中的多轮对话**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `主动引导` `目标适应` `强化学习` `知识蒸馏` `用户体验` `工业搜索`

## 📋 核心要点

1. 现有多轮对话系统在动态适应用户目标变化和保持低延迟交互方面存在显著挑战。
2. 本文提出的双阶段框架通过目标自适应监督微调和点击导向强化学习，提供主动引导以提升用户体验。
3. 实验结果显示，该框架在准确率和点击率上均有显著提升，同时有效降低了推理延迟。

## 📝 摘要（中文）

大型语言模型（LLMs）的发展显著推动了多轮对话系统的进步，强调了主动引导以增强用户交互的必要性。然而，这些系统在动态适应用户目标变化和保持实时交互的低延迟方面面临挑战。本文在百度搜索AI助手中提出了一种新颖的双阶段框架，以提供主动引导。第一阶段为目标自适应监督微调（G-SFT），通过目标适应代理动态调整用户目标并提供相关上下文信息，同时结合可扩展知识转移，将LLMs的见解提炼到轻量级模型中以实现实时交互。第二阶段为点击导向强化学习（C-RL），采用生成-排序范式，从用户点击信号系统构建偏好对，并通过更具吸引力的引导主动提高点击率。实验结果表明，该框架在离线评估中实现了86.10%的准确率（比基线提高23.95%），在线部署中的点击率为25.28%（相对提升149.06%），同时通过可扩展知识蒸馏将推理延迟降低了69.55%。

## 🔬 方法详解

**问题定义**：本文旨在解决工业搜索中的多轮对话系统在用户目标动态变化时的适应性不足及实时交互的延迟问题。现有方法难以有效跟踪用户目标并提供及时的反馈。

**核心思路**：论文提出的双阶段框架通过G-SFT和C-RL相结合，动态调整用户目标并优化交互质量，以实现更高效的用户引导。这样的设计旨在确保系统能够实时响应用户需求，同时提升用户的交互体验。

**技术框架**：整体架构分为两个主要阶段：第一阶段为目标自适应监督微调（G-SFT），通过目标适应代理提供相关上下文信息；第二阶段为点击导向强化学习（C-RL），通过生成-排序范式优化用户点击率。

**关键创新**：最重要的技术创新在于将G-SFT与C-RL结合，形成一个互补的双阶段架构，确保准确的目标跟踪与高质量的用户交互。这与现有方法的单一目标追踪或反馈机制形成了明显区别。

**关键设计**：在G-SFT中，采用了可扩展的知识转移技术，将LLMs的知识提炼到轻量级模型中；在C-RL中，通过用户点击信号构建偏好对，设计了相应的损失函数以优化点击率。

## 📊 实验亮点

实验结果表明，提出的双阶段框架在离线评估中达到了86.10%的准确率，相较于基线提升了23.95%；在线部署中点击率达25.28%，实现了149.06%的相对提升，同时推理延迟降低了69.55%。

## 🎯 应用场景

该研究的潜在应用领域包括智能搜索助手、在线客服系统和人机交互界面等。通过提升多轮对话的交互质量和响应速度，能够显著改善用户体验，推动相关行业的智能化进程。未来，该框架有望在更广泛的场景中应用，进一步提升人机交互的智能化水平。

## 📄 摘要（原文）

> The evolution of Large Language Models (LLMs) has significantly advanced multi-turn conversation systems, emphasizing the need for proactive guidance to enhance users' interactions. However, these systems face challenges in dynamically adapting to shifts in users' goals and maintaining low latency for real-time interactions. In the Baidu Search AI assistant, an industrial-scale multi-turn search system, we propose a novel two-phase framework to provide proactive guidance. The first phase, Goal-adaptive Supervised Fine-Tuning (G-SFT), employs a goal adaptation agent that dynamically adapts to user goal shifts and provides goal-relevant contextual information. G-SFT also incorporates scalable knowledge transfer to distill insights from LLMs into a lightweight model for real-time interaction. The second phase, Click-oriented Reinforcement Learning (C-RL), adopts a generate-rank paradigm, systematically constructs preference pairs from user click signals, and proactively improves click-through rates through more engaging guidance. This dual-phase architecture achieves complementary objectives: G-SFT ensures accurate goal tracking, while C-RL optimizes interaction quality through click signal-driven reinforcement learning. Extensive experiments demonstrate that our framework achieves 86.10% accuracy in offline evaluation (+23.95% over baseline) and 25.28% CTR in online deployment (149.06% relative improvement), while reducing inference latency by 69.55% through scalable knowledge distillation.

