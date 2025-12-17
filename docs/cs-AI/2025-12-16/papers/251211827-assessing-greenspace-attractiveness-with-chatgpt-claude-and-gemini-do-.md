---
layout: default
title: Assessing Greenspace Attractiveness with ChatGPT, Claude, and Gemini: Do AI Models Reflect Human Perceptions?
---

# Assessing Greenspace Attractiveness with ChatGPT, Claude, and Gemini: Do AI Models Reflect Human Perceptions?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11827" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11827</a>
  <a href="https://arxiv.org/pdf/2512.11827.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11827" onclick="toggleFavorite(this, '2512.11827', 'Assessing Greenspace Attractiveness with ChatGPT, Claude, and Gemini: Do AI Models Reflect Human Perceptions?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Milad Malekzadeh, Magdalena Biernacka, Elias Willberg, Jussi Torkko, Edyta Łaszkiewicz, Tuuli Toivonen

**分类**: cs.CY, cs.AI, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**利用多模态大语言模型评估绿地吸引力，对比AI与人类感知差异**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `绿地吸引力评估` `多模态大语言模型` `城市规划` `街景图像分析` `人类感知` `AI对齐` `非正式绿地` `主观评价`

## 📋 核心要点

1. 现有绿地评估方法忽略非正式空间，且难以大规模捕捉主观感知，限制了城市环境设计的包容性。
2. 本研究利用多模态大语言模型分析街景图像，评估绿地吸引力，并与人类感知进行对比分析。
3. 实验表明，AI在评估正式绿地和非正式空间上与人类有较高一致性，但在其他类型绿地上存在差异，强调了人工监督的必要性。

## 📝 摘要（中文）

理解绿地吸引力对于设计宜居和包容的城市环境至关重要。然而，现有的评估方法通常忽略非正式或瞬时空间，并且在捕捉大规模主观感知方面资源消耗过大。本研究探讨了多模态大语言模型（MLLM），包括ChatGPT GPT-4o、Claude 3.5 Haiku和Gemini 2.0 Flash，使用谷歌街景图像评估绿地吸引力的能力，并与人类感知进行对比。我们将模型输出与波兰罗兹居民的地理问卷调查结果进行了比较，涵盖正式（如公园和管理的绿地）和非正式（如草地和荒地）绿地。调查受访者和模型都表明了每个绿地是否具有吸引力，并提供了最多三个自由文本解释。分析考察了他们的吸引力判断一致的频率，并在将解释分类为共享推理类别后比较了它们的解释。结果表明，对于有吸引力的正式绿地和没有吸引力的非正式空间，AI与人类的协议度很高，但对于有吸引力的非正式和没有吸引力的正式绿地，一致性较低。模型始终强调美学和设计导向的特征，低估了安全、功能基础设施和调查受访者重视的本地嵌入式品质。虽然这些发现突出了可扩展预评估的潜力，但它们也强调了人工监督和补充参与式方法的必要性。我们得出结论，MLLM可以支持规划实践中对环境敏感的绿地评估，但不能取代它。

## 🔬 方法详解

**问题定义**：论文旨在解决如何更高效、更全面地评估城市绿地吸引力的问题。现有方法主要依赖于人工调查或专家评估，存在成本高、覆盖范围有限以及难以捕捉主观感知等痛点。特别是对于非正式绿地（如荒地、草地），传统方法往往难以有效评估其吸引力。

**核心思路**：论文的核心思路是利用多模态大语言模型（MLLM）的图像理解和文本生成能力，通过分析谷歌街景图像来自动评估绿地的吸引力。通过将模型评估结果与人类调查结果进行对比，分析AI模型在多大程度上能够反映人类对绿地吸引力的感知，并识别模型评估的偏差。

**技术框架**：整体框架包括以下几个主要阶段：1) 数据收集：收集波兰罗兹市的谷歌街景图像，并进行地理编码；2) 人类调查：通过地理问卷调查收集当地居民对绿地吸引力的主观评价和解释；3) 模型评估：使用ChatGPT GPT-4o、Claude 3.5 Haiku和Gemini 2.0 Flash等MLLM模型，基于街景图像评估绿地的吸引力，并生成解释文本；4) 结果对比分析：比较模型和人类的吸引力判断，以及解释文本的语义内容，分析一致性和差异性。

**关键创新**：本研究的关键创新在于将多模态大语言模型应用于城市绿地吸引力评估，探索了AI模型在理解和模拟人类主观感知方面的潜力。与传统方法相比，该方法具有自动化、可扩展性强的优势，可以为城市规划和设计提供更高效的决策支持。

**关键设计**：研究中，关键设计包括：1) 绿地类型的划分：区分正式绿地（如公园）和非正式绿地（如荒地），以便更细致地分析模型在不同类型绿地上的表现；2) 解释文本的分类：将模型和人类生成的解释文本进行分类，提取共同的推理类别，以便更深入地理解模型和人类的判断逻辑；3) 模型选择：选择了多种主流的MLLM模型进行对比，以评估不同模型在绿地吸引力评估任务上的性能。

## 📊 实验亮点

实验结果表明，对于吸引人的正式绿地和不吸引人的非正式空间，AI模型与人类的判断高度一致。然而，对于吸引人的非正式绿地和不吸引人的正式绿地，一致性较低。模型更倾向于强调美学和设计导向的特征，而忽略了安全、功能基础设施和本地嵌入式品质等因素。这表明AI模型在绿地吸引力评估方面具有潜力，但也需要人工监督和补充参与式方法。

## 🎯 应用场景

该研究成果可应用于城市规划、景观设计、公共健康等领域。通过AI自动评估绿地吸引力，可以帮助规划者更高效地识别和改善城市中的绿地资源，提升居民的生活质量和幸福感。此外，该方法还可以扩展到其他城市环境要素的评估，例如建筑风格、街道景观等，为城市精细化管理提供技术支持。

## 📄 摘要（原文）

> Understanding greenspace attractiveness is essential for designing livable and inclusive urban environments, yet existing assessment approaches often overlook informal or transient spaces and remain too resource intensive to capture subjective perceptions at scale. This study examines the ability of multimodal large language models (MLLMs), ChatGPT GPT-4o, Claude 3.5 Haiku, and Gemini 2.0 Flash, to assess greenspace attractiveness similarly to humans using Google Street View imagery. We compared model outputs with responses from a geo-questionnaire of residents in Lodz, Poland, across both formal (for example, parks and managed greenspaces) and informal (for example, meadows and wastelands) greenspaces. Survey respondents and models indicated whether each greenspace was attractive or unattractive and provided up to three free text explanations. Analyses examined how often their attractiveness judgments aligned and compared their explanations after classifying them into shared reasoning categories. Results show high AI human agreement for attractive formal greenspaces and unattractive informal spaces, but low alignment for attractive informal and unattractive formal greenspaces. Models consistently emphasized aesthetic and design oriented features, underrepresenting safety, functional infrastructure, and locally embedded qualities valued by survey respondents. While these findings highlight the potential for scalable pre-assessment, they also underscore the need for human oversight and complementary participatory approaches. We conclude that MLLMs can support, but not replace, context sensitive greenspace evaluation in planning practice.

