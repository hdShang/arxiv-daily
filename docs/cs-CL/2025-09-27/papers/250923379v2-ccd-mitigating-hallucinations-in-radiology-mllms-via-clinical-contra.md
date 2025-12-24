---
layout: default
title: "CCD: Mitigating Hallucinations in Radiology MLLMs via Clinical Contrastive Decoding"
---

# CCD: Mitigating Hallucinations in Radiology MLLMs via Clinical Contrastive Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23379" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23379v2</a>
  <a href="https://arxiv.org/pdf/2509.23379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23379v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23379v2', 'CCD: Mitigating Hallucinations in Radiology MLLMs via Clinical Contrastive Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xi Zhang, Zaiqiao Meng, Jake Lever, Edmond S. L. Ho

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-09-27 (更新: 2025-10-17)

**备注**: Preprint, 27 pages, 3 figures

---

## 💡 一句话要点

**提出临床对比解码(CCD)框架，缓解放射学多模态大语言模型中的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `放射学报告生成` `多模态大语言模型` `临床对比解码` `医学幻觉缓解` `知识蒸馏`

## 📋 核心要点

1. 放射学多模态大语言模型易产生临床幻觉，现有方法难以保证报告的准确性和可靠性。
2. 提出临床对比解码(CCD)框架，利用专家模型的临床信号，在解码阶段提升临床保真度。
3. 实验表明，CCD在多个数据集上显著提升放射学报告生成性能，RadGraph-F1指标最高提升17%。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)通过整合视觉感知和自然语言理解，在放射学领域取得了显著进展。然而，它们经常生成临床上不支持的描述，即医学幻觉，这给需要准确性和图像依据的医疗应用带来了严重风险。实证分析表明，提示诱导的幻觉在放射学MLLM中仍然普遍存在，这主要是由于对临床部分的过度敏感。为了解决这个问题，我们引入了临床对比解码(CCD)，这是一个无需训练和检索的推理框架，它集成了来自特定任务放射学专家模型的结构化临床信号。CCD引入了一种双阶段对比机制来细化生成过程中的token级别logits，从而在不修改基础MLLM的情况下增强临床保真度。在三个数据集和多个模型上的实验表明，CCD持续提高了放射学报告生成(RRG)的整体性能。在MIMIC-CXR数据集上，当应用于最先进的RRG模型时，RadGraph-F1指标提高了高达17%。我们的方法为缓解医学幻觉提供了一种轻量级和通用的解决方案，有效地桥接了放射学领域的专家模型和MLLM。

## 🔬 方法详解

**问题定义**：放射学多模态大语言模型(MLLMs)在生成报告时，容易产生与图像不符或临床上不合理的“幻觉”，导致报告质量下降，影响临床应用。现有方法难以有效抑制这种幻觉，尤其是在对临床信息敏感的情况下，模型更容易受到提示的影响而产生错误描述。

**核心思路**：论文的核心思路是利用已有的放射学专家模型，提取结构化的临床信息，并在MLLM的解码阶段，通过对比学习的方式，引导模型生成更符合临床实际的报告。这种方法无需重新训练MLLM，而是通过推理阶段的干预，提升报告的临床保真度。

**技术框架**：CCD框架包含两个主要阶段：1) **临床信号提取**：利用预训练的放射学专家模型，对输入图像进行分析，提取结构化的临床信息，例如疾病类型、位置等。2) **对比解码**：在MLLM生成报告的过程中，CCD引入双阶段对比机制，在token级别调整logits。第一阶段，利用专家模型提取的临床信息，对logits进行对比，增强与临床信息相关的token的概率。第二阶段，对不同临床部分的logits进行对比，抑制模型对特定临床部分的过度敏感。

**关键创新**：该论文的关键创新在于提出了临床对比解码(CCD)框架，这是一种无需训练和检索的推理方法，可以有效地缓解放射学MLLM中的幻觉问题。与现有方法相比，CCD不需要对MLLM进行任何修改，而是通过在解码阶段引入对比机制，利用专家模型的知识来提升报告的临床保真度。

**关键设计**：CCD的关键设计包括：1) **双阶段对比机制**：通过token级别和临床部分级别的对比，更精细地调整logits，提升临床保真度。2) **专家模型集成**：利用预训练的放射学专家模型，提取结构化的临床信息，为对比解码提供指导。3) **训练自由**：无需对MLLM进行任何训练，即可实现性能提升，降低了应用成本。

## 📊 实验亮点

实验结果表明，CCD框架在三个数据集上均能有效提升放射学报告生成的性能。在MIMIC-CXR数据集上，将CCD应用于最先进的RRG模型时，RadGraph-F1指标提升高达17%。此外，该方法无需训练，易于部署和应用，具有良好的通用性和可扩展性。

## 🎯 应用场景

该研究成果可应用于辅助放射科医生进行报告撰写，提高诊断效率和准确性，降低医疗风险。通过减轻多模态大语言模型中的幻觉问题，可以提升其在医疗领域的可靠性和实用性，未来有望应用于更广泛的医学影像分析和诊断场景。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have recently achieved remarkable progress in radiology by integrating visual perception with natural language understanding. However, they often generate clinically unsupported descriptions, known as medical hallucinations, which pose serious risks in medical applications that demand accuracy and image-grounded outputs. Through empirical analysis, we find that prompt-induced hallucinations remain prevalent in radiology MLLMs, largely due to over-sensitivity to clinical sections. To address this, we introduce Clinical Contrastive Decoding (CCD), a training-free and retrieval-free inference framework that integrates structured clinical signals from task-specific radiology expert models. CCD introduces a dual-stage contrastive mechanism to refine token-level logits during generation, thereby enhancing clinical fidelity without modifying the base MLLM. Experiments on three datasets and multiple models demonstrate that CCD consistently improves overall performance on radiology report generation (RRG). On the MIMIC-CXR dataset, it yields up to a 17% improvement in RadGraph-F1 when applied to state-of-the-art RRG models. Our approach provides a lightweight and generalisable solution for mitigating medical hallucinations, effectively bridging expert models and MLLMs in radiology.

