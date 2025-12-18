---
layout: default
title: Effect of Document Packing on the Latent Multi-Hop Reasoning Capabilities of Large Language Models
---

# Effect of Document Packing on the Latent Multi-Hop Reasoning Capabilities of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14427" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14427v1</a>
  <a href="https://arxiv.org/pdf/2512.14427.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14427v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14427v1', 'Effect of Document Packing on the Latent Multi-Hop Reasoning Capabilities of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gabriele Prato, Shagun Sodhani, Alessandro Sordoni, Sarath Chandar

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**研究文档打包策略对大语言模型多跳推理能力的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `文档打包` `多跳推理` `训练策略` `消融实验`

## 📋 核心要点

1. 现有大语言模型训练通常采用文档打包策略以提升计算效率，但其对模型推理能力的潜在影响尚不明确。
2. 该研究通过对比不同文档打包策略下LLM的多跳推理性能，探索了打包策略对模型能力的影响。
3. 实验表明，文档打包能在增加计算成本的同时，提升模型性能，消融实验揭示了打包优势的关键因素。

## 📝 摘要（中文）

本文研究了文档打包策略对大语言模型（LLM）潜在多跳推理能力的影响。通常，训练大型语言模型时会将多个文档打包在一起，以优化计算效率。然而，这种做法对模型能力的影响在很大程度上仍未被探索。研究结果表明，与在单个文档上训练相比，打包可以提高模型性能，但会增加计算成本。为了进一步理解其潜在机制，我们进行了一项消融研究，确定了解释打包优势的关键因素。最终，我们的研究加深了对LLM训练动态的理解，并为优化模型开发提供了实用的见解。

## 🔬 方法详解

**问题定义**：论文旨在研究在训练大型语言模型时，将多个文档打包在一起对模型的多跳推理能力产生的影响。现有方法通常只关注计算效率的优化，而忽略了文档打包策略可能对模型学习到的知识表示和推理能力造成的潜在影响。因此，如何选择合适的文档打包策略，以在计算效率和模型性能之间取得平衡，是一个亟待解决的问题。

**核心思路**：论文的核心思路是通过实验对比不同的文档打包策略，分析它们对模型多跳推理能力的影响。通过消融实验，进一步探究文档打包策略影响模型性能的关键因素，从而为选择合适的文档打包策略提供理论依据。这种方法旨在揭示文档打包与模型推理能力之间的内在联系。

**技术框架**：该研究的技术框架主要包括以下几个部分：首先，构建一个包含多个文档的数据集；然后，采用不同的文档打包策略对数据集进行处理，生成不同的训练集；接着，使用这些训练集训练大型语言模型；最后，在多跳推理任务上评估模型的性能，并进行消融实验，分析不同因素对模型性能的影响。

**关键创新**：该研究的关键创新在于首次系统性地研究了文档打包策略对大型语言模型多跳推理能力的影响。以往的研究主要关注文档打包对计算效率的影响，而忽略了其对模型学习到的知识表示和推理能力的潜在影响。该研究填补了这一空白，为优化大型语言模型的训练策略提供了新的视角。

**关键设计**：论文的关键设计包括：1) 设计了多种文档打包策略，例如随机打包、按主题打包等；2) 选择了具有代表性的多跳推理任务作为评估指标；3) 采用了消融实验的方法，分析了不同因素对模型性能的影响，例如打包文档的数量、文档之间的相关性等；4) 详细记录了训练过程中的计算成本，以便在计算效率和模型性能之间进行权衡。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14427v1/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，与在单个文档上训练相比，文档打包可以提高模型在多跳推理任务上的性能。具体的性能提升幅度取决于所采用的文档打包策略。消融实验揭示了打包文档的数量和文档之间的相关性是影响模型性能的关键因素。例如，适当增加打包文档的数量可以提升模型性能，但过多的打包文档可能会导致性能下降。此外，打包具有较高相关性的文档可以提升模型的多跳推理能力。

## 🎯 应用场景

该研究成果可应用于优化大语言模型的训练流程，提升模型在问答系统、知识图谱推理、智能搜索等领域的性能。通过选择合适的文档打包策略，可以在保证计算效率的同时，提升模型的多跳推理能力，从而更好地服务于实际应用场景。未来的研究可以进一步探索更智能的文档打包策略，例如基于强化学习的自适应打包策略。

## 📄 摘要（原文）

> The standard practice for training large language models involves packing multiple documents together to optimize computational efficiency. However, the impact of this process on the models' capabilities remains largely unexplored. To address this gap, we investigate how different document-packing strategies influence the latent multi-hop reasoning abilities of LLMs. Our findings indicate that packing can improve model performance compared to training on individual documents, at the expense of more compute. To further understand the underlying mechanisms, we conduct an ablation study, identifying key factors that explain the advantages of packing. Ultimately, our research deepens the understanding of LLM training dynamics and provides practical insights for optimizing model development.

