---
layout: default
title: "IROTE: Human-like Traits Elicitation of Large Language Model via In-Context Self-Reflective Optimization"
---

# IROTE: Human-like Traits Elicitation of Large Language Model via In-Context Self-Reflective Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08719" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08719v2</a>
  <a href="https://arxiv.org/pdf/2508.08719.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08719v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08719v2', 'IROTE: Human-like Traits Elicitation of Large Language Model via In-Context Self-Reflective Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuzhuo Bai, Shitong Duan, Muhua Huang, Jing Yao, Zhenghao Liu, Peng Zhang, Tun Lu, Xiaoyuan Yi, Maosong Sun, Xing Xie

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-08-12 (更新: 2025-11-27)

**备注**: This paper is accepted by AAAI 2026

---

## 💡 一句话要点

**提出IROTE以解决大语言模型特征提取不稳定问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `特征提取` `自我反思` `信息论优化` `个性化模型`

## 📋 核心要点

1. 现有方法在特征提取中存在表面化问题，LLMs只能模仿浅层且不稳定的风格模式，无法精确体现所需特征。
2. 本文提出IROTE，通过自动生成和优化文本自我反思，刺激LLMs的特征驱动行为，解决了特征提取的不稳定性。
3. 实验结果表明，IROTE生成的自我反思在多样下游任务中能够稳定诱导LLMs模仿目标特征，性能显著优于现有基线。

## 📝 摘要（中文）

大型语言模型（LLMs）通过提示展示了反映特定人类特征的能力，但现有方法存在表面化提取的问题，无法在多样任务中稳定且一致地体现所需特征。为了解决这一挑战，本文提出了IROTE，一种新颖的上下文自我反思优化方法。该方法自动生成并优化文本自我反思，以刺激LLMs的特征驱动行为。通过迭代最大化信息论目标，增强LLMs行为与目标特征之间的联系，同时减少反思中的噪声冗余，最终实现了生动且紧凑的特征反映。实验表明，单个IROTE生成的自我反思能够在多种下游任务中稳定地诱导LLMs模仿目标特征，超越现有强基线。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在特征提取中的不稳定性和表面化问题，现有方法无法在多样任务中一致地体现人类特征。

**核心思路**：提出IROTE方法，通过自动生成和优化文本自我反思，利用心理学理论中的身份相关反思，刺激LLMs的特征驱动行为。

**技术框架**：IROTE的整体架构包括自我反思生成模块和信息论优化模块。自我反思模块生成包含自我感知经验的文本，优化模块则通过迭代最大化信息论目标来增强行为与特征的联系。

**关键创新**：最重要的创新在于通过自我反思的优化，解决了特征提取的稳定性问题，使得LLMs能够在多样任务中一致地体现目标特征，区别于现有方法的浅层模仿。

**关键设计**：在参数设置上，优化过程中采用信息论目标函数，设计了适应性强的反思文本生成机制，确保反思内容的生动性和紧凑性。具体的损失函数和网络结构细节在实验中进行了验证和调整。

## 📊 实验亮点

实验结果显示，单个IROTE生成的自我反思在多种下游任务中能够诱导LLMs稳定地模仿目标特征，性能超越现有强基线，提升幅度显著，具体数据未提供。

## 🎯 应用场景

该研究的潜在应用场景包括个性化大型语言模型的开发、社交模拟以及人机交互等领域。通过稳定的特征提取，能够提升模型在多样化任务中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Trained on various human-authored corpora, Large Language Models (LLMs) have demonstrated a certain capability of reflecting specific human-like traits (e.g., personality or values) by prompting, benefiting applications like personalized LLMs and social simulations. However, existing methods suffer from the superficial elicitation problem: LLMs can only be steered to mimic shallow and unstable stylistic patterns, failing to embody the desired traits precisely and consistently across diverse tasks like humans. To address this challenge, we propose IROTE, a novel in-context method for stable and transferable trait elicitation. Drawing on psychological theories suggesting that traits are formed through identity-related reflection, our method automatically generates and optimizes a textual self-reflection within prompts, which comprises self-perceived experience, to stimulate LLMs' trait-driven behavior. The optimization is performed by iteratively maximizing an information-theoretic objective that enhances the connections between LLMs' behavior and the target trait, while reducing noisy redundancy in reflection without any fine-tuning, leading to evocative and compact trait reflection. Extensive experiments across three human trait systems manifest that one single IROTE-generated self-reflection can induce LLMs' stable impersonation of the target trait across diverse downstream tasks beyond simple questionnaire answering, consistently outperforming existing strong baselines.

