---
layout: default
title: HELM: Hyperbolic Large Language Models via Mixture-of-Curvature Experts
---

# HELM: Hyperbolic Large Language Models via Mixture-of-Curvature Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24722" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24722v2</a>
  <a href="https://arxiv.org/pdf/2505.24722.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24722v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24722v2', 'HELM: Hyperbolic Large Language Models via Mixture-of-Curvature Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Neil He, Rishabh Anand, Hiren Madhu, Ali Maatouk, Smita Krishnaswamy, Leandros Tassiulas, Menglin Yang, Rex Ying

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-11-06)

---

## 💡 一句话要点

**提出HELM以解决现有语言模型几何结构不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `超曲率模型` `语言模型` `几何结构` `Transformer` `混合曲率专家` `自然语言处理` `模型训练` `推理能力`

## 📋 核心要点

1. 现有大型语言模型未能充分利用自然语言的几何结构，导致训练不稳定和生成能力不足。
2. 本文提出HELM，通过在超曲率空间中操作，解决了现有模型的表示灵活性不足和扩展性差的问题。
3. 实验结果表明，HELM在多个基准测试中相较于传统欧几里得架构提升了最高4%的性能，显示出超曲率几何的优势。

## 📝 摘要（中文）

大型语言模型（LLMs）在文本建模任务中取得了显著成功，但由于依赖欧几里得操作，未能完全捕捉自然语言的固有语义层次和几何结构。研究表明，忽视标记嵌入的几何特性会导致训练不稳定和生成能力下降。因此，本文提出在超曲率空间中完全操作的HELM（HypErbolic Large Language Models），并引入混合曲率专家模型HELM-MICE，以更细致地编码文本的几何结构。我们首次在十亿参数规模下训练完全超曲率的LLMs，并在多个基准测试中评估其性能，结果显示HELM架构在推理能力上相较于流行的欧几里得架构有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型在处理自然语言时未能充分考虑其几何结构的问题，导致模型训练不稳定和生成能力下降。

**核心思路**：论文提出在超曲率空间中完全操作的HELM模型，利用超曲率的扩展性和低失真特性，重新思考基于Transformer的语言模型架构。

**技术框架**：HELM包括HELM-MICE和HELM-D两个模型，HELM-MICE采用混合曲率专家模型，每个专家在不同的曲率空间中操作，以编码更细致的几何结构。HELM-D则为密集模型，二者均引入超曲率的多头潜在注意力机制（HMLA）以提高训练和推理效率。

**关键创新**：本文首次在十亿参数规模下训练完全超曲率的语言模型，并开发了超曲率的旋转位置编码和RMS归一化，显著提升了模型的推理能力。

**关键设计**：HELM模型设计中，采用了混合曲率专家机制，优化了参数设置和损失函数，确保模型在不同几何空间中有效学习文本的结构特征。

## 📊 实验亮点

实验结果显示，HELM模型在MMLU和ARC等基准测试中，相较于LLaMA和DeepSeek等流行的欧几里得架构，性能提升最高可达4%。这一结果突显了超曲率几何在大规模语言模型预训练中的有效性和增强的推理能力。

## 🎯 应用场景

HELM模型在自然语言处理领域具有广泛的应用潜力，尤其是在需要深度理解文本几何结构的任务中，如知识问答、文本生成和语义理解等。其改进的推理能力和稳定性将推动更复杂的语言模型的开发，未来可能在多种智能应用中发挥重要作用。

## 📄 摘要（原文）

> Large language models (LLMs) have shown great success in text modeling tasks across domains. However, natural language exhibits inherent semantic hierarchies and nuanced geometric structure, which current LLMs do not capture completely owing to their reliance on Euclidean operations. Recent studies have also shown that not respecting the geometry of token embeddings leads to training instabilities and degradation of generative capabilities. These findings suggest that shifting to non-Euclidean geometries can better align language models with the underlying geometry of text. We thus propose to operate fully in Hyperbolic space, known for its expansive, scale-free, and low-distortion properties. We thus introduce HELM, a family of HypErbolic Large Language Models, offering a geometric rethinking of the Transformer-based LLM that addresses the representational inflexibility, missing set of necessary operations, and poor scalability of existing hyperbolic LMs. We additionally introduce a Mixture-of-Curvature Experts model, HELM-MICE, where each expert operates in a distinct curvature space to encode more fine-grained geometric structure from text, as well as a dense model, HELM-D. For HELM-MICE, we further develop hyperbolic Multi-Head Latent Attention (HMLA) for efficient, reduced-KV-cache training and inference. For both models, we develop essential hyperbolic equivalents of rotary positional encodings and RMS normalization. We are the first to train fully hyperbolic LLMs at billion-parameter scale, and evaluate them on well-known benchmarks such as MMLU and ARC, spanning STEM problem-solving, general knowledge, and commonsense reasoning. Our results show consistent gains from our HELM architectures -- up to 4% -- over popular Euclidean architectures used in LLaMA and DeepSeek, highlighting the efficacy and enhanced reasoning afforded by hyperbolic geometry in large-scale LM pretraining.

