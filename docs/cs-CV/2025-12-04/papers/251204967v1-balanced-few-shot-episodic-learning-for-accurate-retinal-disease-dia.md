---
layout: default
title: Balanced Few-Shot Episodic Learning for Accurate Retinal Disease Diagnosis
---

# Balanced Few-Shot Episodic Learning for Accurate Retinal Disease Diagnosis

**arXiv**: [2512.04967v1](https://arxiv.org/abs/2512.04967) | [PDF](https://arxiv.org/pdf/2512.04967.pdf)

**作者**: Jasmaine Khale, Ravi Prakash Srivastava

---

## 💡 一句话要点

**提出平衡少样本情景学习框架，以提升数据受限下视网膜疾病诊断的准确性与公平性。**

**关键词**: `少样本学习` `视网膜疾病诊断` `平衡采样` `CLAHE增强` `原型网络` `数据不平衡`

## 📋 核心要点

1. 核心问题：视网膜疾病诊断中数据标注成本高且类别不平衡，传统深度学习方法可靠性受限。
2. 方法要点：采用平衡情景采样、目标增强（如CLAHE）和ResNet-50编码器，结合原型计算与余弦相似度分类。
3. 实验或效果：在RFMiD数据集上训练100个情景并测试1000个情景，显著提升准确率并减少对多数类别的偏见。

## 📄 摘要（原文）

> Automated retinal disease diagnosis is vital given the rising prevalence of conditions such as diabetic retinopathy and macular degeneration. Conventional deep learning approaches require large annotated datasets, which are costly and often imbalanced across disease categories, limiting their reliability in practice. Few-shot learning (FSL) addresses this challenge by enabling models to generalize from only a few labeled samples per class. In this study,we propose a balanced few-shot episodic learning framework tailored to the Retinal Fundus Multi-Disease Image Dataset (RFMiD). Focusing on the ten most represented classes, which still show substantial imbalance between majority diseases (e.g., Diabetic Retinopathy, Macular Hole) and minority ones (e.g., Optic Disc Edema, Branch Retinal Vein Occlusion), our method integrates three key components: (i) balanced episodic sampling, ensuring equal participation of all classes in each 5-way 5-shot episode; (ii) targeted augmentation, including Contrast Limited Adaptive Histogram Equalization (CLAHE) and color/geometry transformations, to improve minority-class di- versity; and (iii) a ResNet-50 encoder pretrained on ImageNet, selected for its superior ability to capture fine-grained retinal features. Prototypes are computed in the embedding space and classification is performed with cosine similarity for improved stability. Trained on 100 episodes and evaluated on 1,000 test episodes, our framework achieves substantial accuracy gains and reduces bias toward majority classes, with notable improvements for underrepresented diseases. These results demonstrate that dataset-aware few-shot pipelines, combined with balanced sampling and CLAHE-enhanced preprocessing, can deliver more robust and clinically fair retinal disease diagnosis under data-constrained conditions.

