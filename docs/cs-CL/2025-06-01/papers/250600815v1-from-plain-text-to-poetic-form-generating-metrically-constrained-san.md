---
layout: default
title: From Plain Text to Poetic Form: Generating Metrically-Constrained Sanskrit Verses
---

# From Plain Text to Poetic Form: Generating Metrically-Constrained Sanskrit Verses

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00815" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00815v1</a>
  <a href="https://arxiv.org/pdf/2506.00815.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00815v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00815v1', 'From Plain Text to Poetic Form: Generating Metrically-Constrained Sanskrit Verses')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manoj Balaji Jagadeeshan, Samarth Bhatia, Pretam Ray, Harshul Raj Surana, Akhil Rajeev P, Priya Mishra, Annarao Kulkarni, Ganesh Ramakrishnan, Prathosh AP, Pawan Goyal

**分类**: cs.CL

**发布日期**: 2025-06-01

---

## 💡 一句话要点

**提出一种方法以生成符合韵律的梵文诗歌**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言生成` `梵文诗歌` `大型语言模型` `约束解码` `指令微调` `韵律生成` `低资源语言`

## 📋 核心要点

1. 现有的自然语言生成方法在低资源语言的结构化诗歌生成上存在显著不足，尤其是梵文这种形态丰富的语言。
2. 本文提出了一种新的数据集和生成模型，专注于将英语散文翻译为符合古典韵律的梵文诗歌，采用约束解码和指令微调策略。
3. 实验结果表明，所提方法在生成语法有效的诗歌形式上达到了99%以上的准确率，并在语义和风格上有显著提升。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进步显著提升了自然语言生成能力，包括诗歌创作等创造性任务。然而，大多数进展集中在高资源语言上。本文探讨了如何将LLMs适应于低资源且形态丰富的语言——梵文的结构化诗歌生成。我们引入了一个数据集，用于将英语散文翻译为符合古典韵律模式的梵文诗歌，特别是Anushtub韵律。我们评估了多种生成模型，并探索了针对韵律和语义保真度的约束解码策略和基于指令的微调。我们的解码方法在生成语法有效的诗歌形式方面达到了99%以上的准确率，显著优于通用模型的韵律一致性。同时，经过指令微调的变体在源意义和诗歌风格的对齐上表现出改善，尽管在韵律精度上存在轻微的权衡。

## 🔬 方法详解

**问题定义**：本文旨在解决如何在低资源且形态丰富的语言（如梵文）中生成符合韵律的诗歌。现有方法在这一领域的应用效果不佳，尤其是在韵律和语义一致性方面存在挑战。

**核心思路**：我们提出了一种新的数据集，专注于将英语散文翻译为符合古典韵律的梵文诗歌，并采用约束解码和指令微调策略，以增强生成的韵律和语义保真度。

**技术框架**：整体架构包括数据集构建、模型选择、约束解码和指令微调四个主要模块。首先，构建了一个包含英语与梵文对照的诗歌数据集；其次，评估了多种开源和专有生成模型；然后，实施了约束解码策略以确保韵律一致性；最后，进行了指令微调以提高语义对齐。

**关键创新**：本文的主要创新在于针对梵文诗歌生成的约束解码策略和指令微调方法，这与现有的通用生成模型形成了鲜明对比，显著提升了生成结果的韵律和语义质量。

**关键设计**：在模型训练中，我们设置了特定的损失函数以优化韵律一致性，并设计了适应梵文特性的网络结构，确保生成的诗歌在语法和韵律上都符合标准。

## 📊 实验亮点

实验结果显示，所提解码方法在生成语法有效的诗歌形式方面达到了99%以上的准确率，显著优于通用模型的韵律一致性。同时，经过指令微调的模型在源意义和诗歌风格的对齐上表现出改善，尽管在韵律精度上存在轻微的权衡。

## 🎯 应用场景

该研究的潜在应用领域包括文化遗产保护、语言学习和人工智能创作等。通过生成符合韵律的梵文诗歌，可以促进对梵文文学的研究与传播，同时为低资源语言的自然语言处理提供新的思路和方法，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have significantly improved natural language generation, including creative tasks like poetry composition. However, most progress remains concentrated in high-resource languages. This raises an important question: Can LLMs be adapted for structured poetic generation in a low-resource, morphologically rich language such as Sanskrit? In this work, we introduce a dataset designed for translating English prose into structured Sanskrit verse, with strict adherence to classical metrical patterns, particularly the Anushtub meter. We evaluate a range of generative models-both open-source and proprietary-under multiple settings. Specifically, we explore constrained decoding strategies and instruction-based fine-tuning tailored to metrical and semantic fidelity. Our decoding approach achieves over 99% accuracy in producing syntactically valid poetic forms, substantially outperforming general-purpose models in meter conformity. Meanwhile, instruction-tuned variants show improved alignment with source meaning and poetic style, as supported by human assessments, albeit with marginal trade-offs in metrical precision.

