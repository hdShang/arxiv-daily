---
layout: default
title: "VERA: Variational Inference Framework for Jailbreaking Large Language Models"
---

# VERA: Variational Inference Framework for Jailbreaking Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22666" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22666v2</a>
  <a href="https://arxiv.org/pdf/2506.22666.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22666v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22666v2', 'VERA: Variational Inference Framework for Jailbreaking Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anamika Lochab, Lu Yan, Patrick Pynadath, Xiangyu Zhang, Ruqi Zhang

**分类**: cs.CR, cs.CL, cs.LG, stat.ML

**发布日期**: 2025-06-27 (更新: 2025-11-06)

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出VERA框架以解决大型语言模型的黑箱越狱问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `黑箱越狱` `变分推断` `对抗提示` `大型语言模型` `模型脆弱性` `安全性测试` `机器学习`

## 📋 核心要点

1. 现有黑箱越狱方法依赖遗传算法，存在初始化依赖和手动提示池的局限，无法全面表征模型脆弱性。
2. VERA框架将黑箱越狱提示视为变分推断问题，通过训练小型攻击者模型生成多样化的对抗提示，避免了重复优化。
3. 实验结果显示，VERA在多种目标语言模型上表现出色，验证了概率推断在对抗提示生成中的有效性。

## 📝 摘要（中文）

随着API访问主流大型语言模型的普及，识别模型在实际应用中的脆弱性变得愈发重要。现有的黑箱越狱方法多依赖遗传算法，面临初始化依赖和手动提示池的局限性，且每个提示需单独优化，无法全面表征模型脆弱性。为此，本文提出VERA：变分推断框架用于越狱，旨在将黑箱越狱提示视为变分推断问题，通过训练小型攻击者语言模型来近似目标模型的对抗提示后验分布。实验结果表明，VERA在多种目标语言模型上表现优异，展示了概率推断在对抗提示生成中的价值。

## 🔬 方法详解

**问题定义**：本文旨在解决现有黑箱越狱方法的局限性，包括对初始化的依赖、手动提示池的使用以及每个提示需单独优化的问题。这些问题导致无法全面表征模型的脆弱性。

**核心思路**：VERA框架的核心思路是将黑箱越狱提示生成视为变分推断问题，通过训练一个小型攻击者语言模型来近似目标模型的对抗提示后验分布。这种设计使得攻击者模型能够生成多样化且流畅的越狱提示，而无需对每个提示进行重新优化。

**技术框架**：VERA的整体架构包括两个主要模块：攻击者模型和目标模型。首先，攻击者模型通过变分推断学习目标模型的对抗提示分布；然后，利用训练好的攻击者模型生成多样化的越狱提示。

**关键创新**：VERA的主要创新在于将黑箱越狱问题转化为变分推断问题，这一方法与传统的遗传算法等方法本质上不同，后者往往依赖于手动提示和单独优化。

**关键设计**：在设计中，VERA采用了特定的损失函数来优化攻击者模型的输出，并通过调整模型参数来提高生成提示的多样性和流畅性。

## 📊 实验亮点

实验结果表明，VERA在多种目标语言模型上均取得了显著的性能提升，生成的对抗提示在流畅性和多样性上优于传统方法，验证了其在对抗提示生成中的有效性和实用性。

## 🎯 应用场景

VERA框架在安全性测试、模型脆弱性评估等领域具有广泛的应用潜力。通过有效识别大型语言模型的脆弱性，能够帮助开发者增强模型的安全性，防止潜在的滥用和攻击。此外，VERA的思路也可扩展至其他类型的机器学习模型，推动模型安全研究的发展。

## 📄 摘要（原文）

> The rise of API-only access to state-of-the-art LLMs highlights the need for effective black-box jailbreak methods to identify model vulnerabilities in real-world settings. Without a principled objective for gradient-based optimization, most existing approaches rely on genetic algorithms, which are limited by their initialization and dependence on manually curated prompt pools. Furthermore, these methods require individual optimization for each prompt, failing to provide a comprehensive characterization of model vulnerabilities. To address this gap, we introduce VERA: Variational infErence fRamework for jAilbreaking. VERA casts black-box jailbreak prompting as a variational inference problem, training a small attacker LLM to approximate the target LLM's posterior over adversarial prompts. Once trained, the attacker can generate diverse, fluent jailbreak prompts for a target query without re-optimization. Experimental results show that VERA achieves strong performance across a range of target LLMs, highlighting the value of probabilistic inference for adversarial prompt generation.

