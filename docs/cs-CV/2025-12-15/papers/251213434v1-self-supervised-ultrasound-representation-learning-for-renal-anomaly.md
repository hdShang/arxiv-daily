---
layout: default
title: Self-Supervised Ultrasound Representation Learning for Renal Anomaly Prediction in Prenatal Imaging
---

# Self-Supervised Ultrasound Representation Learning for Renal Anomaly Prediction in Prenatal Imaging

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13434" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13434v1</a>
  <a href="https://arxiv.org/pdf/2512.13434.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13434v1" onclick="toggleFavorite(this, '2512.13434v1', 'Self-Supervised Ultrasound Representation Learning for Renal Anomaly Prediction in Prenatal Imaging')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youssef Megahed, Inok Lee, Robin Ducharme, Kevin Dick, Adrian D. C. Chan, Steven Hawken, Mark C. Walker

**分类**: eess.IV, cs.CV

**发布日期**: 2025-12-15

**备注**: 14 pages, 8 figures, 4 tables

---

## 💡 一句话要点

**提出基于自监督学习的USF-MAE模型，用于产前超声肾脏异常自动预测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自监督学习` `超声图像` `肾脏异常检测` `产前诊断` `掩码自编码器` `Transformer` `医学影像分析`

## 📋 核心要点

1. 产前超声诊断依赖操作者经验，且易受成像条件影响，导致肾脏异常检测存在挑战。
2. 提出基于掩码自编码器(MAE)的超声自监督基础模型(USF-MAE)，学习超声图像的通用表示。
3. 实验表明，USF-MAE在肾脏异常分类任务中显著优于传统模型，尤其在多分类任务中提升明显。

## 📝 摘要（中文）

产前超声是检测先天性肾脏和泌尿道异常的基础，但诊断受到操作者依赖性和次优成像条件的限制。本文旨在评估自监督超声基础模型在自动胎儿肾脏异常分类中的性能，使用包含969张二维超声图像的数据集。一个预训练的基于掩码自编码器(MAE)的超声自监督基础模型(USF-MAE)被用于微调，以进行正常肾脏、尿路扩张和多囊性发育不良肾的二元和多类分类。模型与DenseNet-169卷积基线进行交叉验证和独立测试集的比较。USF-MAE在二元和多类设置的所有评估指标上都优于基线。USF-MAE在验证集上实现了约1.87%(AUC)和7.8%(F1-score)的提升，在独立保留测试集上实现了2.32%(AUC)和4.33%(F1-score)的提升。在多类设置中，增益最大，AUC提升了16.28%，F1-score提升了46.15%。为了提高模型的可解释性，Score-CAM可视化被调整为Transformer架构，并表明模型预测受到已知的、临床相关的肾脏结构的影响，包括尿路扩张中的肾盂和多囊性发育不良肾中的囊性区域。这些结果表明，超声特定的自监督学习可以生成有用的表示，作为下游诊断任务的基础。所提出的框架提供了一种稳健、可解释的方法来支持产前肾脏异常的检测，并展示了基础模型在产科成像中的前景。

## 🔬 方法详解

**问题定义**：产前超声是检测胎儿肾脏异常的重要手段，但其诊断结果依赖于操作者的经验和成像质量。现有的方法，如依赖人工特征工程的传统机器学习方法，泛化能力较弱。卷积神经网络虽然能够自动提取特征，但需要大量的标注数据，而医学图像的标注成本很高。因此，如何利用有限的标注数据，提高肾脏异常检测的准确性和鲁棒性是一个关键问题。

**核心思路**：本文的核心思路是利用自监督学习，从未标注的超声图像中学习到通用的、与任务无关的特征表示。然后，利用这些预训练的特征表示，在少量标注数据上进行微调，从而提高肾脏异常检测的性能。这种方法可以有效利用大量的未标注数据，降低对标注数据的依赖，提高模型的泛化能力。

**技术框架**：该方法主要包含两个阶段：预训练阶段和微调阶段。在预训练阶段，使用大量的未标注超声图像训练一个基于掩码自编码器(MAE)的超声自监督基础模型(USF-MAE)。MAE通过随机掩盖输入图像的部分区域，并预测被掩盖区域的内容，从而学习到图像的内在结构和特征表示。在微调阶段，使用少量标注的超声图像，对预训练的USF-MAE模型进行微调，使其适应肾脏异常检测的任务。

**关键创新**：该论文的关键创新在于将自监督学习方法应用于产前超声图像分析，并提出了针对超声图像特点的USF-MAE模型。与传统的监督学习方法相比，该方法可以有效利用大量的未标注数据，降低对标注数据的依赖。此外，该论文还针对Transformer架构，改进了Score-CAM可视化方法，提高了模型的可解释性。

**关键设计**：USF-MAE模型采用Transformer架构，使用随机掩码策略，掩盖输入图像的75%的区域。损失函数采用均方误差(MSE)，用于衡量重建图像与原始图像之间的差异。在微调阶段，使用交叉熵损失函数，用于衡量模型预测的类别与真实类别之间的差异。为了提高模型的可解释性，该论文使用Score-CAM可视化方法，并针对Transformer架构进行了改进，使其能够可视化模型关注的区域。

## 📊 实验亮点

实验结果表明，USF-MAE在肾脏异常分类任务中显著优于DenseNet-169基线模型。在验证集上，USF-MAE的AUC提升了1.87%，F1-score提升了7.8%。在独立的测试集上，AUC提升了2.32%，F1-score提升了4.33%。尤其是在多分类任务中，USF-MAE的AUC提升了16.28%，F1-score提升了46.15%，表明自监督学习方法在复杂医学图像分析任务中具有巨大潜力。

## 🎯 应用场景

该研究成果可应用于产前超声筛查，辅助医生进行肾脏和泌尿系统先天性异常的早期诊断。通过提高诊断准确率和降低对操作者的依赖性，有望减少漏诊和误诊，改善患者预后。此外，该方法也可推广到其他医学影像分析任务，例如其他器官的病灶检测和疾病诊断。

## 📄 摘要（原文）

> Prenatal ultrasound is the cornerstone for detecting congenital anomalies of the kidneys and urinary tract, but diagnosis is limited by operator dependence and suboptimal imaging conditions. We sought to assess the performance of a self-supervised ultrasound foundation model for automated fetal renal anomaly classification using a curated dataset of 969 two-dimensional ultrasound images. A pretrained Ultrasound Self-Supervised Foundation Model with Masked Autoencoding (USF-MAE) was fine-tuned for binary and multi-class classification of normal kidneys, urinary tract dilation, and multicystic dysplastic kidney. Models were compared with a DenseNet-169 convolutional baseline using cross-validation and an independent test set. USF-MAE consistently improved upon the baseline across all evaluation metrics in both binary and multi-class settings. USF-MAE achieved an improvement of about 1.87% (AUC) and 7.8% (F1-score) on the validation set, 2.32% (AUC) and 4.33% (F1-score) on the independent holdout test set. The largest gains were observed in the multi-class setting, where the improvement in AUC was 16.28% and 46.15% in F1-score. To facilitate model interpretability, Score-CAM visualizations were adapted for a transformer architecture and show that model predictions were informed by known, clinically relevant renal structures, including the renal pelvis in urinary tract dilation and cystic regions in multicystic dysplastic kidney. These results show that ultrasound-specific self-supervised learning can generate a useful representation as a foundation for downstream diagnostic tasks. The proposed framework offers a robust, interpretable approach to support the prenatal detection of renal anomalies and demonstrates the promise of foundation models in obstetric imaging.

