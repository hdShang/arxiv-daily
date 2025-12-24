---
layout: default
title: "DaMoC: Efficiently Selecting the Optimal Large Language Model for Fine-tuning Domain Tasks Based on Data and Model Compression"
---

# DaMoC: Efficiently Selecting the Optimal Large Language Model for Fine-tuning Domain Tasks Based on Data and Model Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01221" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01221v2</a>
  <a href="https://arxiv.org/pdf/2509.01221.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01221v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01221v2', 'DaMoC: Efficiently Selecting the Optimal Large Language Model for Fine-tuning Domain Tasks Based on Data and Model Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Huang, Huang Wei, Yinggui Wang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-01 (更新: 2025-09-04)

**备注**: Accepted by EMNLP 2025

---

## 💡 一句话要点

**DaMoC：基于数据和模型压缩高效选择领域任务微调的最佳大语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `模型微调` `数据压缩` `模型压缩` `领域知识` `模型选择` `知识问答`

## 📋 核心要点

1. 现有方法难以快速有效地为特定领域任务选择最佳的大语言模型进行微调，面临着计算资源和时间成本的挑战。
2. DaMoC框架通过数据层面的压缩和优化以及模型层面的剪枝和合并，旨在加速最佳LLM的识别过程。
3. 实验结果表明，DaMoC能够在节省约20倍训练时间的同时，有效地选择出适合特定任务的最佳LLM。

## 📝 摘要（中文）

大语言模型（LLMs）在通用任务中表现出色，但在特定领域任务中表现不佳，需要使用特定数据进行微调。由于有许多开源LLM可用，因此选择最适合微调下游任务的模型具有挑战性，主要集中在如何快速识别最佳LLM。我们引入了一个数据和模型压缩框架（DaMoC），通过以下方式应对这一挑战：1）数据层面：首先系统地对LLM的数据过滤方法进行分类，将其分为三种不同的范式：（1）分布感知方法，（2）质量感知方法，以及（3）同时考虑这两个维度的混合方法。此外，我们提高了文本中关键token的密度，实现了token压缩。随后，我们使用LLM迭代地重写文本，以优化其表达。2）模型层面：我们使用层相似度分数来评估每一层的重要性，并删除重要性较低的层。然后，我们引入了一种稀疏合并范式，以尽可能保留原始模型的能力。在医疗问答、金融问答、通用问答和阅读理解四个数据集上的大量实验表明，我们可以选择最佳LLM，同时节省大约20倍的训练时间。

## 🔬 方法详解

**问题定义**：论文旨在解决为特定领域任务选择最佳大语言模型（LLM）进行微调的问题。现有方法通常需要对多个LLM进行完整的微调实验，耗费大量时间和计算资源，效率低下。痛点在于缺乏一种快速有效的方法来评估不同LLM在特定领域任务上的潜力。

**核心思路**：DaMoC的核心思路是通过数据和模型压缩，减少微调所需的计算量，从而加速最佳LLM的识别过程。数据压缩旨在保留关键信息并减少冗余，模型压缩则通过剪枝和合并减少模型参数量，降低计算复杂度。

**技术框架**：DaMoC框架包含数据层面和模型层面两个主要阶段。在数据层面，首先对数据进行过滤，采用分布感知、质量感知或混合方法去除噪声数据。然后，通过token压缩提高关键token密度，并使用LLM迭代重写文本以优化表达。在模型层面，使用层相似度评估每一层的重要性，剪枝不重要的层，并采用稀疏合并范式保留原始模型能力。

**关键创新**：DaMoC的关键创新在于结合了数据和模型压缩技术，并针对LLM微调的特点进行了优化。数据层面的token压缩和LLM重写以及模型层面的稀疏合并范式，都是针对LLM微调任务的创新设计。

**关键设计**：数据过滤方法包括分布感知（例如基于困惑度过滤）、质量感知（例如基于规则或模型预测质量过滤）和混合方法。Token压缩的具体实现未知。模型层面的层相似度计算方法未知，稀疏合并范式的具体实现也未知。损失函数和网络结构沿用原始LLM的设置，未做修改。

## 📊 实验亮点

实验结果表明，DaMoC框架能够在医疗问答、金融问答、通用问答和阅读理解四个数据集上，以大约20倍的训练时间节省，有效地选择出适合特定任务的最佳LLM。具体的性能提升数据未知，但时间节省的幅度非常显著，表明该方法具有很高的实用价值。

## 🎯 应用场景

该研究成果可广泛应用于各种需要领域知识的大语言模型微调场景，例如医疗、金融、法律等。通过DaMoC框架，可以显著降低选择最佳LLM的成本，加速领域模型的开发和部署，提升特定领域任务的性能。未来，该方法可以进一步扩展到其他模型压缩和加速技术，并应用于更多领域。

## 📄 摘要（原文）

> Large language models (LLMs) excel in general tasks but struggle with domain-specific ones, requiring fine-tuning with specific data. With many open-source LLMs available, selecting the best model for fine-tuning downstream tasks is challenging, primarily focusing on how to quickly identify the optimal LLM. We introduce a Data and Model Compression Framework (DaMoC) that addresses this challenge by: 1) Data Level: A systematic categorization of data filtering methodologies for LLMs is first established, classifying them into three distinct paradigms: (1) distribution-aware methods, (2) quality-aware methods, and (3) hybrid approaches considering both dimensions. Further, we enhance the density of key tokens in the text achieving token compression. Subsequently, we use an LLM to iterative rewrite the text to optimize its expression. 2) Model Level: We use layer similarity scores to assess each layer's importance and remove those with lower importance. Then, we introduce a sparse merging paradigm to preserve as much of the original model's capability as possible. Extensive experiments on four datasets, medical Q&A, financial Q&A, general Q&A, and reading comprehension, show that we can select the optimal LLM while saving approximately 20-fold in training time.

