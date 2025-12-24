---
layout: default
title: "ZPD-SCA: Unveiling the Blind Spots of LLMs in Assessing Students' Cognitive Abilities"
---

# ZPD-SCA: Unveiling the Blind Spots of LLMs in Assessing Students' Cognitive Abilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14377" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14377v2</a>
  <a href="https://arxiv.org/pdf/2508.14377.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14377v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14377v2', 'ZPD-SCA: Unveiling the Blind Spots of LLMs in Assessing Students\' Cognitive Abilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhan Dong, Zhen Sun, Yuemeng Zhao, Zifan Peng, Jun Wu, Jingyi Zheng, Yule Liu, Xinlei He, Yu Wang, Ruiming Wang, Xinyi Huang, Lei Mo

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-08-20 (更新: 2025-08-23)

---

## 💡 一句话要点

**提出ZPD-SCA以解决LLMs评估学生认知能力的盲点问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `认知能力评估` `阅读理解` `教育应用` `中文教育` `基准测试` `个性化学习`

## 📋 核心要点

1. 现有研究缺乏对LLMs在不同年龄段学生阅读理解难度评估能力的全面探讨，尤其是在中文教育背景下。
2. 本文提出ZPD-SCA基准，旨在通过60名特级教师的标注，评估中文阅读理解的阶段性难度。
3. 实验结果表明，LLMs在零样本学习中的表现较差，但在提供示例后，准确率显著提高，显示出其评估能力的潜力。

## 📝 摘要（中文）

大型语言模型（LLMs）在教育应用中展现出潜力，但其准确评估阅读材料与学生发展阶段的认知一致性能力尚未得到充分探索。为填补这一空白，本文提出了ZPD-SCA，一个专门设计用于评估阶段性中文阅读理解难度的基准。实验结果显示，LLMs在零样本学习场景中的表现不佳，但在提供上下文示例后，性能显著提升，部分模型的准确率几乎是零样本基线的两倍。这些结果揭示了LLMs在评估阅读难度方面的潜在能力，同时也暴露了其在教育对齐判断中的局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决LLMs在评估学生认知能力与阅读材料难度匹配方面的不足，尤其是在中文教育中缺乏相关研究。

**核心思路**：通过构建ZPD-SCA基准，利用特级教师的专业知识对阅读材料进行标注，以评估LLMs在不同学习阶段的表现。

**技术框架**：ZPD-SCA基准包括数据收集、标注、模型评估等多个阶段，重点在于通过专家标注确保数据的高质量和可靠性。

**关键创新**：ZPD-SCA基准的提出是一个重要创新，填补了LLMs在教育应用中评估认知能力的研究空白，与现有方法相比，更加关注教育对齐的准确性。

**关键设计**：在实验中，采用了多种模型进行评估，并通过上下文示例提升其表现，关键参数设置和损失函数设计旨在优化模型在特定任务上的学习效果。

## 📊 实验亮点

实验结果显示，LLMs在零样本学习场景中的表现不佳，部分模型如Qwen-max和GLM的准确率甚至低于随机猜测。然而，在提供上下文示例后，某些模型的准确率几乎达到了零样本基线的两倍，显示出显著的性能提升。

## 🎯 应用场景

该研究为教育领域提供了新的评估工具，能够帮助教师和教育工作者更好地理解学生的认知能力与学习材料的匹配程度。未来，ZPD-SCA基准可用于改进LLMs在教育应用中的表现，推动个性化学习的发展。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated potential in educational applications, yet their capacity to accurately assess the cognitive alignment of reading materials with students' developmental stages remains insufficiently explored. This gap is particularly critical given the foundational educational principle of the Zone of Proximal Development (ZPD), which emphasizes the need to match learning resources with Students' Cognitive Abilities (SCA). Despite the importance of this alignment, there is a notable absence of comprehensive studies investigating LLMs' ability to evaluate reading comprehension difficulty across different student age groups, especially in the context of Chinese language education. To fill this gap, we introduce ZPD-SCA, a novel benchmark specifically designed to assess stage-level Chinese reading comprehension difficulty. The benchmark is annotated by 60 Special Grade teachers, a group that represents the top 0.15% of all in-service teachers nationwide. Experimental results reveal that LLMs perform poorly in zero-shot learning scenarios, with Qwen-max and GLM even falling below the probability of random guessing. When provided with in-context examples, LLMs performance improves substantially, with some models achieving nearly double the accuracy of their zero-shot baselines. These results reveal that LLMs possess emerging abilities to assess reading difficulty, while also exposing limitations in their current training for educationally aligned judgment. Notably, even the best-performing models display systematic directional biases, suggesting difficulties in accurately aligning material difficulty with SCA. Furthermore, significant variations in model performance across different genres underscore the complexity of task. We envision that ZPD-SCA can provide a foundation for evaluating and improving LLMs in cognitively aligned educational applications.

