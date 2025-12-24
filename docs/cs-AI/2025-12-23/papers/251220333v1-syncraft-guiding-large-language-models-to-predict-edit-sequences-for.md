---
layout: default
title: SynCraft: Guiding Large Language Models to Predict Edit Sequences for Molecular Synthesizability Optimization
---

# SynCraft: Guiding Large Language Models to Predict Edit Sequences for Molecular Synthesizability Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20333" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20333v1</a>
  <a href="https://arxiv.org/pdf/2512.20333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20333v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20333v1', 'SynCraft: Guiding Large Language Models to Predict Edit Sequences for Molecular Synthesizability Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junren Li, Luhua Lai

**分类**: cs.AI, q-bio.QM

**发布日期**: 2025-12-23

**备注**: 28 pages, 4 figures, 1 table

---

## 💡 一句话要点

**SynCraft：引导大语言模型预测编辑序列，优化分子合成可行性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分子生成` `合成可行性` `大语言模型` `结构编辑` `药物发现`

## 📋 核心要点

1. 现有分子生成方法在合成可行性方面存在瓶颈，后处理或投影方法牺牲了结构新颖性。
2. SynCraft将合成可行性优化视为结构编辑问题，利用大语言模型的推理能力预测原子级别的编辑序列。
3. 实验表明，SynCraft在生成可合成类似物方面优于现有方法，并能模拟药物化学专家的编辑直觉。

## 📝 摘要（中文）

生成式人工智能极大地推动了化学空间探索，但大量生成的分子难以合成仍然是一个关键瓶颈。现有的后处理过滤或基于投影的方法通常会牺牲结构新颖性或破坏关键药效团，因为它们强制将分子纳入预定义的合成模板。本文介绍SynCraft，一个基于推理的框架，它将合成可行性优化重新定义为一个精确的结构编辑问题，而非序列翻译任务。SynCraft利用大语言模型涌现的推理能力，在最小结构修改下实现合成可行性的显著提升。通过预测原子级别编辑的可执行序列，而非直接生成SMILES字符串，SynCraft规避了LLM的句法脆弱性，同时利用了它们的化学直觉。广泛的基准测试表明，SynCraft在生成具有高结构保真度的可合成类似物方面优于最先进的基线。此外，通过交互感知的提示，SynCraft成功地复制了药物化学专家的直觉，编辑了PLK1抑制剂，并在先前的分子生成文献中拯救了高分但先前被丢弃的RIPK1候选物。

## 🔬 方法详解

**问题定义**：现有分子生成方法生成的分子，很多难以合成，导致化学空间探索受限。传统的解决方法，如后处理过滤或基于投影的方法，虽然能提高合成可行性，但往往会牺牲生成分子的结构新颖性，或者破坏分子中的关键药效团，因为这些方法依赖于预定义的合成模板，缺乏灵活性。

**核心思路**：SynCraft的核心思路是将分子合成可行性优化问题，转化为一个精确的结构编辑问题。它不直接生成完整的SMILES字符串，而是通过预测一系列原子级别的编辑操作，逐步优化分子的结构，使其更易于合成。这种方法能够更好地保留分子的结构特征，同时提高合成可行性。

**技术框架**：SynCraft框架主要包含以下几个阶段：首先，输入一个初始分子结构。然后，利用大语言模型（LLM）的推理能力，预测一系列原子级别的编辑操作，例如添加、删除或修改原子或化学键。这些编辑操作是基于对分子结构的分析和合成可行性的评估而生成的。最后，将这些编辑操作应用到初始分子结构上，得到优化后的分子结构。整个过程可以迭代进行，直到分子结构的合成可行性达到预定的标准。

**关键创新**：SynCraft最重要的创新点在于它将大语言模型应用于分子结构的编辑，而不是直接生成SMILES字符串。这种方法能够更好地利用LLM的推理能力和化学直觉，同时避免了SMILES字符串的句法脆弱性问题。此外，SynCraft还引入了交互感知的提示机制，允许用户根据自己的经验和知识，对LLM的编辑操作进行指导，从而更好地模拟药物化学专家的编辑直觉。

**关键设计**：SynCraft的关键设计包括：1) 使用预训练的大语言模型，并针对化学领域的数据进行微调，以提高其化学推理能力。2) 设计了一套原子级别的编辑操作，包括添加、删除和修改原子或化学键，这些操作需要足够细粒度，以保证分子结构能够被精确地编辑。3) 引入了交互感知的提示机制，允许用户根据自己的经验和知识，对LLM的编辑操作进行指导。4) 使用合适的损失函数，例如合成可行性评分和结构相似性评分，来指导LLM的学习过程。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20333v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20333v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20333v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SynCraft在生成可合成类似物方面显著优于现有方法。实验结果表明，SynCraft在保持高结构保真度的前提下，能够有效提高生成分子的合成可行性。此外，SynCraft成功地复制了药物化学专家的编辑直觉，在PLK1抑制剂和RIPK1候选物的编辑任务中取得了良好的效果。

## 🎯 应用场景

SynCraft可应用于药物发现、材料科学等领域，加速新分子设计与优化。通过提高生成分子的合成可行性，降低了后期合成难度和成本，缩短研发周期。该方法有望辅助药物化学家快速找到具有所需性质且易于合成的候选分子，加速新药研发进程。

## 📄 摘要（原文）

> Generative artificial intelligence has revolutionized the exploration of chemical space, yet a critical bottleneck remains that a substantial fraction of generated molecules is synthetically inaccessible. Current solutions, such as post-hoc filtering or projection-based methods, often compromise structural novelty or disrupt key pharmacophores by forcing molecules into pre-defined synthetic templates. Herein, we introduce SynCraft, a reasoning-based framework that reframes synthesizability optimization not as a sequence translation task, but as a precise structural editing problem. Leveraging the emergent reasoning capabilities of Large Language Models, SynCraft navigates the "synthesis cliff" where minimal structural modifications yield significant gains in synthetic feasibility. By predicting executable sequences of atom-level edits rather than generating SMILES strings directly, SynCraft circumvents the syntactic fragility of LLMs while harnessing their chemical intuition. Extensive benchmarks demonstrate that SynCraft outperforms state-of-the-art baselines in generating synthesizable analogs with high structural fidelity. Furthermore, through interaction-aware prompting, SynCraft successfully replicates expert medicinal chemistry intuition in editing PLK1 inhibitors and rescuing high-scoring but previously discarded RIPK1 candidates in previous molecular generation literatures.

