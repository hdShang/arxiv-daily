---
layout: default
title: "From Essence to Defense: Adaptive Semantic-aware Watermarking for Embedding-as-a-Service Copyright Protection"
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

**提出SemMark：一种自适应语义感知水印方法，用于保护Embedding-as-a-Service的版权**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Embedding-as-a-Service` `版权保护` `语义水印` `局部敏感哈希` `自适应权重` `模仿攻击` `自然语言处理`

## 📋 核心要点

1. 现有EaaS水印方法忽略了嵌入的语义信息，导致水印的隐蔽性和对原始嵌入的影响控制不足。
2. SemMark通过局部敏感哈希划分语义空间，并注入语义感知水印，保证水印的不可感知性和多样性。
3. 实验证明，SemMark在可验证性、多样性、隐蔽性和无害性方面优于现有方法，有效抵抗新型攻击。

## 📝 摘要（中文）

Embedding-as-a-Service (EaaS) 凭借大型语言模型在自然语言理解和生成方面的卓越能力，已成为一种成功的商业模式。然而，先前的研究表明EaaS容易受到模仿攻击。现有的水印技术试图保护EaaS的知识产权，但它们都忽略了嵌入最重要的属性：语义，导致其无害性和隐蔽性有限。为此，我们提出SemMark，一种新颖的基于语义的水印范式，用于EaaS版权保护。SemMark采用局部敏感哈希来划分语义空间，并将语义感知水印注入到特定区域，确保水印信号保持难以察觉和多样化。此外，我们引入了基于局部离群因子（LOF）的自适应水印权重机制，以保留原始嵌入分布。我们还提出了Detect-Sampling和Dimensionality-Reduction攻击，并构建了四种场景来评估水印方法。在四个流行的NLP数据集上进行了大量实验，SemMark实现了卓越的可验证性、多样性、隐蔽性和无害性。

## 🔬 方法详解

**问题定义**：论文旨在解决Embedding-as-a-Service (EaaS) 的版权保护问题。现有的水印方法主要痛点在于忽略了嵌入的语义信息，导致水印的隐蔽性不足，容易被检测和移除，并且可能对原始嵌入的语义造成较大干扰，影响下游任务的性能。

**核心思路**：SemMark的核心思路是利用嵌入的语义信息，将水印嵌入到特定的语义区域，并根据语义区域的特性自适应地调整水印的强度。通过这种方式，可以提高水印的隐蔽性和鲁棒性，同时减少对原始嵌入语义的干扰。

**技术框架**：SemMark主要包含以下几个模块：1) 语义空间划分：使用局部敏感哈希（LSH）将嵌入空间划分为多个语义区域。2) 水印注入：在特定的语义区域注入语义感知水印。水印的强度由基于局部离群因子（LOF）的自适应权重机制控制。3) 水印检测：通过检测特定语义区域的水印信号来验证版权。

**关键创新**：SemMark的关键创新在于：1) 提出了语义感知水印的概念，将水印嵌入到特定的语义区域，提高了水印的隐蔽性和鲁棒性。2) 引入了基于局部离群因子（LOF）的自适应权重机制，可以根据语义区域的特性自适应地调整水印的强度，减少对原始嵌入语义的干扰。

**关键设计**：在语义空间划分阶段，LSH的参数（如哈希函数的数量和哈希桶的大小）需要根据数据集的特性进行调整。在水印注入阶段，水印的强度由基于LOF的自适应权重机制控制，LOF的计算需要选择合适的邻域大小。此外，论文还提出了Detect-Sampling和Dimensionality-Reduction两种新型攻击方法，并针对这些攻击方法设计了相应的防御策略。

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

实验结果表明，SemMark在四个流行的NLP数据集上实现了卓越的性能。与现有方法相比，SemMark在可验证性、多样性、隐蔽性和无害性方面均有显著提升。例如，在抵抗Detect-Sampling和Dimensionality-Reduction攻击方面，SemMark表现出更强的鲁棒性，能够有效地保护EaaS的版权。

## 🎯 应用场景

SemMark可应用于各种基于Embedding-as-a-Service的场景，例如文本分类、情感分析、机器翻译等。它可以有效地保护EaaS提供商的知识产权，防止未经授权的复制和使用。该研究成果有助于构建更安全、更可靠的EaaS生态系统，促进人工智能技术的健康发展。

## 📄 摘要（原文）

> Benefiting from the superior capabilities of large language models in natural language understanding and generation, Embeddings-as-a-Service (EaaS) has emerged as a successful commercial paradigm on the web platform. However, prior studies have revealed that EaaS is vulnerable to imitation attacks. Existing methods protect the intellectual property of EaaS through watermarking techniques, but they all ignore the most important properties of embedding: semantics, resulting in limited harmlessness and stealthiness. To this end, we propose SemMark, a novel semantic-based watermarking paradigm for EaaS copyright protection. SemMark employs locality-sensitive hashing to partition the semantic space and inject semantic-aware watermarks into specific regions, ensuring that the watermark signals remain imperceptible and diverse. In addition, we introduce the adaptive watermark weight mechanism based on the local outlier factor to preserve the original embedding distribution. Furthermore, we propose Detect-Sampling and Dimensionality-Reduction attacks and construct four scenarios to evaluate the watermarking method. Extensive experiments are conducted on four popular NLP datasets, and SemMark achieves superior verifiability, diversity, stealthiness, and harmlessness.

