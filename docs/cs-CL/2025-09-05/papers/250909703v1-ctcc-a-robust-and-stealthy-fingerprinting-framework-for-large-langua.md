---
layout: default
title: "CTCC: A Robust and Stealthy Fingerprinting Framework for Large Language Models via Cross-Turn Contextual Correlation Backdoor"
---

# CTCC: A Robust and Stealthy Fingerprinting Framework for Large Language Models via Cross-Turn Contextual Correlation Backdoor

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09703" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09703v1</a>
  <a href="https://arxiv.org/pdf/2509.09703.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09703v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09703v1', 'CTCC: A Robust and Stealthy Fingerprinting Framework for Large Language Models via Cross-Turn Contextual Correlation Backdoor')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenhua Xu, Xixiang Zhao, Xubin Yue, Shengwei Tian, Changting Lin, Meng Han

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-05

**备注**: Accepted by EMNLP2025 MainConference

**🔗 代码/项目**: [GITHUB](https://github.com/Xuzhenhua55/CTCC)

---

## 💡 一句话要点

**提出CTCC框架，通过跨轮上下文关联后门实现大语言模型鲁棒且隐蔽的指纹识别**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `指纹识别` `知识产权保护` `上下文关联` `后门攻击`

## 📋 核心要点

1. 现有LLM指纹识别方法在隐蔽性、鲁棒性和泛化性之间存在权衡，容易被检测或攻击，且指纹泄露后失效。
2. CTCC框架通过编码跨多轮对话的上下文关联，而非单轮触发，实现隐蔽且鲁棒的指纹嵌入。
3. 实验表明，CTCC在多个LLM架构上实现了比现有方法更强的隐蔽性和鲁棒性，适用于实际部署场景。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的广泛部署，模型盗用和未经授权的再分发变得越来越可行，知识产权（IP）保护问题日益突出。为了解决这个问题，模型指纹识别旨在将可验证的所有权追踪嵌入到LLM中。然而，现有的方法在隐蔽性、鲁棒性和泛化性之间存在固有的权衡，要么可以通过分布偏移检测到，要么容易受到对抗性修改的影响，或者一旦指纹泄露就很容易失效。本文介绍了一种新颖的规则驱动的指纹识别框架CTCC，该框架编码跨多个对话轮次的上下文关联（例如，反事实），而不是依赖于token级别的或单轮触发器。CTCC支持黑盒访问下的指纹验证，同时减轻了误报和指纹泄露，即使部分触发器暴露，也支持在共享语义规则下进行连续构建。在多个LLM架构上的大量实验表明，CTCC始终比以前的工作实现更强的隐蔽性和鲁棒性。我们的发现使CTCC成为现实世界LLM部署场景中所有权验证的可靠且实用的解决方案。我们的代码和数据可在<https://github.com/Xuzhenhua55/CTCC>公开获得。

## 🔬 方法详解

**问题定义**：现有LLM指纹识别方法容易被检测（隐蔽性不足），容易受到对抗攻击（鲁棒性不足），且一旦指纹泄露，整个指纹识别方案就会失效。因此，需要一种更隐蔽、更鲁棒、且能抵抗指纹泄露的LLM指纹识别方案。

**核心思路**：CTCC的核心思路是利用跨轮对话的上下文关联性来嵌入指纹。不同于以往依赖于token级别或单轮触发的方法，CTCC通过预定义的语义规则，在多轮对话中建立特定的上下文关联，从而实现指纹的嵌入和验证。这种方式使得指纹更难被检测和篡改，并且即使部分触发条件泄露，仍然可以通过其他关联条件进行验证。

**技术框架**：CTCC框架主要包含三个阶段：指纹生成阶段、指纹嵌入阶段和指纹验证阶段。在指纹生成阶段，根据预定义的语义规则生成一系列跨轮对话的触发条件。在指纹嵌入阶段，将这些触发条件注入到LLM的训练数据中，或者通过对抗训练等方式，使LLM在特定上下文下产生预期的响应。在指纹验证阶段，通过向LLM输入特定的对话序列，观察其输出是否符合预定义的语义规则，从而判断LLM是否包含该指纹。

**关键创新**：CTCC最重要的创新在于其利用跨轮上下文关联进行指纹嵌入。这种方法避免了对单个token或单轮对话的依赖，使得指纹更加隐蔽和鲁棒。此外，CTCC的规则驱动特性使得即使部分触发条件泄露，仍然可以通过其他关联条件进行验证，从而提高了指纹识别的安全性。

**关键设计**：CTCC的关键设计包括：1) 语义规则的设计，需要保证规则的合理性和可验证性，避免引入过多的噪声；2) 触发条件的选择，需要选择对LLM的输出影响较小的触发条件，以保证隐蔽性；3) 指纹验证的阈值设置，需要根据实际情况调整阈值，以平衡误报率和漏报率。

## 📊 实验亮点

CTCC在多个LLM架构上进行了广泛的实验，结果表明CTCC在隐蔽性和鲁棒性方面均优于现有方法。具体来说，CTCC能够抵抗多种对抗攻击，并且即使部分触发条件泄露，仍然可以进行有效的指纹验证。实验结果表明，CTCC是一种可靠且实用的LLM指纹识别解决方案。

## 🎯 应用场景

CTCC可应用于保护大型语言模型的知识产权，防止模型盗用和未经授权的再分发。该技术可用于验证模型的来源和所有权，尤其是在商业部署和API服务中。此外，CTCC还可以用于检测恶意模型，例如被植入后门的模型，从而提高LLM的安全性。

## 📄 摘要（原文）

> The widespread deployment of large language models (LLMs) has intensified concerns around intellectual property (IP) protection, as model theft and unauthorized redistribution become increasingly feasible. To address this, model fingerprinting aims to embed verifiable ownership traces into LLMs. However, existing methods face inherent trade-offs between stealthness, robustness, and generalizability, being either detectable via distributional shifts, vulnerable to adversarial modifications, or easily invalidated once the fingerprint is revealed. In this work, we introduce CTCC, a novel rule-driven fingerprinting framework that encodes contextual correlations across multiple dialogue turns, such as counterfactual, rather than relying on token-level or single-turn triggers. CTCC enables fingerprint verification under black-box access while mitigating false positives and fingerprint leakage, supporting continuous construction under a shared semantic rule even if partial triggers are exposed. Extensive experiments across multiple LLM architectures demonstrate that CTCC consistently achieves stronger stealth and robustness than prior work. Our findings position CTCC as a reliable and practical solution for ownership verification in real-world LLM deployment scenarios. Our code and data are publicly available at <https://github.com/Xuzhenhua55/CTCC>.

