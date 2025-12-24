---
layout: default
title: "DeHate: A Stable Diffusion-based Multimodal Approach to Mitigate Hate Speech in Images"
---

# DeHate: A Stable Diffusion-based Multimodal Approach to Mitigate Hate Speech in Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21787" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21787v2</a>
  <a href="https://arxiv.org/pdf/2509.21787.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21787v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21787v2', 'DeHate: A Stable Diffusion-based Multimodal Approach to Mitigate Hate Speech in Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dwip Dalal, Gautam Vashishtha, Anku Rani, Aishwarya Reganti, Parth Patwa, Mohd Sarique, Chandan Gupta, Keshav Nath, Viswanatha Reddy, Vinija Jain, Aman Chadha, Amitava Das, Amit Sheth, Asif Ekbal

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-26 (更新: 2025-10-10)

**备注**: Defactify 3 workshop at AAAI 2024

---

## 💡 一句话要点

**提出基于Stable Diffusion的多模态方法DeHate，以缓解图像中的仇恨言论**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `仇恨言论检测` `多模态学习` `Stable Diffusion` `数字注意力分析` `图像处理` `视觉-语言模型` `内容审核`

## 📋 核心要点

1. 现有方法难以有效识别和消除图像中的仇恨言论，尤其是在多模态上下文中。
2. 利用Stable Diffusion生成仇恨注意力图，并结合DAAM模块精确定位并模糊图像中的仇恨区域。
3. 构建了多模态数据集，并提出了视觉-语言模型DeHater，为图像仇恨检测设定了新标准。

## 📝 摘要（中文）

有害在线内容的激增不仅扭曲了公共讨论，还对维护健康的数字环境构成了重大挑战。为了应对这一问题，我们引入了一个专门为识别数字内容中的仇恨言论而独特设计的多模态数据集。我们的方法的核心是创新性地应用了带有水印、稳定性增强的Stable Diffusion技术，并结合了数字注意力分析模块（DAAM）。这种结合有助于精确定位图像中的仇恨元素，从而生成详细的仇恨注意力图，用于模糊图像中的这些区域，从而删除图像中的仇恨部分。我们将此数据集作为dehate共享任务的一部分发布。本文还详细介绍了共享任务的细节。此外，我们还提出了DeHater，这是一种专为多模态去仇恨任务设计的视觉-语言模型。我们的方法为在文本提示下进行AI驱动的图像仇恨检测设定了新的标准，为社交媒体中更符合道德规范的AI应用程序的开发做出了贡献。

## 🔬 方法详解

**问题定义**：论文旨在解决图像中仇恨言论的自动检测与消除问题。现有方法在处理多模态数据（图像和文本提示）时，精度和效率存在不足，难以精确定位图像中的仇恨区域并进行有效处理。

**核心思路**：论文的核心思路是利用Stable Diffusion模型生成带有水印的、稳定性增强的图像，并结合数字注意力分析模块（DAAM）来精确定位图像中的仇恨元素。通过生成仇恨注意力图，可以有效地模糊或删除图像中的仇恨区域，从而达到“去仇恨”的目的。

**技术框架**：整体框架包含以下几个主要模块：1) 多模态数据集构建：构建包含图像和文本提示的数据集，用于训练和评估模型；2) Stable Diffusion模型：使用Stable Diffusion模型生成图像，并添加水印以增强模型的稳定性；3) 数字注意力分析模块（DAAM）：利用DAAM模块分析图像，生成仇恨注意力图，精确定位图像中的仇恨区域；4) 图像处理：根据仇恨注意力图，模糊或删除图像中的仇恨区域；5) 视觉-语言模型DeHater：构建视觉-语言模型DeHater，用于多模态去仇恨任务。

**关键创新**：论文的关键创新在于将Stable Diffusion模型与DAAM模块相结合，用于精确定位和消除图像中的仇恨言论。此外，论文还构建了一个多模态数据集，为相关研究提供了数据支持。

**关键设计**：论文的关键设计包括：1) 使用带有水印的Stable Diffusion模型，增强模型的稳定性；2) 利用DAAM模块生成仇恨注意力图，精确定位图像中的仇恨区域；3) 构建视觉-语言模型DeHater，用于多模态去仇恨任务。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

论文构建了一个多模态数据集，并提出了DeHater模型，该模型在图像仇恨检测任务上取得了新的进展。虽然论文中没有提供具体的性能数据和对比基线，但该方法为AI驱动的图像仇恨检测设定了新的标准，并为社交媒体中更符合道德规范的AI应用程序的开发做出了贡献。

## 🎯 应用场景

该研究成果可应用于社交媒体平台、在线论坛等，自动检测和消除图像中的仇恨言论，维护健康的数字环境。该技术还有助于提高内容审核的效率和准确性，减少人工审核的工作量，并为构建更负责任和符合道德规范的AI应用做出贡献。

## 📄 摘要（原文）

> The rise in harmful online content not only distorts public discourse but also poses significant challenges to maintaining a healthy digital environment. In response to this, we introduce a multimodal dataset uniquely crafted for identifying hate in digital content. Central to our methodology is the innovative application of watermarked, stability-enhanced, stable diffusion techniques combined with the Digital Attention Analysis Module (DAAM). This combination is instrumental in pinpointing the hateful elements within images, thereby generating detailed hate attention maps, which are used to blur these regions from the image, thereby removing the hateful sections of the image. We release this data set as a part of the dehate shared task. This paper also describes the details of the shared task. Furthermore, we present DeHater, a vision-language model designed for multimodal dehatification tasks. Our approach sets a new standard in AI-driven image hate detection given textual prompts, contributing to the development of more ethical AI applications in social media.

