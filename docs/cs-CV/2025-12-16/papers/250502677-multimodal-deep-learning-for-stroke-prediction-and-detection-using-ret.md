---
layout: default
title: Multimodal Deep Learning for Stroke Prediction and Detection using Retinal Imaging and Clinical Data
---

# Multimodal Deep Learning for Stroke Prediction and Detection using Retinal Imaging and Clinical Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02677" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02677</a>
  <a href="https://arxiv.org/pdf/2505.02677.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02677" onclick="toggleFavorite(this, '2505.02677', 'Multimodal Deep Learning for Stroke Prediction and Detection using Retinal Imaging and Clinical Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saeed Shurrab, Aadim Nepal, Terrence J. Lee-St. John, Nicola G. Ghazi, Bartlomiej Piechowski-Jozwiak, Farah E. Shamout

**分类**: eess.IV, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出一种基于视网膜影像和临床数据的多模态深度学习方法，用于卒中预测和检测。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `卒中预测` `视网膜成像` `多模态学习` `深度学习` `自监督学习`

## 📋 核心要点

1. 现有卒中诊断方法依赖昂贵的CT等医学影像，成本高且不便普及，限制了早期筛查。
2. 提出一种多模态深度学习框架，融合OCT、红外视网膜扫描和临床数据，提升卒中预测能力。
3. 实验表明，该方法在卒中检测和风险预测方面优于单模态基线和现有模型，AUROC最高提升8%。

## 📝 摘要（中文）

卒中是一个影响全球数百万人的重大公共健康问题。深度学习最近在增强卒中的诊断和风险预测方面展现出潜力。然而，现有方法依赖于昂贵的医学影像模态，如计算机断层扫描。最近的研究表明，由于视网膜和大脑之间存在共同的临床通路，视网膜成像可能为脑血管健康评估提供一种经济高效的替代方案。因此，本研究探讨了利用视网膜图像和临床数据进行卒中检测和风险预测的影响。我们提出了一种多模态深度神经网络，该网络处理光学相干断层扫描（OCT）和红外反射视网膜扫描，并结合临床数据，如人口统计学、生命体征和诊断代码。我们使用包含 3.7 万次扫描的真实世界数据集，通过自监督学习框架预训练了我们的模型，然后使用较小的标记子集对模型进行微调和评估。我们的经验结果证实了所考虑的模态在检测与急性卒中相关的视网膜持久影响以及预测特定时间范围内的未来风险方面的预测能力。实验结果表明，与仅使用图像的单模态基线相比，我们提出的框架的 AUROC 提高了 5%，与现有的最先进的基础模型相比，提高了 8%。总之，我们的研究强调了视网膜成像在识别高危患者和改善长期预后方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决卒中早期预测和检测的问题，现有方法主要依赖于昂贵的医学影像设备，如CT扫描，这限制了其在早期筛查和大规模应用中的可行性。因此，需要一种更经济、更便捷的方法来评估卒中风险。

**核心思路**：论文的核心思路是利用视网膜成像作为卒中风险评估的替代方案。由于视网膜与大脑之间存在共同的临床通路，视网膜图像可以反映脑血管的健康状况。通过结合视网膜图像（OCT和红外反射扫描）和临床数据，可以更全面地评估卒中风险。

**技术框架**：该方法采用多模态深度神经网络，整体框架包含以下几个主要阶段：1) 数据收集：收集包含OCT、红外反射视网膜扫描和临床数据（如人口统计学、生命体征和诊断代码）的数据集。2) 自监督预训练：使用大规模未标记的视网膜图像数据集，通过自监督学习方法预训练模型，以学习视网膜图像的通用特征表示。3) 多模态融合：将视网膜图像和临床数据输入到深度神经网络中，通过融合不同模态的信息，提取与卒中相关的特征。4) 微调和评估：使用标记的卒中数据集对模型进行微调，并在测试集上评估模型的性能。

**关键创新**：该论文的关键创新在于：1) 提出了一种基于视网膜成像的卒中预测方法，避免了对昂贵医学影像设备的依赖。2) 采用多模态深度学习框架，融合视网膜图像和临床数据，提高了卒中预测的准确性。3) 使用自监督学习方法预训练模型，充分利用了大规模未标记的视网膜图像数据。

**关键设计**：在模型设计方面，论文采用了深度神经网络结构，具体网络结构未知。自监督预训练阶段使用了特定的自监督学习任务，具体任务未知。损失函数方面，使用了标准的分类损失函数（如交叉熵损失）进行微调。临床数据可能经过了特征工程处理，例如one-hot编码或标准化。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.02677/RetStroke-overview.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.02677/overall.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.02677/comorbidities.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在卒中检测和风险预测方面取得了显著的性能提升。与仅使用图像的单模态基线相比，AUROC提高了5%。与现有的最先进的基础模型相比，AUROC提高了8%。这些结果表明，融合视网膜图像和临床数据可以有效提高卒中预测的准确性。

## 🎯 应用场景

该研究成果可应用于卒中高危人群的早期筛查，尤其是在医疗资源有限的地区。通过分析视网膜图像和临床数据，可以识别出潜在的卒中患者，从而进行早期干预和治疗，降低卒中的发生率和致残率。此外，该方法还可以用于评估卒中患者的预后，指导康复治疗方案的制定。

## 📄 摘要（原文）

> Stroke is a major public health problem, affecting millions worldwide. Deep learning has recently demonstrated promise for enhancing the diagnosis and risk prediction of stroke. However, existing methods rely on costly medical imaging modalities, such as computed tomography. Recent studies suggest that retinal imaging could offer a cost-effective alternative for cerebrovascular health assessment due to the shared clinical pathways between the retina and the brain. Hence, this study explores the impact of leveraging retinal images and clinical data for stroke detection and risk prediction. We propose a multimodal deep neural network that processes Optical Coherence Tomography (OCT) and infrared reflectance retinal scans, combined with clinical data, such as demographics, vital signs, and diagnosis codes. We pretrained our model using a self-supervised learning framework using a real-world dataset consisting of $37$ k scans, and then fine-tuned and evaluated the model using a smaller labeled subset. Our empirical findings establish the predictive ability of the considered modalities in detecting lasting effects in the retina associated with acute stroke and forecasting future risk within a specific time horizon. The experimental results demonstrate the effectiveness of our proposed framework by achieving $5$\% AUROC improvement as compared to the unimodal image-only baseline, and $8$\% improvement compared to an existing state-of-the-art foundation model. In conclusion, our study highlights the potential of retinal imaging in identifying high-risk patients and improving long-term outcomes.

