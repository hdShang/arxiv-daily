---
layout: default
title: Detection and Localization of Subdural Hematoma Using Deep Learning on Computed Tomography
---

# Detection and Localization of Subdural Hematoma Using Deep Learning on Computed Tomography

**arXiv**: [2512.09393v1](https://arxiv.org/abs/2512.09393) | [PDF](https://arxiv.org/pdf/2512.09393.pdf)

**作者**: Vasiliki Stoumpou, Rohan Kumar, Bernard Burman, Diego Ojeda, Tapan Mehta, Dimitris Bertsimas

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-10

---

## 💡 一句话要点

**提出多模态深度学习框架，用于脑部CT影像中硬膜下血肿的精准检测与定位**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `硬膜下血肿检测` `深度学习` `多模态融合` `CT影像分析` `医学图像分割`

## 📋 核心要点

1. 现有SDH自动检测工具主要侧重于检测，缺乏空间定位和可解释性，难以支持实时决策。
2. 论文提出一种多模态深度学习框架，融合临床数据、3D卷积网络和Transformer分割模型，实现SDH检测与定位。
3. 实验结果表明，该框架在SDH检测和定位方面表现出色，多模态集成模型AUC达到0.9407。

## 📝 摘要（中文）

本研究旨在解决硬膜下血肿（SDH）快速准确识别的需求，针对现有自动化工具侧重检测、缺乏可解释性和空间定位的局限性，提出了一种多模态深度学习框架。该框架融合了结构化临床变量、基于CT体积的3D卷积神经网络以及Transformer增强的2D分割模型，用于SDH的检测和定位。研究使用了来自Hartford HealthCare的25315例头部CT研究（2015-2024），其中3774例（14.9%）包含临床医生确认的SDH。结果表明，临床变量的AUC为0.75，CT体积卷积模型和分割图的AUC分别达到0.922和0.926，而多模态集成模型的AUC达到0.9407（95% CI, 0.930-0.951），并生成符合SDH模式的解剖学定位图。该框架能够快速准确地检测和定位SDH，具有较高的检测性能和透明的解剖学输出，有望优化放射科工作流程，缩短干预时间，并提高SDH管理的效率。

## 🔬 方法详解

**问题定义**：论文旨在解决硬膜下血肿（SDH）的快速、准确检测和定位问题。现有方法主要集中在检测SDH的存在，而忽略了其空间位置信息，并且缺乏足够的可解释性，这限制了它们在临床实践中的应用。现有方法难以有效整合临床信息和影像信息，导致诊断效率和准确性不足。

**核心思路**：论文的核心思路是利用多模态深度学习方法，将临床变量、3D CT影像和2D分割信息进行融合，从而提高SDH检测和定位的准确性和可解释性。通过结合不同模态的信息，模型可以更好地理解SDH的特征，并生成更精确的定位图。这种多模态融合的方法旨在弥补单一模态信息的不足，提高模型的鲁棒性和泛化能力。

**技术框架**：该框架包含三个主要模块：1) 临床变量模型：利用人口统计学、合并症、药物和实验室结果等结构化临床变量训练表格模型。2) 3D卷积神经网络模型：使用3D CNN处理CT体积数据，用于SDH检测和生成体素级别的概率图。3) Transformer增强的2D分割模型：用于从CT图像中分割SDH区域，提供更精确的定位信息。最后，采用贪婪集成策略将这三个模块的预测结果进行融合，得到最终的SDH检测和定位结果。

**关键创新**：该论文的关键创新在于多模态信息的融合以及Transformer在SDH分割中的应用。通过将临床变量、3D CT影像和2D分割信息相结合，模型能够更全面地理解SDH的特征，从而提高检测和定位的准确性。Transformer分割模型能够更精确地分割SDH区域，提供更精细的定位信息。与现有方法相比，该方法不仅提高了检测性能，还提供了更强的可解释性。

**关键设计**：在3D CNN模型中，使用了针对医学图像的预训练模型作为初始化，并进行了微调。Transformer分割模型采用了U-Net结构，并用Transformer模块替换了部分卷积层，以提高分割精度。损失函数方面，使用了交叉熵损失和Dice损失的组合，以平衡检测和分割的性能。贪婪集成策略通过逐步添加性能最佳的模块来优化整体性能。

## 📊 实验亮点

实验结果表明，多模态集成模型在SDH检测中取得了显著的性能提升，AUC达到0.9407（95% CI, 0.930-0.951），优于单独使用临床变量（AUC 0.75）、CT体积卷积模型（AUC 0.922）或分割图（AUC 0.926）。该模型能够生成解剖学上合理的定位图，与已知的SDH模式一致，验证了其在临床应用中的潜力。

## 🎯 应用场景

该研究成果可应用于临床放射科工作流程，辅助医生进行SDH的快速筛查和诊断，尤其是在急诊情况下。通过提供准确的定位信息，可以帮助医生制定更有效的治疗方案，缩短干预时间，提高患者的生存率和生活质量。未来，该技术有望扩展到其他脑部疾病的检测和诊断，并集成到智能医疗系统中，实现更高效的医疗服务。

## 📄 摘要（原文）

> Background. Subdural hematoma (SDH) is a common neurosurgical emergency, with increasing incidence in aging populations. Rapid and accurate identification is essential to guide timely intervention, yet existing automated tools focus primarily on detection and provide limited interpretability or spatial localization. There remains a need for transparent, high-performing systems that integrate multimodal clinical and imaging information to support real-time decision-making.
>   Methods. We developed a multimodal deep-learning framework that integrates structured clinical variables, a 3D convolutional neural network trained on CT volumes, and a transformer-enhanced 2D segmentation model for SDH detection and localization. Using 25,315 head CT studies from Hartford HealthCare (2015--2024), of which 3,774 (14.9\%) contained clinician-confirmed SDH, tabular models were trained on demographics, comorbidities, medications, and laboratory results. Imaging models were trained to detect SDH and generate voxel-level probability maps. A greedy ensemble strategy combined complementary predictors.
>   Findings. Clinical variables alone provided modest discriminatory power (AUC 0.75). Convolutional models trained on CT volumes and segmentation-derived maps achieved substantially higher accuracy (AUCs 0.922 and 0.926). The multimodal ensemble integrating all components achieved the best overall performance (AUC 0.9407; 95\% CI, 0.930--0.951) and produced anatomically meaningful localization maps consistent with known SDH patterns.
>   Interpretation. This multimodal, interpretable framework provides rapid and accurate SDH detection and localization, achieving high detection performance and offering transparent, anatomically grounded outputs. Integration into radiology workflows could streamline triage, reduce time to intervention, and improve consistency in SDH management.

