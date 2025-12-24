---
layout: default
title: "TIT-Score: Evaluating Long-Prompt Based Text-to-Image Alignment via Text-to-Image-to-Text Consistency"
---

# TIT-Score: Evaluating Long-Prompt Based Text-to-Image Alignment via Text-to-Image-to-Text Consistency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02987" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02987v1</a>
  <a href="https://arxiv.org/pdf/2510.02987.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02987v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02987v1', 'TIT-Score: Evaluating Long-Prompt Based Text-to-Image Alignment via Text-to-Image-to-Text Consistency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juntong Wang, Huiyu Duan, Jiarui Wang, Ziheng Jia, Guangtao Zhai, Xiongkuo Min

**分类**: cs.CV

**发布日期**: 2025-10-03

---

## 💡 一句话要点

**提出TIT-Score，通过文本-图像-文本一致性评估长文本提示下的文图对齐质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `长文本提示` `图像评估` `文本-图像-文本一致性` `零样本评估`

## 📋 核心要点

1. 现有文图模型在长文本提示下生成图像时，难以保证图像内容与提示信息的高度一致性，面临对齐挑战。
2. 提出TIT-Score，通过比较原始文本提示与模型生成的图像描述之间的一致性，来评估文图对齐程度。
3. 实验表明，TIT-Score与人类判断具有更高的一致性，在文图对齐评估方面优于现有方法，提升显著。

## 📝 摘要（中文）

随着大型多模态模型(LMMs)的快速发展，现有的文本到图像(T2I)模型能够生成高质量的图像，并在短文本提示下表现出良好的对齐效果。然而，这些模型在理解和遵循长而详细的提示方面仍然存在困难，导致生成结果不一致。为了解决这个问题，我们引入了LPG-Bench，这是一个用于评估基于长文本提示的文本到图像生成效果的综合基准。LPG-Bench包含200个精心设计的提示，平均长度超过250个单词，接近于一些领先商业模型的输入容量。我们使用这些提示从13个最先进的模型中生成了2600张图像，并进行了全面的人工排序标注。基于LPG-Bench，我们观察到，最先进的T2I对齐评估指标在基于长文本提示的图像生成方面与人类偏好的一致性较差。为了弥补这一差距，我们提出了一种基于文本到图像到文本一致性的新型零样本指标，称为TIT，用于评估长文本提示生成的图像。TIT的核心概念是通过直接比较原始提示和LMM生成的图像描述之间的一致性来量化T2I对齐，包括一个高效的基于分数的实例TIT-Score和一个基于大型语言模型(LLM)的实例TIT-Score-LLM。大量的实验表明，与CLIP-score、LMM-score等相比，我们的框架与人类判断实现了更好的对齐，其中TIT-Score-LLM在成对准确率方面比最强的基线提高了7.31%。LPG-Bench和TIT方法共同为基准测试和促进T2I模型的发展提供了更深层次的视角。所有资源都将公开。

## 🔬 方法详解

**问题定义**：现有文本到图像（T2I）模型在处理长文本提示时，生成的图像往往不能很好地反映提示中的所有细节，导致图像与文本描述不一致。现有的评估指标，如CLIP-score等，在长文本提示下与人类的感知一致性较差，无法准确评估T2I模型的性能。

**核心思路**：论文的核心思路是利用文本-图像-文本（T2I2T）的一致性来评估T2I模型的对齐程度。具体来说，首先使用T2I模型生成图像，然后使用大型语言模型（LLM）对生成的图像进行描述，最后比较原始文本提示和LLM生成的图像描述之间的一致性。如果T2I模型生成的图像能够准确反映原始文本提示的内容，那么LLM生成的图像描述应该与原始文本提示非常相似。

**技术框架**：TIT框架主要包含以下几个步骤：
1.  **图像生成**：使用待评估的T2I模型，根据给定的长文本提示生成图像。
2.  **图像描述**：使用大型语言模型（LLM），例如BLIP-2，对生成的图像进行描述，得到图像的文本描述。
3.  **一致性评估**：比较原始文本提示和LLM生成的图像描述之间的一致性，得到TIT-Score。论文提出了两种计算一致性的方法：TIT-Score（基于预训练模型打分）和TIT-Score-LLM（基于LLM直接比较）。

**关键创新**：TIT方法的关键创新在于利用了T2I2T的一致性来评估T2I模型的对齐程度。与传统的评估指标相比，TIT方法能够更好地反映人类的感知，并且不需要人工标注数据，是一种零样本的评估方法。此外，TIT方法可以有效地评估T2I模型在长文本提示下的性能，弥补了现有评估指标的不足。

**关键设计**：
*   **TIT-Score**：使用预训练的文本相似度模型（例如Sentence-BERT）计算原始文本提示和LLM生成的图像描述之间的相似度得分，作为TIT-Score。
*   **TIT-Score-LLM**：使用大型语言模型（例如GPT-4）直接比较原始文本提示和LLM生成的图像描述，判断两者是否一致，并给出一致性得分。
*   **LPG-Bench**：构建了一个包含200个长文本提示的基准数据集，用于评估T2I模型在长文本提示下的性能。每个提示的平均长度超过250个单词。

## 📊 实验亮点

实验结果表明，TIT-Score与人类判断具有更高的一致性，显著优于现有的评估指标，如CLIP-score和LMM-score。具体来说，TIT-Score-LLM在成对准确率方面比最强的基线提高了7.31%。LPG-Bench数据集和TIT评估方法为长文本提示下的文图生成提供了一个更可靠的评估框架。

## 🎯 应用场景

TIT-Score可用于评估和改进文本到图像生成模型，尤其是在需要处理复杂和详细描述的场景中，例如艺术创作、产品设计、游戏开发和虚拟现实等领域。通过更准确地评估模型在长文本提示下的生成质量，可以促进T2I模型更好地理解和遵循用户的意图，从而生成更符合用户需求的图像。

## 📄 摘要（原文）

> With the rapid advancement of large multimodal models (LMMs), recent text-to-image (T2I) models can generate high-quality images and demonstrate great alignment to short prompts. However, they still struggle to effectively understand and follow long and detailed prompts, displaying inconsistent generation. To address this challenge, we introduce LPG-Bench, a comprehensive benchmark for evaluating long-prompt-based text-to-image generation. LPG-Bench features 200 meticulously crafted prompts with an average length of over 250 words, approaching the input capacity of several leading commercial models. Using these prompts, we generate 2,600 images from 13 state-of-the-art models and further perform comprehensive human-ranked annotations. Based on LPG-Bench, we observe that state-of-the-art T2I alignment evaluation metrics exhibit poor consistency with human preferences on long-prompt-based image generation. To address the gap, we introduce a novel zero-shot metric based on text-to-image-to-text consistency, termed TIT, for evaluating long-prompt-generated images. The core concept of TIT is to quantify T2I alignment by directly comparing the consistency between the raw prompt and the LMM-produced description on the generated image, which includes an efficient score-based instantiation TIT-Score and a large-language-model (LLM) based instantiation TIT-Score-LLM. Extensive experiments demonstrate that our framework achieves superior alignment with human judgment compared to CLIP-score, LMM-score, etc., with TIT-Score-LLM attaining a 7.31% absolute improvement in pairwise accuracy over the strongest baseline. LPG-Bench and TIT methods together offer a deeper perspective to benchmark and foster the development of T2I models. All resources will be made publicly available.

