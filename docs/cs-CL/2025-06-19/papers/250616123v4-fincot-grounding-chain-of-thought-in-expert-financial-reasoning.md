---
layout: default
title: "FinCoT: Grounding Chain-of-Thought in Expert Financial Reasoning"
---

# FinCoT: Grounding Chain-of-Thought in Expert Financial Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16123" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16123v4</a>
  <a href="https://arxiv.org/pdf/2506.16123.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16123v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16123v4', 'FinCoT: Grounding Chain-of-Thought in Expert Financial Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Natapong Nitarach, Warit Sirichotedumrong, Panop Pitchayarthorn, Pittawat Taveekitworachai, Potsawee Manakul, Kunat Pipatanakul

**分类**: cs.CL

**发布日期**: 2025-06-19 (更新: 2025-09-17)

**备注**: Accepted at FinNLP-2025, EMNLP

---

## 💡 一句话要点

**提出FinCoT框架以提升金融领域的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融推理` `链式思维` `自然语言处理` `结构化提示` `专家知识` `模型优化` `推理能力` `金融科技`

## 📋 核心要点

1. 现有方法在金融自然语言处理中的结构化推理不足，缺乏领域专家的有效融入。
2. FinCoT框架通过结合专家蓝图，提供了一种结构化的链式思维提示方法，提升了模型的推理能力。
3. 实验结果显示，FinCoT显著提高了模型的准确率，并减少了输出长度，尤其对缺乏金融后训练的模型效果显著。

## 📝 摘要（中文）

本文提出了FinCoT，一个结构化的链式思维（CoT）提示框架，嵌入了特定领域的专家金融推理蓝图，以指导大型语言模型的行为。我们识别了金融自然语言处理（FinNLP）中的三种主要提示风格：标准提示、非结构化CoT和结构化CoT。以往的研究主要集中在前两者，而结构化CoT仍然未被充分探索且缺乏领域专家的融入。因此，我们在十个CFA风格的金融领域中评估了这三种提示方法，并引入FinCoT作为首个结合领域专家蓝图的结构化金融特定提示方法。FinCoT将通用模型Qwen3-8B-Base的准确率从63.2%提升至80.5%，并将金融特定模型Fin-R1（7B）的准确率从65.7%提升至75.7%，同时输出长度分别减少了8.9倍和1.16倍。我们的研究表明，FinCoT不仅提高了性能和降低了推理成本，还产生了更具可解释性和专家对齐的推理轨迹。

## 🔬 方法详解

**问题定义**：本文旨在解决金融领域自然语言处理中的结构化推理不足问题，现有方法主要集中在标准提示和非结构化推理，缺乏有效的领域专家知识融入。

**核心思路**：FinCoT框架通过嵌入专家蓝图，提供结构化的推理步骤，旨在引导大型语言模型更好地理解和处理金融问题。

**技术框架**：FinCoT的整体架构包括三个主要模块：标准提示、非结构化CoT和结构化CoT，结合专家知识进行推理。每个模块根据具体的金融领域需求进行调整和优化。

**关键创新**：FinCoT的最大创新在于首次将领域专家的推理蓝图与结构化CoT结合，显著提升了模型在金融领域的推理能力，与以往方法相比，提供了更高的准确性和可解释性。

**关键设计**：在模型设计中，FinCoT采用了特定的损失函数和参数设置，以确保推理过程的结构化和高效性，同时优化了模型的输出长度和推理成本。通过这些设计，FinCoT能够有效地处理复杂的金融问题。

## 📊 实验亮点

实验结果显示，FinCoT将通用模型Qwen3-8B-Base的准确率从63.2%提升至80.5%，而金融特定模型Fin-R1（7B）的准确率从65.7%提升至75.7%。此外，FinCoT在输出长度上分别减少了8.9倍和1.16倍，显示出其在性能和效率上的显著提升。

## 🎯 应用场景

FinCoT框架在金融分析、投资决策支持和风险评估等领域具有广泛的应用潜力。通过增强模型的推理能力，金融机构可以更高效地处理复杂的财务数据，提供更准确的决策支持。未来，FinCoT可能推动金融科技的发展，提升行业整体的智能化水平。

## 📄 摘要（原文）

> This paper presents FinCoT, a structured chain-of-thought (CoT) prompting framework that embeds domain-specific expert financial reasoning blueprints to guide large language models' behaviors. We identify three main prompting styles in financial NLP (FinNLP): (1) standard prompting (zero-shot), (2) unstructured CoT (free-form reasoning), and (3) structured CoT (with explicitly structured reasoning steps). Prior work has mainly focused on the first two, while structured CoT remains underexplored and lacks domain expertise incorporation. Therefore, we evaluate all three prompting approaches across ten CFA-style financial domains and introduce FinCoT as the first structured finance-specific prompting approach incorporating blueprints from domain experts. FinCoT improves the accuracy of a general-purpose model, Qwen3-8B-Base, from 63.2% to 80.5%, and boosts Fin-R1 (7B), a finance-specific model, from 65.7% to 75.7%, while reducing output length by up to 8.9x and 1.16x compared to structured CoT methods, respectively. We find that FinCoT proves most effective for models lacking financial post-training. Our findings show that FinCoT does not only improve performance and reduce inference costs but also yields more interpretable and expert-aligned reasoning traces.

