---
layout: default
title: VaseVQA-3D: Benchmarking 3D VLMs on Ancient Greek Pottery
---

# VaseVQA-3D: Benchmarking 3D VLMs on Ancient Greek Pottery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04479" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04479v2</a>
  <a href="https://arxiv.org/pdf/2510.04479.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04479v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.04479v2', 'VaseVQA-3D: Benchmarking 3D VLMs on Ancient Greek Pottery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nonghai Zhang, Zeyu Zhang, Jiazi Wang, Yang Zhao, Hao Tang

**分类**: cs.CV

**发布日期**: 2025-10-06 (更新: 2025-10-10)

**🔗 代码/项目**: [GITHUB](https://github.com/AIGeeksGroup/VaseVQA-3D) | [PROJECT_PAGE](https://aigeeksgroup.github.io/VaseVQA-3D)

---

## 💡 一句话要点

**提出VaseVQA-3D数据集和VaseVLM模型，解决3D文物领域视觉问答的数据稀缺和知识不足问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉问答` `视觉-语言模型` `文化遗产` `领域自适应` `数据集构建`

## 📋 核心要点

1. 现有视觉-语言模型在3D文物等专业领域面临数据稀缺和领域知识不足的挑战，限制了其在该领域的应用。
2. 论文提出VaseVQA-3D数据集和VaseVLM模型，通过构建数据集和领域自适应训练，提升模型在3D花瓶文物分析中的性能。
3. 实验结果表明，该方法在VaseVQA-3D数据集上显著提升了R@1指标和词汇相似度，验证了其有效性。

## 📝 摘要（中文）

视觉-语言模型(VLMs)在多模态理解任务中取得了显著进展，尤其是在图像描述和视觉推理等通用任务中表现出强大的能力。然而，在处理像3D花瓶文物这样的专业文化遗产领域时，现有模型面临严重的数据稀缺问题和领域知识不足的限制。由于缺乏有针对性的训练数据，当前的VLMs难以有效地处理这种具有文化意义的专业任务。为了应对这些挑战，我们提出了VaseVQA-3D数据集，这是第一个用于古希腊陶器分析的3D视觉问答数据集，收集了664个古希腊花瓶的3D模型以及相应的问答数据，并建立了一个完整的数据构建流程。我们进一步开发了VaseVLM模型，通过领域自适应训练来提高模型在花瓶文物分析中的性能。实验结果验证了我们方法的有效性，在VaseVQA-3D数据集上，R@1指标提高了12.8%，词汇相似度提高了6.6%，显著提高了对3D花瓶文物的识别和理解，为数字遗产保护研究提供了新的技术途径。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型在处理3D花瓶文物等专业领域时，由于缺乏针对性的训练数据和领域知识，难以有效进行视觉问答。现有方法无法充分利用3D文物的几何信息和文化背景知识，导致识别和理解能力不足。

**核心思路**：论文的核心思路是构建一个专门针对3D花瓶文物的视觉问答数据集（VaseVQA-3D），并在此基础上进行领域自适应训练，以提升模型在该领域的性能。通过引入领域知识和数据，弥补通用视觉-语言模型在专业领域的不足。

**技术框架**：整体框架包含两个主要部分：一是VaseVQA-3D数据集的构建，包括3D模型收集、问题生成和答案标注等步骤；二是VaseVLM模型的训练，采用领域自适应训练策略，利用VaseVQA-3D数据集对预训练的视觉-语言模型进行微调。

**关键创新**：最重要的技术创新点在于构建了首个针对古希腊陶器分析的3D视觉问答数据集VaseVQA-3D，并提出了基于该数据集的领域自适应训练方法。与现有方法相比，该方法能够更好地利用3D文物的几何信息和文化背景知识，从而提高视觉问答的准确性。

**关键设计**：数据集构建方面，采用了半自动化的方式生成问题，并由专家进行答案标注，保证了数据的质量和多样性。模型训练方面，采用了预训练的视觉-语言模型作为基础模型，并根据VaseVQA-3D数据集的特点，设计了合适的损失函数和训练策略，以实现领域自适应。

## 📊 实验亮点

实验结果表明，提出的VaseVLM模型在VaseVQA-3D数据集上取得了显著的性能提升。与之前的state-of-the-art方法相比，R@1指标提高了12.8%，词汇相似度提高了6.6%。这些结果验证了VaseVQA-3D数据集和领域自适应训练方法的有效性，表明该方法能够显著提高对3D花瓶文物的识别和理解能力。

## 🎯 应用场景

该研究成果可应用于数字遗产保护、博物馆展览、文物研究等领域。通过视觉问答技术，用户可以更方便地了解3D文物的信息，促进文化遗产的传播和保护。未来，该方法可以推广到其他类型的3D文物分析，为数字文化遗产领域提供更强大的技术支持。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have achieved significant progress in multimodal understanding tasks, demonstrating strong capabilities particularly in general tasks such as image captioning and visual reasoning. However, when dealing with specialized cultural heritage domains like 3D vase artifacts, existing models face severe data scarcity issues and insufficient domain knowledge limitations. Due to the lack of targeted training data, current VLMs struggle to effectively handle such culturally significant specialized tasks. To address these challenges, we propose the VaseVQA-3D dataset, which serves as the first 3D visual question answering dataset for ancient Greek pottery analysis, collecting 664 ancient Greek vase 3D models with corresponding question-answer data and establishing a complete data construction pipeline. We further develop the VaseVLM model, enhancing model performance in vase artifact analysis through domain-adaptive training. Experimental results validate the effectiveness of our approach, where we improve by 12.8% on R@1 metrics and by 6.6% on lexical similarity compared with previous state-of-the-art on the VaseVQA-3D dataset, significantly improving the recognition and understanding of 3D vase artifacts, providing new technical pathways for digital heritage preservation research. Code: https://github.com/AIGeeksGroup/VaseVQA-3D. Website: https://aigeeksgroup.github.io/VaseVQA-3D.

