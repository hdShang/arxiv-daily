---
layout: default
title: A Reward-driven Automated Webshell Malicious-code Generator for Red-teaming
---

# A Reward-driven Automated Webshell Malicious-code Generator for Red-teaming

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24252" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24252v1</a>
  <a href="https://arxiv.org/pdf/2505.24252.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24252v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24252v1', 'A Reward-driven Automated Webshell Malicious-code Generator for Red-teaming')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yizhong Ding

**分类**: cs.CR, cs.AI

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出RAWG以解决WebShell恶意代码生成多样性不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `WebShell` `恶意代码生成` `网络安全` `强化学习` `大型语言模型` `红队测试` `数据集构建`

## 📋 核心要点

1. 现有恶意代码生成方法主要依赖提示工程，导致生成的负载多样性不足且冗余性高。
2. 本文提出RAWG，通过对WebShell样本进行分类并利用大型语言模型提取关键标记，创建标准化语料库以提升生成质量。
3. 实验结果显示，RAWG在负载多样性和逃逸有效性上显著优于当前最先进的方法，展示了其有效性。

## 📝 摘要（中文）

频繁的网络攻击使得WebShell的利用与防御成为网络安全研究的重点。然而，现有的恶意代码数据集缺乏公开且分类明确的样本，且现有生成方法在多样性和冗余性方面存在显著不足。为了解决这些问题，本文提出了RAWG，一个基于奖励驱动的自动WebShell恶意代码生成器，旨在红队应用中使用。我们首先将常见数据集中的WebShell样本分类为七种不同的混淆类型，然后利用大型语言模型提取和标准化关键标记，创建高质量的语料库。通过对开源大模型进行监督微调，RAWG能够生成多样化且高度混淆的恶意负载。实验表明，RAWG在负载多样性和逃逸有效性方面显著优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有WebShell恶意代码生成方法在多样性和冗余性方面的不足。现有方法主要依赖提示工程，导致生成的恶意代码缺乏变化，难以应对复杂的网络安全环境。

**核心思路**：RAWG的核心思路是通过奖励驱动的方式生成多样化的WebShell恶意代码。我们首先对WebShell样本进行分类，然后利用大型语言模型提取关键标记，创建标准化的高质量语料库，从而提升生成的多样性和有效性。

**技术框架**：RAWG的整体架构包括样本分类、关键标记提取、语料库构建、监督微调和强化学习五个主要模块。首先对样本进行分类，然后提取关键标记，接着构建语料库，最后通过监督微调和强化学习生成恶意代码。

**关键创新**：RAWG的主要创新在于引入了奖励驱动的强化学习方法，通过将恶意代码样本视为“选择”数据，良性代码视为“拒绝”数据，从而优化生成过程。这一方法显著提升了生成负载的多样性和逃逸能力。

**关键设计**：在关键设计上，我们采用了Proximal Policy Optimization (PPO)算法进行强化学习，设置了适当的损失函数以平衡恶意与良性样本的生成，确保生成的恶意代码在多样性和有效性之间取得良好平衡。通过对开源大模型的监督微调，进一步提升了生成质量。

## 📊 实验亮点

实验结果表明，RAWG在负载多样性和逃逸有效性方面显著优于现有最先进的方法，具体表现为生成的恶意代码在多样性上提升了XX%，逃逸成功率提高了YY%。这些结果验证了RAWG在实际应用中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全红队测试、恶意软件分析和防御策略评估。通过生成多样化的WebShell恶意代码，安全研究人员可以更有效地测试和评估现有防御机制的有效性，进而提升网络安全防护能力。未来，RAWG的技术可扩展到其他类型的恶意代码生成，推动网络安全领域的研究与应用发展。

## 📄 摘要（原文）

> Frequent cyber-attacks have elevated WebShell exploitation and defense to a critical research focus within network security. However, there remains a significant shortage of publicly available, well-categorized malicious-code datasets organized by obfuscation method. Existing malicious-code generation methods, which primarily rely on prompt engineering, often suffer from limited diversity and high redundancy in the payloads they produce. To address these limitations, we propose \textbf{RAWG}, a \textbf{R}eward-driven \textbf{A}utomated \textbf{W}ebshell Malicious-code \textbf{G}enerator designed for red-teaming applications. Our approach begins by categorizing webshell samples from common datasets into seven distinct types of obfuscation. We then employ a large language model (LLM) to extract and normalize key tokens from each sample, creating a standardized, high-quality corpus. Using this curated dataset, we perform supervised fine-tuning (SFT) on an open-source large model to enable the generation of diverse, highly obfuscated webshell malicious payloads. To further enhance generation quality, we apply Proximal Policy Optimization (PPO), treating malicious-code samples as "chosen" data and benign code as "rejected" data during reinforcement learning. Extensive experiments demonstrate that RAWG significantly outperforms current state-of-the-art methods in both payload diversity and escape effectiveness.

