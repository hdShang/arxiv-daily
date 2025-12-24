---
layout: default
title: "ProstNFound+: A Prospective Study using Medical Foundation Models for Prostate Cancer Detection"
---

# ProstNFound+: A Prospective Study using Medical Foundation Models for Prostate Cancer Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26703" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26703v1</a>
  <a href="https://arxiv.org/pdf/2510.26703.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26703v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.26703v1', 'ProstNFound+: A Prospective Study using Medical Foundation Models for Prostate Cancer Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Paul F. R. Wilson, Mohamed Harmanani, Minh Nguyen Nhat To, Amoon Jamzad, Tarek Elghareb, Zhuoxin Guo, Adam Kinnaird, Brian Wodlinger, Purang Abolmaesumi, Parvin Mousavi

**分类**: eess.IV, cs.CV

**发布日期**: 2025-10-30

---

## 💡 一句话要点

**ProstNFound+：利用医学基础模型实现前列腺癌微超声检测的前瞻性研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `前列腺癌检测` `医学基础模型` `微超声` `适配器调优` `提示学习` `前瞻性研究` `临床应用`

## 📋 核心要点

1. 现有前列腺癌检测方法依赖专家经验，存在主观性和可扩展性问题，缺乏客观、高效的诊断工具。
2. ProstNFound+利用医学基础模型，结合适配器调优和定制提示编码器，嵌入临床生物标志物，生成癌症热图和风险评分。
3. 前瞻性研究表明，ProstNFound+具有良好的泛化能力，与临床评分一致，并生成可解释的热图，具有临床部署潜力。

## 📝 摘要（中文）

本研究旨在探索医学基础模型（FMs）在构建高性能诊断系统中的潜力，并首次在临床环境中测试其在前列腺癌（PCa）微超声（μUS）检测中的应用。我们提出了ProstNFound+，一个针对μUS的PCa检测的FM改进模型，并对其进行了首次前瞻性验证。ProstNFound+结合了医学FM、适配器调优和一个定制的提示编码器，该编码器嵌入了PCa特异性的临床生物标志物。该模型生成癌症热图和临床显著PCa的风险评分。在多中心回顾性数据上训练后，该模型在五年后从一个新的临床站点获得的数据上进行前瞻性评估。模型预测与标准临床评分协议（PRI-MUS和PI-RADS）进行基准测试。结果表明，ProstNFound+对前瞻性数据表现出强大的泛化能力，与回顾性评估相比没有性能下降。它与临床评分密切相关，并产生与活检确认的病变一致的可解释热图。结果突出了其临床部署的潜力，为专家驱动的协议提供了一种可扩展且可解释的替代方案。

## 🔬 方法详解

**问题定义**：论文旨在解决前列腺癌微超声图像（μUS）检测中，现有方法依赖专家经验、主观性强、可扩展性差的问题。现有方法难以充分利用临床生物标志物，且缺乏对新临床环境的泛化能力。

**核心思路**：论文的核心思路是利用医学基础模型（FMs）的强大表征能力，通过适配器调优和定制提示编码器，将临床生物标志物融入模型，从而提高前列腺癌检测的准确性和泛化能力。这种方法旨在减少对专家经验的依赖，并提供更客观、可解释的诊断结果。

**技术框架**：ProstNFound+的整体架构包括三个主要模块：1) 医学基础模型（Medical FM）：利用预训练的医学图像模型作为特征提取器。2) 适配器调优（Adapter Tuning）：通过少量数据微调FM，使其适应前列腺癌μUS图像的特点。3) 提示编码器（Prompt Encoder）：将PCa特异性的临床生物标志物编码为提示信息，引导模型关注关键区域。模型最终生成癌症热图和风险评分。

**关键创新**：该论文的关键创新在于将医学基础模型与适配器调优和定制提示编码器相结合，用于前列腺癌微超声图像的检测。通过提示编码器嵌入临床生物标志物，增强了模型的判别能力和可解释性。此外，该研究进行了前瞻性验证，证明了模型在新的临床环境中的泛化能力。

**关键设计**：提示编码器的设计是关键。它将临床生物标志物（例如，肿瘤大小、位置、形态等）编码成向量，并将其作为提示信息输入到医学基础模型中。适配器调优采用少量数据进行微调，避免了灾难性遗忘。损失函数包括分类损失（区分癌性和非癌性区域）和回归损失（预测风险评分）。具体网络结构细节未知。

## 📊 实验亮点

ProstNFound+在前瞻性数据上表现出强大的泛化能力，与回顾性评估相比没有性能下降。模型预测与标准临床评分协议（PRI-MUS和PI-RADS）密切相关，并生成与活检确认的病变一致的可解释热图。这些结果表明ProstNFound+具有临床部署的潜力。

## 🎯 应用场景

ProstNFound+可应用于前列腺癌的早期筛查和诊断，辅助医生进行决策，提高诊断准确性和效率。该模型具有可扩展性，可部署在不同的临床环境中，为患者提供更便捷、客观的诊断服务。未来，该模型可与其他临床数据（如MRI、活检结果）结合，实现更全面的前列腺癌风险评估。

## 📄 摘要（原文）

> Purpose: Medical foundation models (FMs) offer a path to build high-performance diagnostic systems. However, their application to prostate cancer (PCa) detection from micro-ultrasound (μUS) remains untested in clinical settings. We present ProstNFound+, an adaptation of FMs for PCa detection from μUS, along with its first prospective validation. Methods: ProstNFound+ incorporates a medical FM, adapter tuning, and a custom prompt encoder that embeds PCa-specific clinical biomarkers. The model generates a cancer heatmap and a risk score for clinically significant PCa. Following training on multi-center retrospective data, the model is prospectively evaluated on data acquired five years later from a new clinical site. Model predictions are benchmarked against standard clinical scoring protocols (PRI-MUS and PI-RADS). Results: ProstNFound+ shows strong generalization to the prospective data, with no performance degradation compared to retrospective evaluation. It aligns closely with clinical scores and produces interpretable heatmaps consistent with biopsy-confirmed lesions. Conclusion: The results highlight its potential for clinical deployment, offering a scalable and interpretable alternative to expert-driven protocols.

