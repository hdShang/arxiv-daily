---
layout: default
title: Adversarial Preference Learning for Robust LLM Alignment
---

# Adversarial Preference Learning for Robust LLM Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24369" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24369v1</a>
  <a href="https://arxiv.org/pdf/2505.24369.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24369v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24369v1', 'Adversarial Preference Learning for Robust LLM Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanfu Wang, Pengyu Wang, Chenyang Xi, Bo Tang, Junyi Zhu, Wenqiang Wei, Chen Chen, Chao Yang, Jingfeng Zhang, Chaochao Lu, Yijun Niu, Keming Mao, Zhiyu Li, Feiyu Xiong, Jie Hu, Mingchuan Yang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-30

**备注**: Accepted at ACL2025 Findings

---

## 💡 一句话要点

**提出对抗偏好学习以解决大型语言模型的鲁棒性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `对抗学习` `大型语言模型` `鲁棒性` `人类反馈` `强化学习` `自动化反馈` `生成对抗网络` `安全性`

## 📋 核心要点

1. 核心问题：现有的强化学习方法在处理对抗攻击时效率低且成本高，且容易受到反馈偏差影响。
2. 方法要点：提出对抗偏好学习（APL），通过直接有害性度量和条件生成攻击者来增强模型的鲁棒性。
3. 实验或效果：APL在Mistral-7B-Instruct-v0.3上实现了83.33%的无害性胜率，有害输出减少至0.43%，攻击成功率降低65%。

## 📝 摘要（中文）

现代语言模型通常依赖于人类反馈的强化学习（RLHF）来促进安全行为。然而，由于人类标注效率低、潜在对抗攻击多样性以及反馈偏差和奖励操控风险等三大限制，它们仍然容易受到对抗攻击。为了解决这些挑战，本文提出了对抗偏好学习（APL），这是一种迭代的对抗训练方法，包含三个关键创新：基于模型内在偏好概率的直接有害性度量、合成输入特定对抗变体的条件生成攻击者，以及通过自动闭环反馈实现的迭代框架。实验结果表明，APL显著增强了模型的鲁棒性，减少了有害输出，并保持了竞争力的实用性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在对抗攻击下的脆弱性，现有方法在处理人类反馈时存在效率低、成本高和反馈偏差等痛点。

**核心思路**：提出对抗偏好学习（APL），通过引入直接有害性度量和条件生成攻击者，减少对外部评估的依赖，从而提升模型的鲁棒性。

**技术框架**：APL的整体架构包括三个主要模块：直接有害性度量、条件生成攻击者和迭代反馈机制。直接有害性度量用于评估模型输出的潜在危害，条件生成攻击者则根据输入生成特定的对抗样本，迭代反馈机制则通过闭环反馈不断优化模型。

**关键创新**：APL的核心创新在于引入了基于模型内在偏好概率的有害性度量和条件生成攻击者，这与传统方法依赖外部评估的方式有本质区别。

**关键设计**：在设计中，采用了自动化的闭环反馈机制，确保模型能够在发现脆弱性后进行持续适应，此外，损失函数的设计也考虑了对抗样本的生成和评估。

## 📊 实验亮点

实验结果显示，APL在Mistral-7B-Instruct-v0.3上实现了83.33%的无害性胜率，相较于基线模型，有害输出从5.88%降至0.43%，攻击成功率降低了65%。同时，APL在实用性方面保持竞争力，MT-Bench得分为6.59，接近基线的6.78。

## 🎯 应用场景

该研究的潜在应用领域包括安全性要求高的对话系统、自动内容审核和人机交互等。通过提升大型语言模型的鲁棒性，APL能够有效减少有害输出，增强用户信任，未来可能在多个行业中发挥重要作用。

## 📄 摘要（原文）

> Modern language models often rely on Reinforcement Learning from Human Feedback (RLHF) to encourage safe behaviors. However, they remain vulnerable to adversarial attacks due to three key limitations: (1) the inefficiency and high cost of human annotation, (2) the vast diversity of potential adversarial attacks, and (3) the risk of feedback bias and reward hacking. To address these challenges, we introduce Adversarial Preference Learning (APL), an iterative adversarial training method incorporating three key innovations. First, a direct harmfulness metric based on the model's intrinsic preference probabilities, eliminating reliance on external assessment. Second, a conditional generative attacker that synthesizes input-specific adversarial variations. Third, an iterative framework with automated closed-loop feedback, enabling continuous adaptation through vulnerability discovery and mitigation. Experiments on Mistral-7B-Instruct-v0.3 demonstrate that APL significantly enhances robustness, achieving 83.33% harmlessness win rate over the base model (evaluated by GPT-4o), reducing harmful outputs from 5.88% to 0.43% (measured by LLaMA-Guard), and lowering attack success rate by up to 65% according to HarmBench. Notably, APL maintains competitive utility, with an MT-Bench score of 6.59 (comparable to the baseline 6.78) and an LC-WinRate of 46.52% against the base model.

