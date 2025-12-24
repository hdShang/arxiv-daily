---
layout: default
title: "Toward a robust lesion detection model in breast DCE-MRI: adapting foundation models to high-risk women"
---

# Toward a robust lesion detection model in breast DCE-MRI: adapting foundation models to high-risk women

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02710" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02710v1</a>
  <a href="https://arxiv.org/pdf/2509.02710.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02710v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02710v1', 'Toward a robust lesion detection model in breast DCE-MRI: adapting foundation models to high-risk women')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gabriel A. B. do Nascimento, Vincent Dong, Guilherme J. Cavalcante, Alex Nguyen, Thaís G. do Rêgo, Yuri Malheiros, Telmo M. Silva Filho, Carla R. Zeballos Torrez, James C. Gee, Anne Marie McCarthy, Andrew D. A. Maidment, Bruno Barufaldi

**分类**: physics.med-ph, cs.CV, cs.LG

**发布日期**: 2025-09-02

---

## 💡 一句话要点

**针对高危女性，提出基于医学切片Transformer和KAN的乳腺DCE-MRI病灶检测模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `乳腺MRI` `病灶检测` `深度学习` `Transformer` `Kolmogorov--Arnold Network`

## 📋 核心要点

1. 乳腺MRI病灶检测对于早期癌症诊断至关重要，尤其是在高危人群中，现有方法在处理不平衡和异构数据时存在挑战。
2. 论文提出将预训练的医学切片Transformer (MST) 与Kolmogorov--Arnold Network (KAN) 相结合，利用KAN的非线性变换能力提升分类性能。
3. 实验结果表明，MST+KAN流程在乳腺病灶分类任务中优于基线MST分类器，AUC达到0.80 ± 0.02，并保持了模型的可解释性。

## 📝 摘要（中文）

本研究提出了一种分类流程，用于在动态对比增强MRI（DCE-MRI）中进行乳腺病灶分类，尤其针对高危人群。该流程将预训练的基础模型Medical Slice Transformer (MST) 进行适配。MST利用基于DINOv2的自监督预训练，生成鲁棒的每切片特征嵌入，然后用于训练Kolmogorov--Arnold Network (KAN) 分类器。KAN通过自适应B样条激活实现局部非线性变换，为传统卷积网络提供了一种灵活且可解释的替代方案。这增强了模型在不平衡和异构临床数据集中区分良性和恶性病变的能力。实验结果表明，MST+KAN流程优于基线MST分类器，实现了AUC = 0.80 ± 0.02，同时通过基于注意力的热图保留了可解释性。研究结果强调了结合基础模型嵌入和高级分类策略在构建鲁棒且通用的乳腺MRI分析工具方面的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决乳腺DCE-MRI图像中病灶检测的准确性问题，尤其是在高危女性群体中。现有方法在处理临床数据集中常见的不平衡和异构性时表现不佳，难以有效区分良性和恶性病灶。

**核心思路**：论文的核心思路是利用预训练的基础模型Medical Slice Transformer (MST) 提取鲁棒的特征嵌入，并结合Kolmogorov--Arnold Network (KAN) 进行分类。MST通过自监督学习获得强大的特征表示能力，KAN则通过自适应B样条激活实现局部非线性变换，从而增强模型对复杂病灶的区分能力。

**技术框架**：整体流程包括两个主要阶段：1) 特征提取阶段：使用预训练的MST模型对DCE-MRI图像的每个切片进行特征提取，得到每切片的特征嵌入。2) 分类阶段：将提取的特征嵌入输入到KAN分类器中进行训练和预测，KAN输出病灶的良恶性概率。

**关键创新**：论文的关键创新在于将预训练的MST模型与KAN分类器相结合。MST提供了强大的特征表示能力，而KAN则通过其独特的网络结构和激活函数，实现了更灵活和可解释的分类。KAN相较于传统卷积神经网络，能够进行局部非线性变换，更好地适应异构数据。

**关键设计**：MST模型基于DINOv2进行自监督预训练，学习图像的通用特征表示。KAN分类器采用自适应B样条激活函数，允许网络根据输入数据动态调整激活函数的形状。损失函数方面，论文可能采用了二元交叉熵损失函数，以优化分类性能。具体的网络结构细节，如KAN的层数和每层神经元数量，以及B样条激活函数的参数设置，需要在论文正文中查找。

## 📊 实验亮点

实验结果表明，MST+KAN流程在乳腺病灶分类任务中取得了显著的性能提升，AUC达到0.80 ± 0.02，优于基线MST分类器。同时，该方法通过注意力热图保留了模型的可解释性，有助于医生理解模型的决策依据。这些结果表明，结合基础模型嵌入和高级分类策略可以有效提升乳腺MRI分析工具的性能和可靠性。

## 🎯 应用场景

该研究成果可应用于乳腺癌的早期诊断和风险评估，尤其是在高危女性群体中。通过提高病灶检测的准确性和效率，可以帮助医生更早地发现潜在的恶性病变，从而改善患者的预后。此外，该方法的可解释性有助于医生理解模型的决策过程，增强其对诊断结果的信任。

## 📄 摘要（原文）

> Accurate breast MRI lesion detection is critical for early cancer diagnosis, especially in high-risk populations. We present a classification pipeline that adapts a pretrained foundation model, the Medical Slice Transformer (MST), for breast lesion classification using dynamic contrast-enhanced MRI (DCE-MRI). Leveraging DINOv2-based self-supervised pretraining, MST generates robust per-slice feature embeddings, which are then used to train a Kolmogorov--Arnold Network (KAN) classifier. The KAN provides a flexible and interpretable alternative to conventional convolutional networks by enabling localized nonlinear transformations via adaptive B-spline activations. This enhances the model's ability to differentiate benign from malignant lesions in imbalanced and heterogeneous clinical datasets. Experimental results demonstrate that the MST+KAN pipeline outperforms the baseline MST classifier, achieving AUC = 0.80 \pm 0.02 while preserving interpretability through attention-based heatmaps. Our findings highlight the effectiveness of combining foundation model embeddings with advanced classification strategies for building robust and generalizable breast MRI analysis tools.

