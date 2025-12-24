---
layout: default
title: "Igniting Creative Writing in Small Language Models: LLM-as-a-Judge versus Multi-Agent Refined Rewards"
---

# Igniting Creative Writing in Small Language Models: LLM-as-a-Judge versus Multi-Agent Refined Rewards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21476" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21476v1</a>
  <a href="https://arxiv.org/pdf/2508.21476.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21476v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21476v1', 'Igniting Creative Writing in Small Language Models: LLM-as-a-Judge versus Multi-Agent Refined Rewards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaolong Wei, Bo Lu, Xingyu Zhang, Zhejun Zhao, Dongdong Shen, Long Xia, Dawei Yin

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-29

**备注**: EMNLP 2025 Main

**🔗 代码/项目**: [GITHUB](https://github.com/weixiaolong94-hub/Igniting-Creative-Writing-in-Small-Language-Models)

---

## 💡 一句话要点

**提出RLAIF框架以提升小型语言模型的创意写作能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小型语言模型` `创意写作` `强化学习` `AI反馈` `多代理框架` `对抗训练` `中文生成`

## 📋 核心要点

1. 现有的小型语言模型在创意写作方面的能力有限，尤其是在新颖性和生成质量上存在不足。
2. 论文提出了两种基于AI反馈的奖励策略，旨在提升小型语言模型的创意写作能力，特别是中文问候语的生成。
3. 实验结果显示，原则引导的LLM作为评判者在生成质量和训练效率上均优于传统方法，显著提升了创意输出。

## 📝 摘要（中文）

大型语言模型（LLMs）在创意写作方面表现出色，但其高计算需求限制了广泛应用。增强小型语言模型（SLMs）成为一种有前景的替代方案，但现有的监督微调（SFT）方法在新颖性上存在不足，而基于人类反馈的强化学习（RLHF）成本高昂。本文探讨了在强化学习框架下的两种AI驱动奖励策略，以激发7B参数SLM的创意写作能力，特别是在生成中文问候语方面。第一种策略利用高质量偏好数据训练的奖励模型（RM），通过一种新颖的多代理拒绝采样框架进行创意任务的设计。第二种更具创新性的策略采用原则引导的LLM作为评判者，通过对抗训练方案优化奖励函数，直接提供奖励信号。实验结果表明，两种方法均显著提升了创意输出，且原则引导的LLM作为评判者在生成质量上表现优越，训练效率高且对人类标注数据的依赖减少，展示了更具可扩展性和有效性的创意SLM路径。

## 🔬 方法详解

**问题定义**：本文旨在解决小型语言模型在创意写作中的新颖性不足和生成质量低的问题。现有的监督微调和基于人类反馈的强化学习方法在成本和效率上均存在挑战。

**核心思路**：论文提出的RLAIF框架结合了两种AI驱动的奖励策略，旨在通过高质量的偏好数据和原则引导的评判机制来提升小型语言模型的创意写作能力。

**技术框架**：整体架构包括两个主要模块：第一是基于多代理拒绝采样的奖励模型，第二是原则引导的LLM作为评判者，后者通过对抗训练优化奖励信号。

**关键创新**：最重要的创新在于引入了原则引导的LLM作为评判者，通过对抗训练机制直接提供奖励信号，这一方法显著提高了生成质量和训练效率。

**关键设计**：在奖励模型的训练中，使用了高质量的偏好数据，损失函数设计考虑了生成内容的多样性和质量，网络结构则采用了适合创意任务的多代理框架。

## 📊 实验亮点

实验结果表明，原则引导的LLM作为评判者在生成质量上显著优于基线方法，创意输出提升幅度明显。此外，该方法在训练效率上也表现出色，减少了对人类标注数据的依赖，展示了更高的可扩展性。

## 🎯 应用场景

该研究的潜在应用领域包括智能写作助手、社交媒体内容生成和个性化问候语生成等。通过提升小型语言模型的创意写作能力，可以在多种场景中实现更自然和人性化的交互，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable creative writing capabilities, yet their substantial computational demands hinder widespread use. Enhancing Small Language Models (SLMs) offers a promising alternative, but current methods like Supervised Fine-Tuning (SFT) struggle with novelty, and Reinforcement Learning from Human Feedback (RLHF) is costly. This paper explores two distinct AI-driven reward strategies within a Reinforcement Learning from AI Feedback (RLAIF) framework to ignite the creative writing of a 7B-parameter SLM, specifically for generating Chinese greetings. The first strategy employs a RM trained on high-quality preference data curated by a novel multi-agent rejection sampling framework designed for creative tasks. The second, more novel strategy utilizes a principle-guided LLM-as-a-Judge, whose reward function is optimized via an adversarial training scheme with a reflection mechanism, to directly provide reward signals. Comprehensive experiments reveal that while both approaches significantly enhance creative output over baselines, the principle-guided LLM-as-a-Judge demonstrably yields superior generation quality. Furthermore, it offers notable advantages in training efficiency and reduced dependency on human-annotated data, presenting a more scalable and effective path towards creative SLMs. Our automated evaluation methods also exhibit strong alignment with human judgments. Our code and data are publicly available at https://github.com/weixiaolong94-hub/Igniting-Creative-Writing-in-Small-Language-Models.

