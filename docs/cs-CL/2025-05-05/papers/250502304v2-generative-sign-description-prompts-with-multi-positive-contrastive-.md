---
layout: default
title: Generative Sign-description Prompts with Multi-positive Contrastive Learning for Sign Language Recognition
---

# Generative Sign-description Prompts with Multi-positive Contrastive Learning for Sign Language Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02304" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02304v2</a>
  <a href="https://arxiv.org/pdf/2505.02304.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02304v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02304v2', 'Generative Sign-description Prompts with Multi-positive Contrastive Learning for Sign Language Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyu Liang, Yunan Li, Wentian Xin, Huizhou Chen, Xujie Liu, Kang Liu, Qiguang Miao

**分类**: cs.CL, cs.CV

**发布日期**: 2025-05-05 (更新: 2025-07-22)

**备注**: 9 pages, 6 figures

---

## 💡 一句话要点

**提出GSP-MC方法以解决手语识别中的标注准确性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手语识别` `生成性模型` `对比学习` `多模态学习` `跨语言技术`

## 📋 核心要点

1. 手语识别面临标注准确性不足的挑战，现有方法难以处理复杂的手动与非手动信号。
2. 提出GSP-MC方法，通过生成性大型语言模型与多正对比学习，优化手语描述的生成与对齐。
3. 在Chinese SLR500和Turkish AUTSL数据集上，GSP-MC方法分别达到了97.1%和97.07%的准确率，表现优异。

## 📝 摘要（中文）

手语识别（SLR）面临由于手动和非手动信号的复杂性而导致的准确标注挑战。本文首次将生成性大型语言模型（LLMs）整合到SLR任务中，提出了一种新颖的生成性手语描述提示多正对比学习（GSP-MC）方法。该方法利用检索增强生成（RAG）与领域特定的LLMs，结合多步骤提示工程和专家验证的手语语料库，生成精确的多部分描述。GSP-MC方法采用双编码器架构，通过概率匹配双向对齐层次骨架特征与多种文本描述（全局、同义词和部分级别）。实验结果表明，该方法在Chinese SLR500（达到97.1%）和Turkish AUTSL数据集（97.07%准确率）上实现了领先的性能，展示了其跨语言的有效性，突显了其在开发包容性沟通技术方面的潜力。

## 🔬 方法详解

**问题定义**：手语识别中的标注准确性问题主要源于手动和非手动信号的复杂性，现有方法在生成精确描述方面存在不足。

**核心思路**：GSP-MC方法通过结合生成性大型语言模型与多正对比学习，利用检索增强生成技术，生成精确的手语描述，旨在提升标注的准确性和一致性。

**技术框架**：该方法采用双编码器架构，首先通过多步骤提示工程生成手语描述，然后通过概率匹配将层次骨架特征与文本描述进行双向对齐，最后结合全局和部分级损失进行优化。

**关键创新**：GSP-MC方法的创新在于将生成性大型语言模型与对比学习相结合，利用多层次的描述生成与对齐，显著提升了手语识别的准确性和鲁棒性。

**关键设计**：在损失函数设计上，结合了KL散度优化，确保文本与骨架特征的对齐，同时在网络结构上采用双编码器架构，以实现更高效的特征匹配和描述生成。

## 📊 实验亮点

实验结果显示，GSP-MC方法在Chinese SLR500数据集上达到了97.1%的准确率，在Turkish AUTSL数据集上达到了97.07%的准确率，均超越了现有方法，展示了显著的性能提升，验证了其在手语识别领域的有效性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在手语翻译、无障碍沟通技术和教育领域。通过提高手语识别的准确性，能够帮助聋哑人士更好地与社会沟通，促进包容性交流。此外，该方法的跨语言有效性也为多语言环境下的手语识别提供了新的解决方案。

## 📄 摘要（原文）

> Sign language recognition (SLR) faces fundamental challenges in creating accurate annotations due to the inherent complexity of simultaneous manual and non-manual signals. To the best of our knowledge, this is the first work to integrate generative large language models (LLMs) into SLR tasks. We propose a novel Generative Sign-description Prompts Multi-positive Contrastive learning (GSP-MC) method that leverages retrieval-augmented generation (RAG) with domain-specific LLMs, incorporating multi-step prompt engineering and expert-validated sign language corpora to produce precise multipart descriptions. The GSP-MC method also employs a dual-encoder architecture to bidirectionally align hierarchical skeleton features with multiple text descriptions (global, synonym, and part level) through probabilistic matching. Our approach combines global and part-level losses, optimizing KL divergence to ensure robust alignment across all relevant text-skeleton pairs while capturing both sign-level semantics and detailed part dynamics. Experiments demonstrate state-of-the-art performance against existing methods on the Chinese SLR500 (reaching 97.1%) and Turkish AUTSL datasets (97.07% accuracy). The method's cross-lingual effectiveness highlight its potential for developing inclusive communication technologies.

