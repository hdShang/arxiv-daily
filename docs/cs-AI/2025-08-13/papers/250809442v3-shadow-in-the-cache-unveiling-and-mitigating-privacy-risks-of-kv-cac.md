---
layout: default
title: "Shadow in the Cache: Unveiling and Mitigating Privacy Risks of KV-cache in LLM Inference"
---

# Shadow in the Cache: Unveiling and Mitigating Privacy Risks of KV-cache in LLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09442" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09442v3</a>
  <a href="https://arxiv.org/pdf/2508.09442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09442v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09442v3', 'Shadow in the Cache: Unveiling and Mitigating Privacy Risks of KV-cache in LLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhifan Luo, Shuo Shao, Su Zhang, Lijing Zhou, Yuke Hu, Chenxu Zhao, Zhihao Liu, Zhan Qin

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-08-13 (更新: 2025-12-08)

**备注**: This paper is accepted by Network and Distributed System Security Symposium (NDSS) 2026

---

## 💡 一句话要点

**提出KV-Cloak以解决LLM推理中的KV缓存隐私风险问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私保护` `大型语言模型` `KV缓存` `攻击防御` `数据安全` `机器学习` `模型推理`

## 📋 核心要点

1. 现有的KV缓存机制在加速LLM推理的同时，存在严重的隐私泄露风险，攻击者可重构用户输入。
2. 本文提出KV-Cloak，通过可逆矩阵混淆和操作融合技术，提供了一种有效的KV缓存保护方案。
3. 实验结果显示，KV-Cloak能够有效抵御所有攻击，重构质量降至随机噪声，且对模型性能影响极小。

## 📝 摘要（中文）

关键值（KV）缓存是加速大型语言模型（LLM）推理的基础机制，但其效率优化引入了显著的隐私风险。本文首次全面分析了这些漏洞，表明攻击者可以直接从KV缓存中重构敏感用户输入。我们设计并实现了三种攻击方式：直接反演攻击、广泛适用的碰撞攻击和基于语义的注入攻击，展示了KV缓存隐私泄露问题的实用性和严重性。为此，我们提出了KV-Cloak，一种新颖、轻量且高效的防御机制，利用可逆矩阵混淆方案和操作融合来保护KV缓存。实验表明，KV-Cloak有效阻止所有提出的攻击，将重构质量降低到随机噪声，同时几乎不影响模型准确性和性能开销，为可信的LLM部署提供了实用解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决KV缓存中存在的隐私泄露问题，现有方法未能有效防止攻击者重构用户输入，导致用户敏感信息的泄露。

**核心思路**：提出KV-Cloak作为防御机制，通过可逆矩阵混淆技术和操作融合，增强KV缓存的安全性，确保用户隐私不被泄露。

**技术框架**：KV-Cloak的整体架构包括数据输入、KV缓存混淆、操作融合和输出阶段，确保在推理过程中对缓存数据进行有效保护。

**关键创新**：最重要的创新在于引入了可逆矩阵混淆方案，与传统方法相比，KV-Cloak在保护隐私的同时，几乎不影响模型的推理准确性和性能。

**关键设计**：在设计中，采用了特定的混淆参数设置和损失函数，以确保混淆过程的可逆性和有效性，同时优化了操作融合的实现，以降低性能开销。

## 📊 实验亮点

实验结果表明，KV-Cloak能够有效阻止所有三种攻击方式，重构质量降低至随机噪声，且在模型准确性方面几乎没有下降，性能开销也保持在最低水平，展示了其在实际应用中的可行性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能客服和任何依赖于大型语言模型的系统。通过有效保护用户隐私，KV-Cloak为可信赖的AI应用提供了保障，未来可能在数据隐私法规日益严格的背景下，成为行业标准。

## 📄 摘要（原文）

> The Key-Value (KV) cache, which stores intermediate attention computations (Key and Value pairs) to avoid redundant calculations, is a fundamental mechanism for accelerating Large Language Model (LLM) inference. However, this efficiency optimization introduces significant yet underexplored privacy risks. This paper provides the first comprehensive analysis of these vulnerabilities, demonstrating that an attacker can reconstruct sensitive user inputs directly from the KV-cache. We design and implement three distinct attack vectors: a direct Inversion Attack, a more broadly applicable and potent Collision Attack, and a semantic-based Injection Attack. These methods demonstrate the practicality and severity of KV-cache privacy leakage issues. To mitigate this, we propose KV-Cloak, a novel, lightweight, and efficient defense mechanism. KV-Cloak uses a reversible matrix-based obfuscation scheme, combined with operator fusion, to secure the KV-cache. Our extensive experiments show that KV-Cloak effectively thwarts all proposed attacks, reducing reconstruction quality to random noise. Crucially, it achieves this robust security with virtually no degradation in model accuracy and minimal performance overhead, offering a practical solution for trustworthy LLM deployment.

