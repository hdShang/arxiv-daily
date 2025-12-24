---
layout: default
title: "Decoding Latent Attack Surfaces in LLMs: Prompt Injection via HTML in Web Summarization"
---

# Decoding Latent Attack Surfaces in LLMs: Prompt Injection via HTML in Web Summarization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05831" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05831v3</a>
  <a href="https://arxiv.org/pdf/2509.05831.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05831v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05831v3', 'Decoding Latent Attack Surfaces in LLMs: Prompt Injection via HTML in Web Summarization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ishaan Verma, Arsheya Yadav

**分类**: cs.CR, cs.AI

**发布日期**: 2025-09-06 (更新: 2025-11-11)

---

## 💡 一句话要点

**揭示LLM在Web摘要中的潜在攻击面：通过HTML注入提示**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `提示注入` `大型语言模型` `Web摘要` `HTML攻击` `信息安全`

## 📋 核心要点

1. 现有LLM在Web内容摘要应用中易受提示注入攻击，攻击者可利用隐藏的HTML元素嵌入恶意指令。
2. 该研究提出一种基于HTML的提示注入方法，通过操纵<meta>等标签，在不改变可见内容的前提下影响LLM的摘要结果。
3. 实验表明，Llama 4 Scout和Gemma 9B IT模型均受到该攻击的影响，分别有29%和15%的注入样本导致摘要结果发生变化。

## 📝 摘要（中文）

大型语言模型（LLM）越来越多地被集成到基于Web的系统中用于内容摘要，但它们对提示注入攻击的敏感性仍然是一个紧迫的问题。本研究探讨了如何利用非可见HTML元素（如<meta>、aria-label和alt属性）来嵌入对抗性指令，而不改变网页的可见内容。我们引入了一个包含280个静态网页的新数据集，这些网页均匀地分为干净版本和对抗性注入版本，使用不同的基于HTML的策略制作。这些页面通过浏览器自动化流程进行处理，以提取原始HTML和渲染文本，从而紧密模拟实际的LLM部署场景。我们评估了两个最先进的开源模型Llama 4 Scout (Meta) 和 Gemma 9B IT (Google) 总结这些内容的能力。使用词汇（ROUGE-L）和语义（SBERT余弦相似度）指标，以及手动注释，我们评估了这些隐蔽注入的影响。我们的研究结果表明，超过29%的注入样本导致Llama 4 Scout摘要发生明显变化，而Gemma 9B IT的成功率较低，但仍达到15%。这些结果突出了LLM驱动的Web管道中一个关键且很大程度上被忽视的漏洞，即隐藏的对抗性内容可以巧妙地操纵模型输出。我们的工作提供了一个可重现的框架和基准，用于评估基于HTML的提示注入，并强调在涉及Web内容的LLM应用中迫切需要强大的缓解策略。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在Web内容摘要应用中，由于对HTML结构解析不当而导致的提示注入漏洞问题。现有方法难以检测和防御隐藏在HTML标签中的恶意指令，使得攻击者可以在不改变网页可见内容的情况下操纵LLM的输出。

**核心思路**：核心思路是利用HTML中非可见的元素（如<meta>标签、aria-label属性和alt属性）来嵌入对抗性指令。这些指令不会直接显示在网页上，但会被LLM解析并影响其摘要生成过程。通过构造包含这些恶意指令的网页，可以诱导LLM生成攻击者期望的输出。

**技术框架**：整体框架包含以下几个主要步骤：1) 构建包含干净网页和恶意注入网页的数据集；2) 使用浏览器自动化工具（如Selenium）提取网页的原始HTML和渲染后的文本；3) 将提取的内容输入到LLM（Llama 4 Scout和Gemma 9B IT）中进行摘要生成；4) 使用词汇（ROUGE-L）和语义（SBERT余弦相似度）指标以及人工评估来评估摘要的质量和攻击的成功率。

**关键创新**：关键创新在于发现了利用HTML非可见元素进行提示注入的攻击面。与传统的提示注入方法不同，该方法不需要修改网页的可见内容，因此更难被检测和防御。此外，该研究还构建了一个包含多种HTML注入策略的数据集，为评估LLM的安全性提供了一个基准。

**关键设计**：数据集包含280个静态网页，其中一半是干净的，另一半包含恶意注入。注入策略包括使用<meta>标签、aria-label属性和alt属性等。使用ROUGE-L和SBERT余弦相似度作为评估指标，并进行人工评估以验证结果。没有特别提及损失函数或网络结构，因为重点在于攻击方法而非模型训练。

## 📊 实验亮点

实验结果表明，Llama 4 Scout模型在29%的注入样本中受到影响，摘要结果发生明显变化。Gemma 9B IT模型的受影响比例为15%，虽然较低，但也表明该模型存在类似的漏洞。这些数据突出了LLM在处理Web内容时面临的潜在安全风险，并强调了开发有效防御机制的重要性。

## 🎯 应用场景

该研究成果可应用于提升LLM在Web内容处理中的安全性。通过识别和防御HTML注入攻击，可以防止LLM被恶意操纵，确保其在新闻摘要、信息检索、内容推荐等领域的可靠性和安全性。研究结果也为开发更鲁棒的LLM和Web应用提供了指导。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly integrated into web-based systems for content summarization, yet their susceptibility to prompt injection attacks remains a pressing concern. In this study, we explore how non-visible HTML elements such as <meta>, aria-label, and alt attributes can be exploited to embed adversarial instructions without altering the visible content of a webpage. We introduce a novel dataset comprising 280 static web pages, evenly divided between clean and adversarial injected versions, crafted using diverse HTML-based strategies. These pages are processed through a browser automation pipeline to extract both raw HTML and rendered text, closely mimicking real-world LLM deployment scenarios. We evaluate two state-of-the-art open-source models, Llama 4 Scout (Meta) and Gemma 9B IT (Google), on their ability to summarize this content. Using both lexical (ROUGE-L) and semantic (SBERT cosine similarity) metrics, along with manual annotations, we assess the impact of these covert injections. Our findings reveal that over 29% of injected samples led to noticeable changes in the Llama 4 Scout summaries, while Gemma 9B IT showed a lower, yet non-trivial, success rate of 15%. These results highlight a critical and largely overlooked vulnerability in LLM driven web pipelines, where hidden adversarial content can subtly manipulate model outputs. Our work offers a reproducible framework and benchmark for evaluating HTML-based prompt injection and underscores the urgent need for robust mitigation strategies in LLM applications involving web content.

