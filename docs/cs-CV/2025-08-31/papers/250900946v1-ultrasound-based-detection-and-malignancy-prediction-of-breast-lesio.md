---
layout: default
title: "Ultrasound-based detection and malignancy prediction of breast lesions eligible for biopsy: A multi-center clinical-scenario study using nomograms, large language models, and radiologist evaluation"
---

# Ultrasound-based detection and malignancy prediction of breast lesions eligible for biopsy: A multi-center clinical-scenario study using nomograms, large language models, and radiologist evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00946" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00946v1</a>
  <a href="https://arxiv.org/pdf/2509.00946.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00946v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00946v1', 'Ultrasound-based detection and malignancy prediction of breast lesions eligible for biopsy: A multi-center clinical-scenario study using nomograms, large language models, and radiologist evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Abbasian Ardakani, Afshin Mohammadi, Taha Yusuf Kuzan, Beyza Nur Kuzan, Hamid Khorshidi, Ashkan Ghorbani, Alisa Mohebbi, Fariborz Faeghi, Sepideh Hatamikia, U Rajendra Acharya

**分类**: eess.IV, cs.CV

**发布日期**: 2025-08-31

**备注**: 38 pages, 8 figures, 12 tables

---

## 💡 一句话要点

**提出综合超声nomogram以提高乳腺病变活检推荐准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `乳腺病变` `超声影像` `BIRADS` `恶性预测` `nomogram` `逻辑回归` `多中心研究` `个性化医疗`

## 📋 核心要点

1. 现有方法在乳腺病变的活检推荐和恶性预测中存在准确性不足的问题，尤其是在不同超声设备和人群中的适用性。
2. 本研究提出了一种综合BIRADS和形态特征的nomogram，通过逻辑回归模型整合多种特征，以提高活检推荐和恶性预测的准确性。
3. 实验结果表明，融合nomogram在活检推荐和恶性预测中的准确率分别达到83.0%和83.8%，显著优于单独的形态特征nomogram和放射科医师的判断。

## 📝 摘要（中文）

本研究旨在开发并外部验证结合BIRADS特征和定量形态特征的综合超声nomogram，并将其性能与专家放射科医师及先进的大型语言模型进行比较。研究涉及1747名有病理确认乳腺病变的女性，提取了10个BIRADS和26个形态特征。通过逻辑回归构建了融合nomogram，结果显示该模型在活检推荐和恶性预测中均表现优异，准确率分别为83.0%和83.8%。外部验证确认了其在不同超声平台和人群中的广泛适用性，表明该工具有潜力减少不必要的活检并增强个性化决策。

## 🔬 方法详解

**问题定义**：本研究旨在解决乳腺病变活检推荐和恶性预测的准确性不足问题，现有方法在不同超声设备和人群中的适用性较差，导致误诊和不必要的活检。

**核心思路**：通过结合BIRADS特征和定量形态特征，构建一个综合的nomogram，以提高活检推荐和恶性预测的准确性，旨在提供更可靠的决策支持。

**技术框架**：研究采用回顾性多中心研究设计，提取1747名女性的超声图像特征，构建BIRADS、形态和融合nomogram，并进行内部及外部验证。

**关键创新**：该研究的创新点在于首次将BIRADS特征与形态特征结合，构建融合nomogram，显著提升了活检推荐和恶性预测的准确性，超越了传统单一模型和放射科医师的表现。

**关键设计**：在模型构建中，采用逻辑回归分析，提取10个BIRADS特征和26个形态特征，设置了适当的参数和损失函数，以确保模型的稳定性和准确性。

## 📊 实验亮点

实验结果显示，融合nomogram在活检推荐和恶性预测中的准确率分别为83.0%和83.8%，AUC值分别为0.901和0.853，显著优于单独的形态nomogram、三位放射科医师和两种ChatGPT模型，验证了其在不同超声平台和人群中的广泛适用性。

## 🎯 应用场景

该研究的成果可广泛应用于乳腺影像学领域，尤其是在乳腺病变的筛查和诊断中。通过提供更准确的活检推荐和恶性预测，能够有效减少不必要的活检，提高患者的治疗效率和个性化医疗水平，未来可能在临床实践中发挥重要作用。

## 📄 摘要（原文）

> To develop and externally validate integrated ultrasound nomograms combining BIRADS features and quantitative morphometric characteristics, and to compare their performance with expert radiologists and state of the art large language models in biopsy recommendation and malignancy prediction for breast lesions. In this retrospective multicenter, multinational study, 1747 women with pathologically confirmed breast lesions underwent ultrasound across three centers in Iran and Turkey. A total of 10 BIRADS and 26 morphological features were extracted from each lesion. A BIRADS, morphometric, and fused nomogram integrating both feature sets was constructed via logistic regression. Three radiologists (one senior, two general) and two ChatGPT variants independently interpreted deidentified breast lesion images. Diagnostic performance for biopsy recommendation (BIRADS 4,5) and malignancy prediction was assessed in internal and two external validation cohorts. In pooled analysis, the fused nomogram achieved the highest accuracy for biopsy recommendation (83.0%) and malignancy prediction (83.8%), outperforming the morphometric nomogram, three radiologists and both ChatGPT models. Its AUCs were 0.901 and 0.853 for the two tasks, respectively. In addition, the performance of the BIRADS nomogram was significantly higher than the morphometric nomogram, three radiologists and both ChatGPT models for biopsy recommendation and malignancy prediction. External validation confirmed the robust generalizability across different ultrasound platforms and populations. An integrated BIRADS morphometric nomogram consistently outperforms standalone models, LLMs, and radiologists in guiding biopsy decisions and predicting malignancy. These interpretable, externally validated tools have the potential to reduce unnecessary biopsies and enhance personalized decision making in breast imaging.

