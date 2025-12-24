---
layout: default
title: "R-GenIMA: Integrating Neuroimaging and Genetics with Interpretable Multimodal AI for Alzheimer's Disease Progression"
---

# R-GenIMA: Integrating Neuroimaging and Genetics with Interpretable Multimodal AI for Alzheimer's Disease Progression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.18986" class="toolbar-btn" target="_blank">📄 arXiv: 2512.18986v1</a>
  <a href="https://arxiv.org/pdf/2512.18986.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.18986v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.18986v1', 'R-GenIMA: Integrating Neuroimaging and Genetics with Interpretable Multimodal AI for Alzheimer\'s Disease Progression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kun Zhao, Siyuan Dai, Yingying Zhang, Guodong Liu, Pengfei Gu, Chenghua Lin, Paul M. Thompson, Alex Leow, Heng Huang, Lifang He, Liang Zhan, Haoteng Tang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**R-GenIMA：融合神经影像与遗传信息的Alzheimer病进展可解释多模态AI模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿尔茨海默病` `多模态学习` `神经影像` `遗传信息` `可解释AI` `Transformer` `ROI分析`

## 📋 核心要点

1. 现有方法难以对齐神经影像和遗传异构信号，限制了阿尔茨海默病（AD）的早期检测。
2. R-GenIMA利用ROI-wise视觉Transformer和遗传提示，将大脑区域表示为视觉token，SNP谱编码为文本，实现跨模态关联。
3. R-GenIMA在ADNI数据集上实现了四分类任务的SOTA性能，并揭示了疾病阶段特异性的大脑区域和基因特征。

## 📝 摘要（中文）

本研究提出R-GenIMA，一种可解释的多模态大语言模型，旨在整合宏观神经解剖学改变与微观遗传易感性，从而实现阿尔茨海默病（AD）的早期检测。R-GenIMA将ROI-wise视觉Transformer与遗传提示相结合，联合建模结构MRI和单核苷酸多态性（SNP）变异。该框架将每个解剖学分割的大脑区域表示为视觉token，并将SNP谱编码为结构化文本，从而实现跨模态注意力，将区域萎缩模式与潜在的遗传因素联系起来。在ADNI队列上的实验表明，R-GenIMA在正常认知（NC）、主观记忆障碍（SMC）、轻度认知障碍（MCI）和AD的四分类任务中取得了最先进的性能。此外，该模型通过识别特定阶段的大脑区域和基因特征，以及整个疾病过程中的连贯的ROI-基因关联模式，提供了生物学上有意义的解释。基于注意力的归因揭示了与已建立的GWAS支持的AD风险基因座（包括APOE、BIN1、CLU和RBFOX1）一致富集的基因。阶段解析的神经解剖学特征识别了跨疾病阶段的共享脆弱性中心，以及阶段特异性模式：主观下降中的纹状体参与，前驱期损害中的额颞叶参与，以及AD中整合的多模态网络破坏。这些结果表明，可解释的多模态AI可以综合影像和遗传学信息，揭示机制见解，为临床可部署的工具奠定基础，从而实现更早的风险分层，并为阿尔茨海默病的精准治疗策略提供信息。

## 🔬 方法详解

**问题定义**：阿尔茨海默病（AD）的早期检测需要整合宏观的神经解剖学变化和微观的遗传易感性。然而，现有的多模态方法难以有效地对齐和融合这些异构信号，导致预测精度和可解释性不足。因此，需要一种能够桥接神经影像和遗传信息的模型，以揭示AD的潜在机制。

**核心思路**：R-GenIMA的核心思路是将神经影像数据（结构MRI）和遗传数据（SNP）进行联合建模，通过跨模态注意力机制学习它们之间的关联。具体来说，将大脑区域作为视觉token，SNP谱作为结构化文本，利用Transformer架构学习区域萎缩模式与潜在遗传因素之间的关系。这种设计能够捕捉到AD进展过程中大脑结构和基因表达的复杂相互作用。

**技术框架**：R-GenIMA的整体框架包括以下几个主要模块：1) ROI-wise视觉Transformer：将结构MRI图像分割成多个感兴趣区域（ROI），并将每个ROI表示为一个视觉token。2) 遗传提示：将SNP数据编码为结构化文本，作为模型的输入。3) 跨模态注意力机制：利用Transformer架构中的自注意力机制，学习视觉token和文本提示之间的关联。4) 分类器：基于学习到的跨模态表示，对AD的不同阶段进行分类（NC, SMC, MCI, AD）。

**关键创新**：R-GenIMA的关键创新在于其可解释的多模态建模方法。通过将大脑区域表示为视觉token，SNP谱表示为文本提示，并利用跨模态注意力机制学习它们之间的关联，该模型能够提供生物学上有意义的解释。与现有方法相比，R-GenIMA不仅提高了预测精度，还能够揭示AD进展过程中大脑结构和基因表达的复杂相互作用。

**关键设计**：R-GenIMA的关键设计包括：1) ROI分割策略：选择合适的ROI分割方案，以确保每个ROI都具有生物学意义。2) 遗传提示编码：设计有效的SNP数据编码方法，以捕捉遗传变异与AD风险之间的关系。3) 注意力机制：使用多头注意力机制，以捕捉不同ROI和SNP之间的复杂关联。4) 损失函数：使用交叉熵损失函数，优化模型的分类性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18986v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18986v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18986v1/images/main_fig.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

R-GenIMA在ADNI数据集上实现了四分类任务的SOTA性能，显著优于现有方法。该模型能够识别与AD相关的关键基因（如APOE、BIN1、CLU和RBFOX1）和脑区，并揭示疾病阶段特异性的神经解剖学特征。例如，纹状体参与主观下降，额颞叶参与前驱期损害，多模态网络破坏则发生在AD阶段。

## 🎯 应用场景

R-GenIMA具有广泛的应用前景，可用于阿尔茨海默病（AD）的早期风险预测、疾病分期和精准治疗。通过整合神经影像和遗传信息，该模型可以识别高风险个体，并为他们提供个性化的干预措施。此外，R-GenIMA还可以用于药物研发，通过识别与AD相关的关键基因和脑区，为新药开发提供靶点。未来，该模型有望成为临床医生辅助诊断和治疗AD的重要工具。

## 📄 摘要（原文）

> Early detection of Alzheimer's disease (AD) requires models capable of integrating macro-scale neuroanatomical alterations with micro-scale genetic susceptibility, yet existing multimodal approaches struggle to align these heterogeneous signals. We introduce R-GenIMA, an interpretable multimodal large language model that couples a novel ROI-wise vision transformer with genetic prompting to jointly model structural MRI and single nucleotide polymorphisms (SNPs) variations. By representing each anatomically parcellated brain region as a visual token and encoding SNP profiles as structured text, the framework enables cross-modal attention that links regional atrophy patterns to underlying genetic factors. Applied to the ADNI cohort, R-GenIMA achieves state-of-the-art performance in four-way classification across normal cognition (NC), subjective memory concerns (SMC), mild cognitive impairment (MCI), and AD. Beyond predictive accuracy, the model yields biologically meaningful explanations by identifying stage-specific brain regions and gene signatures, as well as coherent ROI-Gene association patterns across the disease continuum. Attention-based attribution revealed genes consistently enriched for established GWAS-supported AD risk loci, including APOE, BIN1, CLU, and RBFOX1. Stage-resolved neuroanatomical signatures identified shared vulnerability hubs across disease stages alongside stage-specific patterns: striatal involvement in subjective decline, frontotemporal engagement during prodromal impairment, and consolidated multimodal network disruption in AD. These results demonstrate that interpretable multimodal AI can synthesize imaging and genetics to reveal mechanistic insights, providing a foundation for clinically deployable tools that enable earlier risk stratification and inform precision therapeutic strategies in Alzheimer's disease.

