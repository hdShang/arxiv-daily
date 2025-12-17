---
layout: default
title: VERA-V: Variational Inference Framework for Jailbreaking Vision-Language Models
---

# VERA-V: Variational Inference Framework for Jailbreaking Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17759" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17759v1</a>
  <a href="https://arxiv.org/pdf/2510.17759.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17759v1" onclick="toggleFavorite(this, '2510.17759v1', 'VERA-V: Variational Inference Framework for Jailbreaking Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qilin Liao, Anamika Lochab, Ruqi Zhang

**分类**: cs.CR, cs.CL, cs.CV, cs.LG, stat.ML

**发布日期**: 2025-10-20

**备注**: 18 pages, 7 Figures,

---

## 💡 一句话要点

**提出VERA-V框架以解决多模态模型的漏洞发现问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `对抗攻击` `变分推断` `视觉-语言模型` `安全性测试` `模型脆弱性` `隐蔽攻击` `深度学习`

## 📋 核心要点

1. 现有的多模态攻击方法依赖脆弱模板，且集中于单一攻击场景，导致漏洞发现的局限性。
2. VERA-V框架通过学习文本-图像提示的联合后验分布，生成隐蔽的对抗输入，从而有效绕过模型的保护机制。
3. 在HarmBench和HADES基准测试中，VERA-V在攻击成功率上显著提升，最高可达53.75%的增幅。

## 📝 摘要（中文）

视觉-语言模型（VLMs）扩展了大型语言模型的视觉推理能力，但其多模态设计也引入了新的、尚未充分探索的脆弱性。现有的多模态攻击方法主要依赖脆弱的模板，集中于单一攻击场景，并仅暴露出狭窄的漏洞。为了解决这些局限性，本文提出了VERA-V，一个变分推断框架，将多模态越狱发现重新表述为学习成对文本-图像提示的联合后验分布。这种概率视角使得生成隐蔽的、耦合的对抗输入成为可能，从而绕过模型的保护机制。我们训练了一个轻量级攻击者来近似后验，从而高效采样多样的越狱输入，并提供对漏洞的分布性洞察。VERA-V还整合了三种互补策略：基于排版的文本提示、基于扩散的图像合成以及结构化干扰物，以分散VLM的注意力。实验结果表明，VERA-V在HarmBench和HADES基准测试中，持续超越现有最先进的基线，在GPT-4o上攻击成功率提高了53.75%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态模型在越狱攻击中的脆弱性，现有方法主要依赖于脆弱的模板，无法全面揭示模型的漏洞。

**核心思路**：VERA-V框架通过变分推断的方式，将多模态越狱问题转化为学习文本与图像提示的联合后验分布，从而生成隐蔽的对抗输入。

**技术框架**：VERA-V的整体架构包括三个主要模块：1) 轻量级攻击者用于近似后验分布；2) 基于排版的文本提示嵌入有害线索；3) 基于扩散的图像合成引入对抗信号。

**关键创新**：VERA-V的核心创新在于将越狱发现视为概率问题，允许生成耦合的对抗输入，显著提高了攻击的隐蔽性和成功率。

**关键设计**：在设计中，采用了特定的损失函数以优化后验近似，网络结构经过精简以提高采样效率，同时引入结构化干扰物以分散模型的注意力。

## 📊 实验亮点

实验结果显示，VERA-V在HarmBench和HADES基准测试中表现优异，相较于最佳基线在GPT-4o上攻击成功率提高了53.75%，展现了其在多模态越狱攻击中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括安全性测试、对抗样本生成以及多模态模型的鲁棒性评估。通过揭示模型的脆弱性，VERA-V能够帮助开发更安全的视觉-语言系统，提升其在实际应用中的可靠性和安全性。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) extend large language models with visual reasoning, but their multimodal design also introduces new, underexplored vulnerabilities. Existing multimodal red-teaming methods largely rely on brittle templates, focus on single-attack settings, and expose only a narrow subset of vulnerabilities. To address these limitations, we introduce VERA-V, a variational inference framework that recasts multimodal jailbreak discovery as learning a joint posterior distribution over paired text-image prompts. This probabilistic view enables the generation of stealthy, coupled adversarial inputs that bypass model guardrails. We train a lightweight attacker to approximate the posterior, allowing efficient sampling of diverse jailbreaks and providing distributional insights into vulnerabilities. VERA-V further integrates three complementary strategies: (i) typography-based text prompts that embed harmful cues, (ii) diffusion-based image synthesis that introduces adversarial signals, and (iii) structured distractors to fragment VLM attention. Experiments on HarmBench and HADES benchmarks show that VERA-V consistently outperforms state-of-the-art baselines on both open-source and frontier VLMs, achieving up to 53.75% higher attack success rate (ASR) over the best baseline on GPT-4o.

