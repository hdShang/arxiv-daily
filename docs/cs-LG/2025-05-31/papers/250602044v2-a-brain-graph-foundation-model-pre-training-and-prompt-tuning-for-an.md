---
layout: default
title: A Brain Graph Foundation Model: Pre-Training and Prompt-Tuning for Any Atlas and Disorder
---

# A Brain Graph Foundation Model: Pre-Training and Prompt-Tuning for Any Atlas and Disorder

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02044" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02044v2</a>
  <a href="https://arxiv.org/pdf/2506.02044.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02044v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02044v2', 'A Brain Graph Foundation Model: Pre-Training and Prompt-Tuning for Any Atlas and Disorder')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinxu Wei, Kanhao Zhao, Yong Jiao, Lifang He, Yu Zhang

**分类**: q-bio.NC, cs.LG

**发布日期**: 2025-05-31 (更新: 2025-08-03)

**备注**: 30pages

**🔗 代码/项目**: [GITHUB](https://github.com/weixinxu666/BrainGFM)

---

## 💡 一句话要点

**提出脑图基础模型以解决神经科学领域的多样性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脑图模型` `图对比学习` `fMRI预训练` `神经科学` `机器学习` `图掩码自编码器` `少样本学习` `零样本学习`

## 📋 核心要点

1. 现有脑基础模型主要依赖时间序列信号或连接组特征，缺乏对多样化脑图谱的有效利用。
2. 本文提出的BrainGFM模型结合图对比学习和图掩码自编码器，支持多种脑图谱和疾病的灵活适应。
3. BrainGFM在27个神经影像数据集上进行预训练，覆盖25种常见神经精神疾病，显著提升了模型的泛化能力。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在人工智能研究中的革命性进展，构建大规模脑基础模型以推动神经科学的兴趣日益增长。现有的脑基础模型大多基于时间序列信号或连接组特征进行预训练，而本文提出了一种新颖的基于图的预训练范式，构建脑图基础模型（BrainGFM）。该模型利用图对比学习和图掩码自编码器进行大规模fMRI预训练，支持多种脑图谱和神经精神疾病的适应性，显著提升了模型在异质fMRI衍生脑表征上的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有脑基础模型在处理多样化脑图谱和疾病时的局限性，尤其是对异质fMRI数据的泛化能力不足。

**核心思路**：提出BrainGFM模型，通过图对比学习和图掩码自编码器进行预训练，增强模型对不同脑图谱和疾病的适应性。

**技术框架**：BrainGFM的整体架构包括预训练阶段和下游任务适应阶段，前者利用多种脑图谱进行大规模fMRI数据的学习，后者通过图提示和语言提示实现灵活转移。

**关键创新**：该模型的核心创新在于结合图学习与语言提示，支持在少样本和零样本学习条件下的强泛化能力，显著区别于传统的时间序列模型。

**关键设计**：模型设计中采用了多种脑图谱的混合，使用了优化的图提示和语言提示，损失函数结合了对比学习和自编码器的特点，确保了模型的高效学习。

## 📊 实验亮点

在27个神经影像数据集上进行的实验表明，BrainGFM模型在处理25种常见神经精神疾病时，表现出优于现有基线模型的泛化能力，尤其在少样本和零样本学习条件下，显著提升了模型的准确性和适应性。

## 🎯 应用场景

BrainGFM模型的潜在应用场景包括神经科学研究、临床诊断和个性化医疗等领域。通过对不同脑图谱和疾病的适应性，该模型能够帮助研究人员更好地理解脑功能和疾病机制，推动相关领域的进步。

## 📄 摘要（原文）

> As large language models (LLMs) continue to revolutionize AI research, there is a growing interest in building large-scale brain foundation models to advance neuroscience. While most existing brain foundation models are pre-trained on time-series signals or connectome features, we propose a novel graph-based pre-training paradigm for constructing a brain graph foundation model. In this paper, we introduce the Brain Graph Foundation Model, termed BrainGFM, a unified framework that leverages graph contrastive learning and graph masked autoencoders for large-scale fMRI-based pre-training. BrainGFM is pre-trained on a diverse mixture of brain atlases with varying parcellations, significantly expanding the pre-training corpus and enhancing the model's ability to generalize across heterogeneous fMRI-derived brain representations. To support efficient and versatile downstream transfer, we integrate both graph prompts and language prompts into the model design, enabling BrainGFM to flexibly adapt to a wide range of atlases, neurological and psychiatric disorders, and task settings. Furthermore, we employ meta-learning to optimize the graph prompts, facilitating strong generalization to previously unseen disorders under both few-shot and zero-shot learning conditions via language-guided prompting. BrainGFM is pre-trained on 27 neuroimaging datasets spanning 25 common neurological and psychiatric disorders, encompassing 2 types of brain atlases (functional and anatomical) across 8 widely-used parcellations, and covering over 25,000 subjects, 60,000 fMRI scans, and a total of 400,000 graph samples aggregated across all atlases and parcellations. The code is available at: https://github.com/weixinxu666/BrainGFM

