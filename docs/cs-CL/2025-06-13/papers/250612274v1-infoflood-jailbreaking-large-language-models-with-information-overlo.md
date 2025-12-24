---
layout: default
title: "InfoFlood: Jailbreaking Large Language Models with Information Overload"
---

# InfoFlood: Jailbreaking Large Language Models with Information Overload

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12274" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12274v1</a>
  <a href="https://arxiv.org/pdf/2506.12274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12274v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12274v1', 'InfoFlood: Jailbreaking Large Language Models with Information Overload')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Advait Yadav, Haibo Jin, Man Luo, Jun Zhuang, Haohan Wang

**分类**: cs.CR, cs.CL

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出InfoFlood以解决大语言模型的安全漏洞问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信息过载` `越狱攻击` `大型语言模型` `安全机制` `语言转换` `网络安全` `人工智能伦理`

## 📋 核心要点

1. 现有的越狱方法依赖于添加前缀或后缀，存在一定的局限性，无法有效应对信息过载带来的新型攻击。
2. InfoFlood通过语言转换将恶意查询转化为复杂查询，直接利用语言复杂性来绕过安全机制。
3. 实验结果表明，InfoFlood在四种主流LLMs上表现优异，成功率比传统方法高出三倍，显示出其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个领域展现了卓越的能力，但其生成有害响应的潜力引发了社会和监管方面的重大担忧。现有的越狱方法通常通过在恶意提示中附加精心设计的前缀或后缀来绕过模型的内置安全机制。本文识别出一种新漏洞，即过度的语言复杂性可以在不需要任何附加前缀或后缀的情况下破坏内置安全机制，从而允许攻击者直接引发有害输出。我们提出了InfoFlood，一种越狱攻击，能够将恶意查询转化为复杂的信息过载查询，从而绕过内置安全机制。通过对四种广泛使用的LLMs进行实证验证，InfoFlood的成功率显著高于基线攻击，最高可达三倍。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在面对信息过载时的安全漏洞，现有方法无法有效应对这种新型攻击，导致模型易受操控。

**核心思路**：InfoFlood的核心思路是利用语言复杂性而非传统的前缀或后缀，直接生成复杂的恶意查询，从而绕过模型的安全机制。

**技术框架**：InfoFlood的整体架构包括三个主要模块：1) 语言转换模块，用于重述恶意查询；2) 失败原因识别模块，分析未成功的尝试；3) 结构优化模块，调整查询结构以保持恶意意图。

**关键创新**：InfoFlood的最大创新在于其不依赖于附加的前缀或后缀，而是通过信息过载直接影响模型的输出，显著区别于传统的越狱方法。

**关键设计**：在设计上，InfoFlood采用了多种语言转换技术，确保生成的查询在复杂性上超出模型的处理能力，同时保持其恶意意图不变。

## 📊 实验亮点

实验结果显示，InfoFlood在四种主流大型语言模型上实现了显著的越狱成功率，最高可达三倍于基线攻击，且常用的后处理防御措施如OpenAI的Moderation API未能有效抵御此类攻击，揭示了传统AI安全防护的重大缺陷。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、内容审查和人工智能伦理等。通过识别和利用大型语言模型的漏洞，研究者和开发者可以更好地理解模型的局限性，从而设计出更有效的安全防护措施，提升AI系统的安全性和可靠性。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities across various domains. However, their potential to generate harmful responses has raised significant societal and regulatory concerns, especially when manipulated by adversarial techniques known as "jailbreak" attacks. Existing jailbreak methods typically involve appending carefully crafted prefixes or suffixes to malicious prompts in order to bypass the built-in safety mechanisms of these models.
>   In this work, we identify a new vulnerability in which excessive linguistic complexity can disrupt built-in safety mechanisms-without the need for any added prefixes or suffixes-allowing attackers to elicit harmful outputs directly. We refer to this phenomenon as Information Overload.
>   To automatically exploit this vulnerability, we propose InfoFlood, a jailbreak attack that transforms malicious queries into complex, information-overloaded queries capable of bypassing built-in safety mechanisms. Specifically, InfoFlood: (1) uses linguistic transformations to rephrase malicious queries, (2) identifies the root cause of failure when an attempt is unsuccessful, and (3) refines the prompt's linguistic structure to address the failure while preserving its malicious intent.
>   We empirically validate the effectiveness of InfoFlood on four widely used LLMs-GPT-4o, GPT-3.5-turbo, Gemini 2.0, and LLaMA 3.1-by measuring their jailbreak success rates. InfoFlood consistently outperforms baseline attacks, achieving up to 3 times higher success rates across multiple jailbreak benchmarks. Furthermore, we demonstrate that commonly adopted post-processing defenses, including OpenAI's Moderation API, Perspective API, and SmoothLLM, fail to mitigate these attacks. This highlights a critical weakness in traditional AI safety guardrails when confronted with information overload-based jailbreaks.

