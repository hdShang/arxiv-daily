---
layout: default
title: "Privacy-Aware Decoding: Mitigating Privacy Leakage of Large Language Models in Retrieval-Augmented Generation"
---

# Privacy-Aware Decoding: Mitigating Privacy Leakage of Large Language Models in Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03098" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03098v1</a>
  <a href="https://arxiv.org/pdf/2508.03098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03098v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03098v1', 'Privacy-Aware Decoding: Mitigating Privacy Leakage of Large Language Models in Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Wang, Xiongxiao Xu, Baixiang Huang, Kai Shu

**分类**: cs.CL

**发布日期**: 2025-08-05

**🔗 代码/项目**: [GITHUB](https://github.com/wang2226/PAD)

---

## 💡 一句话要点

**提出隐私感知解码以解决大语言模型隐私泄露问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私保护` `大语言模型` `检索增强生成` `差分隐私` `高斯噪声` `信息安全` `机器学习`

## 📋 核心要点

1. 现有的检索增强生成方法在处理私密数据时容易遭受提取攻击，导致敏感信息泄露。
2. 本文提出隐私感知解码（PAD），通过在生成过程中注入高斯噪声来保护高风险token，增强隐私保护。
3. 实验结果显示，PAD在三个真实数据集上显著降低了隐私泄露，同时保持了生成响应的质量，超越了现有防御方法。

## 📝 摘要（中文）

检索增强生成（RAG）通过外部知识源提高大语言模型（LLMs）的事实准确性。然而，当检索涉及私密或敏感数据时，RAG系统容易受到提取攻击，导致机密信息泄露。本文提出隐私感知解码（PAD），这是一种轻量级的推理时防御方法，通过在生成过程中自适应地向token logits注入经过校准的高斯噪声。PAD结合基于置信度的筛选、有效的敏感性估计和上下文感知的噪声校准，以平衡隐私与生成质量。通过enyi差分隐私（RDP）会计，严格跟踪累积隐私损失，为敏感输出提供明确的每响应$(	ext{ε}, 	ext{δ})$-DP保证。与需要重新训练或语料库级过滤的先前方法不同，PAD是模型无关的，完全在解码时操作，且计算开销最小。实验表明，PAD显著减少了私密信息泄露，同时保持响应的实用性，优于现有的检索和后处理防御方法。

## 🔬 方法详解

**问题定义**：本文旨在解决检索增强生成（RAG）系统在处理私密数据时的隐私泄露问题。现有方法在面对提取攻击时，无法有效保护生成的响应，导致机密信息的泄露。

**核心思路**：提出隐私感知解码（PAD），通过在生成过程中自适应地向token logits注入高斯噪声，结合置信度筛选和敏感性估计，选择性地保护高风险token，从而增强隐私保护。

**技术框架**：PAD的整体架构包括三个主要模块：1) 置信度筛选，识别高风险token；2) 敏感性估计，评估噪声注入的必要性；3) 噪声校准，确保生成质量与隐私保护之间的平衡。

**关键创新**：PAD的主要创新在于其模型无关性和推理时操作的能力，避免了传统方法需要重新训练或进行语料库级过滤的缺陷。通过RDP会计，PAD能够提供明确的隐私保证。

**关键设计**：在设计中，PAD使用了基于置信度的筛选机制，动态调整噪声注入的强度，并通过上下文信息进行噪声的校准，确保生成的响应既保护隐私又保持实用性。具体的参数设置和损失函数设计在实验中进行了优化。

## 📊 实验亮点

实验结果表明，PAD在三个真实数据集上显著降低了私密信息泄露，具体性能提升超过了现有的检索和后处理防御方法，展示了其在隐私保护方面的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融和社交媒体等敏感数据处理场景。通过有效保护用户隐私，PAD为大语言模型在实际应用中的安全性提供了保障，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) enhances the factual accuracy of large language models (LLMs) by conditioning outputs on external knowledge sources. However, when retrieval involves private or sensitive data, RAG systems are susceptible to extraction attacks that can leak confidential information through generated responses. We propose Privacy-Aware Decoding (PAD), a lightweight, inference-time defense that adaptively injects calibrated Gaussian noise into token logits during generation. PAD integrates confidence-based screening to selectively protect high-risk tokens, efficient sensitivity estimation to minimize unnecessary noise, and context-aware noise calibration to balance privacy with generation quality. A \renyi Differential Privacy (RDP) accountant rigorously tracks cumulative privacy loss, enabling explicit per-response $(\varepsilon, δ)$-DP guarantees for sensitive outputs. Unlike prior approaches requiring retraining or corpus-level filtering, PAD is model-agnostic and operates entirely at decoding time with minimal computational overhead. Experiments on three real-world datasets demonstrate that PAD substantially reduces private information leakage while preserving response utility, outperforming existing retrieval- and post-processing-based defenses. Our work takes an important step toward mitigating privacy risks in RAG via decoding strategies, paving the way for universal and scalable privacy solutions in sensitive domains. Our code is available: https://github.com/wang2226/PAD.

