---
layout: default
title: From Essence to Defense: Adaptive Semantic-aware Watermarking for Embedding-as-a-Service Copyright Protection
---

# From Essence to Defense: Adaptive Semantic-aware Watermarking for Embedding-as-a-Service Copyright Protection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16439" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16439v1</a>
  <a href="https://arxiv.org/pdf/2512.16439.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16439v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16439v1', 'From Essence to Defense: Adaptive Semantic-aware Watermarking for Embedding-as-a-Service Copyright Protection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Li, Yubing Ren, Yanan Cao, Yingjie Li, Fang Fang, Xuebin Wang

**分类**: cs.CR, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出SemMark以解决EaaS版权保护中的水印隐蔽性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `嵌入即服务` `版权保护` `水印技术` `自然语言处理` `语义感知`

## 📋 核心要点

1. 现有EaaS保护方法在水印设计上忽视了嵌入的语义特性，导致其隐蔽性和无害性不足。
2. 本文提出SemMark，通过局部敏感哈希技术在语义空间中注入水印，确保水印信号隐形且多样。
3. 在四个流行的NLP数据集上进行的实验表明，SemMark在可验证性和隐蔽性等方面显著优于现有方法。

## 📝 摘要（中文）

随着大型语言模型在自然语言理解和生成方面的优越能力，嵌入即服务（EaaS）已成为一种成功的商业模式。然而，现有研究表明EaaS易受模仿攻击。虽然已有方法通过水印技术保护EaaS的知识产权，但忽视了嵌入的语义特性，导致隐蔽性和无害性有限。为此，本文提出了SemMark，一种基于语义的水印范式，利用局部敏感哈希将语义空间划分，并在特定区域注入语义感知水印，确保水印信号隐形且多样。此外，基于局部离群因子的自适应水印权重机制被引入，以保持原始嵌入分布。通过构建四种场景进行评估，SemMark在可验证性、多样性、隐蔽性和无害性方面表现优越。

## 🔬 方法详解

**问题定义**：本文旨在解决EaaS在版权保护中面临的模仿攻击问题，现有水印方法未能充分考虑嵌入的语义特性，导致水印的隐蔽性和无害性不足。

**核心思路**：SemMark的核心思路是利用局部敏感哈希技术将语义空间划分，并在特定区域注入语义感知水印，从而确保水印信号的隐形和多样性，同时引入自适应水印权重机制以保持原始嵌入分布。

**技术框架**：SemMark的整体架构包括语义空间的划分、语义水印的注入、以及自适应水印权重的调整。主要模块包括局部敏感哈希、语义水印生成和水印检测。

**关键创新**：SemMark的主要创新在于其语义感知水印设计和自适应水印权重机制，这与现有方法的设计思路有本质区别，能够更好地保护EaaS的知识产权。

**关键设计**：在设计中，采用局部离群因子来动态调整水印权重，确保水印的多样性和隐蔽性，同时保持原始嵌入的分布特性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16439v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16439v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16439v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，SemMark在可验证性、多样性、隐蔽性和无害性方面均优于现有水印方法，具体表现为在四个NLP数据集上实现了显著的性能提升，验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、知识产权保护和内容创作等。通过提供一种有效的水印保护机制，SemMark能够帮助企业保护其EaaS产品的知识产权，防止模仿和盗用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Benefiting from the superior capabilities of large language models in natural language understanding and generation, Embeddings-as-a-Service (EaaS) has emerged as a successful commercial paradigm on the web platform. However, prior studies have revealed that EaaS is vulnerable to imitation attacks. Existing methods protect the intellectual property of EaaS through watermarking techniques, but they all ignore the most important properties of embedding: semantics, resulting in limited harmlessness and stealthiness. To this end, we propose SemMark, a novel semantic-based watermarking paradigm for EaaS copyright protection. SemMark employs locality-sensitive hashing to partition the semantic space and inject semantic-aware watermarks into specific regions, ensuring that the watermark signals remain imperceptible and diverse. In addition, we introduce the adaptive watermark weight mechanism based on the local outlier factor to preserve the original embedding distribution. Furthermore, we propose Detect-Sampling and Dimensionality-Reduction attacks and construct four scenarios to evaluate the watermarking method. Extensive experiments are conducted on four popular NLP datasets, and SemMark achieves superior verifiability, diversity, stealthiness, and harmlessness.

