---
layout: default
title: "SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms"
---

# SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06499" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06499v2</a>
  <a href="https://arxiv.org/pdf/2506.06499.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06499v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06499v2', 'SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alex Havrilla, Edward Hughes, Mikayel Samvelyan, Jacob Abernethy

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-06-17)

---

## 💡 一句话要点

**提出SPARQ以解决复杂数学问题生成的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据生成` `数学问题生成` `质量-多样性算法` `模型微调` `推理能力提升` `教育技术` `智能辅导系统`

## 📋 核心要点

1. 现有合成数据生成方法在处理复杂和多样化问题时面临可扩展性限制。
2. SPARQ通过单一模型生成高质量的合成数学问题及解决方案，利用解答率作为难度的代理。
3. 实验结果表明，基于难度过滤的数据微调可提升模型性能，且高质量数据有助于更好的模型泛化。

## 📝 摘要（中文）

基于大型语言模型（LLM）的合成数据生成已成为提升模型推理能力的重要方法。然而，现有方法通常依赖于将大型模型蒸馏为小型模型或使用自然的真实问题陈述来保证问题质量，这限制了其在更复杂和多样化问题领域的可扩展性。为此，本文提出了SPARQ：一种通过质量-多样性算法生成高质量和多样化合成数学问题及其解决方案对的新方法。通过测量问题的解答率作为难度的代理，SPARQ从一个包含7500个样本的种子数据集出发，生成超过2000万个新的问题-解决方案对。我们发现，通过难度过滤生成的数据并对同一模型进行微调，可以将模型性能提高多达24%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有合成数据生成方法在复杂数学问题领域的可扩展性不足，尤其是依赖于大型模型或真实问题陈述的局限性。

**核心思路**：SPARQ的核心思路是通过质量-多样性算法生成合成问题，利用解答率作为问题难度的代理，从而实现高效且多样化的问题生成。

**技术框架**：SPARQ的整体架构包括数据生成、难度过滤和模型微调三个主要模块。首先，从种子数据集中生成新的问题-解决方案对，然后根据难度进行过滤，最后对模型进行微调以提升性能。

**关键创新**：SPARQ的最大创新在于仅使用单一模型生成高质量和多样化的合成问题，突破了传统方法对大型模型的依赖，显著提高了生成效率和问题多样性。

**关键设计**：在技术细节上，SPARQ设置了合适的难度阈值用于过滤生成的数据，并采用特定的损失函数和网络结构来优化模型的微调过程。

## 📊 实验亮点

实验结果显示，经过难度过滤的合成数据微调可将模型性能提升多达24%。此外，研究还确认了合成问题的模型和数据扩展规律，表明高质量数据有助于模型的更好泛化能力。

## 🎯 应用场景

SPARQ的研究成果在教育技术、智能辅导系统及自动化问题生成等领域具有广泛的应用潜力。通过生成多样化的数学问题，能够有效提升学生的学习体验和模型的推理能力，推动个性化学习的发展。

## 📄 摘要（原文）

> Large language model (LLM) driven synthetic data generation has emerged as a powerful method for improving model reasoning capabilities. However, most methods either distill large state-of-the-art models into small students or use natural ground-truth problem statements to guarantee problem statement quality. This limits the scalability of these approaches to more complex and diverse problem domains. To address this, we present SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms, a novel approach for generating high-quality and diverse synthetic math problem and solution pairs using only a single model by measuring a problem's solve-rate: a proxy for problem difficulty. Starting from a seed dataset of 7.5K samples, we generate over 20 million new problem-solution pairs. We show that filtering the generated data by difficulty and then fine-tuning the same model on the resulting data improves relative model performance by up to 24\%. Additionally, we conduct ablations studying the impact of synthetic data quantity, quality and diversity on model generalization. We find that higher quality, as measured by problem difficulty, facilitates better in-distribution performance. Further, while generating diverse synthetic data does not as strongly benefit in-distribution performance, filtering for more diverse data facilitates more robust OOD generalization. We also confirm the existence of model and data scaling laws for synthetically generated problems, which positively benefit downstream model generalization.

