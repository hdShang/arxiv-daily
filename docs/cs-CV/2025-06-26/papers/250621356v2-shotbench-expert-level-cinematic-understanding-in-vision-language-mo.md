---
layout: default
title: "ShotBench: Expert-Level Cinematic Understanding in Vision-Language Models"
---

# ShotBench: Expert-Level Cinematic Understanding in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21356" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21356v2</a>
  <a href="https://arxiv.org/pdf/2506.21356.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21356v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21356v2', 'ShotBench: Expert-Level Cinematic Understanding in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongbo Liu, Jingwen He, Yi Jin, Dian Zheng, Yuhao Dong, Fan Zhang, Ziqi Huang, Yinan He, Yangguang Li, Weichao Chen, Yu Qiao, Wanli Ouyang, Shengjie Zhao, Ziwei Liu

**分类**: cs.CV

**发布日期**: 2025-06-26 (更新: 2025-06-27)

---

## 💡 一句话要点

**提出ShotBench以解决电影语言理解不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电影语言理解` `视觉-语言模型` `多模态数据集` `细粒度视觉理解` `空间推理` `AI辅助创作` `ShotBench` `ShotQA`

## 📋 核心要点

1. 现有的视觉-语言模型在理解电影语言方面存在显著不足，尤其是在细粒度视觉线索和空间推理上表现不佳。
2. 论文提出了ShotBench基准和ShotQA数据集，以系统性地评估和提升模型在电影语言理解中的能力。
3. 实验结果显示，开发的ShotVL模型在ShotBench上显著超越所有现有模型，建立了新的性能标杆。

## 📝 摘要（中文）

电影摄影是电影的基本视觉语言，对于传达叙事、情感和美学质量至关重要。尽管近期的视觉-语言模型（VLMs）在一般视觉理解上表现出色，但它们在理解个别镜头中蕴含的细腻电影语法方面仍然缺乏探索和评估。这一关键缺口限制了细粒度视觉理解和AI辅助视频生成的精确性。为此，我们提出了ShotBench，这是一个专门设计用于电影语言理解的综合基准，包含3500多个专家注释的问答对，涵盖200多部著名电影的八个关键电影摄影维度。我们的评估显示，24个领先的VLM在ShotBench上的表现存在显著局限，尤其在细粒度视觉线索和复杂空间推理方面。为推动该领域的发展，我们构建了ShotQA，一个包含约7万个电影问答对的大规模多模态数据集，并通过监督微调和组相对策略优化开发了ShotVL，显著超越现有模型，建立了新的最先进性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有视觉-语言模型在电影语言理解方面的不足，尤其是对细粒度视觉线索和复杂空间推理的理解能力不足。

**核心思路**：通过构建ShotBench基准和ShotQA数据集，提供系统的评估机制和丰富的数据支持，以推动模型在电影语言理解上的进步。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要模块。数据集包含专家注释的问答对，模型通过监督微调和策略优化进行训练。

**关键创新**：最重要的创新在于ShotBench基准的提出和ShotQA数据集的构建，这为电影语言理解提供了新的评估标准和数据支持，填补了现有研究的空白。

**关键设计**：在模型训练中，采用了组相对策略优化方法，并对网络结构进行了优化，以提升模型在复杂场景下的表现。

## 📊 实验亮点

在实验中，开发的ShotVL模型在ShotBench基准上表现优异，超越所有现有开源和专有模型，达到了新的最先进性能，具体表现为平均准确率超过60%，显著提升了对细粒度视觉线索的理解能力。

## 🎯 应用场景

该研究的潜在应用领域包括电影制作、视频编辑和AI辅助创作等。通过提升模型对电影语言的理解能力，可以为创作者提供更智能的工具，帮助他们在叙事和情感表达上实现更高的艺术效果，推动影视行业的创新发展。

## 📄 摘要（原文）

> Cinematography, the fundamental visual language of film, is essential for conveying narrative, emotion, and aesthetic quality. While recent Vision-Language Models (VLMs) demonstrate strong general visual understanding, their proficiency in comprehending the nuanced cinematic grammar embedded within individual shots remains largely unexplored and lacks robust evaluation. This critical gap limits both fine-grained visual comprehension and the precision of AI-assisted video generation. To address this, we introduce ShotBench, a comprehensive benchmark specifically designed for cinematic language understanding. It features over 3.5k expert-annotated QA pairs from images and video clips, meticulously curated from over 200 acclaimed (predominantly Oscar-nominated) films and spanning eight key cinematography dimensions. Our evaluation of 24 leading VLMs on ShotBench reveals their substantial limitations: even the top-performing model achieves less than 60% average accuracy, particularly struggling with fine-grained visual cues and complex spatial reasoning. To catalyze advancement in this domain, we construct ShotQA, a large-scale multimodal dataset comprising approximately 70k cinematic QA pairs. Leveraging ShotQA, we develop ShotVL through supervised fine-tuning and Group Relative Policy Optimization. ShotVL significantly outperforms all existing open-source and proprietary models on ShotBench, establishing new state-of-the-art performance. We open-source our models, data, and code to foster rapid progress in this crucial area of AI-driven cinematic understanding and generation.

