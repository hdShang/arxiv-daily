---
layout: default
title: "GuardNet: Graph-Attention Filtering for Jailbreak Defense in Large Language Models"
---

# GuardNet: Graph-Attention Filtering for Jailbreak Defense in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23037" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23037v1</a>
  <a href="https://arxiv.org/pdf/2509.23037.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23037v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23037v1', 'GuardNet: Graph-Attention Filtering for Jailbreak Defense in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Javad Forough, Mohammad Maheri, Hamed Haddadi

**分类**: cs.LG

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出GuardNet，通过图注意力过滤防御大型语言模型的越狱攻击**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `越狱攻击防御` `图神经网络` `图注意力网络` `对抗性提示` `分层过滤` `自然语言处理`

## 📋 核心要点

1. 现有防御方法难以有效识别和过滤针对大型语言模型的越狱攻击，导致模型输出不安全或有害内容。
2. GuardNet构建结合语言结构和上下文模式的图结构，利用图神经网络进行分层过滤，从而检测和定位对抗性提示。
3. 实验结果表明，GuardNet在多个数据集和攻击场景下显著优于现有防御方法，并在F1和IoU指标上取得了显著提升。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越容易受到越狱攻击的影响，这些攻击通过对抗性提示绕过对齐约束，诱导未经授权或有害的行为。这些漏洞破坏了LLM输出的安全性、可靠性和可信度，在医疗保健、金融和法律合规等领域构成严重风险。本文提出了GuardNet，一个分层过滤框架，用于在推理之前检测和过滤越狱提示。GuardNet构建结构化图，结合序列链接、句法依赖和注意力导出的token关系，以捕获语言结构和指示越狱行为的上下文模式。然后，它在两个层级应用图神经网络：（i）检测全局对抗性提示的提示级别过滤器，以及（ii）精确定位细粒度对抗性跨度的token级别过滤器。在三个数据集和多个攻击设置下进行的大量实验表明，GuardNet显著优于先前的防御方法。在LLM-Fuzzer上，它将提示级别的F$_1$分数从66.4％提高到99.8％，在PLeak数据集上，从67-79％提高到94％以上。在token级别，GuardNet将F$_1$从48-75％提高到74-91％，IoU增益高达+28％。尽管其结构复杂，但GuardNet保持了可接受的延迟，并在跨域评估中表现出良好的泛化能力，使其成为在实际LLM部署中防御越狱威胁的实用且强大的防御方法。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）的越狱攻击问题。现有的防御方法通常无法有效识别和过滤对抗性提示，导致LLMs产生不安全、不期望或有害的输出。这些方法在捕捉复杂语言结构和上下文信息方面存在不足，难以应对各种类型的越狱攻击。

**核心思路**：GuardNet的核心思路是利用图神经网络（GNNs）对提示进行结构化分析，从而更有效地检测和过滤越狱攻击。通过构建包含序列链接、句法依赖和注意力关系的图结构，GuardNet能够同时捕捉提示的语言结构和上下文模式，从而更准确地识别对抗性提示。

**技术框架**：GuardNet采用分层过滤框架，包含以下主要模块：1) **图构建模块**：将输入提示转换为结构化图，节点表示token，边表示token之间的关系（序列关系、句法依赖关系、注意力关系）。2) **提示级别过滤器**：使用图神经网络对整个提示图进行分类，判断是否存在越狱攻击。3) **Token级别过滤器**：使用图神经网络对提示图中的每个token进行分类，识别对抗性token的范围。这两个过滤器协同工作，实现对越狱攻击的全面防御。

**关键创新**：GuardNet的关键创新在于其图结构的构建方式和分层过滤框架。通过结合多种类型的token关系，GuardNet能够更全面地捕捉提示的语言结构和上下文信息。分层过滤框架允许GuardNet在全局和局部两个层面检测和定位对抗性提示，从而提高防御的准确性和鲁棒性。

**关键设计**：GuardNet使用图注意力网络（GAT）作为其图神经网络的核心组件。GAT允许节点根据其邻居的重要性动态调整权重，从而更好地捕捉token之间的关系。此外，GuardNet还采用了交叉熵损失函数来训练两个过滤器，并使用Adam优化器进行优化。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

GuardNet在三个数据集和多个攻击设置下进行了广泛的实验，结果表明其性能显著优于现有的防御方法。在LLM-Fuzzer数据集上，GuardNet将提示级别的F1分数从66.4％提高到99.8％，在PLeak数据集上，从67-79％提高到94％以上。在token级别，GuardNet将F1分数从48-75％提高到74-91％，IoU增益高达+28％。这些结果表明GuardNet是一种实用且强大的防御方法。

## 🎯 应用场景

GuardNet可应用于各种需要安全可靠的大型语言模型部署场景，例如：医疗诊断、金融风控、法律咨询等。通过有效防御越狱攻击，GuardNet能够提高LLM的安全性、可靠性和可信度，降低因模型输出不当而造成的风险。该研究成果有助于推动LLM在敏感领域的广泛应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly susceptible to jailbreak attacks, which are adversarial prompts that bypass alignment constraints and induce unauthorized or harmful behaviors. These vulnerabilities undermine the safety, reliability, and trustworthiness of LLM outputs, posing critical risks in domains such as healthcare, finance, and legal compliance. In this paper, we propose GuardNet, a hierarchical filtering framework that detects and filters jailbreak prompts prior to inference. GuardNet constructs structured graphs that combine sequential links, syntactic dependencies, and attention-derived token relations to capture both linguistic structure and contextual patterns indicative of jailbreak behavior. It then applies graph neural networks at two levels: (i) a prompt-level filter that detects global adversarial prompts, and (ii) a token-level filter that pinpoints fine-grained adversarial spans. Extensive experiments across three datasets and multiple attack settings show that GuardNet substantially outperforms prior defenses. It raises prompt-level F$_1$ scores from 66.4\% to 99.8\% on LLM-Fuzzer, and from 67-79\% to over 94\% on PLeak datasets. At the token level, GuardNet improves F$_1$ from 48-75\% to 74-91\%, with IoU gains up to +28\%. Despite its structural complexity, GuardNet maintains acceptable latency and generalizes well in cross-domain evaluations, making it a practical and robust defense against jailbreak threats in real-world LLM deployments.

