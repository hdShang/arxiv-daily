---
layout: default
title: Enhancing Geo-localization for Crowdsourced Flood Imagery via LLM-Guided Attention
---

# Enhancing Geo-localization for Crowdsourced Flood Imagery via LLM-Guided Attention

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11811" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11811</a>
  <a href="https://arxiv.org/pdf/2512.11811.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11811" onclick="toggleFavorite(this, '2512.11811', 'Enhancing Geo-localization for Crowdsourced Flood Imagery via LLM-Guided Attention')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fengyi Xu, Jun Ma, Waishan Qiu, Cui Guo, Jack C.P. Cheng

**分类**: cs.CL, cs.AI, cs.CV, cs.CY

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出VPR-AttLLM，利用LLM增强视觉定位，提升众包洪水图像地理定位精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉定位` `地理定位` `大型语言模型` `注意力机制` `多模态融合` `众包图像` `城市感知`

## 📋 核心要点

1. 现有视觉定位模型在处理众包图像时，因视觉扭曲和跨域差异导致性能显著下降。
2. VPR-AttLLM利用LLM的语义知识，通过注意力机制增强VPR模型的描述符，无需重新训练。
3. 实验表明，VPR-AttLLM在多个数据集上提升了召回率，尤其在真实洪水图像上提升高达8%。

## 📝 摘要（中文）

本文提出VPR-AttLLM，一个模型无关的框架，通过注意力引导的描述符增强，将大型语言模型(LLM)的语义推理和地理知识集成到现有的视觉定位(VPR)流程中。通过利用LLM识别城市环境中具有位置信息的区域并抑制视觉噪声，VPR-AttLLM在不需要模型重新训练或额外数据的情况下提高了检索性能。在扩展的基准测试中进行了全面的评估，包括用真实社交媒体洪水图像丰富的SF-XL，建立的查询集上的合成洪水场景和Mapillary照片，以及一个新的捕捉形态各异的城市景观的HK-URBAN数据集。将VPR-AttLLM与三个最先进的VPR模型（CosPlace、EigenPlaces和SALAD）集成，始终如一地提高了召回性能，相对增益通常在1-3%之间，在最具挑战性的真实洪水图像上达到8%。除了可衡量的检索准确性提升之外，本研究还建立了一个通用的范例，用于视觉检索系统中LLM引导的多模态融合。通过将城市感知理论的原则嵌入到注意力机制中，VPR-AttLLM将类人空间推理与现代VPR架构联系起来。其即插即用设计、强大的跨源鲁棒性和可解释性突出了其在可扩展的城市监测和众包危机图像快速地理定位方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决众包街景图像地理定位不准确的问题，尤其是在城市洪水等危机事件中。现有视觉定位（VPR）模型在处理此类图像时，由于图像质量差、视角变化大以及与训练数据存在领域差异，导致定位精度显著下降。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的语义理解能力和地理知识，引导VPR模型关注图像中与位置信息相关的区域，并抑制噪声干扰。通过LLM的辅助，VPR模型可以更有效地提取图像的地理特征，从而提高定位精度。

**技术框架**：VPR-AttLLM框架主要包含以下几个模块：1) 图像输入：输入待定位的众包图像。2) VPR模型：使用现有的VPR模型（如CosPlace、EigenPlaces、SALAD）提取图像的全局特征。3) LLM：利用LLM分析图像内容，识别图像中具有位置信息的区域，并生成注意力权重。4) 注意力机制：将LLM生成的注意力权重应用于VPR模型的特征图，增强关键区域的特征，抑制噪声区域的特征。5) 地理位置检索：使用增强后的特征进行地理位置检索，得到最终的定位结果。

**关键创新**：该方法最重要的创新点在于将LLM的语义理解能力与VPR模型的视觉特征提取能力相结合，通过注意力机制实现多模态融合。与传统的VPR方法相比，VPR-AttLLM能够更好地利用图像中的语义信息，提高对跨域和噪声图像的鲁棒性。

**关键设计**：LLM部分的关键设计在于如何有效地提取图像中的位置信息。论文采用了一种基于提示学习的方法，通过设计合适的提示语，引导LLM识别图像中的地标、建筑物等具有位置信息的元素。注意力机制的设计也至关重要，需要保证LLM生成的注意力权重能够准确地反映图像中各个区域的重要性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.11811/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.11811/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.11811/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

VPR-AttLLM在多个数据集上进行了评估，包括SF-XL、合成洪水数据集和HK-URBAN。实验结果表明，VPR-AttLLM与CosPlace、EigenPlaces和SALAD等先进VPR模型集成后，召回率均得到显著提升，在最具挑战性的真实洪水图像上，召回率提升高达8%。这表明VPR-AttLLM具有很强的泛化能力和鲁棒性。

## 🎯 应用场景

该研究成果可应用于城市应急响应、灾害监测、城市规划等领域。通过快速准确地定位众包图像，可以帮助救援人员快速了解灾情，制定合理的救援方案。此外，该技术还可以用于城市环境监测、交通流量分析等方面，为智慧城市建设提供支持。

## 📄 摘要（原文）

> Crowdsourced street-view imagery from social media provides real-time visual evidence of urban flooding and other crisis events, yet it often lacks reliable geographic metadata for emergency response. Existing image geo-localization approaches, also known as Visual Place Recognition (VPR) models, exhibit substantial performance degradation when applied to such imagery due to visual distortions and domain shifts in cross-source scenarios. This paper presents VPR-AttLLM, a model-agnostic framework that integrates the semantic reasoning and geo-knowledge of Large Language Models (LLMs) into established VPR pipelines through attention-guided descriptor enhancement. By leveraging LLMs to identify location-informative regions within the city context and suppress visual noise, VPR-AttLLM improves retrieval performance without requiring model retraining or additional data. Comprehensive evaluations are conducted on extended benchmarks including SF-XL enriched with real social-media flood images, synthetic flooding scenarios over established query sets and Mapillary photos, and a new HK-URBAN dataset capturing morphologically distinct cityscapes. Integrating VPR-AttLLM with three state-of-the-art VPR models-CosPlace, EigenPlaces, and SALAD-consistently improves recall performance, yielding relative gains typically between 1-3% and reaching up to 8% on the most challenging real flood imagery. Beyond measurable gains in retrieval accuracy, this study establishes a generalizable paradigm for LLM-guided multimodal fusion in visual retrieval systems. By embedding principles from urban perception theory into attention mechanisms, VPR-AttLLM bridges human-like spatial reasoning with modern VPR architectures. Its plug-and-play design, strong cross-source robustness, and interpretability highlight its potential for scalable urban monitoring and rapid geo-localization of crowdsourced crisis imagery.

