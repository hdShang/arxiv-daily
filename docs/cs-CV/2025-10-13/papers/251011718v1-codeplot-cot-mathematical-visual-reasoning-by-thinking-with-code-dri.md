---
layout: default
title: CodePlot-CoT: Mathematical Visual Reasoning by Thinking with Code-Driven Images
---

# CodePlot-CoT: Mathematical Visual Reasoning by Thinking with Code-Driven Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11718" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11718v1</a>
  <a href="https://arxiv.org/pdf/2510.11718.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11718v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.11718v1', 'CodePlot-CoT: Mathematical Visual Reasoning by Thinking with Code-Driven Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengqi Duan, Kaiyue Sun, Rongyao Fang, Manyuan Zhang, Yan Feng, Ying Luo, Yufang Liu, Ke Wang, Peng Pei, Xunliang Cai, Hongsheng Li, Yi Ma, Xihui Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-13

**🔗 代码/项目**: [GITHUB](https://github.com/HKU-MMLab/Math-VR-CodePlot-CoT)

---

## 💡 一句话要点

**提出CodePlot-CoT，通过代码驱动图像的思维链解决数学视觉推理难题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学推理` `视觉推理` `代码生成` `思维链` `视觉语言模型`

## 📋 核心要点

1. 现有大型语言模型和视觉语言模型在数学推理中面临瓶颈，尤其是在需要视觉辅助的问题上，如绘制辅助线或函数图像。
2. CodePlot-CoT的核心思想是利用VLM生成文本推理和可执行绘图代码，并将代码渲染成图像，形成“视觉思维”辅助解决数学问题。
3. 实验结果表明，CodePlot-CoT在Math-VR基准测试中相比基线模型取得了高达21%的性能提升，验证了代码驱动推理的有效性。

## 📝 摘要（中文）

本文提出CodePlot-CoT，一种用于数学“图像思维”的代码驱动思维链范式。该方法利用视觉语言模型（VLM）生成文本推理和可执行的绘图代码，并将代码渲染成图像作为“视觉思维”，从而解决数学问题。为此，构建了首个大规模双语数学视觉推理数据集和基准Math-VR，包含17.8万个样本。开发了最先进的图像到代码转换器，专门用于将复杂的数学图形解析为代码，以创建高质量的训练数据。最后，使用这些数据训练CodePlot-CoT模型来解决数学问题。实验结果表明，该模型在新基准测试中比基线模型提高了高达21%，充分验证了所提出的代码驱动推理范式的有效性。该工作为多模态数学推理开辟了新方向，并为社区提供了首个大规模数据集、综合基准和强大的方法。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLMs）和视觉语言模型（VLMs）在解决需要视觉辅助的数学问题时存在困难。这些问题通常需要绘制辅助线或函数图像才能解决，而现有的模型要么只能进行文本推理，要么缺乏生成精确可控图像的能力。因此，如何让模型能够像人类一样，通过“图像思维”来解决数学问题是一个挑战。

**核心思路**：CodePlot-CoT的核心思路是利用代码作为桥梁，将文本推理和图像生成结合起来。模型首先生成文本形式的推理步骤，然后生成可执行的绘图代码，最后将代码渲染成图像，作为视觉辅助信息。这种方法允许模型在推理过程中利用视觉信息，从而更好地解决需要视觉辅助的数学问题。

**技术框架**：CodePlot-CoT的整体框架包含以下几个主要模块：1) VLM：用于生成文本推理和绘图代码；2) 代码执行器：用于执行绘图代码，生成图像；3) Math-VR数据集：用于训练和评估模型；4) 图像到代码转换器：用于将数学图形解析为代码，生成高质量的训练数据。整个流程是，给定一个数学问题，VLM生成文本推理和绘图代码，代码执行器执行代码生成图像，然后VLM结合文本推理和图像信息，最终给出答案。

**关键创新**：CodePlot-CoT的关键创新在于提出了代码驱动的思维链范式，将文本推理和图像生成结合起来，实现了“图像思维”。与现有的方法相比，CodePlot-CoT能够更精确地控制图像的生成过程，并且能够更好地利用视觉信息进行推理。此外，Math-VR数据集的构建和图像到代码转换器的开发也为该研究提供了重要的支持。

**关键设计**：CodePlot-CoT的关键设计包括：1) VLM的选择和训练：选择合适的VLM，并使用Math-VR数据集进行微调，使其能够生成高质量的文本推理和绘图代码；2) 绘图代码的格式和语法：设计一种易于执行和解析的绘图代码格式，例如使用Python的matplotlib库；3) 图像到代码转换器的设计：设计一种能够将复杂的数学图形解析为代码的转换器，例如使用深度学习模型进行图像分割和识别；4) 损失函数的设计：设计一种能够同时优化文本推理和图像生成的损失函数，例如使用交叉熵损失和图像相似度损失。

## 📊 实验亮点

CodePlot-CoT在Math-VR基准测试中取得了显著的性能提升，相比基线模型提高了高达21%。这充分验证了代码驱动推理范式的有效性。此外，该模型在不同类型的数学问题上都表现出了良好的性能，表明其具有较强的泛化能力。Math-VR数据集的发布也为多模态数学推理领域的研究提供了重要的资源。

## 🎯 应用场景

CodePlot-CoT具有广泛的应用前景，可应用于在线教育、智能辅导、数学题自动解答等领域。通过结合文本推理和图像思维，可以帮助学生更好地理解和解决数学问题。此外，该方法还可以扩展到其他需要视觉辅助的推理任务中，例如几何证明、电路分析等。

## 📄 摘要（原文）

> Recent advances in Large Language Models (LLMs) and Vision Language Models (VLMs) have shown significant progress in mathematical reasoning, yet they still face a critical bottleneck with problems requiring visual assistance, such as drawing auxiliary lines or plotting functions to solve the problems. Most LLMs and VLMs are constrained to text-only reasoning chains, while multimodal unified models that can generate interleaved text and images lack the necessary precision and controllability for such tasks. To address this, we propose CodePlot-CoT, a code-driven Chain-of-Thought paradigm for "thinking with images" in mathematics. Our approach leverages the VLM to generate text reasoning as well as executable plotting code, which is then rendered into images as "visual thought", to solve mathematical problems. To achieve this, we first construct Math-VR, the first large-scale, bilingual dataset and benchmark for Mathematics problems with Visual Reasoning, comprising 178K samples. Second, to create high-quality training data, we develop a state-of-the-art image-to-code converter specialized for parsing complex mathematical figures into codes. Finally, using these training data, we train the CodePlot-CoT model for solving mathematical problems. Experimental results show that our model achieves up to 21% increase over base model on our new benchmark, fully validating the efficacy of our proposed code-driven reasoning paradigm. Our work opens a new direction for multimodal mathematical reasoning and provides the community with the first large-scale dataset, comprehensive benchmark, and strong approach for such problems. To facilitate future research, we make our datasets, code, and pretrained models publicly available at https://github.com/HKU-MMLab/Math-VR-CodePlot-CoT.

