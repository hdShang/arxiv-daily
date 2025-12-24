---
layout: default
title: What Really Matters in Many-Shot Attacks? An Empirical Study of Long-Context Vulnerabilities in LLMs
---

# What Really Matters in Many-Shot Attacks? An Empirical Study of Long-Context Vulnerabilities in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19773" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19773v1</a>
  <a href="https://arxiv.org/pdf/2505.19773.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19773v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19773v1', 'What Really Matters in Many-Shot Attacks? An Empirical Study of Long-Context Vulnerabilities in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sangyeop Kim, Yohan Lee, Yongwoo Song, Kimin Lee

**分类**: cs.CL, cs.CR

**发布日期**: 2025-05-26

**备注**: Accepted by ACL 2025

---

## 💡 一句话要点

**研究长上下文漏洞，揭示LLM安全机制的不足**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文` `大型语言模型` `安全机制` `多次攻击` `模型漏洞` `实验研究` `文本生成`

## 📋 核心要点

1. 现有大型语言模型在处理长上下文时存在安全漏洞，攻击者可以利用这些漏洞绕过安全措施。
2. 论文通过多次攻击实验，揭示上下文长度对攻击有效性的影响，提出了新的安全机制需求。
3. 实验结果表明，即使是简单的重复文本也能成功攻击模型，显示出模型在长上下文处理上的不足。

## 📝 摘要（中文）

本研究通过多次攻击（Many-Shot Jailbreaking, MSJ）探讨大型语言模型（LLMs）中的长上下文漏洞。实验使用了高达128K标记的上下文长度。通过对不同指令风格、攻击密度、主题和格式的多种多次攻击设置进行全面分析，发现上下文长度是决定攻击有效性的主要因素。成功的攻击并不需要精心设计的有害内容，即使是重复的样本或随机的虚假文本也能绕过模型的安全措施。这表明LLMs在长上下文处理能力上的根本局限性，且随着上下文的增加，模型的安全行为变得越来越不一致。这些发现突显了LLMs在上下文扩展能力上的重大安全缺口，强调了新安全机制的必要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在长上下文处理中的安全漏洞问题。现有方法在面对长上下文时，模型的安全性和一致性显著下降，攻击者可以轻易绕过安全措施。

**核心思路**：论文的核心思路是通过多次攻击实验来分析长上下文对模型安全性的影响，强调上下文长度是决定攻击成功与否的关键因素。通过这种方式，研究揭示了模型在长上下文处理中的根本局限性。

**技术框架**：整体架构包括多个实验设置，涵盖不同的指令风格、攻击密度、主题和格式。每个实验都旨在评估上下文长度对攻击效果的影响，最终形成对模型安全性的综合评估。

**关键创新**：最重要的技术创新点在于揭示了长上下文处理中的安全漏洞，尤其是成功攻击不需要复杂的有害内容，这与现有方法的假设形成鲜明对比。

**关键设计**：实验中使用了高达128K标记的上下文长度，设计了多种攻击样本，包括重复文本和随机虚假文本，以测试模型的安全性和一致性。

## 📊 实验亮点

实验结果表明，使用128K标记的上下文长度时，攻击成功率显著提高，甚至简单的重复文本和随机内容也能有效绕过模型的安全措施。这一发现强调了现有模型在长上下文处理中的安全缺陷，促使对新安全机制的需求。

## 🎯 应用场景

该研究的潜在应用场景包括大型语言模型的安全性评估和改进，尤其是在需要处理长文本的应用中，如法律文书分析、技术文档生成等。研究结果将推动新安全机制的开发，以增强模型在长上下文处理中的安全性和可靠性。

## 📄 摘要（原文）

> We investigate long-context vulnerabilities in Large Language Models (LLMs) through Many-Shot Jailbreaking (MSJ). Our experiments utilize context length of up to 128K tokens. Through comprehensive analysis with various many-shot attack settings with different instruction styles, shot density, topic, and format, we reveal that context length is the primary factor determining attack effectiveness. Critically, we find that successful attacks do not require carefully crafted harmful content. Even repetitive shots or random dummy text can circumvent model safety measures, suggesting fundamental limitations in long-context processing capabilities of LLMs. The safety behavior of well-aligned models becomes increasingly inconsistent with longer contexts. These findings highlight significant safety gaps in context expansion capabilities of LLMs, emphasizing the need for new safety mechanisms.

