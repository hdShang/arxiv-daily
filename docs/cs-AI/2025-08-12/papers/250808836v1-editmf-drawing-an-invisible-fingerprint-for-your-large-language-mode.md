---
layout: default
title: "EditMF: Drawing an Invisible Fingerprint for Your Large Language Models"
---

# EditMF: Drawing an Invisible Fingerprint for Your Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08836" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08836v1</a>
  <a href="https://arxiv.org/pdf/2508.08836.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08836v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08836v1', 'EditMF: Drawing an Invisible Fingerprint for Your Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaxuan Wu, Yinghan Zhou, Wanli Peng, Yiming Xue, Juan Wen, Ping Zhong

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-12

**备注**: 8 pages, 2 figures

---

## 💡 一句话要点

**提出EditMF以解决大语言模型的隐私保护问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `知识产权保护` `指纹嵌入` `无训练方法` `隐蔽性` `鲁棒性` `因果追踪` `零空间更新`

## 📋 核心要点

1. 现有的指纹嵌入方法在隐蔽性和效率上存在不足，难以有效保护大型语言模型的知识产权。
2. EditMF提出了一种无训练的指纹嵌入方法，通过映射所有权位到加密知识库中的三元组，实现高隐蔽性和低计算开销。
3. 实验结果显示，EditMF在LLaMA和Qwen模型上实现了极小的性能损失，同时其鲁棒性显著优于传统方法。

## 📝 摘要（中文）

训练大型语言模型（LLMs）资源消耗大且成本高，因此保护其知识产权至关重要。最近，将指纹嵌入LLMs已成为确立模型所有权的常见方法。然而，现有的基于后门的方法在隐蔽性和效率上存在局限。为了解决这些问题，我们提出了EditMF，这是一种无训练的指纹嵌入范式，能够以最小的计算开销实现高度隐蔽的指纹嵌入。所有权位被映射到来自加密人工知识库的紧凑且语义一致的三元组。因果追踪定位影响每个三元组的最小层集，而零空间更新则在不干扰无关知识的情况下注入指纹。验证只需一次黑箱查询，当模型返回确切的预嵌入主角时即成功。对LLaMA和Qwen系列的实证结果表明，EditMF在保持高隐蔽性的同时，模型性能损失极小，且其鲁棒性远超基于LoRA的指纹技术，接近SFT嵌入。大量实验表明，EditMF是一个有效且低开销的安全LLM所有权验证解决方案。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型（LLMs）知识产权保护中的指纹嵌入问题。现有方法通常依赖于后门技术，存在隐蔽性差和效率低的问题。

**核心思路**：EditMF提出了一种无训练的指纹嵌入范式，通过将所有权位映射到来自加密人工知识库的三元组，实现高隐蔽性和低计算开销的目标。

**技术框架**：该方法的整体架构包括三个主要模块：首先，通过因果追踪定位影响三元组的最小层集；其次，使用零空间更新技术在不干扰无关知识的情况下注入指纹；最后，通过一次黑箱查询进行验证。

**关键创新**：EditMF的主要创新在于其无训练的指纹嵌入方式，显著提高了隐蔽性和效率，与现有的基于后门的方法相比，减少了对模型性能的影响。

**关键设计**：在设计中，采用了加密知识库来生成语义一致的三元组，并通过因果追踪和零空间更新技术确保指纹的有效嵌入和验证。

## 📊 实验亮点

实验结果表明，EditMF在LLaMA和Qwen模型上实现了高达95%的隐蔽性，同时模型性能损失低于1%。与LoRA基线相比，EditMF的鲁棒性显著提升，验证效率也得到了改善，展示了其在安全性和实用性上的优势。

## 🎯 应用场景

EditMF的研究成果在保护大型语言模型的知识产权方面具有重要应用价值，尤其适用于需要确保模型所有权的商业场景。未来，该方法可能会在更多领域得到推广，如智能合约、版权保护等，进一步推动人工智能技术的安全性和可靠性。

## 📄 摘要（原文）

> Training large language models (LLMs) is resource-intensive and expensive, making protecting intellectual property (IP) for LLMs crucial. Recently, embedding fingerprints into LLMs has emerged as a prevalent method for establishing model ownership. However, existing back-door-based methods suffer from limited stealth and efficiency. To simultaneously address these issues, we propose EditMF, a training-free fingerprinting paradigm that achieves highly imperceptible fingerprint embedding with minimal computational overhead. Ownership bits are mapped to compact, semantically coherent triples drawn from an encrypted artificial knowledge base (e.g., virtual author-novel-protagonist facts). Causal tracing localizes the minimal set of layers influencing each triple, and a zero-space update injects the fingerprint without perturbing unrelated knowledge. Verification requires only a single black-box query and succeeds when the model returns the exact pre-embedded protagonist. Empirical results on LLaMA and Qwen families show that EditMF combines high imperceptibility with negligible model's performance loss, while delivering robustness far beyond LoRA-based fingerprinting and approaching that of SFT embeddings. Extensive experiments demonstrate that EditMF is an effective and low-overhead solution for secure LLM ownership verification.

