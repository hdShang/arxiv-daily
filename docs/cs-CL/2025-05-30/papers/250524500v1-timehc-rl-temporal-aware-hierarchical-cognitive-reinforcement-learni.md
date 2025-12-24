---
layout: default
title: TimeHC-RL: Temporal-aware Hierarchical Cognitive Reinforcement Learning for Enhancing LLMs' Social Intelligence
---

# TimeHC-RL: Temporal-aware Hierarchical Cognitive Reinforcement Learning for Enhancing LLMs' Social Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24500" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24500v1</a>
  <a href="https://arxiv.org/pdf/2505.24500.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24500v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24500v1', 'TimeHC-RL: Temporal-aware Hierarchical Cognitive Reinforcement Learning for Enhancing LLMs\' Social Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guiyang Hou, Xing Gao, Yuchuan Wu, Xiang Huang, Wenqi Zhang, Zhe Zheng, Yongliang Shen, Jialu Du, Fei Huang, Yongbin Li, Weiming Lu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30

**备注**: 22 pages, 12 figures

---

## 💡 一句话要点

**提出TimeHC-RL以提升大语言模型的社会智能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `社会智能` `强化学习` `时间感知` `层次认知` `后训练` `认知发展`

## 📋 核心要点

1. 现有方法在提升大语言模型的社会智能方面探索不足，尤其是在后训练阶段的应用。
2. 提出的TimeHC-RL方法结合了时间感知和层次认知，旨在通过多种认知模式提升LLMs的社会智能。
3. 实验结果表明，TimeHC-RL方法在多个数据集上优于传统的系统2强化学习方法，显著提升了模型性能。

## 📝 摘要（中文）

近年来，大语言模型（LLMs）在需要深思熟虑的IQ相关领域取得了显著进展，如数学和编程。然而，从后训练的角度来看，提升LLMs在社会领域的认知发展仍然未被充分探索。本文提出了时间感知层次认知强化学习（TimeHC-RL），旨在增强LLMs的社会智能。通过对八个具有多样数据模式的数据集进行实验，我们系统地探索了提升LLMs社会智能的有效性，并验证了TimeHC-RL方法的优越性。实验结果显示，TimeHC-RL方法在性能上超越了广泛采用的系统2强化学习方法，使得7B基础模型的表现能够与DeepSeek-R1和OpenAI-O3等先进模型相媲美。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在社会智能方面的认知发展不足，现有方法主要集中于数学等领域，缺乏对社会认知的深入探索。

**核心思路**：TimeHC-RL方法通过引入时间感知和层次认知的概念，结合直观反应与深思熟虑的思维模式，以适应社会领域的复杂性。

**技术框架**：该方法的整体架构包括时间感知模块、层次认知模块和强化学习模块，旨在通过多层次的认知过程提升模型的社会智能。

**关键创新**：TimeHC-RL的核心创新在于将时间感知与层次认知结合，突破了传统系统2强化学习方法的局限，使得模型能够更好地处理社会交互中的动态变化。

**关键设计**：在模型设计中，采用了特定的损失函数和参数设置，以优化时间感知和层次认知的融合效果，同时确保模型在多样化数据集上的适应性。

## 📊 实验亮点

实验结果显示，TimeHC-RL方法在八个数据集上的表现显著优于传统的系统2强化学习方法，尤其是在社会智能任务中，7B基础模型的性能提升幅度达到与DeepSeek-R1和OpenAI-O3相当的水平，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、智能客服和教育领域等，能够帮助这些系统更好地理解和应对人类的社会行为。未来，TimeHC-RL方法可能在提升人机交互的自然性和有效性方面发挥重要作用。

## 📄 摘要（原文）

> Recently, Large Language Models (LLMs) have made significant progress in IQ-related domains that require careful thinking, such as mathematics and coding. However, enhancing LLMs' cognitive development in social domains, particularly from a post-training perspective, remains underexplored. Recognizing that the social world follows a distinct timeline and requires a richer blend of cognitive modes (from intuitive reactions (System 1) and surface-level thinking to deliberate thinking (System 2)) than mathematics, which primarily relies on System 2 cognition (careful, step-by-step reasoning), we introduce Temporal-aware Hierarchical Cognitive Reinforcement Learning (TimeHC-RL) for enhancing LLMs' social intelligence. In our experiments, we systematically explore improving LLMs' social intelligence and validate the effectiveness of the TimeHC-RL method, through five other post-training paradigms and two test-time intervention paradigms on eight datasets with diverse data patterns. Experimental results reveal the superiority of our proposed TimeHC-RL method compared to the widely adopted System 2 RL method. It gives the 7B backbone model wings, enabling it to rival the performance of advanced models like DeepSeek-R1 and OpenAI-O3. Additionally, the systematic exploration from post-training and test-time interventions perspectives to improve LLMs' social intelligence has uncovered several valuable insights.

