---
layout: default
title: Guiding Multimodal Large Language Models with Blind and Low Vision People Visual Questions for Proactive Visual Interpretations
---

# Guiding Multimodal Large Language Models with Blind and Low Vision People Visual Questions for Proactive Visual Interpretations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01576" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01576v1</a>
  <a href="https://arxiv.org/pdf/2510.01576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01576v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01576v1', 'Guiding Multimodal Large Language Models with Blind and Low Vision People Visual Questions for Proactive Visual Interpretations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ricardo Gonzalez Penuela, Felipe Arias-Russi, Victor Capriles

**分类**: cs.CV, cs.AI, cs.HC

**发布日期**: 2025-10-02

**备注**: 7 pages, 2 figure, 2 tables, CV4A11y Workshop at ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/rgonzalezp/guiding-multimodal-large-language-models-with-blind-and-low-vision-people-visual-questions)

---

## 💡 一句话要点

**利用盲人和低视力人群视觉问题引导多模态大语言模型，实现主动视觉解读**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉解读` `盲人辅助` `低视力辅助` `上下文感知` `问题引导` `VizWiz-LF数据集`

## 📋 核心要点

1. 现有MLLM视觉解读应用为BLV用户提供信息时，缺乏针对性，产生冗余信息，效率低下。
2. 该论文提出利用历史BLV用户提问数据，引导MLLM生成更符合用户需求的上下文相关描述。
3. 实验结果表明，该方法生成的描述在预测用户需求和用户偏好方面均优于无上下文描述。

## 📝 摘要（中文）

多模态大语言模型(MLLM)因其准确性和提供丰富、类人解读的能力而被集成到视觉解读应用中，以支持盲人和低视力(BLV)用户。然而，这些应用通常默认提供全面、冗长的描述，而忽略了上下文。这导致了低效的交流，因为用户必须筛选不相关的细节，而不是接收他们可能寻求的特定信息。为了提供更具上下文相关性的信息，我们开发了一个系统，该系统利用了历史BLV用户的问题。当给定一张图像时，我们的系统从VizWiz-LF数据集中识别出相似的过去视觉上下文，并使用相关的问题来引导MLLM生成与BLV用户更相关的描述。对92个上下文感知和无上下文描述的评估显示，上下文感知描述在76.1%的情况下(92个中的70个)预测并回答了用户的问题，并且在54.4%的比较中(92个中的50个)更受欢迎。我们的论文审查和数据分析可在Github存储库https://github.com/rgonzalezp/guiding-multimodal-large-language-models-with-blind-and-low-vision-people-visual-questions 中公开获取。

## 🔬 方法详解

**问题定义**：现有面向盲人和低视力人群的视觉解读应用，在使用多模态大语言模型时，通常提供冗长且全面的描述，忽略了用户实际的需求和上下文信息。这导致用户需要花费大量时间筛选信息，效率低下。因此，需要一种方法能够让MLLM生成更具针对性和上下文相关性的描述，以满足BLV用户的特定需求。

**核心思路**：该论文的核心思路是利用历史BLV用户提出的问题来引导MLLM生成描述。通过检索与当前图像相似的视觉上下文，并提取相关的用户问题，可以有效地指导MLLM关注用户最关心的信息，从而生成更简洁、更相关的描述。这种方法的核心在于将用户的提问作为一种先验知识，融入到MLLM的视觉解读过程中。

**技术框架**：该系统主要包含以下几个模块：1. 图像输入模块：接收待解读的图像。2. 视觉上下文检索模块：在VizWiz-LF数据集中检索与输入图像相似的视觉上下文。3. 问题提取模块：从检索到的视觉上下文中提取相关的用户问题。4. MLLM引导模块：利用提取到的用户问题，引导MLLM生成描述。5. 描述输出模块：输出最终的视觉解读描述。整体流程是，给定一张图像，系统首先检索相似的视觉上下文，然后提取相关问题，最后利用这些问题引导MLLM生成更符合用户需求的描述。

**关键创新**：该论文的关键创新在于将历史BLV用户的问题作为一种引导信号，用于指导MLLM生成视觉解读描述。与传统的无上下文描述方法相比，该方法能够更好地捕捉用户的需求，生成更具针对性和上下文相关性的描述。这种方法有效地解决了现有MLLM视觉解读应用中信息冗余的问题，提高了用户获取信息的效率。

**关键设计**：论文中没有详细描述具体的参数设置、损失函数或网络结构等技术细节。但是，视觉上下文检索模块的相似度度量方式、问题提取模块的策略以及MLLM引导模块的具体实现方式（例如，如何将问题融入到MLLM的输入或训练过程中）是影响系统性能的关键设计因素。这些细节需要在实际应用中进行仔细的调整和优化。

## 📊 实验亮点

人工评估结果显示，上下文感知描述在76.1%的情况下预测并回答了用户的问题，并且在54.4%的比较中更受欢迎。这表明该方法能够有效地提高视觉解读的针对性和用户满意度。与无上下文描述相比，该方法能够更好地满足BLV用户的实际需求。

## 🎯 应用场景

该研究成果可应用于各种面向盲人和低视力人群的视觉辅助设备和应用，例如智能眼镜、手机应用等。通过提供更具针对性和上下文相关性的视觉解读，可以帮助BLV用户更好地理解周围环境，提高生活质量。此外，该方法也可以推广到其他需要个性化视觉解读的场景，例如智能客服、智能家居等。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have been integrated into visual interpretation applications to support Blind and Low Vision (BLV) users because of their accuracy and ability to provide rich, human-like interpretations. However, these applications often default to comprehensive, lengthy descriptions regardless of context. This leads to inefficient exchanges, as users must go through irrelevant details rather than receiving the specific information they are likely to seek. To deliver more contextually-relevant information, we developed a system that draws on historical BLV users questions. When given an image, our system identifies similar past visual contexts from the VizWiz-LF dataset and uses the associated questions to guide the MLLM generate descriptions more relevant to BLV users. An evaluation with three human labelers who revised 92 context-aware and context-free descriptions showed that context-aware descriptions anticipated and answered users' questions in 76.1% of cases (70 out of 92) and were preferred in 54.4% of comparisons (50 out of 92). Our paper reviews, and data analysis are publicly available in a Github repository at https://github.com/rgonzalezp/guiding-multimodal-large-language-models-with-blind-and-low-vision-people-visual-questions .

