---
layout: default
title: "$μ^2$Tokenizer: Differentiable Multi-Scale Multi-Modal Tokenizer for Radiology Report Generation"
---

# $μ^2$Tokenizer: Differentiable Multi-Scale Multi-Modal Tokenizer for Radiology Report Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00316" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00316v2</a>
  <a href="https://arxiv.org/pdf/2507.00316.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00316v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00316v2', '$μ^2$Tokenizer: Differentiable Multi-Scale Multi-Modal Tokenizer for Radiology Report Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyou Li, Pengyao Qin, Huanan Wu, Dong Nie, Arun J. Thirunavukarasu, Juntao Yu, Le Zhang

**分类**: cs.LG, cs.CL, eess.IV

**发布日期**: 2025-06-30 (更新: 2025-07-02)

**备注**: Accepted by MICCAI 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Siyou-Li/u2Tokenizer)

---

## 💡 一句话要点

**提出$μ^2$Tokenizer以解决放射学报告生成中的信息提取与评估问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `放射学报告生成` `多模态学习` `大语言模型` `信息提取` `直接偏好优化` `CT影像分析` `深度学习`

## 📋 核心要点

1. 现有的放射学报告生成方法在从影像数据中提取信息时面临复杂性和资源限制的挑战。
2. 本文提出的$μ^2$Tokenizer通过整合多模态特征，优化报告生成过程，提升生成质量。
3. 实验结果显示，$μ^2$LLM在有限数据条件下的表现优于现有方法，展示了其在RRG任务中的潜力。

## 📝 摘要（中文）

自动化放射学报告生成（RRG）旨在从临床影像（如CT扫描）中生成详细的文本报告，以提高诊断的准确性和效率。RRG面临两个主要挑战：一是从影像数据中提取相关信息的复杂性，二是客观评估模型生成报告与专家撰写报告之间差异的困难。为此，本文提出了$μ^2$LLM，利用多尺度多模态大语言模型来解决这些问题。新颖的$μ^2$Tokenizer作为中间层，整合了来自多尺度视觉标记器和文本标记器的多模态特征，通过直接偏好优化（DPO）提升报告生成质量。实验结果表明，该方法在四个大型CT影像-报告医学数据集上超越了现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决自动化放射学报告生成中的信息提取复杂性和模型生成报告与专家报告之间评估困难的问题。现有方法在处理多模态数据时常常无法有效整合信息，导致生成报告的质量不高。

**核心思路**：论文提出的$μ^2$Tokenizer通过多尺度和多模态特征的整合，利用直接偏好优化（DPO）来提升报告生成的质量。这种设计使得模型能够更好地理解和生成与影像数据相关的文本信息。

**技术框架**：整体架构包括多尺度视觉标记器和文本标记器，$μ^2$Tokenizer作为中间层进行特征整合，最后通过GREEN-RedLlama进行优化。该方法还引入了一个五阶段的LLM驱动管道，将常规CT报告转化为视觉-问答三元组和引用链接的推理叙述。

**关键创新**：最重要的技术创新在于$μ^2$Tokenizer的设计，它有效整合了多模态特征，并通过DPO优化生成过程，与传统方法相比，显著提升了生成报告的质量和一致性。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多模态特征的融合，确保生成的文本与影像数据高度相关。此外，模型的训练过程中使用了多种数据集，以增强其泛化能力。

## 📊 实验亮点

实验结果表明，$μ^2$LLM在四个大型CT影像-报告数据集上的表现优于现有方法，具体提升幅度达到XX%（具体数据未知），显示出其在有限数据条件下的强大潜力。该方法的创新设计为放射学报告生成提供了新的思路。

## 🎯 应用场景

该研究在医疗影像分析领域具有广泛的应用潜力，尤其是在自动化放射学报告生成中。通过提高报告生成的准确性和效率，能够帮助医生更快地做出诊断决策，从而改善患者的管理和治疗效果。未来，该方法还可扩展到其他医学领域的报告生成任务中。

## 📄 摘要（原文）

> Automated radiology report generation (RRG) aims to produce detailed textual reports from clinical imaging, such as computed tomography (CT) scans, to improve the accuracy and efficiency of diagnosis and provision of management advice. RRG is complicated by two key challenges: (1) inherent complexity in extracting relevant information from imaging data under resource constraints, and (2) difficulty in objectively evaluating discrepancies between model-generated and expert-written reports. To address these challenges, we propose $μ^2$LLM, a $\underline{\textbf{mu}}$ltiscale $\underline{\textbf{mu}}$ltimodal large language models for RRG tasks. The novel $μ^2$Tokenizer, as an intermediate layer, integrates multi-modal features from the multiscale visual tokenizer and the text tokenizer, then enhances report generation quality through direct preference optimization (DPO), guided by GREEN-RedLlama. Experimental results on four large CT image-report medical datasets demonstrate that our method outperforms existing approaches, highlighting the potential of our fine-tuned $μ^2$LLMs on limited data for RRG tasks. At the same time, for prompt engineering, we introduce a five-stage, LLM-driven pipeline that converts routine CT reports into paired visual-question-answer triples and citation-linked reasoning narratives, creating a scalable, high-quality supervisory corpus for explainable multimodal radiology LLM. All code, datasets, and models will be publicly available in our official repository. https://github.com/Siyou-Li/u2Tokenizer

