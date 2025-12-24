---
layout: default
title: "Simple Yet Effective: Extracting Private Data Across Clients in Federated Fine-Tuning of Large Language Models"
---

# Simple Yet Effective: Extracting Private Data Across Clients in Federated Fine-Tuning of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06060" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06060v1</a>
  <a href="https://arxiv.org/pdf/2506.06060.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06060v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06060v1', 'Simple Yet Effective: Extracting Private Data Across Clients in Federated Fine-Tuning of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingqi Hu, Zhuo Zhang, Jingyuan Zhang, Lizhen Qu, Zenglin Xu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06

**备注**: 10 pages, 4 figures

---

## 💡 一句话要点

**提出简单有效的提取攻击算法以解决联邦微调中的隐私数据风险**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `隐私保护` `数据提取` `大型语言模型` `个人可识别信息` `安全性评估` `攻击模型`

## 📋 核心要点

1. 现有的联邦学习方法在保护数据隐私的同时，面临着大型语言模型的记忆能力带来的训练数据提取攻击风险。
2. 本文提出了一种新的提取攻击算法，攻击者仅需访问单个客户端的数据，通过上下文前缀进行跨客户端的个人可识别信息提取。
3. 实验结果显示，提出的方法能够提取高达56.57%的受害者专属PII，且在多个类别中表现出显著的脆弱性。

## 📝 摘要（中文）

联邦微调大型语言模型（FedLLMs）是一种在敏感领域实现强大模型性能的有前景的方法，同时保护数据隐私。然而，LLMs固有的记忆能力使其容易受到训练数据提取攻击。为此，本文提出了专门针对FedLLMs的简单有效的提取攻击算法，与以往假设访问所有训练数据片段的“逐字”提取攻击不同，我们的方法在更现实的威胁模型下运作，攻击者仅访问单个客户端的数据，旨在提取其他客户端的未见个人可识别信息（PII）。我们提出了两个严格的评估指标，并扩展了一个与CPIS、GDPR和CCPA标准对齐的真实法律数据集，获得了89.9%的人工验证精度。实验结果表明，我们的方法可以提取高达56.57%的受害者专属PII，其中“地址”、“生日”和“姓名”是最脆弱的类别。我们的研究强调了强大防御策略的迫切需求，并为未来隐私保护联邦学习的研究贡献了新的基准和评估框架。

## 🔬 方法详解

**问题定义**：本文旨在解决联邦微调大型语言模型中存在的隐私数据提取风险。现有方法通常假设攻击者可以访问所有训练数据片段，未能考虑更现实的攻击场景。

**核心思路**：我们提出的攻击算法允许攻击者仅访问单个客户端的数据，通过利用上下文前缀来提取其他客户端的未见PII。这种方法更贴近实际攻击情况，具有较高的实用性。

**技术框架**：整体架构包括数据收集、上下文前缀生成、PII提取和评估四个主要模块。首先，攻击者收集目标客户端的数据，然后生成上下文前缀，接着进行PII提取，最后通过评估指标验证提取效果。

**关键创新**：本文的主要创新在于提出了一种新的攻击模型，允许在仅访问单个客户端数据的情况下进行有效的PII提取。这与传统的“逐字”提取方法形成鲜明对比，具有更高的现实意义。

**关键设计**：在算法设计中，我们设置了两个评估指标：覆盖率和效率，并使用了与法律标准对齐的真实数据集进行验证。实验中，采用了精确度为89.9%的PII注释，确保了结果的可靠性。

## 📊 实验亮点

实验结果表明，提出的方法能够提取高达56.57%的受害者专属PII，尤其在“地址”、“生日”和“姓名”类别中表现出显著的脆弱性。这一发现强调了在联邦学习中加强隐私保护的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融和社交网络等敏感数据处理场景。通过提高对隐私数据提取风险的认识，研究成果可为设计更安全的联邦学习系统提供理论支持，推动隐私保护技术的发展。

## 📄 摘要（原文）

> Federated fine-tuning of large language models (FedLLMs) presents a promising approach for achieving strong model performance while preserving data privacy in sensitive domains. However, the inherent memorization ability of LLMs makes them vulnerable to training data extraction attacks. To investigate this risk, we introduce simple yet effective extraction attack algorithms specifically designed for FedLLMs. In contrast to prior "verbatim" extraction attacks, which assume access to fragments from all training data, our approach operates under a more realistic threat model, where the attacker only has access to a single client's data and aims to extract previously unseen personally identifiable information (PII) from other clients. This requires leveraging contextual prefixes held by the attacker to generalize across clients. To evaluate the effectiveness of our approaches, we propose two rigorous metrics-coverage rate and efficiency-and extend a real-world legal dataset with PII annotations aligned with CPIS, GDPR, and CCPA standards, achieving 89.9% human-verified precision. Experimental results show that our method can extract up to 56.57% of victim-exclusive PII, with "Address," "Birthday," and "Name" being the most vulnerable categories. Our findings underscore the pressing need for robust defense strategies and contribute a new benchmark and evaluation framework for future research in privacy-preserving federated learning.

