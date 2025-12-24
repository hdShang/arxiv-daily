---
layout: default
title: Donate or Create? Comparing Data Collection Strategies for Emotion-labeled Multimodal Social Media Posts
---

# Donate or Create? Comparing Data Collection Strategies for Emotion-labeled Multimodal Social Media Posts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24427" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24427v1</a>
  <a href="https://arxiv.org/pdf/2505.24427.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24427v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24427v1', 'Donate or Create? Comparing Data Collection Strategies for Emotion-labeled Multimodal Social Media Posts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christopher Bagdon, Aidan Combs, Carina Silberer, Roman Klinger

**分类**: cs.CL

**发布日期**: 2025-05-30

**备注**: Published at ACL 2025

---

## 💡 一句话要点

**比较数据收集策略以优化情感标注的多模态社交媒体帖子**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感分析` `多模态数据` `社交媒体` `数据收集策略` `模型训练` `情感标注` `用户隐私`

## 📋 核心要点

1. 现有方法在收集情感标注数据时面临参与者隐私风险和实施复杂性的问题。
2. 论文提出通过比较研究创建与真实内容的多模态社交媒体帖子，分析其对情感模型的影响。
3. 实验结果表明，研究创建的帖子在长度、情感表达方式及参与者特征上与真实帖子存在显著差异。

## 📝 摘要（中文）

准确建模情感表达等主观现象需要标注作者意图的数据。常见的数据收集方式包括要求参与者捐赠真实内容或在研究中创建符合特定标签的内容。虽然创建内容的实施更简单且对参与者隐私风险较小，但尚不清楚研究创建的内容与真实内容的差异及其对模型的影响。本文收集并比较了标注情感的研究创建和真实的多模态社交媒体帖子，发现研究创建的帖子通常更长，情感表达更依赖文本而非图像，并且更关注情感原型事件。愿意捐赠与创建帖子的参与者在人口统计上存在差异。研究创建的数据对训练能够很好泛化到真实数据的模型是有价值的，但真实数据是评估有效性的必要条件。

## 🔬 方法详解

**问题定义**：本文旨在解决在情感标注数据收集过程中，研究创建内容与真实内容之间的差异及其对模型性能的影响。现有方法在隐私保护和实施复杂性上存在挑战。

**核心思路**：通过收集和比较研究创建的内容与真实社交媒体帖子，分析其在情感表达上的差异，从而评估不同数据收集策略的有效性。

**技术框架**：研究采用了多模态数据收集框架，包含数据收集、标注、模型训练和性能评估四个主要模块。数据收集阶段分别获取研究创建和真实内容，标注阶段进行情感标签的分配，模型训练阶段使用不同数据集进行训练，最后在性能评估阶段比较模型表现。

**关键创新**：本研究的创新点在于系统性地比较了两种数据收集策略的效果，揭示了研究创建内容在情感表达上的特征差异，为情感模型的训练提供了新的视角。

**关键设计**：在实验中，设置了不同的情感标签和多模态输入，采用了适应性损失函数以优化模型性能，确保模型能够有效处理文本和图像信息。

## 📊 实验亮点

实验结果显示，与真实帖子相比，研究创建的帖子在长度上显著增加，情感表达更依赖文本而非图像，且更集中于情感原型事件。这些差异可能影响模型的训练效果，强调了真实数据在模型评估中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体分析、情感计算和人机交互等。通过优化数据收集策略，可以提升情感模型的泛化能力，进而在情感识别、情感推荐等实际应用中发挥重要作用。未来，研究成果可能推动更高效的情感数据收集方法的发展。

## 📄 摘要（原文）

> Accurate modeling of subjective phenomena such as emotion expression requires data annotated with authors' intentions. Commonly such data is collected by asking study participants to donate and label genuine content produced in the real world, or create content fitting particular labels during the study. Asking participants to create content is often simpler to implement and presents fewer risks to participant privacy than data donation. However, it is unclear if and how study-created content may differ from genuine content, and how differences may impact models. We collect study-created and genuine multimodal social media posts labeled for emotion and compare them on several dimensions, including model performance. We find that compared to genuine posts, study-created posts are longer, rely more on their text and less on their images for emotion expression, and focus more on emotion-prototypical events. The samples of participants willing to donate versus create posts are demographically different. Study-created data is valuable to train models that generalize well to genuine data, but realistic effectiveness estimates require genuine data.

