---
layout: default
title: LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction
---

# LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14594" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14594</a>
  <a href="https://arxiv.org/pdf/2512.14594.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14594" onclick="toggleFavorite(this, '2512.14594', 'LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyu Zhao, Yingxue Xu, Fengtao Zhou, Yihui Wang, Hao Chen

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出KEMM模型，利用LLM增强知识的多模态癌症生存预测。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `癌症生存预测` `大型语言模型` `知识增强` `跨模态注意力`

## 📋 核心要点

1. 现有方法难以从高维冗余的病理图像和基因组数据中提取判别性特征，且缺乏有效的模态对齐手段。
2. KEMM模型利用LLM处理专家报告和生成预后背景知识，增强模型对生存预测相关特征的关注。
3. 实验结果表明，KEMM在五个数据集上实现了最先进的性能，验证了知识增强方法的有效性。

## 📝 摘要（中文）

当前的多模态生存预测方法通常依赖于病理图像（WSIs）和基因组数据，这些数据维度高且冗余，难以从中提取判别性特征并对齐不同模态。此外，使用简单的生存随访标签不足以监督如此复杂的任务。为了解决这些挑战，我们提出了一种基于LLM驱动的知识增强多模态模型KEMM，用于癌症生存预测，该模型集成了专家报告和预后背景知识。专家报告由病理学家逐个案例提供，并由大型语言模型（LLM）提炼，提供了简洁且以临床为中心的诊断声明，这些信息通常暗示不同的生存结果。预后背景知识（PBK）由LLM简洁地生成，提供了关于不同癌症类型的有价值的预后背景知识，这也增强了生存预测。为了利用这些知识，我们引入了知识增强的跨模态（KECM）注意力模块。KECM可以有效地引导网络关注来自高度冗余模态的判别性和生存相关的特征。在五个数据集上的大量实验表明，KEMM实现了最先进的性能。代码将在接受后发布。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态癌症生存预测中，病理图像和基因组数据维度高、冗余度大，以及缺乏有效利用临床知识的问题。现有方法难以从这些数据中提取判别性特征，并且简单的生存随访标签不足以充分监督模型的训练。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）处理和提炼临床知识，包括专家报告和预后背景知识，并将这些知识融入到多模态融合的过程中，从而引导模型关注与生存预测相关的关键特征。

**技术框架**：KEMM模型主要包含以下几个模块：1) LLM驱动的知识提取模块，用于从专家报告中提取诊断信息，并生成预后背景知识；2) 特征提取模块，用于从病理图像和基因组数据中提取特征；3) 知识增强的跨模态（KECM）注意力模块，用于融合不同模态的特征，并利用提取的知识引导模型关注关键特征；4) 生存预测模块，用于预测患者的生存概率。

**关键创新**：论文的关键创新在于引入了LLM来处理和生成临床知识，并设计了知识增强的跨模态注意力模块（KECM）。KECM能够有效地将外部知识融入到多模态特征融合的过程中，从而提高模型的预测性能。与现有方法相比，KEMM能够更好地利用临床知识，并更有效地提取和融合不同模态的特征。

**关键设计**：KECM模块的设计是关键。具体来说，KECM利用LLM生成的知识作为query，去attention病理图像和基因组数据的特征，从而突出与生存预测相关的特征。损失函数方面，使用了标准的生存分析损失函数，例如Cox比例风险损失函数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14594/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14594/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

KEMM模型在五个癌症数据集上进行了广泛的实验，结果表明KEMM显著优于现有的多模态生存预测方法。具体性能提升数据在论文中给出，证明了KEMM模型在癌症生存预测任务上的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于临床辅助诊断，帮助医生更准确地预测癌症患者的生存概率，从而制定更个性化的治疗方案。此外，该方法也可以推广到其他多模态医学数据分析任务中，例如疾病诊断、预后评估等，具有广阔的应用前景。

## 📄 摘要（原文）

> Current multimodal survival prediction methods typically rely on pathology images (WSIs) and genomic data, both of which are high-dimensional and redundant, making it difficult to extract discriminative features from them and align different modalities. Moreover, using a simple survival follow-up label is insufficient to supervise such a complex task. To address these challenges, we propose KEMM, an LLM-driven Knowledge-Enhanced Multimodal Model for cancer survival prediction, which integrates expert reports and prognostic background knowledge. 1) Expert reports, provided by pathologists on a case-by-case basis and refined by large language model (LLM), offer succinct and clinically focused diagnostic statements. This information may typically suggest different survival outcomes. 2) Prognostic background knowledge (PBK), generated concisely by LLM, provides valuable prognostic background knowledge on different cancer types, which also enhances survival prediction. To leverage these knowledge, we introduce the knowledge-enhanced cross-modal (KECM) attention module. KECM can effectively guide the network to focus on discriminative and survival-relevant features from highly redundant modalities. Extensive experiments on five datasets demonstrate that KEMM achieves state-of-the-art performance. The code will be released upon acceptance.

