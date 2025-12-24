---
layout: default
title: "Color Me Correctly: Bridging Perceptual Color Spaces and Text Embeddings for Improved Diffusion Generation"
---

# Color Me Correctly: Bridging Perceptual Color Spaces and Text Embeddings for Improved Diffusion Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10058" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10058v1</a>
  <a href="https://arxiv.org/pdf/2509.10058.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10058v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10058v1', 'Color Me Correctly: Bridging Perceptual Color Spaces and Text Embeddings for Improved Diffusion Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sung-Lin Tsai, Bo-Lun Huang, Yu Ting Shen, Cheng Yu Yeo, Chiang Tseng, Bo-Kai Ruan, Wen-Sheng Lien, Hong-Han Shuai

**分类**: cs.CV

**发布日期**: 2025-09-12

**备注**: Accepted to ACM Multimedia 2025 (MM '25)

**DOI**: [10.1145/3746027.3755385](https://doi.org/10.1145/3746027.3755385)

---

## 💡 一句话要点

**提出一种免训练框架，通过LLM增强文本嵌入，提升扩散模型生成图像的颜色准确性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `扩散模型` `颜色对齐` `大型语言模型` `文本嵌入` `CIELAB颜色空间` `免训练方法`

## 📋 核心要点

1. 现有文本到图像生成模型在处理复杂颜色描述时存在颜色偏差，难以准确反映用户意图。
2. 利用大型语言模型消解颜色歧义，并在文本嵌入空间中引导颜色混合，无需额外训练。
3. 实验表明，该方法显著提升了生成图像的颜色准确性，同时保持了良好的图像质量。

## 📝 摘要（中文）

本文提出了一种免训练框架，旨在提高文本到图像（T2I）生成中颜色对齐的准确性。现有的扩散模型在处理细微和复合颜色术语（如蒂芙尼蓝、石灰绿、亮粉色）时存在困难，导致生成的图像与人类意图不符。为了精确渲染提示中的颜色，该方法利用大型语言模型（LLM）消除颜色相关提示的歧义，并直接在文本嵌入空间中引导颜色混合操作。该方法首先使用LLM解析文本提示中模糊的颜色术语，然后基于CIELAB颜色空间中颜色术语的空间关系来细化文本嵌入。实验结果表明，该框架在不影响图像质量的前提下，提高了颜色对齐的准确性，弥合了文本语义和视觉生成之间的差距。

## 🔬 方法详解

**问题定义**：文本到图像生成模型在处理包含复杂颜色描述的文本提示时，经常无法准确地生成符合要求的颜色。例如，“Tiffany blue”或“lime green”等复合颜色词汇，模型容易产生偏差，导致生成的图像颜色与用户期望不符。现有方法如交叉注意力操作、参考图像或微调等，无法系统性地解决这种颜色歧义问题。

**核心思路**：该论文的核心思路是利用大型语言模型（LLM）的语义理解能力，对文本提示中的颜色描述进行消歧，并将消歧后的颜色信息融入到文本嵌入中，从而引导扩散模型生成更准确的颜色。通过在文本嵌入空间中进行颜色混合操作，可以更精细地控制生成图像的颜色。

**技术框架**：该框架主要包含两个阶段：1) 颜色歧义消解阶段：使用LLM解析文本提示，识别并消除颜色描述中的歧义。例如，将“Tiffany blue”解析为更具体的颜色信息。2) 文本嵌入增强阶段：基于CIELAB颜色空间中颜色术语的空间关系，对文本嵌入进行细化。具体来说，根据颜色之间的相似性和差异性，调整文本嵌入向量，从而更好地表达颜色信息。

**关键创新**：该方法最重要的创新点在于提出了一种免训练的颜色增强框架，无需额外的训练数据或外部参考图像。通过利用LLM的语义理解能力和CIELAB颜色空间的颜色关系，可以直接在文本嵌入空间中进行颜色调整，从而提高生成图像的颜色准确性。与现有方法相比，该方法更加灵活和高效。

**关键设计**：该方法的关键设计包括：1) 使用LLM进行颜色歧义消解的具体prompt工程；2) 如何将LLM的输出信息有效地融入到文本嵌入中；3) 如何利用CIELAB颜色空间中的颜色关系来指导文本嵌入的调整。论文中可能涉及一些超参数的设置，例如LLM的选择、文本嵌入调整的权重等，但具体细节未知。

## 📊 实验亮点

该框架在不进行额外训练的情况下，显著提高了文本到图像生成中颜色对齐的准确性。实验结果表明，该方法能够有效地处理复杂的颜色描述，并生成符合用户期望的图像。具体的性能数据和对比基线未知，但摘要强调了在不影响图像质量的前提下，提升了颜色准确性。

## 🎯 应用场景

该研究成果可广泛应用于需要精确颜色控制的文本到图像生成任务中，例如时尚设计、产品可视化、室内设计等领域。通过提高颜色准确性，可以提升用户体验，并为创意设计提供更强大的工具。未来，该方法还可以扩展到其他属性的控制，例如材质、纹理等，从而实现更精细的图像生成。

## 📄 摘要（原文）

> Accurate color alignment in text-to-image (T2I) generation is critical for applications such as fashion, product visualization, and interior design, yet current diffusion models struggle with nuanced and compound color terms (e.g., Tiffany blue, lime green, hot pink), often producing images that are misaligned with human intent. Existing approaches rely on cross-attention manipulation, reference images, or fine-tuning but fail to systematically resolve ambiguous color descriptions. To precisely render colors under prompt ambiguity, we propose a training-free framework that enhances color fidelity by leveraging a large language model (LLM) to disambiguate color-related prompts and guiding color blending operations directly in the text embedding space. Our method first employs a large language model (LLM) to resolve ambiguous color terms in the text prompt, and then refines the text embeddings based on the spatial relationships of the resulting color terms in the CIELAB color space. Unlike prior methods, our approach improves color accuracy without requiring additional training or external reference images. Experimental results demonstrate that our framework improves color alignment without compromising image quality, bridging the gap between text semantics and visual generation.

