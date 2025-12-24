---
layout: default
title: "PathReasoning: A multimodal reasoning agent for query-based ROI navigation on whole-slide images"
---

# PathReasoning: A multimodal reasoning agent for query-based ROI navigation on whole-slide images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21902" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21902v1</a>
  <a href="https://arxiv.org/pdf/2511.21902.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21902v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.21902v1', 'PathReasoning: A multimodal reasoning agent for query-based ROI navigation on whole-slide images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kunpeng Zhang, Hanwen Xu, Sheng Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-26

---

## 💡 一句话要点

**PathReasoning：一种用于全切片图像上基于查询的ROI导航的多模态推理Agent**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `全切片图像` `ROI导航` `多模态推理` `数字病理学` `肿瘤微环境`

## 📋 核心要点

1. 全切片图像巨大，人工导航耗时，现有方法缺乏有效的问题引导和推理机制。
2. PathReasoning通过多轮推理和自我反思，逐步引导模型关注诊断相关区域，构建可解释的推理链。
3. 实验表明，PathReasoning在ROI选择和报告生成方面显著优于现有方法，AUROC最高提升6.7%，报告准确率提升10%。

## 📝 摘要（中文）

从全切片图像(WSI)中解读肿瘤微环境对于癌症的诊断、预后和治疗反应至关重要。然而，这些高达数十亿像素的图像在提供全面癌症图景的同时，其巨大的尺寸也使得导航到相应区域以支持各种临床检查变得具有挑战性和耗时。受病理学家在WSI上结合采样、推理和自我反思进行导航的启发，我们提出了“PathReasoning”，这是一种多模态推理Agent，通过多轮推理和改进在WSI中迭代导航。具体来说，PathReasoning从随机采样的候选区域开始，通过自我反思来回顾当前的选择，推理视觉观察和临床问题之间的对应关系，并通过提出新的探索区域来结束。在多轮迭代中，PathReasoning构建了一个推理链，逐步将注意力引导到具有诊断相关性的区域。PathReasoning将每个全切片图像转换为一系列问题引导的视图，使模型能够在固定步数内有效地找到信息丰富的ROI，而无需密集的像素级注释。PathReasoning在亚型分析和纵向分析任务中，显著优于强大的ROI选择方法，AUROC分别提高了6.7%和3.1%。高质量的ROI进一步支持了乳腺癌的准确报告生成，在准确性方面显著优于标准GPT-4o 10%。PathReasoning优先考虑特定问题的区域并构建可解释的推理链，从而支持数字病理学中的高效切片审查、一致的诊断解释、全面的报告和证据可追溯性。

## 🔬 方法详解

**问题定义**：全切片图像（WSI）尺寸巨大，人工导航耗时且容易出错。现有的ROI选择方法通常缺乏有效的问题引导和推理机制，难以快速准确地定位到具有诊断价值的区域。这阻碍了对肿瘤微环境的深入理解和临床应用。

**核心思路**：PathReasoning的核心思路是模拟病理学家的诊断过程，通过迭代的采样、推理和自我反思，逐步缩小搜索范围，最终定位到与临床问题相关的ROI。这种方法将全局搜索问题转化为一个序列决策问题，利用多模态信息进行推理。

**技术框架**：PathReasoning包含以下主要模块：1) 候选区域采样：从WSI中随机采样候选ROI；2) 自我反思：评估当前选择的ROI的质量；3) 多模态推理：结合视觉信息和临床问题，推理ROI与问题的相关性；4) 区域提议：基于推理结果，提出新的探索区域。整个流程迭代进行，直到达到预设的步数或满足停止条件。

**关键创新**：PathReasoning的关键创新在于其多模态推理和迭代改进机制。它不仅利用视觉信息，还结合了临床问题，从而实现了问题引导的ROI导航。此外，通过自我反思和迭代改进，PathReasoning能够逐步提高ROI的质量，并构建可解释的推理链。

**关键设计**：PathReasoning的具体实现细节包括：使用预训练的视觉模型提取ROI的特征；使用自然语言处理模型解析临床问题；设计一个推理模块，将视觉特征和问题表示映射到ROI的相关性得分；使用强化学习或监督学习方法训练模型，使其能够有效地进行自我反思和区域提议。损失函数的设计需要考虑ROI的质量、与问题的相关性以及推理链的可解释性。

## 📊 实验亮点

PathReasoning在亚型分析和纵向分析任务中，AUROC分别提高了6.7%和3.1%，显著优于现有的ROI选择方法。在乳腺癌报告生成任务中，PathReasoning的准确性比GPT-4o提高了10%。这些结果表明，PathReasoning能够有效地定位到具有诊断价值的ROI，并生成更准确的报告。

## 🎯 应用场景

PathReasoning可应用于数字病理学领域，辅助病理学家进行全切片图像的快速审查和诊断。它可以提高诊断效率和准确性，减少人为误差，并为临床决策提供更可靠的依据。此外，PathReasoning还可以用于药物研发、生物标志物发现等领域，加速癌症研究的进展。

## 📄 摘要（原文）

> Deciphering tumor microenvironment from Whole Slide Images (WSIs) is intriguing as it is key to cancer diagnosis, prognosis and treatment response. While these gigapixel images on one hand offer a comprehensive portrait of cancer, on the other hand, the extremely large size, as much as more than 10 billion pixels, make it challenging and time-consuming to navigate to corresponding regions to support diverse clinical inspection. Inspired by pathologists who conducted navigation on WSIs with a combination of sampling, reasoning and self-reflection, we proposed "PathReasoning", a multi-modal reasoning agent that iteratively navigates across WSIs through multiple rounds of reasoning and refinements. Specifically, starting with randomly sampled candidate regions, PathReasoning reviews current selections with self-reflection, reasoning over the correspondence between visual observations and clinical questions, and concludes by proposing new regions to explore. Across rounds, PathReasoning builds a reasoning chain that gradually directs attention to diagnostically relevant areas. PathReasoning turns each whole slide into a sequence of question-guided views, allowing the model to efficiently find informative ROIs within a fixed number of steps, without the need for dense pixel-level annotations. PathReasoning can substantially outperform strong ROI-selection approaches by 6.7% and 3.1% of AUROC on subtyping and longitudinal analysis tasks. The high-quality ROIs further support accurate report generation on breast cancer, significantly outperforming the standard GPT-4o by 10% in accuracy. PathReasoning prioritizes question-specific regions and constructs interpretable reasoning chains, supporting efficient slide review, consistent diagnostic interpretations, comprehensive reporting, and evidence traceability in digital pathology.

