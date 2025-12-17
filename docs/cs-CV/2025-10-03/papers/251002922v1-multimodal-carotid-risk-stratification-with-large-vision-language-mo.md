---
layout: default
title: Multimodal Carotid Risk Stratification with Large Vision-Language Models: Benchmarking, Fine-Tuning, and Clinical Insights
---

# Multimodal Carotid Risk Stratification with Large Vision-Language Models: Benchmarking, Fine-Tuning, and Clinical Insights

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.02922" target="_blank" class="toolbar-btn">arXiv: 2510.02922v1</a>
    <a href="https://arxiv.org/pdf/2510.02922.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02922v1" 
            onclick="toggleFavorite(this, '2510.02922v1', 'Multimodal Carotid Risk Stratification with Large Vision-Language Models: Benchmarking, Fine-Tuning, and Clinical Insights')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Daphne Tsolissou, Theofanis Ganitidis, Konstantinos Mitsis, Stergios CHristodoulidis, Maria Vakalopoulou, Konstantina Nikita

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-03

---

## 💡 一句话要点

**利用大型视觉-语言模型进行多模态颈动脉风险分层**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `颈动脉风险分层` `大型视觉-语言模型` `多模态融合` `超声成像` `领域自适应`

## 📋 核心要点

1. 颈动脉粥样硬化疾病的可靠风险评估面临挑战，需要整合多种临床和影像信息，并保证对临床医生透明且可解释。
2. 本研究提出利用大型视觉-语言模型（LVLM）整合超声影像和临床数据，进行颈动脉斑块评估和卒中风险分层。
3. 通过低秩自适应（LoRA）对LLaVa-NeXT-Vicuna进行领域适配，并整合多模态表格数据，显著提升了卒中风险分层的准确性。

## 📝 摘要（中文）

本研究探讨了最先进的大型视觉-语言模型（LVLM）在多模态颈动脉斑块评估中的潜力，通过整合超声成像（USI）与结构化的临床、人口统计学、实验室和蛋白质生物标志物数据。提出了一个通过访谈式问题序列模拟真实诊断场景的框架，比较了一系列开源LVLM，包括通用模型和医学调优模型。零样本实验表明，并非所有LVLM都能准确识别成像方式和解剖结构，且在准确的风险分类方面表现不佳。为此，使用低秩自适应（LoRA）将LLaVa-NeXT-Vicuna适配到超声领域，从而显著改善了卒中风险分层。以文本形式整合多模态表格数据进一步提高了特异性和平衡准确性，与先前在相同数据集上训练的卷积神经网络（CNN）基线相比，获得了具有竞争力的性能。研究结果强调了LVLM在基于超声的心血管风险预测中的潜力和局限性，突出了多模态整合、模型校准和领域自适应对于临床转化的重要性。

## 🔬 方法详解

**问题定义**：颈动脉粥样硬化风险评估需要整合超声影像、临床数据等多种模态信息。现有方法，如传统的CNN，难以有效融合多模态数据，且缺乏可解释性。大型视觉-语言模型（LVLM）虽然强大，但在医学图像理解和风险预测方面仍存在不足，尤其是在零样本场景下表现不佳。

**核心思路**：利用LVLM强大的视觉和语言理解能力，将超声影像和临床数据转化为统一的文本表示，并通过问答形式模拟临床诊断流程。通过领域自适应和多模态融合，提升LVLM在颈动脉风险分层任务中的性能。

**技术框架**：该研究构建了一个基于LVLM的多模态颈动脉风险分层框架，主要包含以下几个阶段：1) 数据预处理：对超声影像和临床数据进行清洗和格式化。2) 模型选择：选择一系列开源LVLM，包括通用模型和医学调优模型。3) 领域自适应：使用低秩自适应（LoRA）将LLaVa-NeXT-Vicuna适配到超声领域。4) 多模态融合：将临床数据以文本形式整合到LVLM的输入中。5) 风险预测：通过问答形式，利用LVLM进行卒中风险分层。6) 性能评估：使用多种指标评估模型的性能，并与CNN基线进行比较。

**关键创新**：1) 将LVLM应用于颈动脉风险分层任务，探索了其在医学图像理解和风险预测方面的潜力。2) 提出了一个基于问答形式的多模态融合框架，模拟了真实的临床诊断流程。3) 使用低秩自适应（LoRA）对LVLM进行领域适配，显著提升了其在超声图像理解方面的性能。

**关键设计**：1) 使用LLaVa-NeXT-Vicuna作为基础LVLM，并使用LoRA进行领域适配，LoRA的秩（rank）是一个关键参数，需要根据数据集大小和模型复杂度进行调整。2) 将临床数据以文本形式整合到LVLM的输入中，文本的格式和内容需要 carefully 设计，以确保LVLM能够有效地理解和利用这些信息。3) 使用问答形式进行风险预测，问题的设计需要涵盖关键的临床信息和影像特征。

## 📊 实验亮点

通过低秩自适应（LoRA）将LLaVa-NeXT-Vicuna适配到超声领域，显著改善了卒中风险分层。整合多模态表格数据进一步提高了特异性和平衡准确性，与先前在相同数据集上训练的卷积神经网络（CNN）基线相比，获得了具有竞争力的性能。具体性能数据未知，但强调了优于CNN基线。

## 🎯 应用场景

该研究成果可应用于颈动脉疾病的早期筛查和风险评估，辅助医生进行诊断和治疗决策。通过整合多模态数据，提高风险预测的准确性和可靠性，降低卒中风险。未来可扩展到其他心血管疾病的风险评估，具有广阔的应用前景。

## 📄 摘要（原文）

> Reliable risk assessment for carotid atheromatous disease remains a major clinical challenge, as it requires integrating diverse clinical and imaging information in a manner that is transparent and interpretable to clinicians. This study investigates the potential of state-of-the-art and recent large vision-language models (LVLMs) for multimodal carotid plaque assessment by integrating ultrasound imaging (USI) with structured clinical, demographic, laboratory, and protein biomarker data. A framework that simulates realistic diagnostic scenarios through interview-style question sequences is proposed, comparing a range of open-source LVLMs, including both general-purpose and medically tuned models. Zero-shot experiments reveal that even if they are very powerful, not all LVLMs can accurately identify imaging modality and anatomy, while all of them perform poorly in accurate risk classification. To address this limitation, LLaVa-NeXT-Vicuna is adapted to the ultrasound domain using low-rank adaptation (LoRA), resulting in substantial improvements in stroke risk stratification. The integration of multimodal tabular data in the form of text further enhances specificity and balanced accuracy, yielding competitive performance compared to prior convolutional neural network (CNN) baselines trained on the same dataset. Our findings highlight both the promise and limitations of LVLMs in ultrasound-based cardiovascular risk prediction, underscoring the importance of multimodal integration, model calibration, and domain adaptation for clinical translation.

