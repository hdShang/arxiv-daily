---
layout: default
title: "VeriLoRA: Fine-Tuning Large Language Models with Verifiable Security via Zero-Knowledge Proofs"
---

# VeriLoRA: Fine-Tuning Large Language Models with Verifiable Security via Zero-Knowledge Proofs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21393" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21393v3</a>
  <a href="https://arxiv.org/pdf/2508.21393.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21393v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21393v3', 'VeriLoRA: Fine-Tuning Large Language Models with Verifiable Security via Zero-Knowledge Proofs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guofu Liao, Taotao Wang, Shengli Zhang, Jiqun Zhang, Shi Long, Dacheng Tao

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-29 (更新: 2025-12-02)

**备注**: This paper has been accepted for publication at the Network and Distributed System Security Symposium (NDSS) 2026

---

## 💡 一句话要点

**提出VeriLoRA以解决大语言模型安全性与可验证性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `微调` `零知识证明` `安全性` `可验证性` `密码学技术` `低秩适应` `Transformer架构`

## 📋 核心要点

1. 现有的微调方法在计算资源和隐私保护方面存在不足，尤其是在不可信环境中。
2. VeriLoRA框架将LoRA微调与零知识证明结合，确保微调过程的安全性和可验证性。
3. 实验结果表明，VeriLoRA在开源LLMs上实现了高效的微调，支持大规模模型的安全部署。

## 📝 摘要（中文）

对大型语言模型（LLMs）进行微调对于适应特定任务至关重要，但在计算资源和隐私安全方面仍存在挑战。尽管低秩适应（LoRA）等参数高效方法显著降低了资源需求，但在零知识约束下确保微调的安全性和可验证性仍然是一个未解决的问题。为此，我们提出了VeriLoRA，这是第一个将LoRA微调与零知识证明（ZKPs）相结合的框架，实现了可证明的安全性和正确性。VeriLoRA利用先进的密码学技术，如查找论证、和检查协议和多项式承诺，来验证基于Transformer架构的算术和非算术操作。该框架为LoRA微调过程中的前向传播、反向传播和参数更新提供了端到端的可验证性，同时保护模型参数和训练数据的隐私。通过GPU实现，VeriLoRA在开源LLMs（如LLaMA）上的实验验证显示了其实用性和效率，支持高达130亿参数的模型。结合参数高效的微调与ZKPs，VeriLoRA填补了在敏感或不可信环境中安全可信部署LLMs的关键空白。

## 🔬 方法详解

**问题定义**：论文旨在解决在不可信环境中对大型语言模型进行微调时的安全性和可验证性问题。现有方法在隐私保护和计算资源需求上存在显著不足。

**核心思路**：VeriLoRA通过结合LoRA微调与零知识证明，确保微调过程的安全性和正确性，利用密码学技术实现可验证性。

**技术框架**：VeriLoRA的整体架构包括前向传播、反向传播和参数更新三个主要模块，采用零知识证明技术对每个模块进行验证。

**关键创新**：该框架的最大创新在于将LoRA微调与零知识证明相结合，提供了端到端的可验证性，解决了现有方法无法在不可信环境中安全微调的问题。

**关键设计**：在技术细节上，VeriLoRA使用查找论证、和检查协议和多项式承诺等密码学技术，确保算术和非算术操作的正确性，同时保护模型参数和训练数据的隐私。

## 📊 实验亮点

实验结果显示，VeriLoRA在开源LLMs（如LLaMA）上实现了高达130亿参数的微调，展现出良好的实用性和效率。与传统方法相比，VeriLoRA在安全性和可验证性方面提供了显著提升，确保了模型在敏感环境中的可靠性。

## 🎯 应用场景

VeriLoRA的研究成果在多个领域具有潜在应用价值，尤其是在需要保护敏感数据的场景，如医疗、金融和法律等行业。通过确保大型语言模型的安全性和可验证性，该框架能够促进这些模型在不可信环境中的可信部署，推动相关技术的广泛应用。

## 📄 摘要（原文）

> Fine-tuning large language models (LLMs) is crucial for adapting them to specific tasks, yet it remains computationally demanding and raises concerns about correctness and privacy, particularly in untrusted environments. Although parameter-efficient methods like Low-Rank Adaptation (LoRA) significantly reduce resource requirements, ensuring the security and verifiability of fine-tuning under zero-knowledge constraints remains an unresolved challenge. To address this, we introduce VeriLoRA, the first framework to integrate LoRA fine-tuning with zero-knowledge proofs (ZKPs), achieving provable security and correctness. VeriLoRA employs advanced cryptographic techniques -- such as lookup arguments, sumcheck protocols, and polynomial commitments -- to verify both arithmetic and non-arithmetic operations in Transformer-based architectures. The framework provides end-to-end verifiability for forward propagation, backward propagation, and parameter updates during LoRA fine-tuning, while safeguarding the privacy of model parameters and training data. Leveraging GPU-based implementations, VeriLoRA demonstrates practicality and efficiency through experimental validation on open-source LLMs like LLaMA, scaling up to 13 billion parameters. By combining parameter-efficient fine-tuning with ZKPs, VeriLoRA bridges a critical gap, enabling secure and trustworthy deployment of LLMs in sensitive or untrusted environments.

